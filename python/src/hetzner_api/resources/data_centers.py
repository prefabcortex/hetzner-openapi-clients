"""Resource ``data_centers`` (generated - do not edit by hand)."""

from collections.abc import Mapping, Sequence
from typing import Final
from warnings import deprecated

from hetzner_api._auth import Security
from hetzner_api._base_client import AsyncTransport, SyncTransport, encode_path, encode_query
from hetzner_api._types import UnknownValue
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import (
    ErrorResponse,
    GetDatacenterResponse,
    ListDatacentersResponse,
    SortByIdName,
)

__all__ = [
    "AsyncDataCentersResource",
    "DataCentersResource",
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
    "datacenter_id": Check(minimum=1, maximum=9007199254740991),
}


class DataCentersResource:
    """Operations on ``data_centers`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    @deprecated("GET /datacenters is deprecated by the API")
    def list_datacenters(
        self,
        *,
        name: str | None = None,
        sort: Sequence[SortByIdName | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListDatacentersResponse:
        """List Data Centers.

        **Deprecated:** This endpoint is deprecated as of 01 June 2026 and will be removed after 01
        October 2026.

        Returns all Data Centers.

        ``GET /datacenters``

        Deprecated by the API.

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
            "/datacenters",
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
        return self._transport.parse(ListDatacentersResponse, response)

    @deprecated("GET /datacenters/{id} is deprecated by the API")
    def get_datacenter(self, datacenter_id: int, /) -> GetDatacenterResponse:
        """Get a Data Center.

        **Deprecated:** This endpoint is deprecated as of 01 June 2026 and will be removed after 01
        October 2026.

        Returns a single Data Center.

        ``GET /datacenters/{id}``

        Deprecated by the API.

        Args:
            datacenter_id: ID of the Data Center.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, datacenter_id=datacenter_id)
        response = self._transport.request(
            "GET",
            f"/datacenters/{encode_path(datacenter_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(GetDatacenterResponse, response)


class AsyncDataCentersResource:
    """Operations on ``data_centers`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    @deprecated("GET /datacenters is deprecated by the API")
    async def list_datacenters(
        self,
        *,
        name: str | None = None,
        sort: Sequence[SortByIdName | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListDatacentersResponse:
        """List Data Centers.

        **Deprecated:** This endpoint is deprecated as of 01 June 2026 and will be removed after 01
        October 2026.

        Returns all Data Centers.

        ``GET /datacenters``

        Deprecated by the API.

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
            "/datacenters",
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
        return self._transport.parse(ListDatacentersResponse, response)

    @deprecated("GET /datacenters/{id} is deprecated by the API")
    async def get_datacenter(self, datacenter_id: int, /) -> GetDatacenterResponse:
        """Get a Data Center.

        **Deprecated:** This endpoint is deprecated as of 01 June 2026 and will be removed after 01
        October 2026.

        Returns a single Data Center.

        ``GET /datacenters/{id}``

        Deprecated by the API.

        Args:
            datacenter_id: ID of the Data Center.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, datacenter_id=datacenter_id)
        response = await self._transport.request(
            "GET",
            f"/datacenters/{encode_path(datacenter_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(GetDatacenterResponse, response)
