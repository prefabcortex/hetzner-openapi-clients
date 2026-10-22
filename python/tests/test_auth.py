"""Authentication: credentials, choosing them per operation, keeping them secret."""

import pickle

import httpx2
import pytest

from hetzner_api import HetznerError, NotFoundError, RetryPolicy
from hetzner_api._auth import (
    ApiKey,
    BasicAuth,
    BearerToken,
    Credential,
    Signing,
    redacted_request,
    redacted_url,
    sign,
)
from hetzner_api._base_client import SyncTransport
from tests.support import Recorder

CREDENTIALS: dict[str, Credential] = {
    "bearer": BearerToken("secret-token"),
    "basic": BasicAuth("user", "secret-password"),
    "header": ApiKey("header", "X-Api-Key", "secret-header"),
    "query": ApiKey("query", "api_key", "secret-query"),
    "cookie": ApiKey("cookie", "session", "secret cookie"),
}


def _transport(recorder: Recorder, credentials: dict[str, Credential]) -> SyncTransport:
    return SyncTransport(
        credentials=credentials,
        base_urls={"main": "https://api.example.test"},
        default_server="main",
        retry=RetryPolicy(max_retries=0),
        timeout=5.0,
        http_client=httpx2.Client(transport=httpx2.MockTransport(recorder)),
    )


def test_credentials_sign_where_the_spec_says() -> None:
    signing = Signing()
    for credential in CREDENTIALS.values():
        credential.apply(signing)
    assert signing.headers == {
        "Authorization": "Basic dXNlcjpzZWNyZXQtcGFzc3dvcmQ=",  # the later one wins
        "X-Api-Key": "secret-header",
    }
    assert signing.query == [("api_key", "secret-query")]
    assert signing.cookies == [("session", "secret cookie")]
    assert "secret" not in repr(CREDENTIALS)


def test_the_first_satisfiable_alternative_is_sent() -> None:
    have: dict[str, Credential] = {"header": CREDENTIALS["header"], "query": CREDENTIALS["query"]}
    signing = sign(have, (("bearer",), ("header", "query"), ("header",)))
    assert signing is not None
    assert signing.headers == {"X-Api-Key": "secret-header"}
    assert signing.query == [("api_key", "secret-query")]
    # "()" needs nothing; None (the spec says nothing) sends everything there is
    assert sign(have, (("bearer",), ())) == Signing()
    everything = sign(have, None)
    assert everything is not None
    assert everything.query == [("api_key", "secret-query")]
    assert sign(have, (("bearer",),)) is None


def test_requests_carry_their_credentials() -> None:
    recorder = Recorder(204)
    transport = _transport(recorder, CREDENTIALS)
    transport.request("GET", "/x", params=(("page", "1"),), security=(("query", "cookie"),))
    transport.request(
        "GET", "/x", headers={"Cookie": "theme=dark"}, security=(("cookie", "bearer"),)
    )
    first, second = recorder.requests
    assert first.url.params.multi_items() == [("page", "1"), ("api_key", "secret-query")]
    assert first.headers["cookie"] == "session=secret%20cookie"
    assert "authorization" not in first.headers
    assert second.headers["cookie"] == "theme=dark; session=secret%20cookie"
    assert second.headers["authorization"] == "Bearer secret-token"


def test_missing_credentials_are_reported_before_sending() -> None:
    recorder = Recorder(204)
    transport = _transport(recorder, {})
    with pytest.raises(HetznerError, match=r"needs credentials .*: .+=\.\.\."):
        transport.request("GET", "/x", security=(("APIToken",), ("a", "b")))
    assert recorder.requests == []


def test_credentials_never_show_in_errors() -> None:
    recorder = Recorder(404, {"error": {"code": "not_found", "message": "gone"}})
    transport = _transport(recorder, CREDENTIALS)
    with pytest.raises(NotFoundError) as raised:
        transport.request("GET", "/x", security=(("bearer", "query"),))
    restored = pickle.loads(pickle.dumps(raised.value))  # noqa: S301 - our own data
    assert restored.response.request.headers["authorization"] == "[redacted]"
    assert b"secret-token" not in pickle.dumps(raised.value)


def test_redaction() -> None:
    url = httpx2.URL("https://api.example.test/x?api_key=secret&page=2")
    assert str(redacted_url(url, frozenset({"api_key"}))) == (
        "https://api.example.test/x?api_key=%5Bredacted%5D&page=2"
    )
    assert redacted_url(url, frozenset()) is url
    request = httpx2.Request("GET", url, headers={"Authorization": "Bearer secret", "X-Other": "a"})
    redacted = redacted_request(request)
    assert redacted.headers["authorization"] == "[redacted]"
    assert redacted.headers["x-other"] == "a"
    assert request.headers["authorization"] == "Bearer secret"
