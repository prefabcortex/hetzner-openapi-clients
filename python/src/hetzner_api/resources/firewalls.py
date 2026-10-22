"""Resource ``firewalls`` (generated - do not edit by hand)."""

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
from hetzner_api._types import NOT_GIVEN, NotGiven, UnknownValue
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import (
    CreateFirewallResponse,
    ErrorResponse,
    FirewallResponse,
    FirewallsResponse,
    SortByIdNameCreated,
)
from hetzner_api.params import FirewallResourceParam, RuleParam
from hetzner_api.rules import LABELS_RULES, RULE_FIELDS

__all__ = [
    "AsyncFirewallsResource",
    "FirewallsResource",
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
    "rules": Check(items=Check(fields_of=lambda: RULE_FIELDS)),
}

_CHECKS_3: Final[Mapping[str, Check]] = {
    "firewall_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "firewall_id": Check(minimum=1, maximum=9007199254740991),
    "name": Check(min_length=1, max_length=128),
    "labels": LABELS_RULES,
}


class FirewallsResource:
    """Operations on ``firewalls`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_firewalls(
        self,
        *,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> FirewallsResponse:
        """List Firewalls.

        Returns all Firewalls.

        Use the provided URI parameters to modify the result.

        ``GET /firewalls``

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
            "/firewalls",
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
        return self._transport.parse(FirewallsResponse, response)

    def create_firewall(
        self,
        *,
        name: str,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        rules: Sequence[RuleParam] | NotGiven = NOT_GIVEN,
        apply_to: Sequence[FirewallResourceParam] | NotGiven = NOT_GIVEN,
    ) -> CreateFirewallResponse:
        """Create a Firewall.

        ``POST /firewalls``

        Args:
            name: Name of the Firewall. Must be unique per Project.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            rules: Array of rules. Rules are limited to 50 entries per Firewall and 500 effective
                rules (https://docs.hetzner.com/cloud/firewalls/overview#limits). Omitted if not
                given.
            apply_to: Resources to apply the Firewall to. Resources added directly are taking
                precedence over those added via a Label Selector. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, name=name, labels=labels, rules=rules)
        response = self._transport.request(
            "POST",
            "/firewalls",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                    "rules": rules,
                    "apply_to": apply_to,
                },
            ),
        )
        return self._transport.parse(CreateFirewallResponse, response)

    def get_firewall(self, firewall_id: int, /) -> FirewallResponse:
        """Get a Firewall.

        Returns a single Firewall.

        ``GET /firewalls/{id}``

        Args:
            firewall_id: ID of the Firewall.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, firewall_id=firewall_id)
        response = self._transport.request(
            "GET",
            f"/firewalls/{encode_path(firewall_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(FirewallResponse, response)

    def update_firewall(
        self,
        firewall_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> FirewallResponse:
        """Update a Firewall.

        ``PUT /firewalls/{id}``

        Args:
            firewall_id: ID of the Firewall.
            name: Name of the Firewall. Must be unique per Project. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, firewall_id=firewall_id, name=name, labels=labels)
        response = self._transport.request(
            "PUT",
            f"/firewalls/{encode_path(firewall_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(FirewallResponse, response)

    def delete_firewall(self, firewall_id: int, /) -> None:
        """Delete a Firewall.

        Deletes the Firewall.

        **Operation specific errors**

        - `422` - `resource_in_use` - Firewall still applied to a resource

        ``DELETE /firewalls/{id}``

        Args:
            firewall_id: ID of the Firewall.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, firewall_id=firewall_id)
        self._transport.request(
            "DELETE",
            f"/firewalls/{encode_path(firewall_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )


class AsyncFirewallsResource:
    """Operations on ``firewalls`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_firewalls(
        self,
        *,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> FirewallsResponse:
        """List Firewalls.

        Returns all Firewalls.

        Use the provided URI parameters to modify the result.

        ``GET /firewalls``

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
            "/firewalls",
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
        return self._transport.parse(FirewallsResponse, response)

    async def create_firewall(
        self,
        *,
        name: str,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        rules: Sequence[RuleParam] | NotGiven = NOT_GIVEN,
        apply_to: Sequence[FirewallResourceParam] | NotGiven = NOT_GIVEN,
    ) -> CreateFirewallResponse:
        """Create a Firewall.

        ``POST /firewalls``

        Args:
            name: Name of the Firewall. Must be unique per Project.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            rules: Array of rules. Rules are limited to 50 entries per Firewall and 500 effective
                rules (https://docs.hetzner.com/cloud/firewalls/overview#limits). Omitted if not
                given.
            apply_to: Resources to apply the Firewall to. Resources added directly are taking
                precedence over those added via a Label Selector. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, name=name, labels=labels, rules=rules)
        response = await self._transport.request(
            "POST",
            "/firewalls",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                    "rules": rules,
                    "apply_to": apply_to,
                },
            ),
        )
        return self._transport.parse(CreateFirewallResponse, response)

    async def get_firewall(self, firewall_id: int, /) -> FirewallResponse:
        """Get a Firewall.

        Returns a single Firewall.

        ``GET /firewalls/{id}``

        Args:
            firewall_id: ID of the Firewall.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, firewall_id=firewall_id)
        response = await self._transport.request(
            "GET",
            f"/firewalls/{encode_path(firewall_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(FirewallResponse, response)

    async def update_firewall(
        self,
        firewall_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> FirewallResponse:
        """Update a Firewall.

        ``PUT /firewalls/{id}``

        Args:
            firewall_id: ID of the Firewall.
            name: Name of the Firewall. Must be unique per Project. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, firewall_id=firewall_id, name=name, labels=labels)
        response = await self._transport.request(
            "PUT",
            f"/firewalls/{encode_path(firewall_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(FirewallResponse, response)

    async def delete_firewall(self, firewall_id: int, /) -> None:
        """Delete a Firewall.

        Deletes the Firewall.

        **Operation specific errors**

        - `422` - `resource_in_use` - Firewall still applied to a resource

        ``DELETE /firewalls/{id}``

        Args:
            firewall_id: ID of the Firewall.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, firewall_id=firewall_id)
        await self._transport.request(
            "DELETE",
            f"/firewalls/{encode_path(firewall_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
