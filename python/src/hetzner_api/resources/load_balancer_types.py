"""Resource ``load_balancer_types`` (generated - do not edit by hand)."""

from collections.abc import Mapping
from typing import Final

from hetzner_api._auth import Security
from hetzner_api._base_client import AsyncTransport, SyncTransport, encode_path, encode_query
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import (
    ErrorResponse,
    GetLoadBalancerTypeResponse,
    ListLoadBalancerTypesResponse,
)

__all__ = [
    "AsyncLoadBalancerTypesResource",
    "LoadBalancerTypesResource",
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
    "load_balancer_type_id": Check(minimum=1, maximum=9007199254740991),
}


class LoadBalancerTypesResource:
    """Operations on ``load_balancer_types`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_load_balancer_types(
        self,
        *,
        name: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListLoadBalancerTypesResponse:
        """List Load Balancer Types.

        Gets all Load Balancer type objects.

        ``GET /load_balancer_types``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
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
            "/load_balancer_types",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListLoadBalancerTypesResponse, response)

    def get_load_balancer_type(self, load_balancer_type_id: int, /) -> GetLoadBalancerTypeResponse:
        """Get a Load Balancer Type.

        Gets a specific Load Balancer type object.

        ``GET /load_balancer_types/{id}``

        Args:
            load_balancer_type_id: ID of the Load Balancer Type.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, load_balancer_type_id=load_balancer_type_id)
        response = self._transport.request(
            "GET",
            f"/load_balancer_types/{encode_path(load_balancer_type_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(GetLoadBalancerTypeResponse, response)


class AsyncLoadBalancerTypesResource:
    """Operations on ``load_balancer_types`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_load_balancer_types(
        self,
        *,
        name: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListLoadBalancerTypesResponse:
        """List Load Balancer Types.

        Gets all Load Balancer type objects.

        ``GET /load_balancer_types``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
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
            "/load_balancer_types",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListLoadBalancerTypesResponse, response)

    async def get_load_balancer_type(
        self,
        load_balancer_type_id: int,
        /,
    ) -> GetLoadBalancerTypeResponse:
        """Get a Load Balancer Type.

        Gets a specific Load Balancer type object.

        ``GET /load_balancer_types/{id}``

        Args:
            load_balancer_type_id: ID of the Load Balancer Type.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, load_balancer_type_id=load_balancer_type_id)
        response = await self._transport.request(
            "GET",
            f"/load_balancer_types/{encode_path(load_balancer_type_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(GetLoadBalancerTypeResponse, response)
