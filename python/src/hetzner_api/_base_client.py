"""HTTP transport (sync + async): authentication, retries, error mapping."""

import logging
import random
import time
from collections.abc import Mapping, Sequence
from datetime import date, datetime
from decimal import Decimal
from http import HTTPStatus
from typing import Final, cast, override
from urllib.parse import quote

import anyio
import httpx2
import pydantic_core
from pydantic import BaseModel, ValidationError

from hetzner_api._auth import ARGUMENTS, Credential, Security, redacted_url, sign
from hetzner_api._types import NOT_GIVEN, NotGiven
from hetzner_api._validation import STRICT, Check, Validation, ValueType, lenient
from hetzner_api.errors import (
    APIConnectionError,
    APITimeoutError,
    ErrorModel,
    ErrorModels,
    HetznerError,
    RequestValidationError,
    ResponseValidationError,
    error_from_response,
    error_model_for,
    requested_delay,
)

__all__ = [
    "AsyncTransport",
    "QueryValue",
    "RetryPolicy",
    "SyncTransport",
    "encode_body",
    "encode_headers",
    "encode_path",
    "encode_query",
]

type Scalar = str | int | float | bool | datetime | date | Decimal
type JsonBody = object  # anything pydantic_core.to_json can serialize
type QueryValue = Scalar | Sequence[Scalar] | None

_IDEMPOTENT: Final = frozenset({"GET", "HEAD", "PUT", "DELETE", "OPTIONS", "QUERY"})
_RETRY_STATUS_IDEMPOTENT: Final = frozenset(
    {HTTPStatus.BAD_GATEWAY, HTTPStatus.SERVICE_UNAVAILABLE, HTTPStatus.GATEWAY_TIMEOUT},
)
_DEFAULT_TIMEOUT: Final = 30.0
_USER_AGENT: Final = "hetzner-api/0.1.0 (python; httpx2)"
_LOG: Final = logging.getLogger("hetzner_api")


class RetryPolicy:
    """When to retry and how long to wait before the next attempt.

    Exponential backoff with "full jitter" (``base * 2**attempt``, capped), but never shorter
    than a ``Retry-After`` sent by the API.

    Retried are: ``429``, connection failures, and - only for idempotent methods -
    ``502``/``503``/``504`` and read timeouts.

    A ``Retry-After`` longer than ``max_delay`` is not waited for: the error is raised at once
    instead of blocking the caller for minutes.

    Args:
        max_retries: Additional attempts after the first one (0 = never retry).
        base_delay: Delay before the first retry in seconds.
        max_delay: Upper bound of a single delay in seconds.
    """

    __slots__ = ("base_delay", "max_delay", "max_retries")

    def __init__(
        self, *, max_retries: int = 5, base_delay: float = 1.0, max_delay: float = 60.0
    ) -> None:
        if max_retries < 0 or base_delay < 0 or max_delay < base_delay:
            msg = "invalid RetryPolicy"
            raise ValueError(msg)
        self.max_retries: Final = max_retries
        self.base_delay: Final = base_delay
        self.max_delay: Final = max_delay

    def should_retry(self, method: str, response: httpx2.Response) -> bool:
        """Should the request be retried after this response?"""
        requested = requested_delay(response)
        if requested is not None and requested > self.max_delay:
            return False
        if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
            return True
        return method in _IDEMPOTENT and response.status_code in _RETRY_STATUS_IDEMPOTENT

    def delay(self, attempt: int, response: httpx2.Response | None) -> float:
        """Delay before attempt ``attempt + 1`` (``attempt`` starts at 0)."""
        backoff = min(self.max_delay, self.base_delay * 2**attempt)
        jittered = random.uniform(self.base_delay, backoff)  # noqa: S311 - no cryptographic randomness needed
        requested = requested_delay(response) if response is not None else None
        if requested is None:
            return jittered
        return min(self.max_delay, max(jittered, requested))


def encode_path(value: Scalar) -> str:
    """Encodes a path parameter (``/`` and friends are escaped)."""
    return quote(_scalar(value), safe="")


def encode_query(
    values: Mapping[str, QueryValue], *, delimited: Mapping[str, str] | None = None
) -> tuple[tuple[str, str], ...]:
    """Query parameters; ``None`` is dropped.

    Lists are repeated (``?a=1&a=2``), or joined for the keys in ``delimited`` (``?a=1,2``).
    """
    pairs: list[tuple[str, str]] = []
    for key, value in values.items():
        if value is None:
            continue
        if isinstance(value, (str, int, float, bool, datetime, date, Decimal)):
            pairs.append((key, _scalar(value)))
            continue
        items = [_scalar(item) for item in value]
        if delimited is not None and key in delimited:
            if items:
                pairs.append((key, delimited[key].join(items)))
        else:
            pairs.extend((key, item) for item in items)
    return tuple(pairs)


