"""Resource ``network_actions`` (generated - do not edit by hand)."""

from collections.abc import Mapping, Sequence
from typing import Final
from warnings import deprecated

from hetzner_api._auth import Security
from hetzner_api._base_client import (
    AsyncTransport,
    SyncTransport,
    encode_body,
    encode_path,
    encode_query,
)
from hetzner_api._types import NOT_GIVEN, NotGiven, UnknownValue
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import (
    ActionListResponseWithMeta,
    ActionResponse,
    ActionSort,
    ActionStatus,
    ErrorResponse,
    SubnetType,
)

__all__ = [
    "AsyncNetworkActionsResource",
    "NetworkActionsResource",
]

_SECURITY_1: Final[Security] = (("APIToken",),)

_ERRORS_1: Final[ErrorModels] = {
    "4XX": ErrorResponse,
    "5XX": ErrorResponse,
}

_CHECKS_1: Final[Mapping[str, Check]] = {
    "id": Check(items=Check(minimum=1, maximum=9007199254740991)),
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}

_CHECKS_2: Final[Mapping[str, Check]] = {
    "action_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_3: Final[Mapping[str, Check]] = {
    "network_id": Check(minimum=1, maximum=9007199254740991),
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "network_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_5: Final[Mapping[str, Check]] = {
    "network_id": Check(minimum=1, maximum=9007199254740991),
    "action_id": Check(minimum=1, maximum=9007199254740991),
}


