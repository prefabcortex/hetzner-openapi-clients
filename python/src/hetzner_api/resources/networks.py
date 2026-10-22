"""Resource ``networks`` (generated - do not edit by hand)."""

from collections.abc import Mapping, Sequence
from typing import Final

from hetzner_api._auth import Security
from hetzner_api._base_client import (
    AsyncTransport,
    SyncTransport,
    encode_body,
    encode_path,
    encode_query,
)
from hetzner_api._types import NOT_GIVEN, NotGiven, StrSequence, UnknownValue
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import (
    ErrorResponse,
    ListNetworkMembersResponse,
    ListNetworkMembersSort,
    ListNetworksResponse,
    NetworkMemberStatus,
    NetworkMemberType,
    NetworkResponse,
    SortByIdNameCreated,
)
from hetzner_api.params import NetworkCreateRequestSubnetParam, RouteParam
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncNetworksResource",
    "NetworksResource",
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
    "name": Check(min_length=1, max_length=128),
    "labels": LABELS_RULES,
}

_CHECKS_3: Final[Mapping[str, Check]] = {
    "network_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "network_id": Check(minimum=1, maximum=9007199254740991),
    "labels": LABELS_RULES,
}

_CHECKS_5: Final[Mapping[str, Check]] = {
    "network_id": Check(minimum=1, maximum=9007199254740991),
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}