def _scalar(value: Scalar) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, datetime) and value.tzinfo is None:
        # Without a timezone the moment is ambiguous (and not RFC 3339)
        msg = f"naive datetime {value.isoformat()} - pass a timezone-aware datetime"
        raise ValueError(msg)
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    return str(value)


def encode_headers(values: Mapping[str, QueryValue]) -> dict[str, str]:
    """Header parameters; ``None`` is dropped, lists are joined with commas."""
    headers: dict[str, str] = {}
    for key, value in values.items():
        if value is None:
            continue
        if isinstance(value, (str, int, float, bool, datetime, date, Decimal)):
            headers[key] = _scalar(value)
        else:
            headers[key] = ",".join(_scalar(item) for item in value)
    return headers


def encode_body(values: Mapping[str, object]) -> dict[str, object]:
    """JSON body; ``NOT_GIVEN`` values are dropped, ``None`` becomes ``null``.

    Any ``Mapping`` becomes a ``dict`` and any non-string ``Sequence`` a ``list`` (e.g. a
    ``MappingProxyType`` or a ``range``), so everything that type-checks also serializes.
    """
    return {key: _plain(value) for key, value in values.items() if not isinstance(value, NotGiven)}


def _plain(value: object) -> object:
    # isinstance() does not know the element types - cast makes "anything" explicit
    if isinstance(value, Mapping):
        return {key: _plain(entry) for key, entry in cast("Mapping[object, object]", value).items()}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return [_plain(entry) for entry in cast("Sequence[object]", value)]
    return value


def _needed(security: Security) -> str:
    """The client arguments that would satisfy ``security`` (for the error message)."""
    options = [
        " and ".join(f"{ARGUMENTS.get(name, name)}=..." for name in alternative)
        for alternative in security or ()
        if alternative
    ]
    return " or ".join(options)


def _summary(error: ValidationError) -> str:
    """The first problems of ``error`` in one line (for the log)."""
    problems = [
        f"{'.'.join(str(part) for part in detail['loc']) or 'response'}: {detail['msg']}"
        for detail in error.errors()[:3]
    ]
    more = error.error_count() - len(problems)
    return "; ".join(problems) + (f" (and {more} more)" if more > 0 else "")


