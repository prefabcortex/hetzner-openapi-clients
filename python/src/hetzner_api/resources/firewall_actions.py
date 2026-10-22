"""Resource ``firewall_actions`` (generated - do not edit by hand)."""

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
    ActionListResponse,
    ActionListResponseWithMeta,
    ActionResponse,
    ActionSort,
    ActionStatus,
    ErrorResponse,
)
from hetzner_api.params import FirewallResourceParam, RuleParam
from hetzner_api.rules import RULE_FIELDS

__all__ = [
    "AsyncFirewallActionsResource",
    "FirewallActionsResource",
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
    "firewall_id": Check(minimum=1, maximum=9007199254740991),
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "firewall_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_5: Final[Mapping[str, Check]] = {
    "firewall_id": Check(minimum=1, maximum=9007199254740991),
    "rules": Check(max_items=50, items=Check(fields_of=lambda: RULE_FIELDS)),
}

_CHECKS_6: Final[Mapping[str, Check]] = {
    "firewall_id": Check(minimum=1, maximum=9007199254740991),
    "action_id": Check(minimum=1, maximum=9007199254740991),
}


class FirewallActionsResource:
    """Operations on ``firewall_actions`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_firewalls_actions(
        self,
        *,
        id: Sequence[int] | None = None,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions.

        Returns all Actions for Firewalls.

        Use the provided URI parameters to modify the result.

        ``GET /firewalls/actions``

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
            "/firewalls/actions",
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

    def get_firewalls_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns the specific Action.

        ``GET /firewalls/actions/{id}``

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
            f"/firewalls/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def list_firewall_actions(
        self,
        firewall_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Firewall.

        Returns all Actions for the Firewall.

        Use the provided URI parameters to modify the result.

        ``GET /firewalls/{id}/actions``

        Args:
            firewall_id: ID of the Firewall.
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
        self._transport.validate(_CHECKS_3, firewall_id=firewall_id, page=page, per_page=per_page)
        response = self._transport.request(
            "GET",
            f"/firewalls/{encode_path(firewall_id)}/actions",
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

    def apply_firewall_to_resources(
        self,
        firewall_id: int,
        /,
        *,
        apply_to: Sequence[FirewallResourceParam],
    ) -> ActionListResponse:
        """Apply to Resources.

        Applies a Firewall to multiple resources.

        Supported resources:
        - Servers (with a public network interface)
        - Label Selectors

        A Server can be applied to a maximum of 5 Firewalls
        (https://docs.hetzner.com/cloud/firewalls/overview#limits). This limit applies to Servers
        applied via a matching Label Selector as well.

        Updates to resources matching or no longer matching a Label Selector can take up to a few
        seconds to be processed.

        A Firewall is applied to a resource once the related Action with command `apply_firewall`
        successfully finished.

        **Operation specific errors**

        - `404` - `firewall_resource_not_found` - The resource the Firewall should be applied to was
          not found
        - `422` - `firewall_already_applied` - Firewall is already applied to resource
        - `422` - `incompatible_network_type` - The network type of the resource is not supported by
          Firewalls
        - `422` - `private_net_only_server` - The Server the Firewall should be applied to has no
          public interface

        ``POST /firewalls/{id}/actions/apply_to_resources``

        Args:
            firewall_id: ID of the Firewall.
            apply_to: Resources to apply the Firewall to. Extends existing resources.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, firewall_id=firewall_id)
        response = self._transport.request(
            "POST",
            f"/firewalls/{encode_path(firewall_id)}/actions/apply_to_resources",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "apply_to": apply_to,
                },
            ),
        )
        return self._transport.parse(ActionListResponse, response)

    def remove_firewall_from_resources(
        self,
        firewall_id: int,
        /,
        *,
        remove_from: Sequence[FirewallResourceParam],
    ) -> ActionListResponse:
        """Remove from Resources.

        Removes a Firewall from multiple resources.

        Supported resources:
        - Servers (with a public network interface)

        A Firewall is removed from a resource once the related Action with command `remove_firewall`
        successfully finished.

        **Operation specific errors**

        - `404` - `firewall_resource_not_found` - The resource the Firewall should be removed from
          was not found
        - `422` - `firewall_managed_by_label_selector` - Firewall is applied via a Label Selector
          and cannot be removed manually

        ``POST /firewalls/{id}/actions/remove_from_resources``

        Args:
            firewall_id: ID of the Firewall.
            remove_from: Resources to remove the Firewall from.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, firewall_id=firewall_id)
        response = self._transport.request(
            "POST",
            f"/firewalls/{encode_path(firewall_id)}/actions/remove_from_resources",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "remove_from": remove_from,
                },
            ),
        )
        return self._transport.parse(ActionListResponse, response)

    def set_firewall_rules(
        self,
        firewall_id: int,
        /,
        *,
        rules: Sequence[RuleParam],
    ) -> ActionListResponse:
        """Set Rules.

        Set the rules of a Firewall.

        Overwrites the existing rules with the given ones. Pass an empty array to remove all rules.

        Rules are limited to 50 entries per Firewall and 500 effective rules
        (https://docs.hetzner.com/cloud/firewalls/overview#limits).

        ``POST /firewalls/{id}/actions/set_rules``

        Args:
            firewall_id: ID of the Firewall.
            rules: Array of rules. Rules are limited to 50 entries per Firewall and 500 effective
                rules (https://docs.hetzner.com/cloud/firewalls/overview#limits). Existing rules
                will be replaced.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, firewall_id=firewall_id, rules=rules)
        response = self._transport.request(
            "POST",
            f"/firewalls/{encode_path(firewall_id)}/actions/set_rules",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "rules": rules,
                },
            ),
        )
        return self._transport.parse(ActionListResponse, response)

    @deprecated("GET /firewalls/{id}/actions/{action_id} is deprecated by the API")
    def get_firewall_action(self, firewall_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Firewall.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Firewall.

        ``GET /firewalls/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            firewall_id: ID of the Firewall.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, firewall_id=firewall_id, action_id=action_id)
        response = self._transport.request(
            "GET",
            f"/firewalls/{encode_path(firewall_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)


class AsyncFirewallActionsResource:
    """Operations on ``firewall_actions`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_firewalls_actions(
        self,
        *,
        id: Sequence[int] | None = None,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions.

        Returns all Actions for Firewalls.

        Use the provided URI parameters to modify the result.

        ``GET /firewalls/actions``

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
            "/firewalls/actions",
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

    async def get_firewalls_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns the specific Action.

        ``GET /firewalls/actions/{id}``

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
            f"/firewalls/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def list_firewall_actions(
        self,
        firewall_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Firewall.

        Returns all Actions for the Firewall.

        Use the provided URI parameters to modify the result.

        ``GET /firewalls/{id}/actions``

        Args:
            firewall_id: ID of the Firewall.
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
        self._transport.validate(_CHECKS_3, firewall_id=firewall_id, page=page, per_page=per_page)
        response = await self._transport.request(
            "GET",
            f"/firewalls/{encode_path(firewall_id)}/actions",
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

    async def apply_firewall_to_resources(
        self,
        firewall_id: int,
        /,
        *,
        apply_to: Sequence[FirewallResourceParam],
    ) -> ActionListResponse:
        """Apply to Resources.

        Applies a Firewall to multiple resources.

        Supported resources:
        - Servers (with a public network interface)
        - Label Selectors

        A Server can be applied to a maximum of 5 Firewalls
        (https://docs.hetzner.com/cloud/firewalls/overview#limits). This limit applies to Servers
        applied via a matching Label Selector as well.

        Updates to resources matching or no longer matching a Label Selector can take up to a few
        seconds to be processed.

        A Firewall is applied to a resource once the related Action with command `apply_firewall`
        successfully finished.

        **Operation specific errors**

        - `404` - `firewall_resource_not_found` - The resource the Firewall should be applied to was
          not found
        - `422` - `firewall_already_applied` - Firewall is already applied to resource
        - `422` - `incompatible_network_type` - The network type of the resource is not supported by
          Firewalls
        - `422` - `private_net_only_server` - The Server the Firewall should be applied to has no
          public interface

        ``POST /firewalls/{id}/actions/apply_to_resources``

        Args:
            firewall_id: ID of the Firewall.
            apply_to: Resources to apply the Firewall to. Extends existing resources.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, firewall_id=firewall_id)
        response = await self._transport.request(
            "POST",
            f"/firewalls/{encode_path(firewall_id)}/actions/apply_to_resources",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "apply_to": apply_to,
                },
            ),
        )
        return self._transport.parse(ActionListResponse, response)

    async def remove_firewall_from_resources(
        self,
        firewall_id: int,
        /,
        *,
        remove_from: Sequence[FirewallResourceParam],
    ) -> ActionListResponse:
        """Remove from Resources.

        Removes a Firewall from multiple resources.

        Supported resources:
        - Servers (with a public network interface)

        A Firewall is removed from a resource once the related Action with command `remove_firewall`
        successfully finished.

        **Operation specific errors**

        - `404` - `firewall_resource_not_found` - The resource the Firewall should be removed from
          was not found
        - `422` - `firewall_managed_by_label_selector` - Firewall is applied via a Label Selector
          and cannot be removed manually

        ``POST /firewalls/{id}/actions/remove_from_resources``

        Args:
            firewall_id: ID of the Firewall.
            remove_from: Resources to remove the Firewall from.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, firewall_id=firewall_id)
        response = await self._transport.request(
            "POST",
            f"/firewalls/{encode_path(firewall_id)}/actions/remove_from_resources",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "remove_from": remove_from,
                },
            ),
        )
        return self._transport.parse(ActionListResponse, response)

    async def set_firewall_rules(
        self,
        firewall_id: int,
        /,
        *,
        rules: Sequence[RuleParam],
    ) -> ActionListResponse:
        """Set Rules.

        Set the rules of a Firewall.

        Overwrites the existing rules with the given ones. Pass an empty array to remove all rules.

        Rules are limited to 50 entries per Firewall and 500 effective rules
        (https://docs.hetzner.com/cloud/firewalls/overview#limits).

        ``POST /firewalls/{id}/actions/set_rules``

        Args:
            firewall_id: ID of the Firewall.
            rules: Array of rules. Rules are limited to 50 entries per Firewall and 500 effective
                rules (https://docs.hetzner.com/cloud/firewalls/overview#limits). Existing rules
                will be replaced.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, firewall_id=firewall_id, rules=rules)
        response = await self._transport.request(
            "POST",
            f"/firewalls/{encode_path(firewall_id)}/actions/set_rules",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "rules": rules,
                },
            ),
        )
        return self._transport.parse(ActionListResponse, response)

    @deprecated("GET /firewalls/{id}/actions/{action_id} is deprecated by the API")
    async def get_firewall_action(self, firewall_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Firewall.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Firewall.

        ``GET /firewalls/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            firewall_id: ID of the Firewall.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, firewall_id=firewall_id, action_id=action_id)
        response = await self._transport.request(
            "GET",
            f"/firewalls/{encode_path(firewall_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)
