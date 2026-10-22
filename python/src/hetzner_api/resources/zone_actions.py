"""Resource ``zone_actions`` (generated - do not edit by hand)."""

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
)
from hetzner_api.params import ZonePrimaryNameserverParam

__all__ = [
    "AsyncZoneActionsResource",
    "ZoneActionsResource",
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
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "ttl": Check(minimum=60, maximum=2147483647),
}


class ZoneActionsResource:
    """Operations on ``zone_actions`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_zones_actions(
        self,
        *,
        id: Sequence[int] | None = None,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions.

        Returns all Zone Actions.

        Use the provided URI parameters to modify the result.

        ``GET /zones/actions``

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
            "/zones/actions",
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

    def get_zones_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action.

        ``GET /zones/actions/{id}``

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
            f"/zones/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def list_zone_actions(
        self,
        id_or_name: str,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Zone.

        Returns all Actions for a Zone.

        Use the provided URI parameters to modify the result.

        ``GET /zones/{id_or_name}/actions``

        Args:
            id_or_name: ID or Name of the Zone.
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
        self._transport.validate(_CHECKS_3, page=page, per_page=per_page)
        response = self._transport.request(
            "GET",
            f"/zones/{encode_path(id_or_name)}/actions",
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

    @deprecated("GET /zones/{id_or_name}/actions/{action_id} is deprecated by the API")
    def get_zone_action(self, id_or_name: str, action_id: int, /) -> ActionResponse:
        """Get an Action for a Zone.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Zone.

        ``GET /zones/{id_or_name}/actions/{action_id}``

        Deprecated by the API.

        Args:
            id_or_name: ID or Name of the Zone.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, action_id=action_id)
        response = self._transport.request(
            "GET",
            f"/zones/{encode_path(id_or_name)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def change_zone_primary_nameservers(
        self,
        id_or_name: str,
        /,
        *,
        primary_nameservers: Sequence[ZonePrimaryNameserverParam],
    ) -> ActionResponse:
        """Change a Zone's Primary Nameservers.

        Overwrites the primary nameservers of a Zone.

        Only applicable for Zones in secondary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/actions/change_primary_nameservers``

        Args:
            id_or_name: ID or Name of the Zone.
            primary_nameservers: Primary nameservers of the Zone.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/actions/change_primary_nameservers",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "primary_nameservers": primary_nameservers,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_zone_protection(
        self,
        id_or_name: str,
        /,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Change a Zone's Protection.

        Changes the protection configuration of a Zone.

        ``POST /zones/{id_or_name}/actions/change_protection``

        Args:
            id_or_name: ID or Name of the Zone.
            delete: If true, prevents the snapshot from being deleted. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_zone_ttl(self, id_or_name: str, /, *, ttl: int) -> ActionResponse:
        """Change a Zone's Default TTL.

        Changes the default Time To Live (TTL) of a Zone.

        This TTL is used for RRSets that do not explicitly define a TTL.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/actions/change_ttl``

        Args:
            id_or_name: ID or Name of the Zone.
            ttl: Default Time To Live (TTL) of the Zone. Must be in between 60s and 2147483647s.
                This TTL is used for RRSets that do not explicitly define a TTL.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, ttl=ttl)
        response = self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/actions/change_ttl",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ttl": ttl,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def import_zone_zonefile(self, id_or_name: str, /, *, zonefile: str) -> ActionResponse:
        """Import a Zone file.

        Imports a zone file, replacing all resource record sets (RRSets).

        The import will fail if existing RRSet are `change` protected.

        See Zone file import for more details. Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/actions/import_zonefile``

        Args:
            id_or_name: ID or Name of the Zone.
            zonefile: Generated zone file. Example: ```dns $ORIGIN example.com. $TTL 3600 @ IN SOA
                hydrogen.ns.hetzner.com. dns.hetzner.com. 2024010100 86400 10800 3600000 3600 @ IN
                10800 NS hydrogen.ns.hetzner.com. ; Some comment. @ IN 10800 NS
                oxygen.ns.hetzner.com. @ IN 10800 NS helium.ns.hetzner.de. ```

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/actions/import_zonefile",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "zonefile": zonefile,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)


class AsyncZoneActionsResource:
    """Operations on ``zone_actions`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_zones_actions(
        self,
        *,
        id: Sequence[int] | None = None,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions.

        Returns all Zone Actions.

        Use the provided URI parameters to modify the result.

        ``GET /zones/actions``

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
            "/zones/actions",
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

    async def get_zones_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action.

        ``GET /zones/actions/{id}``

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
            f"/zones/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def list_zone_actions(
        self,
        id_or_name: str,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Zone.

        Returns all Actions for a Zone.

        Use the provided URI parameters to modify the result.

        ``GET /zones/{id_or_name}/actions``

        Args:
            id_or_name: ID or Name of the Zone.
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
        self._transport.validate(_CHECKS_3, page=page, per_page=per_page)
        response = await self._transport.request(
            "GET",
            f"/zones/{encode_path(id_or_name)}/actions",
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

    @deprecated("GET /zones/{id_or_name}/actions/{action_id} is deprecated by the API")
    async def get_zone_action(self, id_or_name: str, action_id: int, /) -> ActionResponse:
        """Get an Action for a Zone.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Zone.

        ``GET /zones/{id_or_name}/actions/{action_id}``

        Deprecated by the API.

        Args:
            id_or_name: ID or Name of the Zone.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, action_id=action_id)
        response = await self._transport.request(
            "GET",
            f"/zones/{encode_path(id_or_name)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def change_zone_primary_nameservers(
        self,
        id_or_name: str,
        /,
        *,
        primary_nameservers: Sequence[ZonePrimaryNameserverParam],
    ) -> ActionResponse:
        """Change a Zone's Primary Nameservers.

        Overwrites the primary nameservers of a Zone.

        Only applicable for Zones in secondary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/actions/change_primary_nameservers``

        Args:
            id_or_name: ID or Name of the Zone.
            primary_nameservers: Primary nameservers of the Zone.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = await self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/actions/change_primary_nameservers",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "primary_nameservers": primary_nameservers,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_zone_protection(
        self,
        id_or_name: str,
        /,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Change a Zone's Protection.

        Changes the protection configuration of a Zone.

        ``POST /zones/{id_or_name}/actions/change_protection``

        Args:
            id_or_name: ID or Name of the Zone.
            delete: If true, prevents the snapshot from being deleted. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = await self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_zone_ttl(self, id_or_name: str, /, *, ttl: int) -> ActionResponse:
        """Change a Zone's Default TTL.

        Changes the default Time To Live (TTL) of a Zone.

        This TTL is used for RRSets that do not explicitly define a TTL.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/actions/change_ttl``

        Args:
            id_or_name: ID or Name of the Zone.
            ttl: Default Time To Live (TTL) of the Zone. Must be in between 60s and 2147483647s.
                This TTL is used for RRSets that do not explicitly define a TTL.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, ttl=ttl)
        response = await self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/actions/change_ttl",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ttl": ttl,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def import_zone_zonefile(self, id_or_name: str, /, *, zonefile: str) -> ActionResponse:
        """Import a Zone file.

        Imports a zone file, replacing all resource record sets (RRSets).

        The import will fail if existing RRSet are `change` protected.

        See Zone file import for more details. Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/actions/import_zonefile``

        Args:
            id_or_name: ID or Name of the Zone.
            zonefile: Generated zone file. Example: ```dns $ORIGIN example.com. $TTL 3600 @ IN SOA
                hydrogen.ns.hetzner.com. dns.hetzner.com. 2024010100 86400 10800 3600000 3600 @ IN
                10800 NS hydrogen.ns.hetzner.com. ; Some comment. @ IN 10800 NS
                oxygen.ns.hetzner.com. @ IN 10800 NS helium.ns.hetzner.de. ```

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = await self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/actions/import_zonefile",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "zonefile": zonefile,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)