class _TransportBase:
    __slots__ = (
        "_base_urls",
        "_context",
        "_credentials",
        "_default_server",
        "_headers",
        "_retry",
        "_timeout",
        "_validation",
    )

    def __init__(
        self,
        *,
        credentials: Mapping[str, Credential],
        base_urls: Mapping[str, str],
        default_server: str,
        retry: RetryPolicy,
        timeout: float | httpx2.Timeout | NotGiven | None,
        headers: Mapping[str, str] | None,
        validation: Validation,
    ) -> None:
        self._credentials: Final = dict(credentials)
        self._validation: Final = validation
        self._context: Final = STRICT if validation == "strict" else None
        # NOT_GIVEN: the timeout of the HTTP client (ours: _DEFAULT_TIMEOUT); otherwise per
        # request, so it also applies to an http_client passed in from outside. None = no timeout
        self._timeout: Final = timeout
        self._base_urls: Final = dict(base_urls)
        self._default_server: Final = default_server
        self._retry: Final = retry
        self._headers: Final = {
            "Accept": "application/json",
            "User-Agent": _USER_AGENT,
            **(headers or {}),
        }

    @override
    def __repr__(self) -> str:
        urls = ", ".join(f"{name}={url!r}" for name, url in self._base_urls.items())
        return f"{type(self).__name__}({urls})"  # never the token

    def validate(self, checks: Mapping[str, Check], /, **values: object) -> None:
        """Checks arguments against the rules of the spec - in strict mode only.

        Raises:
            RequestValidationError: An argument breaks a rule (nothing is sent).
        """
        if self._validation != "strict":
            return
        problems = [
            problem
            for name, value in values.items()
            if not isinstance(value, NotGiven)
            for problem in checks[name].problems(_plain(value), name)
        ]
        if problems:
            raise RequestValidationError(problems)

    def parse[M: BaseModel](self, model: type[M], response: httpx2.Response) -> M:
        """The response as ``model`` - how strictly depends on ``validation`` of the client.

        Raises:
            ResponseValidationError: The response does not match the spec (in lax mode: it is no
                JSON object at all).
        """
        try:
            return model.model_validate_json(response.content, context=self._context)
        except ValidationError as error:
            kept = self._lenient(model, response, error)
            if not isinstance(kept, model):
                raise ResponseValidationError(response, error) from error
            return kept

    def parse_value[T](self, value_type: ValueType[T], response: httpx2.Response) -> T:
        """A response that is no object model (list, union, scalar), like :meth:`parse`.

        Raises:
            ResponseValidationError: The response does not match the spec (in lax mode: it is no
                JSON at all).
        """
        try:
            return value_type.adapter.validate_json(response.content, context=self._context)
        except ValidationError as error:
            return cast("T", self._lenient(value_type.annotation, response, error))

    def _lenient(
        self, annotation: object, response: httpx2.Response, error: ValidationError
    ) -> object:
        """Lax mode: keep what does not match the spec as it was sent (and say so in the log)."""
        if self._validation == "strict":
            raise ResponseValidationError(response, error) from error
        try:
            data = pydantic_core.from_json(response.content)
        except ValueError:
            raise ResponseValidationError(response, error) from error
        _LOG.warning(
            "%s %s: the response does not match the spec, kept as sent: %s",
            response.request.method,
            redacted_url(response.request.url),
            _summary(error),
        )
        return lenient(annotation, data)

    def _build(
        self,
        client: httpx2.Client | httpx2.AsyncClient,
        method: str,
        path: str,
        *,
        server: str | None,
        params: tuple[tuple[str, str], ...] | None,
        json_body: JsonBody | NotGiven,
        headers: Mapping[str, str] | None,
        security: Security,
    ) -> httpx2.Request:
        name = server or self._default_server
        base_url = self._base_urls[name]
        if not base_url:
            msg = f"no base URL for {name!r} - pass {name}_base_url=... to the client"
            raise HetznerError(msg)
        url = base_url.rstrip("/") + path
        # case-insensitive: an "accept" parameter replaces the default "Accept"
        all_headers = httpx2.Headers(self._headers)
        all_headers.update(headers or {})
        content: bytes | None = None
        if not isinstance(json_body, NotGiven):  # None is sent as JSON null
            content = pydantic_core.to_json(json_body)
            # a JSON variant of the spec (application/merge-patch+json) is passed as a header
            if "Content-Type" not in all_headers:
                all_headers["Content-Type"] = "application/json"
        signing = sign(self._credentials, security)
        if signing is None:
            msg = f"{method} {path} needs credentials the client does not have: {_needed(security)}"
            raise HetznerError(msg)
        all_headers.update(signing.headers)
        if signing.cookies:
            cookies = "; ".join(f"{key}={quote(value, safe='')}" for key, value in signing.cookies)
            existing = all_headers.get("Cookie")
            all_headers["Cookie"] = f"{existing}; {cookies}" if existing else cookies
        pairs = (*(params or ()), *signing.query)
        query = httpx2.QueryParams(pairs) if pairs else None
        timeout = (
            httpx2.USE_CLIENT_DEFAULT if isinstance(self._timeout, NotGiven) else self._timeout
        )
        return client.build_request(
            method, url, params=query, headers=all_headers, content=content, timeout=timeout
        )

    def _check(
        self,
        request: httpx2.Request,
        response: httpx2.Response,
        attempt: int,
        errors: ErrorModels | None,
    ) -> bool:
        """``True`` = success; ``False`` = retry; otherwise raises."""
        _LOG.debug("%s %s -> %s", request.method, redacted_url(request.url), response.status_code)
        if response.is_success:
            return True
        if attempt < self._retry.max_retries and self._retry.should_retry(request.method, response):
            return False
        raise error_from_response(response, self._error(response, errors))

    def _error(self, response: httpx2.Response, errors: ErrorModels | None) -> ErrorModel | None:
        """The body as the error schema of the operation - ``None`` if there is none or it fails."""
        model = error_model_for(response.status_code, errors or {})
        if model is None:
            return None
        try:
            parsed = model.model_validate_json(response.content, context=self._context)
        except ValidationError:
            return None
        # errors only ever names error schemas of the spec - the cast states that
        return cast("ErrorModel", parsed)

    def _backoff(
        self,
        request: httpx2.Request,
        attempt: int,
        cause: httpx2.Response | httpx2.RequestError,
    ) -> float:
        """Delay before the next attempt; logs why the request is retried."""
        if isinstance(cause, httpx2.Response):
            delay = self._retry.delay(attempt, cause)
            reason = str(cause.status_code)
        else:
            delay = self._retry.delay(attempt, None)
            reason = type(cause).__name__
        _LOG.info(
            "retrying %s %s in %.1f s (attempt %d of %d, reason: %s)",
            request.method,
            redacted_url(request.url),
            delay,
            attempt + 2,
            self._retry.max_retries + 1,
            reason,
        )
        return delay

    def _may_retry_transport(
        self, request: httpx2.Request, error: httpx2.RequestError, attempt: int
    ) -> bool:
        # Broken encoding or redirect loops do not get better by retrying
        if attempt >= self._retry.max_retries or not isinstance(error, httpx2.TransportError):
            return False
        # Connecting failed or no pool slot = the request never left -> always safe to retry
        never_sent = isinstance(
            error, (httpx2.ConnectError, httpx2.ConnectTimeout, httpx2.PoolTimeout)
        )
        return never_sent or request.method in _IDEMPOTENT


