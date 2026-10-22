"""Resource ``floating_ip_actions`` (generated - do not edit by hand)."""

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
from hetzner_api._types import UnknownValue
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import (
    ActionListResponseWithMeta,
    ActionResponse,
    ActionSort,
    ActionStatus,
    ErrorResponse,
)

__all__ = [
    "AsyncFloatingIpActionsResource",
    "FloatingIpActionsResource",
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
    "floating_ip_id": Check(minimum=1, maximum=9007199254740991),
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "floating_ip_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_5: Final[Mapping[str, Check]] = {
    "floating_ip_id": Check(minimum=1, maximum=9007199254740991),
    "action_id": Check(minimum=1, maximum=9007199254740991),
}


class FloatingIpActionsResource:
    """Operations on ``floating_ip_actions`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_floating_ips_actions(
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

        ``GET /floating_ips/actions``

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
            "/floating_ips/actions",
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

    def get_floating_ips_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a single Action.

        ``GET /floating_ips/actions/{id}``

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
            f"/floating_ips/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def list_floating_ip_actions(
        self,
        floating_ip_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Floating IP.

        Lists Actions for a Floating IP.

        Use the provided URI parameters to modify the result.

        ``GET /floating_ips/{id}/actions``

        Args:
            floating_ip_id: ID of the Floating IP.
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
        self._transport.validate(
            _CHECKS_3,
            floating_ip_id=floating_ip_id,
            page=page,
            per_page=per_page,
        )
        response = self._transport.request(
            "GET",
            f"/floating_ips/{encode_path(floating_ip_id)}/actions",
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

    def assign_floating_ip(self, floating_ip_id: int, /, *, server: int | None) -> ActionResponse:
        """Assign a Floating IP to a Server.

        Assigns a Floating IP to a Server.

        **Operation specific errors**

        - `422` - `floating_ip_assigned` - The Floating IP is already assigned

        ``POST /floating_ips/{id}/actions/assign``

        Args:
            floating_ip_id: ID of the Floating IP.
            server: Server the Floating IP is assigned to. `null` if not assigned.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, floating_ip_id=floating_ip_id)
        response = self._transport.request(
            "POST",
            f"/floating_ips/{encode_path(floating_ip_id)}/actions/assign",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "server": server,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_floating_ip_dns_ptr(
        self,
        floating_ip_id: int,
        /,
        *,
        ip: str,
        dns_ptr: str | None,
    ) -> ActionResponse:
        """Change reverse DNS records for a Floating IP.

        Change the reverse DNS records for this Floating IP.

        Allows to modify the PTR records set for the IP address.

        ``POST /floating_ips/{id}/actions/change_dns_ptr``

        Args:
            floating_ip_id: ID of the Floating IP.
            ip: Single IPv4 or IPv6 address to create pointer for.
            dns_ptr: Domain Name to point to. PTR record content used for reverse DNS. Set to null
                to reset (IPv4) to the default value or remove (IPv6) the record.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, floating_ip_id=floating_ip_id)
        response = self._transport.request(
            "POST",
            f"/floating_ips/{encode_path(floating_ip_id)}/actions/change_dns_ptr",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ip": ip,
                    "dns_ptr": dns_ptr,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_floating_ip_protection(
        self,
        floating_ip_id: int,
        /,
        *,
        delete: bool,
    ) -> ActionResponse:
        """Change Floating IP Protection.

        Changes the protection settings configured for the Floating IP.

        ``POST /floating_ips/{id}/actions/change_protection``

        Args:
            floating_ip_id: ID of the Floating IP.
            delete: Prevent the Resource from being deleted.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, floating_ip_id=floating_ip_id)
        response = self._transport.request(
            "POST",
            f"/floating_ips/{encode_path(floating_ip_id)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def unassign_floating_ip(self, floating_ip_id: int, /) -> ActionResponse:
        """Unassign a Floating IP.

        Unassigns a Floating IP.

        Results in the IP being unreachable. Can be assigned to another resource again.

        ``POST /floating_ips/{id}/actions/unassign``

        Args:
            floating_ip_id: ID of the Floating IP.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, floating_ip_id=floating_ip_id)
        response = self._transport.request(
            "POST",
            f"/floating_ips/{encode_path(floating_ip_id)}/actions/unassign",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    @deprecated("GET /floating_ips/{id}/actions/{action_id} is deprecated by the API")
    def get_floating_ip_action(self, floating_ip_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Floating IP.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Floating IP.

        ``GET /floating_ips/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            floating_ip_id: ID of the Floating IP.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, floating_ip_id=floating_ip_id, action_id=action_id)
        response = self._transport.request(
            "GET",
            f"/floating_ips/{encode_path(floating_ip_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)


class AsyncFloatingIpActionsResource:
    """Operations on ``floating_ip_actions`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_floating_ips_actions(
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

        ``GET /floating_ips/actions``

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
            "/floating_ips/actions",
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

    async def get_floating_ips_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a single Action.

        ``GET /floating_ips/actions/{id}``

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
            f"/floating_ips/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def list_floating_ip_actions(
        self,
        floating_ip_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Floating IP.

        Lists Actions for a Floating IP.

        Use the provided URI parameters to modify the result.

        ``GET /floating_ips/{id}/actions``

        Args:
            floating_ip_id: ID of the Floating IP.
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
        self._transport.validate(
            _CHECKS_3,
            floating_ip_id=floating_ip_id,
            page=page,
            per_page=per_page,
        )
        response = await self._transport.request(
            "GET",
            f"/floating_ips/{encode_path(floating_ip_id)}/actions",
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

    async def assign_floating_ip(
        self,
        floating_ip_id: int,
        /,
        *,
        server: int | None,
    ) -> ActionResponse:
        """Assign a Floating IP to a Server.

        Assigns a Floating IP to a Server.

        **Operation specific errors**

        - `422` - `floating_ip_assigned` - The Floating IP is already assigned

        ``POST /floating_ips/{id}/actions/assign``

        Args:
            floating_ip_id: ID of the Floating IP.
            server: Server the Floating IP is assigned to. `null` if not assigned.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, floating_ip_id=floating_ip_id)
        response = await self._transport.request(
            "POST",
            f"/floating_ips/{encode_path(floating_ip_id)}/actions/assign",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "server": server,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_floating_ip_dns_ptr(
        self,
        floating_ip_id: int,
        /,
        *,
        ip: str,
        dns_ptr: str | None,
    ) -> ActionResponse:
        """Change reverse DNS records for a Floating IP.

        Change the reverse DNS records for this Floating IP.

        Allows to modify the PTR records set for the IP address.

        ``POST /floating_ips/{id}/actions/change_dns_ptr``

        Args:
            floating_ip_id: ID of the Floating IP.
            ip: Single IPv4 or IPv6 address to create pointer for.
            dns_ptr: Domain Name to point to. PTR record content used for reverse DNS. Set to null
                to reset (IPv4) to the default value or remove (IPv6) the record.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, floating_ip_id=floating_ip_id)
        response = await self._transport.request(
            "POST",
            f"/floating_ips/{encode_path(floating_ip_id)}/actions/change_dns_ptr",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ip": ip,
                    "dns_ptr": dns_ptr,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_floating_ip_protection(
        self,
        floating_ip_id: int,
        /,
        *,
        delete: bool,
    ) -> ActionResponse:
        """Change Floating IP Protection.

        Changes the protection settings configured for the Floating IP.

        ``POST /floating_ips/{id}/actions/change_protection``

        Args:
            floating_ip_id: ID of the Floating IP.
            delete: Prevent the Resource from being deleted.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, floating_ip_id=floating_ip_id)
        response = await self._transport.request(
            "POST",
            f"/floating_ips/{encode_path(floating_ip_id)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def unassign_floating_ip(self, floating_ip_id: int, /) -> ActionResponse:
        """Unassign a Floating IP.

        Unassigns a Floating IP.

        Results in the IP being unreachable. Can be assigned to another resource again.

        ``POST /floating_ips/{id}/actions/unassign``

        Args:
            floating_ip_id: ID of the Floating IP.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, floating_ip_id=floating_ip_id)
        response = await self._transport.request(
            "POST",
            f"/floating_ips/{encode_path(floating_ip_id)}/actions/unassign",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    @deprecated("GET /floating_ips/{id}/actions/{action_id} is deprecated by the API")
    async def get_floating_ip_action(
        self,
        floating_ip_id: int,
        action_id: int,
        /,
    ) -> ActionResponse:
        """Get an Action for a Floating IP.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Floating IP.

        ``GET /floating_ips/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            floating_ip_id: ID of the Floating IP.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, floating_ip_id=floating_ip_id, action_id=action_id)
        response = await self._transport.request(
            "GET",
            f"/floating_ips/{encode_path(floating_ip_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)
