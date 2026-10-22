"""Resource ``locations`` (generated - do not edit by hand)."""

from collections.abc import Mapping, Sequence
from typing import Final

from hetzner_api._auth import Security
from hetzner_api._base_client import AsyncTransport, SyncTransport, encode_path, encode_query
from hetzner_api._types import UnknownValue
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import (
    ErrorResponse,
    GetLocationResponse,
    ListLocationsResponse,
    SortByIdName,
)

__all__ = [
    "AsyncLocationsResource",
    "LocationsResource",
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
    "location_id": Check(minimum=1, maximum=9007199254740991),
}


class LocationsResource:
    """Operations on ``locations`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_locations(
        self,
        *,
        name: str | None = None,
        sort: Sequence[SortByIdName | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListLocationsResponse:
        """List Locations.

        Returns all Locations.

        ``GET /locations``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
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
            "/locations",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "sort": sort,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListLocationsResponse, response)

    def get_location(self, location_id: int, /) -> GetLocationResponse:
        """Get a Location.

        Returns a Location.

        ``GET /locations/{id}``

        Args:
            location_id: ID of the Location.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, location_id=location_id)
        response = self._transport.request(
            "GET",
            f"/locations/{encode_path(location_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(GetLocationResponse, response)


class AsyncLocationsResource:
    """Operations on ``locations`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_locations(
        self,
        *,
        name: str | None = None,
        sort: Sequence[SortByIdName | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListLocationsResponse:
        """List Locations.

        Returns all Locations.

        ``GET /locations``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
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
            "/locations",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "sort": sort,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListLocationsResponse, response)

    async def get_location(self, location_id: int, /) -> GetLocationResponse:
        """Get a Location.

        Returns a Location.

        ``GET /locations/{id}``

        Args:
            location_id: ID of the Location.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, location_id=location_id)
        response = await self._transport.request(
            "GET",
            f"/locations/{encode_path(location_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(GetLocationResponse, response)
