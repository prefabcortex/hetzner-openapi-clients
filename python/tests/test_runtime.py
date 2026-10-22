"""Runtime tests: transport, retries, error mapping, helper types, client."""

import asyncio
import email.utils
import pickle
import time
from datetime import UTC, date, datetime
from decimal import Decimal
from types import MappingProxyType

import httpx2
import pytest
from pydantic import BaseModel, JsonValue, TypeAdapter

# models qualified: a schema may be named like a name of this test (ProblemDetails, ...)
from hetzner_api import (
    NOT_GIVEN,
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AsyncHetzner,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    Hetzner,
    HetznerError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    PreconditionFailedError,
    ProblemDetails,
    RateLimitError,
    RetryPolicy,
    UnknownValue,
    UnprocessableEntityError,
    models,
)
from hetzner_api._auth import BearerToken
from hetzner_api._base_client import (
    AsyncTransport,
    SyncTransport,
    encode_body,
    encode_headers,
    encode_path,
    encode_query,
)
from hetzner_api.errors import ErrorModels, error_model_for
from tests.payloads import ACTION, ERROR_RESPONSE
from tests.support import Recorder, validated

FAST: RetryPolicy = RetryPolicy(max_retries=2, base_delay=0.0, max_delay=0.0)
BASE: dict[str, str] = {"cloud": "https://api.example.test/v1"}


def _sync(handler: httpx2.MockTransport, retry: RetryPolicy = FAST) -> SyncTransport:
    return SyncTransport(
        credentials={"t": BearerToken("t")},
        base_urls=BASE,
        default_server="cloud",
        retry=retry,
        timeout=5.0,
        http_client=httpx2.Client(transport=handler),
    )


def _async(handler: httpx2.MockTransport, retry: RetryPolicy = FAST) -> AsyncTransport:
    return AsyncTransport(
        credentials={"t": BearerToken("t")},
        base_urls=BASE,
        default_server="cloud",
        retry=retry,
        timeout=5.0,
        http_client=httpx2.AsyncClient(transport=handler),
    )


def _error(status: int, code: str = "some_error") -> tuple[int, JsonValue]:
    return status, {"code": code, "message": "broken"}


# --- Transport -------------------------------------------------------------------------


def test_request_sends_token_user_agent_and_json() -> None:
    recorder = Recorder(200, {"ok": True})
    transport = _sync(httpx2.MockTransport(recorder))
    transport.request("POST", "/things", params=(("a", "1"),), json_body={"name": "x"})
    request = recorder.only()
    assert request.headers["Authorization"] == "Bearer t"
    assert request.headers["User-Agent"].startswith("hetzner-api/")
    assert request.headers["Content-Type"] == "application/json"
    assert str(request.url) == "https://api.example.test/v1/things?a=1"
    assert request.content == b'{"name":"x"}'


def test_retries_rate_limit_then_succeeds(caplog: pytest.LogCaptureFixture) -> None:
    recorder = Recorder.sequence([_error(429, "rate_limit_exceeded"), (200, {"ok": True})])
    with caplog.at_level("DEBUG", logger="hetzner_api"):
        response = _sync(httpx2.MockTransport(recorder)).request("POST", "/x")
    assert response.status_code == 200
    assert len(recorder.requests) == 2
    assert (
        "retrying POST https://api.example.test/v1/x in 0.0 s (attempt 2 of 3, reason: 429)"
        in caplog.text
    )
    assert "POST https://api.example.test/v1/x -> 200" in caplog.text


def test_retries_bad_gateway_only_for_idempotent_methods() -> None:
    recorder = Recorder.sequence([(502, None), (200, {"ok": True})])
    assert _sync(httpx2.MockTransport(recorder)).request("GET", "/x").status_code == 200
    post = Recorder.sequence([(502, None), (200, {"ok": True})])
    with pytest.raises(InternalServerError):
        _sync(httpx2.MockTransport(post)).request("POST", "/x")
    assert len(post.requests) == 1


