"""Strictly typed Python client for the Hetzner API (generated).

Example::

    from hetzner_api import Hetzner

    with Hetzner() as client:
        ...

Response models live in ``models``, request types in ``params``.
"""

from hetzner_api._base_client import RetryPolicy
from hetzner_api._client import AsyncHetzner, Hetzner
from hetzner_api._types import NOT_GIVEN, NotGiven, UnknownValue
from hetzner_api._validation import Validation
from hetzner_api.errors import (
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    HetznerError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    PreconditionFailedError,
    ProblemDetails,
    RateLimitError,
    RequestValidationError,
    ResponseValidationError,
    UnprocessableEntityError,
)

__all__ = [
    "NOT_GIVEN",
    "APIConnectionError",
    "APIStatusError",
    "APITimeoutError",
    "AsyncHetzner",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "Hetzner",
    "HetznerError",
    "InternalServerError",
    "NotFoundError",
    "NotGiven",
    "PermissionDeniedError",
    "PreconditionFailedError",
    "ProblemDetails",
    "RateLimitError",
    "RequestValidationError",
    "ResponseValidationError",
    "RetryPolicy",
    "UnknownValue",
    "UnprocessableEntityError",
    "Validation",
]