class NetworksResource:
    """Operations on ``networks`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_networks(
        self,
        *,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListNetworksResponse:
        """List Networks.

        List multiple Networks.

        Use the provided URI parameters to modify the result.

        ``GET /networks``

        Args:
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
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
            "/networks",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "name": name,
                    "label_selector": label_selector,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListNetworksResponse, response)

    def create_network(
        self,
        *,
        name: str,
        ip_range: str,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        subnets: Sequence[NetworkCreateRequestSubnetParam] | NotGiven = NOT_GIVEN,
        routes: Sequence[RouteParam] | NotGiven = NOT_GIVEN,
        expose_routes_to_vswitch: bool | NotGiven = NOT_GIVEN,
    ) -> NetworkResponse:
        """Create a Network.

        Creates a Network.

        The provided `ip_range` can only be extended later on, but not reduced.

        Subnets can be added now or later on using the add subnet action. If you do not specify an
        `ip_range` for the subnet the first available /24 range will be used.

        Routes can be added now or later by using the add route action.

        ``POST /networks``

        Args:
            name: Name of the Network.
            ip_range: IP range of the Network. Uses CIDR notation. Must span all included subnets.
                Must be one of the private IPv4 ranges of RFC1918. Minimum network size is /24. We
                highly recommend that you pick a larger Network with a /16 netmask.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            subnets: Array of subnets to allocate. Omitted if not given.
            routes: Array of routes set in this Network. Omitted if not given.
            expose_routes_to_vswitch: Toggle to expose routes to the Networks vSwitch. Indicates if
                the routes from this Network should be exposed to the vSwitch in this Network. Only
                takes effect if a vSwitch is setup
                (https://docs.hetzner.com/cloud/networks/connect-dedi-vswitch) in this Network.
                Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, name=name, labels=labels)
        response = self._transport.request(
            "POST",
            "/networks",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "ip_range": ip_range,
                    "labels": labels,
                    "subnets": subnets,
                    "routes": routes,
                    "expose_routes_to_vswitch": expose_routes_to_vswitch,
                },
            ),
        )
        return self._transport.parse(NetworkResponse, response)

    def get_network(self, network_id: int, /) -> NetworkResponse:
        """Get a Network.

        Get a specific Network.

        ``GET /networks/{id}``

        Args:
            network_id: ID of the Network.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, network_id=network_id)
        response = self._transport.request(
            "GET",
            f"/networks/{encode_path(network_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(NetworkResponse, response)

    def update_network(
        self,
        network_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        expose_routes_to_vswitch: bool | NotGiven = NOT_GIVEN,
    ) -> NetworkResponse:
        """Update a Network.

        ``PUT /networks/{id}``

        Args:
            network_id: ID of the Network.
            name: New Network name. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.
            expose_routes_to_vswitch: Toggle to expose routes to the Networks vSwitch. Indicates if
                the routes from this Network should be exposed to the vSwitch in this Network. Only
                takes effect if a vSwitch is setup
                (https://docs.hetzner.com/cloud/networks/connect-dedi-vswitch) in this Network.
                Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id, labels=labels)
        response = self._transport.request(
            "PUT",
            f"/networks/{encode_path(network_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                    "expose_routes_to_vswitch": expose_routes_to_vswitch,
                },
            ),
        )
        return self._transport.parse(NetworkResponse, response)

    def delete_network(self, network_id: int, /) -> None:
        """Delete a Network.

        Deletes a Network.

        Attached resources will be detached automatically.

        ``DELETE /networks/{id}``

        Args:
            network_id: ID of the Network.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, network_id=network_id)
        self._transport.request(
            "DELETE",
            f"/networks/{encode_path(network_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )

    def list_network_members(
        self,
        network_id: int,
        /,
        *,
        type: Sequence[NetworkMemberType | UnknownValue] | None = None,
        subnet: StrSequence | None = None,
        status: Sequence[NetworkMemberStatus | UnknownValue] | None = None,
        sort: Sequence[ListNetworkMembersSort | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListNetworkMembersResponse:
        """List Members of a Network.

        List the resources attached to a specific Network.

        Use the provided URI parameters to modify the result.

        ``GET /networks/{id}/members``

        Args:
            network_id: ID of the Network.
            type: Filter members by type. May be used multiple times. The response will only contain
                members matching the specified types.
            subnet: Filter members by the subnet they are attached to. May be used multiple times.
                The response will only contain members attached to the subnets with the specified IP
                ranges. Uses CIDR notation.
            status: Filter members by status. May be used multiple times. The response will only
                contain members matching the specified statuses.
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
        self._transport.validate(_CHECKS_5, network_id=network_id, page=page, per_page=per_page)
        response = self._transport.request(
            "GET",
            f"/networks/{encode_path(network_id)}/members",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "type": type,
                    "subnet": subnet,
                    "status": status,
                    "sort": sort,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListNetworkMembersResponse, response)


class AsyncNetworksResource:
    """Operations on ``networks`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_networks(
        self,
        *,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListNetworksResponse:
        """List Networks.

        List multiple Networks.

        Use the provided URI parameters to modify the result.

        ``GET /networks``

        Args:
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
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
            "/networks",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "name": name,
                    "label_selector": label_selector,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListNetworksResponse, response)

    async def create_network(
        self,
        *,
        name: str,
        ip_range: str,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        subnets: Sequence[NetworkCreateRequestSubnetParam] | NotGiven = NOT_GIVEN,
        routes: Sequence[RouteParam] | NotGiven = NOT_GIVEN,
        expose_routes_to_vswitch: bool | NotGiven = NOT_GIVEN,
    ) -> NetworkResponse:
        """Create a Network.

        Creates a Network.

        The provided `ip_range` can only be extended later on, but not reduced.

        Subnets can be added now or later on using the add subnet action. If you do not specify an
        `ip_range` for the subnet the first available /24 range will be used.

        Routes can be added now or later by using the add route action.

        ``POST /networks``

        Args:
            name: Name of the Network.
            ip_range: IP range of the Network. Uses CIDR notation. Must span all included subnets.
                Must be one of the private IPv4 ranges of RFC1918. Minimum network size is /24. We
                highly recommend that you pick a larger Network with a /16 netmask.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            subnets: Array of subnets to allocate. Omitted if not given.
            routes: Array of routes set in this Network. Omitted if not given.
            expose_routes_to_vswitch: Toggle to expose routes to the Networks vSwitch. Indicates if
                the routes from this Network should be exposed to the vSwitch in this Network. Only
                takes effect if a vSwitch is setup
                (https://docs.hetzner.com/cloud/networks/connect-dedi-vswitch) in this Network.
                Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, name=name, labels=labels)
        response = await self._transport.request(
            "POST",
            "/networks",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "ip_range": ip_range,
                    "labels": labels,
                    "subnets": subnets,
                    "routes": routes,
                    "expose_routes_to_vswitch": expose_routes_to_vswitch,
                },
            ),
        )
        return self._transport.parse(NetworkResponse, response)

    async def get_network(self, network_id: int, /) -> NetworkResponse:
        """Get a Network.

        Get a specific Network.

        ``GET /networks/{id}``

        Args:
            network_id: ID of the Network.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, network_id=network_id)
        response = await self._transport.request(
            "GET",
            f"/networks/{encode_path(network_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(NetworkResponse, response)

    async def update_network(
        self,
        network_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        expose_routes_to_vswitch: bool | NotGiven = NOT_GIVEN,
    ) -> NetworkResponse:
        """Update a Network.

        ``PUT /networks/{id}``

        Args:
            network_id: ID of the Network.
            name: New Network name. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.
            expose_routes_to_vswitch: Toggle to expose routes to the Networks vSwitch. Indicates if
                the routes from this Network should be exposed to the vSwitch in this Network. Only
                takes effect if a vSwitch is setup
                (https://docs.hetzner.com/cloud/networks/connect-dedi-vswitch) in this Network.
                Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id, labels=labels)
        response = await self._transport.request(
            "PUT",
            f"/networks/{encode_path(network_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                    "expose_routes_to_vswitch": expose_routes_to_vswitch,
                },
            ),
        )
        return self._transport.parse(NetworkResponse, response)

    async def delete_network(self, network_id: int, /) -> None:
        """Delete a Network.

        Deletes a Network.

        Attached resources will be detached automatically.

        ``DELETE /networks/{id}``

        Args:
            network_id: ID of the Network.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, network_id=network_id)
        await self._transport.request(
            "DELETE",
            f"/networks/{encode_path(network_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )

    async def list_network_members(
        self,
        network_id: int,
        /,
        *,
        type: Sequence[NetworkMemberType | UnknownValue] | None = None,
        subnet: StrSequence | None = None,
        status: Sequence[NetworkMemberStatus | UnknownValue] | None = None,
        sort: Sequence[ListNetworkMembersSort | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListNetworkMembersResponse:
        """List Members of a Network.

        List the resources attached to a specific Network.

        Use the provided URI parameters to modify the result.

        ``GET /networks/{id}/members``

        Args:
            network_id: ID of the Network.
            type: Filter members by type. May be used multiple times. The response will only contain
                members matching the specified types.
            subnet: Filter members by the subnet they are attached to. May be used multiple times.
                The response will only contain members attached to the subnets with the specified IP
                ranges. Uses CIDR notation.
            status: Filter members by status. May be used multiple times. The response will only
                contain members matching the specified statuses.
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
        self._transport.validate(_CHECKS_5, network_id=network_id, page=page, per_page=per_page)
        response = await self._transport.request(
            "GET",
            f"/networks/{encode_path(network_id)}/members",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "type": type,
                    "subnet": subnet,
                    "status": status,
                    "sort": sort,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListNetworkMembersResponse, response)
