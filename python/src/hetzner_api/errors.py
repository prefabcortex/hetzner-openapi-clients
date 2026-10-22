"""All exceptions of the client.

Hierarchy::

    HetznerError
    ├── APIConnectionError          network/DNS/TLS/broken response
    │   └── APITimeoutError
    ├── APIStatusError              error status (4xx/5xx)
    │   ├── BadRequestError         400
    │   ├── AuthenticationError     401
    │   ├── PermissionDeniedError   403
    │   ├── NotFoundError           404
    │   ├── ConflictError           409 / 423
    │   ├── PreconditionFailedError 412
    │   ├── UnprocessableEntityError 422
    │   ├── RateLimitError          429
    │   └── InternalServerError     5xx
    ├── RequestValidationError      arguments break a rule of the spec (strict mode)
    └── ResponseValidationError     response does not match the spec
"""

import copy
import email.utils
import time
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from http import HTTPStatus
from typing import Final, override

import httpx2
import pydantic_core
from pydantic import BaseModel, JsonValue, ValidationError

from hetzner_api._auth import redacted_request, redacted_url
from hetzner_api.models import ErrorResponse

# Longer error bodies are cut in the message (the whole body is in ``body``/``response``)
_MAX_TEXT: Final = 500

type ErrorModels = Mapping[str, type[BaseModel]]
"""The error schemas of one operation by status: ``"404"``, ``"4XX"`` or ``"default"``."""
type ErrorModel = ErrorResponse
"""Any error schema of the spec (``APIStatusError.error``)."""

__all__ = [
    "APIConnectionError",
    "APIStatusError",
    "APITimeoutError",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "ErrorModel",
    "ErrorModels",
    "HetznerError",
    "InternalServerError",
    "NotFoundError",
    "PermissionDeniedError",
    "PreconditionFailedError",
    "ProblemDetails",
    "RateLimitError",
    "RequestValidationError",
    "ResponseValidationError",
    "UnprocessableEntityError",
    "error_from_response",
    "error_model_for",
    "requested_delay",
]


class HetznerError(Exception):
    """Base of all errors of this client - ``except HetznerError`` catches everything."""

    @override
    def __reduce__(self) -> tuple[Callable[..., HetznerError], tuple[object, ...]]:
        # Picklable (multiprocessing, Celery, pytest-xdist), although __init__ takes keywords.
        # Pickled errors end up in result backends and logs: the token is redacted.
        state = {name: _redacted(value) for name, value in vars(self).items()}
        return _restore, (type(self), self.args, state)


def _redacted(value: object) -> object:
    match value:
        case httpx2.Request():
            return redacted_request(value)
        case httpx2.Response():
            redacted = copy.copy(value)
            redacted.request = redacted_request(value.request)
            return redacted
        case _:
            return value


def _restore(
    error_type: type[HetznerError],
    args: tuple[object, ...],
    state: dict[str, object],
) -> HetznerError:
    error = error_type.__new__(error_type, *args)
    error.args = args
    vars(error).update(state)
    return error


class APIConnectionError(HetznerError):
    """The HTTP exchange failed (network, DNS, TLS, dropped connection, bad encoding, redirects)."""

    def __init__(self, request: httpx2.Request, cause: httpx2.RequestError) -> None:
        super().__init__(f"{request.method} {redacted_url(request.url)}: {cause}")
        self.request: Final = request


class APITimeoutError(APIConnectionError):
    """Timeout while connecting, sending or reading."""


class APIStatusError(HetznerError):
    """The API answered with an error status.

    Attributes:
        status_code: HTTP status.
        error: The body as the error schema the spec names for this operation and status
            (``None`` if it names none or the body does not match it).
        body: The response body as JSON (``None`` if it is empty or no JSON).
        retry_after: Seconds the API asks to wait (``Retry-After``), if it says so.
        problem: The body as RFC 9457 problem details, if it is ``application/problem+json``.
        response: The complete HTTP response.
    """

    def __init__(
        self, response: httpx2.Response, *, body: JsonValue, error: ErrorModel | None = None
    ) -> None:
        title = f"{response.status_code} {response.reason_phrase}".rstrip()
        text = response.text.strip()
        super().__init__(f"{title}: {text[:_MAX_TEXT]}" if text else title)
        self.response: Final = response
        self.status_code: Final = response.status_code
        self.error: Final = error
        self.body: Final = body
        self.retry_after: Final = requested_delay(response)
        self.problem: Final = ProblemDetails.of(response, body)


class BadRequestError(APIStatusError):
    """400 - the request is invalid."""


class AuthenticationError(APIStatusError):
    """401 - the token is missing or invalid."""


class PermissionDeniedError(APIStatusError):
    """403 - not allowed (e.g. a read-only token)."""


class NotFoundError(APIStatusError):
    """404 - the resource does not exist."""