def _connection_error(request: httpx2.Request, error: httpx2.RequestError) -> APIConnectionError:
    if isinstance(error, httpx2.TimeoutException):
        return APITimeoutError(request, error)
    return APIConnectionError(request, error)


class SyncTransport(_TransportBase):
    """Synchronous transport, shared by all resources of the synchronous client."""

    __slots__ = ("_client", "_owns_client")

    def __init__(
        self,
        *,
        credentials: Mapping[str, Credential],
        base_urls: Mapping[str, str],
        default_server: str,
        retry: RetryPolicy,
        timeout: float | httpx2.Timeout | NotGiven | None,
        http_client: httpx2.Client | None,
        headers: Mapping[str, str] | None = None,
        validation: Validation = "lax",
    ) -> None:
        super().__init__(
            credentials=credentials,
            base_urls=base_urls,
            default_server=default_server,
            retry=retry,
            timeout=timeout,
            headers=headers,
            validation=validation,
        )
        self._owns_client: Final = http_client is None
        self._client: Final = http_client or httpx2.Client(
            timeout=_DEFAULT_TIMEOUT if isinstance(timeout, NotGiven) else timeout
        )

    def request(
        self,
        method: str,
        path: str,
        *,
        server: str | None = None,
        params: tuple[tuple[str, str], ...] | None = None,
        json_body: JsonBody | NotGiven = NOT_GIVEN,
        headers: Mapping[str, str] | None = None,
        security: Security = None,
        errors: ErrorModels | None = None,
    ) -> httpx2.Response:
        """Sends a request, including retries.

        Raises:
            APIStatusError: The API answered with an error (one subclass per status).
            APIConnectionError: Network error or timeout.
        """
        request = self._build(
            self._client,
            method,
            path,
            server=server,
            params=params,
            json_body=json_body,
            headers=headers,
            security=security,
        )
        attempt = 0
        while True:
            try:
                response = self._client.send(request)
            except httpx2.RequestError as error:
                if not self._may_retry_transport(request, error, attempt):
                    raise _connection_error(request, error) from error
                time.sleep(self._backoff(request, attempt, error))
            else:
                if self._check(request, response, attempt, errors):
                    return response
                time.sleep(self._backoff(request, attempt, response))
            attempt += 1

    def close(self) -> None:
        """Closes the HTTP client (only if it was not passed in from outside)."""
        if self._owns_client:
            self._client.close()


class AsyncTransport(_TransportBase):
    """Asynchronous transport, shared by all resources of the async client."""

    __slots__ = ("_client", "_owns_client")

    def __init__(
        self,
        *,
        credentials: Mapping[str, Credential],
        base_urls: Mapping[str, str],
        default_server: str,
        retry: RetryPolicy,
        timeout: float | httpx2.Timeout | NotGiven | None,
        http_client: httpx2.AsyncClient | None,
        headers: Mapping[str, str] | None = None,
        validation: Validation = "lax",
    ) -> None:
        super().__init__(
            credentials=credentials,
            base_urls=base_urls,
            default_server=default_server,
            retry=retry,
            timeout=timeout,
            headers=headers,
            validation=validation,
        )
        self._owns_client: Final = http_client is None
        self._client: Final = http_client or httpx2.AsyncClient(
            timeout=_DEFAULT_TIMEOUT if isinstance(timeout, NotGiven) else timeout
        )

    async def request(
        self,
        method: str,
        path: str,
        *,
        server: str | None = None,
        params: tuple[tuple[str, str], ...] | None = None,
        json_body: JsonBody | NotGiven = NOT_GIVEN,
        headers: Mapping[str, str] | None = None,
        security: Security = None,
        errors: ErrorModels | None = None,
    ) -> httpx2.Response:
        """Sends a request, including retries.

        Raises:
            APIStatusError: The API answered with an error (one subclass per status).
            APIConnectionError: Network error or timeout.
        """
        request = self._build(
            self._client,
            method,
            path,
            server=server,
            params=params,
            json_body=json_body,
            headers=headers,
            security=security,
        )
        attempt = 0
        while True:
            try:
                response = await self._client.send(request)
            except httpx2.RequestError as error:
                if not self._may_retry_transport(request, error, attempt):
                    raise _connection_error(request, error) from error
                await anyio.sleep(self._backoff(request, attempt, error))
            else:
                if self._check(request, response, attempt, errors):
                    return response
                await anyio.sleep(self._backoff(request, attempt, response))
            attempt += 1

    async def aclose(self) -> None:
        """Closes the HTTP client (only if it was not passed in from outside)."""
        if self._owns_client:
            await self._client.aclose()
