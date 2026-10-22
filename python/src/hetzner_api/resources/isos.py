"""Resource ``isos`` (generated - do not edit by hand)."""

from collections.abc import Mapping
from typing import Final

from hetzner_api._auth import Security
from hetzner_api._base_client import AsyncTransport, SyncTransport, encode_path, encode_query
from hetzner_api._types import UnknownValue
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import Architecture, ErrorResponse, GetIsoResponse, ListIsosResponse

__all__ = [
    "AsyncIsosResource",
    "IsosResource",
]

_SECURITY_1: Final[Security] = (("APIToken",),)

_ERRORS_1: Final[ErrorModels] = {
    "4XX": ErrorResponse,
    "5XX": ErrorResponse,
}

_CHECKS_1: Final[Mapping[str, Check]] = {
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}

_CHECKS_2: Final[Mapping[str, Check]] = {
    "iso_id": Check(minimum=1, maximum=9007199254740991),
}


class IsosResource:
    """Operations on ``isos`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_isos(
        self,
        *,
        name: str | None = None,
        architecture: Architecture | UnknownValue | None = None,
        include_architecture_wildcard: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListIsosResponse:
        """List ISOs.

        Returns all available ISO objects.

        ``GET /isos``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            architecture: Filter resources by cpu architecture. The response will only contain the
                resources with the specified cpu architecture.
            include_architecture_wildcard: Include Images with wildcard architecture (architecture
                is null). Architecture filter must be specified.
            page: Page number to return. For more information, see "Pagination". The API default is
                ``1``.
            per_page: Maximum number of entries returned per page. For more information, see
                "Pagination". The API default is ``25``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, page=page, per_page=per_page)
        response = self._transport.request(
            "GET",
            "/isos",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "architecture": architecture,
                    "include_architecture_wildcard": include_architecture_wildcard,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListIsosResponse, response)

    def get_iso(self, iso_id: int, /) -> GetIsoResponse:
        """Get an ISO.

        Returns a specific ISO object.

        ``GET /isos/{id}``

        Args:
            iso_id: ID of the ISO.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, iso_id=iso_id)
        response = self._transport.request(
            "GET",
            f"/isos/{encode_path(iso_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(GetIsoResponse, response)


class AsyncIsosResource:
    """Operations on ``isos`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_isos(
        self,
        *,
        name: str | None = None,
        architecture: Architecture | UnknownValue | None = None,
        include_architecture_wildcard: bool | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListIsosResponse:
        """List ISOs.

        Returns all available ISO objects.

        ``GET /isos``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            architecture: Filter resources by cpu architecture. The response will only contain the
                resources with the specified cpu architecture.
            include_architecture_wildcard: Include Images with wildcard architecture (architecture
                is null). Architecture filter must be specified.
            page: Page number to return. For more information, see "Pagination". The API default is
                ``1``.
            per_page: Maximum number of entries returned per page. For more information, see
                "Pagination". The API default is ``25``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, page=page, per_page=per_page)
        response = await self._transport.request(
            "GET",
            "/isos",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "architecture": architecture,
                    "include_architecture_wildcard": include_architecture_wildcard,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListIsosResponse, response)

    async def get_iso(self, iso_id: int, /) -> GetIsoResponse:
        """Get an ISO.

        Returns a specific ISO object.

        ``GET /isos/{id}``

        Args:
            iso_id: ID of the ISO.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, iso_id=iso_id)
        response = await self._transport.request(
            "GET",
            f"/isos/{encode_path(iso_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(GetIsoResponse, response)