class ConflictError(APIStatusError):
    """409/423 - conflict or resource locked."""


class PreconditionFailedError(APIStatusError):
    """412 - a precondition of the request is not met."""


class UnprocessableEntityError(APIStatusError):
    """422 - the request is well-formed but semantically invalid."""


class RateLimitError(APIStatusError):
    """429 - too many requests (retried automatically until the retries are used up)."""


class InternalServerError(APIStatusError):
    """5xx - an error on the side of the API."""


class RequestValidationError(HetznerError, ValueError):
    """Arguments break rules of the spec (``maxLength``, ``pattern`` …) - nothing was sent.

    Raised only with ``validation="strict"``.

    Attributes:
        problems: One message per broken rule (``"name: longer than 63 characters"``).
    """

    def __init__(self, problems: Sequence[str]) -> None:
        super().__init__("; ".join(problems))
        self.problems: Final = tuple(problems)


class ResponseValidationError(HetznerError):
    """The response of the API does not match the schema of the spec.

    Attributes:
        response: The HTTP response.
        errors: The validation errors reported by pydantic.
    """

    def __init__(self, response: httpx2.Response, error: ValidationError) -> None:
        request = response.request
        super().__init__(f"{request.method} {redacted_url(request.url)}: {error}")
        self.response: Final = response
        self.errors: Final = error.errors()


_BY_STATUS: Final[dict[int, type[APIStatusError]]] = {
    HTTPStatus.BAD_REQUEST: BadRequestError,
    HTTPStatus.UNAUTHORIZED: AuthenticationError,
    HTTPStatus.FORBIDDEN: PermissionDeniedError,
    HTTPStatus.NOT_FOUND: NotFoundError,
    HTTPStatus.CONFLICT: ConflictError,
    HTTPStatus.LOCKED: ConflictError,
    HTTPStatus.PRECONDITION_FAILED: PreconditionFailedError,
    HTTPStatus.UNPROCESSABLE_ENTITY: UnprocessableEntityError,
    HTTPStatus.TOO_MANY_REQUESTS: RateLimitError,
}


@dataclass(frozen=True, slots=True, kw_only=True)
class ProblemDetails:
    """An RFC 9457 error body (``application/problem+json``) - read for any API.

    Members of the wrong type count as absent; members beyond the five of the RFC are in
    ``extensions``.
    """

    type: str | None = None
    title: str | None = None
    status: int | None = None
    detail: str | None = None
    instance: str | None = None
    extensions: Mapping[str, JsonValue] = field(default_factory=dict[str, JsonValue])

    @classmethod
    def of(cls, response: httpx2.Response, body: JsonValue) -> ProblemDetails | None:
        """The problem details of ``response`` - ``None`` unless it is problem+json (an object)."""
        media = response.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
        if media != "application/problem+json" or not isinstance(body, dict):
            return None

        def text(key: str) -> str | None:
            value = body.get(key)
            return value if isinstance(value, str) else None

        status = body.get("status")
        known = {"type", "title", "status", "detail", "instance"}
        return cls(
            type=text("type"),
            title=text("title"),
            # bool is an int in Python - but not a status
            status=status if isinstance(status, int) and not isinstance(status, bool) else None,
            detail=text("detail"),
            instance=text("instance"),
            extensions={key: value for key, value in body.items() if key not in known},
        )


def error_model_for(status: int, errors: ErrorModels) -> type[BaseModel] | None:
    """The schema the spec names for ``status``: exact status, then ``4XX``, then ``default``."""
    return errors.get(str(status)) or errors.get(f"{status // 100}XX") or errors.get("default")


def requested_delay(response: httpx2.Response) -> float | None:
    """Seconds from ``Retry-After`` (a number or an HTTP date), or ``None``."""
    retry_after = response.headers.get("Retry-After")
    if retry_after is not None:
        if retry_after.isdigit():
            return float(retry_after)
        try:
            moment = email.utils.parsedate_to_datetime(retry_after)
        except TypeError, ValueError:
            return None
        return max(0.0, moment.timestamp() - time.time())
    # RateLimit-Reset is deliberately ignored: it is the moment the budget is *full* again
    # (up to an hour away), not when the next request is allowed.
    return None


def error_from_response(
    response: httpx2.Response, error: ErrorModel | None = None
) -> APIStatusError:
    """Builds the matching exception for an error response (``error``: its parsed schema)."""
    try:
        body: JsonValue = pydantic_core.from_json(response.content) if response.content else None
    except ValueError:
        body = None
    if response.status_code >= HTTPStatus.INTERNAL_SERVER_ERROR:
        error_type: type[APIStatusError] = InternalServerError
    else:
        error_type = _BY_STATUS.get(response.status_code, APIStatusError)
    return error_type(response, body=body, error=error)
