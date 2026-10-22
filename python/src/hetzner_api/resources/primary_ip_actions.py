"""Resource ``primary_ip_actions`` (generated - do not edit by hand)."""

from collections.abc import Mapping, Sequence
from typing import Final, Literal
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
    "AsyncPrimaryIpActionsResource",
    "PrimaryIpActionsResource",
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
    "primary_ip_id": Check(minimum=1, maximum=9007199254740991),
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "primary_ip_id": Check(minimum=1, maximum=9007199254740991),
    "action_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_5: Final[Mapping[str, Check]] = {
    "primary_ip_id": Check(minimum=1, maximum=9007199254740991),
}


class PrimaryIpActionsResource:
    """Operations on ``primary_ip_actions`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_primary_ips_actions(
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

        ``GET /primary_ips/actions``

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
            "/primary_ips/actions",
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

    def get_primary_ips_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a single Action.

        ``GET /primary_ips/actions/{id}``

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
            f"/primary_ips/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def list_primary_ip_actions(
        self,
        primary_ip_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Primary IP.

        Returns all Actions for a Primary IP.

        Use the provided URI parameters to modify the result.

        ``GET /primary_ips/{id}/actions``

        Args:
            primary_ip_id: ID of the Primary IP.
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
            primary_ip_id=primary_ip_id,
            page=page,
            per_page=per_page,
        )
        response = self._transport.request(
            "GET",
            f"/primary_ips/{encode_path(primary_ip_id)}/actions",
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

    @deprecated("GET /primary_ips/{id}/actions/{action_id} is deprecated by the API")
    def get_primary_ip_action(self, primary_ip_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Primary IP.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Primary IP.

        ``GET /primary_ips/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            primary_ip_id: ID of the Primary IP.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, primary_ip_id=primary_ip_id, action_id=action_id)
        response = self._transport.request(
            "GET",
            f"/primary_ips/{encode_path(primary_ip_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def assign_primary_ip(
        self,
        primary_ip_id: int,
        /,
        *,
        assignee_type: Literal["server"],
        assignee_id: int,
    ) -> ActionResponse:
        """Assign a Primary IP to a resource.

        ``POST /primary_ips/{id}/actions/assign``

        Args:
            primary_ip_id: ID of the Primary IP.
            assignee_type: Type of resource assigning the Primary IP to.
            assignee_id: ID of a resource of type `assignee_type`.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, primary_ip_id=primary_ip_id)
        response = self._transport.request(
            "POST",
            f"/primary_ips/{encode_path(primary_ip_id)}/actions/assign",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "assignee_type": assignee_type,
                    "assignee_id": assignee_id,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_primary_ip_dns_ptr(
        self,
        primary_ip_id: int,
        /,
        *,
        ip: str,
        dns_ptr: str | None,
    ) -> ActionResponse:
        """Change reverse DNS records for a Primary IP.

        Change the reverse DNS records for this Primary IP.

        Allows to modify the PTR records set for the IP address.

        ``POST /primary_ips/{id}/actions/change_dns_ptr``

        Args:
            primary_ip_id: ID of the Primary IP.
            ip: Single IPv4 or IPv6 address to create pointer for.
            dns_ptr: Domain Name to point to. PTR record content used for reverse DNS. Set to null
                to reset (IPv4) to the default value or remove (IPv6) the record.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, primary_ip_id=primary_ip_id)
        response = self._transport.request(
            "POST",
            f"/primary_ips/{encode_path(primary_ip_id)}/actions/change_dns_ptr",
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

    def change_primary_ip_protection(
        self,
        primary_ip_id: int,
        /,
        *,
        delete: bool,
    ) -> ActionResponse:
        """Change Primary IP Protection.

        Changes the protection configuration of a Primary IP.

        A Primary IPs deletion protection can only be enabled if its `auto_delete` property is set
        to `false`.

        ``POST /primary_ips/{id}/actions/change_protection``

        Args:
            primary_ip_id: ID of the Primary IP.
            delete: Prevent the Resource from being deleted.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, primary_ip_id=primary_ip_id)
        response = self._transport.request(
            "POST",
            f"/primary_ips/{encode_path(primary_ip_id)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def unassign_primary_ip(self, primary_ip_id: int, /) -> ActionResponse:
        """Unassign a Primary IP from a resource.

        ``POST /primary_ips/{id}/actions/unassign``

        Args:
            primary_ip_id: ID of the Primary IP.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, primary_ip_id=primary_ip_id)
        response = self._transport.request(
            "POST",
            f"/primary_ips/{encode_path(primary_ip_id)}/actions/unassign",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)


class AsyncPrimaryIpActionsResource:
    """Operations on ``primary_ip_actions`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_primary_ips_actions(
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

        ``GET /primary_ips/actions``

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
            "/primary_ips/actions",
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

    async def get_primary_ips_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a single Action.

        ``GET /primary_ips/actions/{id}``

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
            f"/primary_ips/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def list_primary_ip_actions(
        self,
        primary_ip_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Primary IP.

        Returns all Actions for a Primary IP.

        Use the provided URI parameters to modify the result.

        ``GET /primary_ips/{id}/actions``

        Args:
            primary_ip_id: ID of the Primary IP.
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
            primary_ip_id=primary_ip_id,
            page=page,
            per_page=per_page,
        )
        response = await self._transport.request(
            "GET",
            f"/primary_ips/{encode_path(primary_ip_id)}/actions",
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

    @deprecated("GET /primary_ips/{id}/actions/{action_id} is deprecated by the API")
    async def get_primary_ip_action(self, primary_ip_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Primary IP.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Primary IP.

        ``GET /primary_ips/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            primary_ip_id: ID of the Primary IP.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, primary_ip_id=primary_ip_id, action_id=action_id)
        response = await self._transport.request(
            "GET",
            f"/primary_ips/{encode_path(primary_ip_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def assign_primary_ip(
        self,
        primary_ip_id: int,
        /,
        *,
        assignee_type: Literal["server"],
        assignee_id: int,
    ) -> ActionResponse:
        """Assign a Primary IP to a resource.

        ``POST /primary_ips/{id}/actions/assign``

        Args:
            primary_ip_id: ID of the Primary IP.
            assignee_type: Type of resource assigning the Primary IP to.
            assignee_id: ID of a resource of type `assignee_type`.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, primary_ip_id=primary_ip_id)
        response = await self._transport.request(
            "POST",
            f"/primary_ips/{encode_path(primary_ip_id)}/actions/assign",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "assignee_type": assignee_type,
                    "assignee_id": assignee_id,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_primary_ip_dns_ptr(
        self,
        primary_ip_id: int,
        /,
        *,
        ip: str,
        dns_ptr: str | None,
    ) -> ActionResponse:
        """Change reverse DNS records for a Primary IP.

        Change the reverse DNS records for this Primary IP.

        Allows to modify the PTR records set for the IP address.

        ``POST /primary_ips/{id}/actions/change_dns_ptr``

        Args:
            primary_ip_id: ID of the Primary IP.
            ip: Single IPv4 or IPv6 address to create pointer for.
            dns_ptr: Domain Name to point to. PTR record content used for reverse DNS. Set to null
                to reset (IPv4) to the default value or remove (IPv6) the record.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, primary_ip_id=primary_ip_id)
        response = await self._transport.request(
            "POST",
            f"/primary_ips/{encode_path(primary_ip_id)}/actions/change_dns_ptr",
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

    async def change_primary_ip_protection(
        self,
        primary_ip_id: int,
        /,
        *,
        delete: bool,
    ) -> ActionResponse:
        """Change Primary IP Protection.

        Changes the protection configuration of a Primary IP.

        A Primary IPs deletion protection can only be enabled if its `auto_delete` property is set
        to `false`.

        ``POST /primary_ips/{id}/actions/change_protection``

        Args:
            primary_ip_id: ID of the Primary IP.
            delete: Prevent the Resource from being deleted.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, primary_ip_id=primary_ip_id)
        response = await self._transport.request(
            "POST",
            f"/primary_ips/{encode_path(primary_ip_id)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def unassign_primary_ip(self, primary_ip_id: int, /) -> ActionResponse:
        """Unassign a Primary IP from a resource.

        ``POST /primary_ips/{id}/actions/unassign``

        Args:
            primary_ip_id: ID of the Primary IP.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, primary_ip_id=primary_ip_id)
        response = await self._transport.request(
            "POST",
            f"/primary_ips/{encode_path(primary_ip_id)}/actions/unassign",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)