class NetworkActionsResource:
    """Operations on ``network_actions`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_networks_actions(
        self,
        *,
        id: Sequence[int] | None = None,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions.

        Lists multiple Actions.

        Use the provided URI parameters to modify the result.

        ``GET /networks/actions``

        Args:
            id: Filter the actions by ID. May be used multiple times. The response will only contain
                actions matching the specified IDs.
            sort: Sort actions by field and direction. May be used multiple times. For more
                information, see "Sorting".
            status: Filter the actions by status. May be used multiple times. The response will only
                contain actions matching the specified statuses.
            page: Page number to return. For more information, see "Pagination". The API default is
                ``1``.
            per_page: Maximum number of entries returned per page. For more information, see
                "Pagination". The API default is ``25``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, id=id, page=page, per_page=per_page)
        response = self._transport.request(
            "GET",
            "/networks/actions",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "id": id,
                    "sort": sort,
                    "status": status,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ActionListResponseWithMeta, response)

    def get_networks_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a single Action.

        ``GET /networks/actions/{id}``

        Args:
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, action_id=action_id)
        response = self._transport.request(
            "GET",
            f"/networks/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def list_network_actions(
        self,
        network_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Network.

        Lists Actions for a Network.

        Use the provided URI parameters to modify the result.

        ``GET /networks/{id}/actions``

        Args:
            network_id: ID of the Network.
            sort: Sort actions by field and direction. May be used multiple times. For more
                information, see "Sorting".
            status: Filter the actions by status. May be used multiple times. The response will only
                contain actions matching the specified statuses.
            page: Page number to return. For more information, see "Pagination". The API default is
                ``1``.
            per_page: Maximum number of entries returned per page. For more information, see
                "Pagination". The API default is ``25``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, network_id=network_id, page=page, per_page=per_page)
        response = self._transport.request(
            "GET",
            f"/networks/{encode_path(network_id)}/actions",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "status": status,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ActionListResponseWithMeta, response)

    def add_network_route(
        self,
        network_id: int,
        /,
        *,
        destination: str,
        gateway: str,
    ) -> ActionResponse:
        """Add a route to a Network.

        Adds a route entry to a Network.

        If a change is currently being performed on this Network, a error response with code
        `conflict` will be returned.

        ``POST /networks/{id}/actions/add_route``

        Args:
            network_id: ID of the Network.
            destination: Destination network or host of the route. Packages addressed for IPs
                matching the destination IP prefix will be send to the specified gateway. Must be
                one of * private IPv4 ranges of RFC1918 * or `0.0.0.0/0`. Must not overlap with * an
                existing ip_range in any subnets * or with any destinations in other routes * or
                with `172.31.1.1`. `172.31.1.1` is being used as a gateway for the public network
                interface of Servers.
            gateway: Gateway of the route. Packages addressed for the specified destination will be
                send to this IP address. Cannot be * the first IP of the networks ip_range, * an IP
                behind a vSwitch or * `172.31.1.1`. `172.31.1.1` is being used as a gateway for the
                public network interface of Servers.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id)
        response = self._transport.request(
            "POST",
            f"/networks/{encode_path(network_id)}/actions/add_route",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "destination": destination,
                    "gateway": gateway,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def add_network_subnet(
        self,
        network_id: int,
        /,
        *,
        type: SubnetType | UnknownValue,
        network_zone: str,
        ip_range: str | NotGiven = NOT_GIVEN,
        vswitch_id: int | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Add a subnet to a Network.

        Adds a new subnet to the Network.

        If the subnet `ip_range` is not provided, the first available `/24` IP range will be used.

        If a change is currently being performed on this Network, a error response with code
        `conflict` will be returned.

        ``POST /networks/{id}/actions/add_subnet``

        Args:
            network_id: ID of the Network.
            type: Type of subnet.
            network_zone: Name of the Network Zone. The Location contains the `network_zone` it
                belongs to.
            ip_range: IP range of the subnet. Uses CIDR notation. Must be a subnet of the parent
                Networks `ip_range`. Must not overlap with any other subnets or with any
                destinations in routes. Minimum network size is /30. We highly recommend that you
                pick a larger subnet with a /24 netmask. Omitted if not given.
            vswitch_id: ID of the robot vSwitch. Must be supplied if the subnet is of type
                `vswitch`. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id)
        response = self._transport.request(
            "POST",
            f"/networks/{encode_path(network_id)}/actions/add_subnet",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "type": type,
                    "ip_range": ip_range,
                    "network_zone": network_zone,
                    "vswitch_id": vswitch_id,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_network_ip_range(self, network_id: int, /, *, ip_range: str) -> ActionResponse:
        """Change IP range of a Network.

        Changes the IP range of a Network.

        The following restrictions apply to changing the IP range:
        - IP ranges can only be extended and never shrunk.
        - IPs can only be added to the end of the existing range, therefore only the netmask is
          allowed to be changed.

        To update the routes on the connected Servers, they need to be rebooted or the routes to be
        updated manually.

        For example if the Network has a range of `10.0.0.0/16` to extend it the new range has to
        start with the IP `10.0.0.0` as well. The netmask `/16` can be changed to a smaller one then
        `16` therefore increasing the IP range. A valid entry would be `10.0.0.0/15`, `10.0.0.0/14`
        or `10.0.0.0/13` and so on.

        If a change is currently being performed on this Network, a error response with code
        `conflict` will be returned.

        ``POST /networks/{id}/actions/change_ip_range``

        Args:
            network_id: ID of the Network.
            ip_range: IP range of the Network. Uses CIDR notation. Must span all included subnets.
                Must be one of the private IPv4 ranges of RFC1918. Minimum network size is /24. We
                highly recommend that you pick a larger Network with a /16 netmask.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id)
        response = self._transport.request(
            "POST",
            f"/networks/{encode_path(network_id)}/actions/change_ip_range",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ip_range": ip_range,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_network_protection(
        self,
        network_id: int,
        /,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Change Network Protection.

        Changes the protection settings of a Network.

        If a change is currently being performed on this Network, a error response with code
        `conflict` will be returned.

        ``POST /networks/{id}/actions/change_protection``

        Args:
            network_id: ID of the Network.
            delete: If true, prevents the snapshot from being deleted. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id)
        response = self._transport.request(
            "POST",
            f"/networks/{encode_path(network_id)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def delete_network_route(
        self,
        network_id: int,
        /,
        *,
        destination: str,
        gateway: str,
    ) -> ActionResponse:
        """Delete a route from a Network.

        Delete a route entry from a Network.

        If a change is currently being performed on this Network, a error response with code
        `conflict` will be returned.

        ``POST /networks/{id}/actions/delete_route``

        Args:
            network_id: ID of the Network.
            destination: Destination network or host of the route. Packages addressed for IPs
                matching the destination IP prefix will be send to the specified gateway. Must be
                one of * private IPv4 ranges of RFC1918 * or `0.0.0.0/0`. Must not overlap with * an
                existing ip_range in any subnets * or with any destinations in other routes * or
                with `172.31.1.1`. `172.31.1.1` is being used as a gateway for the public network
                interface of Servers.
            gateway: Gateway of the route. Packages addressed for the specified destination will be
                send to this IP address. Cannot be * the first IP of the networks ip_range, * an IP
                behind a vSwitch or * `172.31.1.1`. `172.31.1.1` is being used as a gateway for the
                public network interface of Servers.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id)
        response = self._transport.request(
            "POST",
            f"/networks/{encode_path(network_id)}/actions/delete_route",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "destination": destination,
                    "gateway": gateway,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def delete_network_subnet(self, network_id: int, /, *, ip_range: str) -> ActionResponse:
        """Delete a subnet from a Network.

        Deletes a single subnet entry from a Network.

        Subnets containing attached resources can not be deleted, they must be detached beforehand.

        If a change is currently being performed on this Network, a error response with code
        `conflict` will be returned.

        ``POST /networks/{id}/actions/delete_subnet``

        Args:
            network_id: ID of the Network.
            ip_range: IP range in CIDR block notation of the subnet to delete.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id)
        response = self._transport.request(
            "POST",
            f"/networks/{encode_path(network_id)}/actions/delete_subnet",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ip_range": ip_range,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    @deprecated("GET /networks/{id}/actions/{action_id} is deprecated by the API")
    def get_network_action(self, network_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Network.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Network.

        ``GET /networks/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            network_id: ID of the Network.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, network_id=network_id, action_id=action_id)
        response = self._transport.request(
            "GET",
            f"/networks/{encode_path(network_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)


class AsyncNetworkActionsResource:
    """Operations on ``network_actions`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_networks_actions(
        self,
        *,
        id: Sequence[int] | None = None,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions.

        Lists multiple Actions.

        Use the provided URI parameters to modify the result.

        ``GET /networks/actions``

        Args:
            id: Filter the actions by ID. May be used multiple times. The response will only contain
                actions matching the specified IDs.
            sort: Sort actions by field and direction. May be used multiple times. For more
                information, see "Sorting".
            status: Filter the actions by status. May be used multiple times. The response will only
                contain actions matching the specified statuses.
            page: Page number to return. For more information, see "Pagination". The API default is
                ``1``.
            per_page: Maximum number of entries returned per page. For more information, see
                "Pagination". The API default is ``25``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, id=id, page=page, per_page=per_page)
        response = await self._transport.request(
            "GET",
            "/networks/actions",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "id": id,
                    "sort": sort,
                    "status": status,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ActionListResponseWithMeta, response)

    async def get_networks_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a single Action.

        ``GET /networks/actions/{id}``

        Args:
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, action_id=action_id)
        response = await self._transport.request(
            "GET",
            f"/networks/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def list_network_actions(
        self,
        network_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Network.

        Lists Actions for a Network.

        Use the provided URI parameters to modify the result.

        ``GET /networks/{id}/actions``

        Args:
            network_id: ID of the Network.
            sort: Sort actions by field and direction. May be used multiple times. For more
                information, see "Sorting".
            status: Filter the actions by status. May be used multiple times. The response will only
                contain actions matching the specified statuses.
            page: Page number to return. For more information, see "Pagination". The API default is
                ``1``.
            per_page: Maximum number of entries returned per page. For more information, see
                "Pagination". The API default is ``25``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, network_id=network_id, page=page, per_page=per_page)
        response = await self._transport.request(
            "GET",
            f"/networks/{encode_path(network_id)}/actions",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "status": status,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ActionListResponseWithMeta, response)

    async def add_network_route(
        self,
        network_id: int,
        /,
        *,
        destination: str,
        gateway: str,
    ) -> ActionResponse:
        """Add a route to a Network.

        Adds a route entry to a Network.

        If a change is currently being performed on this Network, a error response with code
        `conflict` will be returned.

        ``POST /networks/{id}/actions/add_route``

        Args:
            network_id: ID of the Network.
            destination: Destination network or host of the route. Packages addressed for IPs
                matching the destination IP prefix will be send to the specified gateway. Must be
                one of * private IPv4 ranges of RFC1918 * or `0.0.0.0/0`. Must not overlap with * an
                existing ip_range in any subnets * or with any destinations in other routes * or
                with `172.31.1.1`. `172.31.1.1` is being used as a gateway for the public network
                interface of Servers.
            gateway: Gateway of the route. Packages addressed for the specified destination will be
                send to this IP address. Cannot be * the first IP of the networks ip_range, * an IP
                behind a vSwitch or * `172.31.1.1`. `172.31.1.1` is being used as a gateway for the
                public network interface of Servers.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id)
        response = await self._transport.request(
            "POST",
            f"/networks/{encode_path(network_id)}/actions/add_route",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "destination": destination,
                    "gateway": gateway,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def add_network_subnet(
        self,
        network_id: int,
        /,
        *,
        type: SubnetType | UnknownValue,
        network_zone: str,
        ip_range: str | NotGiven = NOT_GIVEN,
        vswitch_id: int | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Add a subnet to a Network.

        Adds a new subnet to the Network.

        If the subnet `ip_range` is not provided, the first available `/24` IP range will be used.

        If a change is currently being performed on this Network, a error response with code
        `conflict` will be returned.

        ``POST /networks/{id}/actions/add_subnet``

        Args:
            network_id: ID of the Network.
            type: Type of subnet.
            network_zone: Name of the Network Zone. The Location contains the `network_zone` it
                belongs to.
            ip_range: IP range of the subnet. Uses CIDR notation. Must be a subnet of the parent
                Networks `ip_range`. Must not overlap with any other subnets or with any
                destinations in routes. Minimum network size is /30. We highly recommend that you
                pick a larger subnet with a /24 netmask. Omitted if not given.
            vswitch_id: ID of the robot vSwitch. Must be supplied if the subnet is of type
                `vswitch`. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id)
        response = await self._transport.request(
            "POST",
            f"/networks/{encode_path(network_id)}/actions/add_subnet",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "type": type,
                    "ip_range": ip_range,
                    "network_zone": network_zone,
                    "vswitch_id": vswitch_id,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_network_ip_range(self, network_id: int, /, *, ip_range: str) -> ActionResponse:
        """Change IP range of a Network.

        Changes the IP range of a Network.

        The following restrictions apply to changing the IP range:
        - IP ranges can only be extended and never shrunk.
        - IPs can only be added to the end of the existing range, therefore only the netmask is
          allowed to be changed.

        To update the routes on the connected Servers, they need to be rebooted or the routes to be
        updated manually.

        For example if the Network has a range of `10.0.0.0/16` to extend it the new range has to
        start with the IP `10.0.0.0` as well. The netmask `/16` can be changed to a smaller one then
        `16` therefore increasing the IP range. A valid entry would be `10.0.0.0/15`, `10.0.0.0/14`
        or `10.0.0.0/13` and so on.

        If a change is currently being performed on this Network, a error response with code
        `conflict` will be returned.

        ``POST /networks/{id}/actions/change_ip_range``

        Args:
            network_id: ID of the Network.
            ip_range: IP range of the Network. Uses CIDR notation. Must span all included subnets.
                Must be one of the private IPv4 ranges of RFC1918. Minimum network size is /24. We
                highly recommend that you pick a larger Network with a /16 netmask.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id)
        response = await self._transport.request(
            "POST",
            f"/networks/{encode_path(network_id)}/actions/change_ip_range",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ip_range": ip_range,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_network_protection(
        self,
        network_id: int,
        /,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Change Network Protection.

        Changes the protection settings of a Network.

        If a change is currently being performed on this Network, a error response with code
        `conflict` will be returned.

        ``POST /networks/{id}/actions/change_protection``

        Args:
            network_id: ID of the Network.
            delete: If true, prevents the snapshot from being deleted. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id)
        response = await self._transport.request(
            "POST",
            f"/networks/{encode_path(network_id)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def delete_network_route(
        self,
        network_id: int,
        /,
        *,
        destination: str,
        gateway: str,
    ) -> ActionResponse:
        """Delete a route from a Network.

        Delete a route entry from a Network.

        If a change is currently being performed on this Network, a error response with code
        `conflict` will be returned.

        ``POST /networks/{id}/actions/delete_route``

        Args:
            network_id: ID of the Network.
            destination: Destination network or host of the route. Packages addressed for IPs
                matching the destination IP prefix will be send to the specified gateway. Must be
                one of * private IPv4 ranges of RFC1918 * or `0.0.0.0/0`. Must not overlap with * an
                existing ip_range in any subnets * or with any destinations in other routes * or
                with `172.31.1.1`. `172.31.1.1` is being used as a gateway for the public network
                interface of Servers.
            gateway: Gateway of the route. Packages addressed for the specified destination will be
                send to this IP address. Cannot be * the first IP of the networks ip_range, * an IP
                behind a vSwitch or * `172.31.1.1`. `172.31.1.1` is being used as a gateway for the
                public network interface of Servers.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id)
        response = await self._transport.request(
            "POST",
            f"/networks/{encode_path(network_id)}/actions/delete_route",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "destination": destination,
                    "gateway": gateway,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def delete_network_subnet(self, network_id: int, /, *, ip_range: str) -> ActionResponse:
        """Delete a subnet from a Network.

        Deletes a single subnet entry from a Network.

        Subnets containing attached resources can not be deleted, they must be detached beforehand.

        If a change is currently being performed on this Network, a error response with code
        `conflict` will be returned.

        ``POST /networks/{id}/actions/delete_subnet``

        Args:
            network_id: ID of the Network.
            ip_range: IP range in CIDR block notation of the subnet to delete.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, network_id=network_id)
        response = await self._transport.request(
            "POST",
            f"/networks/{encode_path(network_id)}/actions/delete_subnet",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ip_range": ip_range,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    @deprecated("GET /networks/{id}/actions/{action_id} is deprecated by the API")
    async def get_network_action(self, network_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Network.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Network.

        ``GET /networks/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            network_id: ID of the Network.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, network_id=network_id, action_id=action_id)
        response = await self._transport.request(
            "GET",
            f"/networks/{encode_path(network_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)