def test_long_retry_after_is_not_waited_for() -> None:
    recorder = Recorder(429, None, headers={"Retry-After": "3600"})
    with pytest.raises(RateLimitError):
        _sync(httpx2.MockTransport(recorder)).request("GET", "/x")
    assert len(recorder.requests) == 1


def test_gives_up_after_max_retries() -> None:
    recorder = Recorder(503, None)
    with pytest.raises(InternalServerError):
        _sync(httpx2.MockTransport(recorder)).request("PUT", "/x")
    assert len(recorder.requests) == 3


def test_conflicts_are_not_retried() -> None:
    recorder = Recorder.sequence([_error(409, "conflict"), (200, {"ok": True})])
    with pytest.raises(ConflictError):
        _sync(httpx2.MockTransport(recorder)).request("GET", "/x")
    assert len(recorder.requests) == 1


def test_connect_errors_are_retried_and_then_raised(caplog: pytest.LogCaptureFixture) -> None:
    calls: list[httpx2.Request] = []

    def fail(request: httpx2.Request) -> httpx2.Response:
        calls.append(request)
        msg = "no network"
        raise httpx2.ConnectError(msg, request=request)

    with caplog.at_level("INFO", logger="hetzner_api"), pytest.raises(APIConnectionError) as raised:
        _sync(httpx2.MockTransport(fail)).request("POST", "/x")
    assert not isinstance(raised.value, APITimeoutError)
    assert len(calls) == 3
    assert "reason: ConnectError" in caplog.text


@pytest.mark.parametrize("error_type", [httpx2.ConnectTimeout, httpx2.PoolTimeout])
def test_requests_that_never_left_are_retried_even_for_post(
    error_type: type[httpx2.TransportError],
) -> None:
    calls: list[httpx2.Request] = []

    def fail(request: httpx2.Request) -> httpx2.Response:
        calls.append(request)
        msg = "not sent"
        raise error_type(msg, request=request)

    with pytest.raises(APITimeoutError):
        _sync(httpx2.MockTransport(fail)).request("POST", "/x")
    assert len(calls) == 3


def test_read_timeout_on_post_is_not_retried() -> None:
    calls: list[httpx2.Request] = []

    def slow(request: httpx2.Request) -> httpx2.Response:
        calls.append(request)
        msg = "too slow"
        raise httpx2.ReadTimeout(msg, request=request)

    with pytest.raises(APITimeoutError):
        _sync(httpx2.MockTransport(slow)).request("POST", "/x")
    assert len(calls) == 1


def test_async_transport_retries_and_raises() -> None:
    recorder = Recorder.sequence([_error(429), (200, {"ok": True})])
    calls: list[httpx2.Request] = []

    def fail(request: httpx2.Request) -> httpx2.Response:
        calls.append(request)
        msg = "no network"
        raise httpx2.ConnectError(msg, request=request)

    async def run() -> None:
        transport = _async(httpx2.MockTransport(recorder))
        assert (await transport.request("GET", "/x")).status_code == 200
        await transport.aclose()
        failing = _async(httpx2.MockTransport(fail))
        with pytest.raises(APIConnectionError):
            await failing.request("GET", "/x")
        not_found = _async(httpx2.MockTransport(Recorder(*_error(404, "not_found"))))
        with pytest.raises(NotFoundError):
            await not_found.request("GET", "/x")

    asyncio.run(run())
    assert len(recorder.requests) == 2
    assert len(calls) == 3


def test_missing_base_url_is_reported() -> None:
    transport = SyncTransport(
        credentials={"t": BearerToken("t")},
        base_urls={"other": ""},
        default_server="other",
        retry=FAST,
        timeout=5.0,
        http_client=httpx2.Client(transport=httpx2.MockTransport(Recorder(200))),
    )
    with pytest.raises(HetznerError, match="other_base_url"):
        transport.request("GET", "/x")


