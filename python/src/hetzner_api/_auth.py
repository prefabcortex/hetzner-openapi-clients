"""Authentication: the credentials of the client and which of them a request carries.

Each operation names the alternatives of the spec (``security``); the first alternative whose
credentials the client has is sent. Credentials never appear in ``repr()``, logs or pickled
errors.
"""

import base64
import copy
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Final, Literal, Protocol, final

import httpx2

__all__ = [
    "ARGUMENTS",
    "SECRET_HEADERS",
    "SECRET_QUERY",
    "ApiKey",
    "BasicAuth",
    "BearerToken",
    "Credential",
    "Security",
    "Signing",
    "redacted_request",
    "redacted_url",
    "sign",
]

type Security = tuple[tuple[str, ...], ...] | None
"""Alternatives of an operation, each the names of schemes that apply together.

``()`` inside means "no credentials needed"; ``None``: the spec says nothing - every credential
the client has is sent.
"""

SECRET_HEADERS: Final[frozenset[str]] = frozenset({"authorization"})
"""Headers holding credentials (lower case) - redacted wherever requests are shown."""
SECRET_QUERY: Final[frozenset[str]] = frozenset[str]()
"""Query parameters holding credentials - redacted wherever URLs are shown."""

ARGUMENTS: Final[Mapping[str, str]] = {
    "APIToken": "token",
}
"""Scheme → the client arguments that set its credentials (for error messages)."""

_REDACTED: Final = "[redacted]"


@dataclass(slots=True)
class Signing:
    """What credentials add to a request."""

    headers: dict[str, str] = field(default_factory=dict[str, str])
    query: list[tuple[str, str]] = field(default_factory=list[tuple[str, str]])
    cookies: list[tuple[str, str]] = field(default_factory=list[tuple[str, str]])


class Credential(Protocol):
    """Something that signs a request."""

    def apply(self, signing: Signing) -> None:
        """Adds the credential to ``signing``."""
        ...


@final
@dataclass(frozen=True, slots=True)
class BearerToken:
    """``Authorization: Bearer <token>`` (``http bearer``, OAuth2, OpenID Connect)."""

    token: str = field(repr=False)

    def apply(self, signing: Signing) -> None:
        """Sets the ``Authorization`` header."""
        signing.headers["Authorization"] = f"Bearer {self.token}"


@final
@dataclass(frozen=True, slots=True)
class BasicAuth:
    """``Authorization: Basic ...`` (``http basic``)."""

    username: str
    password: str = field(repr=False)

    def apply(self, signing: Signing) -> None:
        """Sets the ``Authorization`` header."""
        pair = f"{self.username}:{self.password}".encode()
        signing.headers["Authorization"] = f"Basic {base64.b64encode(pair).decode()}"


@final
@dataclass(frozen=True, slots=True)
class ApiKey:
    """An API key in a header, the query or a cookie (``apiKey``)."""

    location: Literal["header", "query", "cookie"]
    name: str
    value: str = field(repr=False)

    def apply(self, signing: Signing) -> None:
        """Adds the key where the spec says."""
        if self.location == "header":
            signing.headers[self.name] = self.value
        elif self.location == "query":
            signing.query.append((self.name, self.value))
        else:
            signing.cookies.append((self.name, self.value))


def sign(credentials: Mapping[str, Credential], security: Security) -> Signing | None:
    """What a request with ``security`` carries - ``None`` if the client lacks credentials."""
    signing = Signing()
    if security is None:
        chosen: tuple[str, ...] = tuple(credentials)
    else:
        found = next(
            (
                alternative
                for alternative in security
                if all(name in credentials for name in alternative)
            ),
            None,
        )
        if found is None:
            return None
        chosen = found
    for name in chosen:
        credentials[name].apply(signing)
    return signing


def redacted_url(url: httpx2.URL, secret: frozenset[str] = SECRET_QUERY) -> httpx2.URL:
    """``url`` with the values of credential query parameters (``secret``) replaced."""
    if not any(name in secret for name in url.params):
        return url
    params = tuple(
        (name, _REDACTED if name in secret else value) for name, value in url.params.multi_items()
    )
    return url.copy_with(params=httpx2.QueryParams(params))


def redacted_request(request: httpx2.Request) -> httpx2.Request:
    """A copy of ``request`` without credentials (headers, query, cookies)."""
    redacted = copy.copy(request)
    redacted.url = redacted_url(request.url)
    redacted.headers = httpx2.Headers(
        [
            (name, _REDACTED if name.lower() in SECRET_HEADERS else header)
            for name, header in request.headers.multi_items()
        ],
    )
    return redacted