def test_timeout_applies_to_own_and_external_clients() -> None:
    recorder = Recorder(200)
    explicit = SyncTransport(
        credentials={"t": BearerToken("t")},
        base_urls=BASE,
        default_server="cloud",
        retry=FAST,
        timeout=5.0,
        http_client=httpx2.Client(transport=httpx2.MockTransport(recorder), timeout=99.0),
    )
    explicit.request("GET", "/x")
    inherited = SyncTransport(
        credentials={"t": BearerToken("t")},
        base_urls=BASE,
        default_server="cloud",
        retry=FAST,
        timeout=NOT_GIVEN,
        http_client=httpx2.Client(transport=httpx2.MockTransport(recorder), timeout=99.0),
    )
    inherited.request("GET", "/x")
    disabled = SyncTransport(
        credentials={"t": BearerToken("t")},
        base_urls=BASE,
        default_server="cloud",
        retry=FAST,
        timeout=None,
        http_client=httpx2.Client(transport=httpx2.MockTransport(recorder), timeout=99.0),
    )
    disabled.request("GET", "/x")
    timeouts = [request.extensions["timeout"]["read"] for request in recorder.requests]
    assert timeouts == [5.0, 99.0, None]


def test_transport_closes_only_its_own_client() -> None:
    external = httpx2.Client()
    transport = _sync(httpx2.MockTransport(Recorder(200)))
    transport.close()
    own = SyncTransport(
        credentials={"t": BearerToken("t")},
        base_urls=BASE,
        default_server="cloud",
        retry=FAST,
        timeout=5.0,
        http_client=None,
    )
    own.close()
    assert not external.is_closed
    external.close()

    async def run() -> None:
        own_async = AsyncTransport(
            credentials={"t": BearerToken("t")},
            base_urls=BASE,
            default_server="cloud",
            retry=FAST,
            timeout=5.0,
            http_client=None,
        )
        await own_async.aclose()

    asyncio.run(run())


# --- Error mapping ---------------------------------------------------------------------


@pytest.mark.parametrize(
    ("status", "error_type"),
    [
        (400, BadRequestError),
        (401, AuthenticationError),
        (403, PermissionDeniedError),
        (404, NotFoundError),
        (409, ConflictError),
        (412, PreconditionFailedError),
        (423, ConflictError),
        (422, UnprocessableEntityError),
        (429, RateLimitError),
        (500, InternalServerError),
        (503, InternalServerError),
        (418, APIStatusError),
    ],
)
def test_status_codes_map_to_exceptions(status: int, error_type: type[APIStatusError]) -> None:
    recorder = Recorder(*_error(status, "boom"))
    with pytest.raises(error_type) as raised:
        _sync(httpx2.MockTransport(recorder), RetryPolicy(max_retries=0)).request("GET", "/x")
    error = raised.value
    assert type(error) is error_type
    assert (error.status_code, error.body) == (status, {"code": "boom", "message": "broken"})
    assert str(error).startswith(f"{status}")
    assert str(error).endswith(': {"code":"boom","message":"broken"}')
    assert isinstance(error, HetznerError)


@pytest.mark.parametrize(
    ("content", "body", "message"),
    [
        (b"not json", None, "400 Bad Request: not json"),
        (b"", None, "400 Bad Request"),
        (b"x" * 600, None, "400 Bad Request: " + "x" * 500),
    ],
)
def test_error_bodies_without_json(content: bytes, body: JsonValue, message: str) -> None:
    def handler(_: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(400, content=content)

    with pytest.raises(BadRequestError) as raised:
        _sync(httpx2.MockTransport(handler), RetryPolicy(max_retries=0)).request("GET", "/x")
    assert (raised.value.body, str(raised.value)) == (body, message)


def test_errors_survive_pickling() -> None:
    recorder = Recorder(*_error(404, "not_found"))
    with pytest.raises(NotFoundError) as raised:
        _sync(httpx2.MockTransport(recorder), RetryPolicy(max_retries=0)).request("GET", "/x")
    restored = pickle.loads(pickle.dumps(raised.value))  # noqa: S301 - our own data
    assert type(restored) is NotFoundError
    assert (restored.body, restored.status_code) == (raised.value.body, 404)
    assert str(restored) == str(raised.value)
    assert restored.response.status_code == 404
    # The token must not end up in result backends or logs
    assert b"Bearer t" not in pickle.dumps(raised.value)
    assert restored.response.request.headers["authorization"] == "[redacted]"
    assert raised.value.response.request.headers["authorization"] == "Bearer t"


def test_pickled_connection_error_hides_the_token() -> None:
    def handler(request: httpx2.Request) -> httpx2.Response:
        msg = "down"
        raise httpx2.ConnectError(msg, request=request)

    with pytest.raises(APIConnectionError) as raised:
        _sync(httpx2.MockTransport(handler), RetryPolicy(max_retries=0)).request("GET", "/x")
    restored = pickle.loads(pickle.dumps(raised.value))  # noqa: S301 - our own data
    assert restored.request.headers["authorization"] == "[redacted]"
    assert str(restored.request.url) == str(raised.value.request.url)


def test_broken_response_encoding_is_a_connection_error() -> None:
    calls: list[httpx2.Request] = []

    def handler(request: httpx2.Request) -> httpx2.Response:
        calls.append(request)
        return httpx2.Response(200, headers={"Content-Encoding": "gzip"}, content=b"not gzip")

    with pytest.raises(APIConnectionError) as raised:
        _sync(httpx2.MockTransport(handler)).request("GET", "/x")
    assert isinstance(raised.value.__cause__, httpx2.DecodingError)
    assert len(calls) == 1  # not retried


def test_error_without_reason_phrase() -> None:
    def handler(_: httpx2.Request) -> httpx2.Response:
        return httpx2.Response(599, content=b"")

    with pytest.raises(InternalServerError) as raised:
        _sync(httpx2.MockTransport(handler), RetryPolicy(max_retries=0)).request("POST", "/x")
    assert str(raised.value) == "599"


# --- Retry policy ----------------------------------------------------------------------


def test_retry_policy_validates_arguments() -> None:
    with pytest.raises(ValueError, match="RetryPolicy"):
        RetryPolicy(max_retries=-1)
    with pytest.raises(ValueError, match="RetryPolicy"):
        RetryPolicy(base_delay=2.0, max_delay=1.0)


def test_retry_delay_grows_and_is_capped() -> None:
    policy = RetryPolicy(base_delay=1.0, max_delay=4.0)
    assert 1.0 <= policy.delay(0, None) <= 1.0
    assert 1.0 <= policy.delay(5, None) <= 4.0


@pytest.mark.parametrize("as_date", [False, True])
def test_retry_delay_respects_server_hints(*, as_date: bool) -> None:
    # The date is built here, not at collection time - large suites run long after collecting
    value = email.utils.formatdate(time.time() + 10, usegmt=True) if as_date else "10"
    policy = RetryPolicy(base_delay=0.0, max_delay=30.0)
    # HTTP dates have a resolution of one second
    assert 8.0 <= policy.delay(0, httpx2.Response(429, headers={"Retry-After": value})) <= 10.0


@pytest.mark.parametrize(
    "headers",
    [{}, {"Retry-After": "sometime"}, {"RateLimit-Reset": str(int(time.time()) + 3000)}],
)
def test_retry_delay_ignores_unusable_hints(headers: dict[str, str]) -> None:
    policy = RetryPolicy(base_delay=0.0, max_delay=10.0)
    assert policy.delay(0, httpx2.Response(429, headers=headers)) == 0.0


# --- Encoding and helper types ---------------------------------------------------------


def test_encode_query() -> None:
    when = datetime(2026, 1, 2, 3, 4, 5, tzinfo=UTC)
    assert encode_query(
        {
            "a": "x",
            "b": None,
            "c": True,
            "d": False,
            "e": ["1", "2"],
            "f": when,
            "g": date(2026, 1, 2),
            "h": Decimal("1.5"),
            "i": 7,
        },
    ) == (
        ("a", "x"),
        ("c", "true"),
        ("d", "false"),
        ("e", "1"),
        ("e", "2"),
        ("f", "2026-01-02T03:04:05+00:00"),
        ("g", "2026-01-02"),
        ("h", "1.5"),
        ("i", "7"),
    )


def test_encode_query_rejects_naive_datetimes() -> None:
    with pytest.raises(ValueError, match="naive datetime"):
        encode_query({"start": datetime(2026, 1, 2)})  # noqa: DTZ001 - deliberately naive


def test_encode_body_drops_not_given_but_keeps_none() -> None:
    assert encode_body({"a": NOT_GIVEN, "b": None, "c": 1}) == {"b": None, "c": 1}


def test_encode_body_turns_any_mapping_and_sequence_into_json_containers() -> None:
    body = encode_body({"labels": MappingProxyType({"a": "b"}), "ids": range(2), "name": "x"})
    assert body == {"labels": {"a": "b"}, "ids": [0, 1], "name": "x"}


def test_encode_headers_drops_none() -> None:
    assert encode_headers({"X-A": "1", "X-B": None, "X-C": 2}) == {"X-A": "1", "X-C": "2"}


def test_encode_headers_joins_lists_and_spells_booleans() -> None:
    assert encode_headers({"X-L": ["a", "b"], "X-T": True}) == {"X-L": "a,b", "X-T": "true"}


def test_encode_query_delimited_lists() -> None:
    assert encode_query(
        {"a": ["1", "2"], "b": [3, 4], "c": [], "d": ["x", "y"]},
        delimited={"a": ",", "b": "|", "c": ","},
    ) == (("a", "1,2"), ("b", "3|4"), ("d", "x"), ("d", "y"))


def test_request_sends_json_null_but_no_body_without_json() -> None:
    recorder = Recorder.sequence([(200, {"ok": True}), (200, {"ok": True})])
    transport = _sync(httpx2.MockTransport(recorder))
    transport.request("PUT", "/x", json_body=None)
    transport.request("GET", "/x")
    assert recorder.requests[0].content == b"null"
    assert recorder.requests[1].content == b""
    assert "Content-Type" not in recorder.requests[1].headers


def test_request_headers_ignore_case() -> None:
    recorder = Recorder(200, {"ok": True})
    transport = _sync(httpx2.MockTransport(recorder))
    transport.request("GET", "/x", headers={"accept": "text/csv"})
    assert recorder.only().headers.get_list("Accept") == ["text/csv"]


def test_request_keeps_a_json_content_type_of_the_spec() -> None:
    recorder = Recorder(200, {"ok": True})
    content_type = "application/merge-patch+json"
    transport = _sync(httpx2.MockTransport(recorder))
    transport.request("PATCH", "/x", json_body={"a": 1}, headers={"content-type": content_type})
    assert recorder.only().headers.get_list("Content-Type") == [content_type]


def test_request_merges_extra_headers() -> None:
    recorder = Recorder(200, {"ok": True})
    _sync(httpx2.MockTransport(recorder)).request("GET", "/x", headers={"X-Extra": "1"})
    assert recorder.only().headers["X-Extra"] == "1"


def test_encode_path_escapes() -> None:
    assert encode_path("a/b c") == "a%2Fb%20c"
    assert encode_path(42) == "42"
    assert encode_path(1.5) == "1.5"
    assert encode_path(True) == "true"  # noqa: FBT003 - value of a path parameter
    assert encode_path(date(2026, 1, 2)) == "2026-01-02"


def test_not_given_is_falsy_and_readable() -> None:
    assert not NOT_GIVEN
    assert repr(NOT_GIVEN) == "NOT_GIVEN"


def test_error_schema_is_chosen_by_status() -> None:
    class Exact(BaseModel):
        pass

    class Range(BaseModel):
        pass

    class Fallback(BaseModel):
        pass

    errors: ErrorModels = {"404": Exact, "4XX": Range, "default": Fallback}
    assert error_model_for(404, errors) is Exact
    assert error_model_for(418, errors) is Range
    assert error_model_for(500, errors) is Fallback
    assert error_model_for(500, {}) is None


def test_problem_details_are_read_from_problem_json() -> None:
    def handler(_: httpx2.Request) -> httpx2.Response:
        body = {"type": "about:blank", "title": "Gone", "status": 410, "detail": 5, "trace": "t1"}
        return httpx2.Response(410, json=body, headers={"Content-Type": "application/problem+json"})

    with pytest.raises(APIStatusError) as raised:
        _sync(httpx2.MockTransport(handler), RetryPolicy(max_retries=0)).request("GET", "/x")
    problem = raised.value.problem
    assert problem == ProblemDetails(
        type="about:blank", title="Gone", status=410, extensions={"trace": "t1"}
    )  # detail has the wrong type: absent
    # plain JSON is no problem details
    with pytest.raises(NotFoundError) as plain:
        _sync(httpx2.MockTransport(Recorder(*_error(404))), RetryPolicy(max_retries=0)).request(
            "GET", "/x"
        )
    assert plain.value.problem is None


def test_retry_after_is_read_from_the_error() -> None:
    recorder = Recorder(*_error(429), headers={"Retry-After": "7"})
    with pytest.raises(RateLimitError) as raised:
        _sync(httpx2.MockTransport(recorder), RetryPolicy(max_retries=0)).request("GET", "/x")
    assert raised.value.retry_after == 7.0


def test_error_body_is_read_as_the_schema_of_the_spec() -> None:
    errors: ErrorModels = {"4XX": models.ErrorResponse}
    found = Recorder(404, ERROR_RESPONSE)
    with pytest.raises(NotFoundError) as raised:
        _sync(httpx2.MockTransport(found), RetryPolicy(max_retries=0)).request(
            "GET", "/x", errors=errors
        )
    assert raised.value.error == validated(models.ErrorResponse, ERROR_RESPONSE)
    # a body that does not match the schema: no error, the JSON is still in body
    broken = Recorder(404, ["not", "the", "schema"])
    with pytest.raises(NotFoundError) as raised:
        _sync(httpx2.MockTransport(broken), RetryPolicy(max_retries=0)).request(
            "GET", "/x", errors=errors
        )
    assert raised.value.error is None
    assert raised.value.body == ["not", "the", "schema"]


def test_models_are_hashable_by_value() -> None:
    first = validated(models.Action, ACTION)
    second = validated(models.Action, ACTION)
    assert first == second
    assert hash(first) == hash(second)


def test_unknown_value_is_a_marked_string() -> None:
    value = UnknownValue("new")
    assert value == "new"
    assert repr(value) == "UnknownValue('new')"
    parsed = TypeAdapter(UnknownValue).validate_json('"later"')
    assert type(parsed) is UnknownValue


# --- Client ----------------------------------------------------------------------------


def test_client_credentials_are_checked(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("HCLOUD_TOKEN", raising=False)
    with pytest.raises(HetznerError, match="no credentials"):
        Hetzner()
    with pytest.raises(HetznerError, match="no credentials"):
        AsyncHetzner()


def test_client_reads_credentials_from_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("HCLOUD_TOKEN", "from-environment")
    recorder = Recorder(*_error(404, "not_found"))
    http_client = httpx2.Client(transport=httpx2.MockTransport(recorder))
    client = Hetzner(http_client=http_client, retry=RetryPolicy(max_retries=0))
    with client, pytest.raises(APIStatusError):
        client.actions.get_action(42)
    request = recorder.requests[0]
    assert "from-environment" in f"{request.url} {dict(request.headers)}"


def test_client_repr_shows_urls_but_never_credentials() -> None:
    with Hetzner(token="test-token") as client:
        text = repr(client)
    assert text.startswith("Hetzner(SyncTransport(cloud=")
    assert "test-" not in text

    async def run() -> str:
        async with AsyncHetzner(token="test-token") as client:
            return repr(client)

    assert asyncio.run(run()).startswith("AsyncHetzner(AsyncTransport(")


def test_clients_close_their_connections() -> None:
    Hetzner(token="test-token").close()

    async def run() -> None:
        async with AsyncHetzner(token="test-token") as client:
            assert client is not None

    asyncio.run(run())
