"""Resource ``floating_ips`` (generated - do not edit by hand)."""

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
    CreateFloatingIpResponse,
    ErrorResponse,
    FloatingIpResponse,
    IpType,
    ListFloatingIpsResponse,
    SortByIdCreated,
)
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncFloatingIpsResource",
    "FloatingIpsResource",
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
    "name": Check(min_length=1, max_length=255),
    "labels": LABELS_RULES,
}

_CHECKS_3: Final[Mapping[str, Check]] = {
    "floating_ip_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "floating_ip_id": Check(minimum=1, maximum=9007199254740991),
    "name": Check(min_length=1, max_length=255),
    "labels": LABELS_RULES,
}


class FloatingIpsResource:
    """Operations on ``floating_ips`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_floating_ips(
        self,
        *,
        name: str | None = None,
        label_selector: str | None = None,
        sort: Sequence[SortByIdCreated | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListFloatingIpsResponse:
        """List Floating IPs.

        List multiple Floating IPs.

        Use the provided URI parameters to modify the result.

        ``GET /floating_ips``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
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
            "/floating_ips",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "label_selector": label_selector,
                    "sort": sort,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListFloatingIpsResponse, response)

    def create_floating_ip(
        self,
        *,
        type: IpType | UnknownValue,
        server: int | NotGiven | None = NOT_GIVEN,
        home_location: str | int | NotGiven = NOT_GIVEN,
        description: str | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CreateFloatingIpResponse:
        """Create a Floating IP.

        ``POST /floating_ips``

        Args:
            type: The Floating IP type.
            server: Server the Floating IP is assigned to. `null` if not assigned. Omitted if not
                given.
            home_location: Home Location for the Floating IP. Either the ID or the name of the
                Location. Only optional if no Server is provided. Routing is optimized for this
                Locations. Omitted if not given.
            description: Description of the Resource. Omitted if not given.
            name: Name of the Resource. Must be unique per Project. A name will be generated if none
                is given. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, name=name, labels=labels)
        response = self._transport.request(
            "POST",
            "/floating_ips",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "type": type,
                    "server": server,
                    "home_location": home_location,
                    "description": description,
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(CreateFloatingIpResponse, response)

    def get_floating_ip(self, floating_ip_id: int, /) -> FloatingIpResponse:
        """Get a Floating IP.

        Returns a single Floating IP.

        ``GET /floating_ips/{id}``

        Args:
            floating_ip_id: ID of the Floating IP.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, floating_ip_id=floating_ip_id)
        response = self._transport.request(
            "GET",
            f"/floating_ips/{encode_path(floating_ip_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(FloatingIpResponse, response)

    def update_floating_ip(
        self,
        floating_ip_id: int,
        /,
        *,
        description: str | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> FloatingIpResponse:
        """Update a Floating IP.

        ``PUT /floating_ips/{id}``

        Args:
            floating_ip_id: ID of the Floating IP.
            description: Description of the Resource. Omitted if not given.
            name: Name of the Resource. Must be unique per Project. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, floating_ip_id=floating_ip_id, name=name, labels=labels)
        response = self._transport.request(
            "PUT",
            f"/floating_ips/{encode_path(floating_ip_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "description": description,
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(FloatingIpResponse, response)

    def delete_floating_ip(self, floating_ip_id: int, /) -> None:
        """Delete a Floating IP.

        Deletes a Floating IP.

        If assigned to a Server the Floating IP will be unassigned automatically until 1 May 2026.
        After this date, the Floating IP needs to be unassigned before it can be deleted.

        **Operation specific errors**

        - `422` - `must_be_unassigned` - Error when IP is still assigned to a Resource. This error
          will appear as of 1 May 2026.

        ``DELETE /floating_ips/{id}``

        Args:
            floating_ip_id: ID of the Floating IP.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, floating_ip_id=floating_ip_id)
        self._transport.request(
            "DELETE",
            f"/floating_ips/{encode_path(floating_ip_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )


class AsyncFloatingIpsResource:
    """Operations on ``floating_ips`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_floating_ips(
        self,
        *,
        name: str | None = None,
        label_selector: str | None = None,
        sort: Sequence[SortByIdCreated | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListFloatingIpsResponse:
        """List Floating IPs.

        List multiple Floating IPs.

        Use the provided URI parameters to modify the result.

        ``GET /floating_ips``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
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
            "/floating_ips",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "label_selector": label_selector,
                    "sort": sort,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListFloatingIpsResponse, response)

    async def create_floating_ip(
        self,
        *,
        type: IpType | UnknownValue,
        server: int | NotGiven | None = NOT_GIVEN,
        home_location: str | int | NotGiven = NOT_GIVEN,
        description: str | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CreateFloatingIpResponse:
        """Create a Floating IP.

        ``POST /floating_ips``

        Args:
            type: The Floating IP type.
            server: Server the Floating IP is assigned to. `null` if not assigned. Omitted if not
                given.
            home_location: Home Location for the Floating IP. Either the ID or the name of the
                Location. Only optional if no Server is provided. Routing is optimized for this
                Locations. Omitted if not given.
            description: Description of the Resource. Omitted if not given.
            name: Name of the Resource. Must be unique per Project. A name will be generated if none
                is given. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, name=name, labels=labels)
        response = await self._transport.request(
            "POST",
            "/floating_ips",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "type": type,
                    "server": server,
                    "home_location": home_location,
                    "description": description,
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(CreateFloatingIpResponse, response)

    async def get_floating_ip(self, floating_ip_id: int, /) -> FloatingIpResponse:
        """Get a Floating IP.

        Returns a single Floating IP.

        ``GET /floating_ips/{id}``

        Args:
            floating_ip_id: ID of the Floating IP.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, floating_ip_id=floating_ip_id)
        response = await self._transport.request(
            "GET",
            f"/floating_ips/{encode_path(floating_ip_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(FloatingIpResponse, response)

    async def update_floating_ip(
        self,
        floating_ip_id: int,
        /,
        *,
        description: str | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> FloatingIpResponse:
        """Update a Floating IP.

        ``PUT /floating_ips/{id}``

        Args:
            floating_ip_id: ID of the Floating IP.
            description: Description of the Resource. Omitted if not given.
            name: Name of the Resource. Must be unique per Project. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, floating_ip_id=floating_ip_id, name=name, labels=labels)
        response = await self._transport.request(
            "PUT",
            f"/floating_ips/{encode_path(floating_ip_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "description": description,
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(FloatingIpResponse, response)

    async def delete_floating_ip(self, floating_ip_id: int, /) -> None:
        """Delete a Floating IP.

        Deletes a Floating IP.

        If assigned to a Server the Floating IP will be unassigned automatically until 1 May 2026.
        After this date, the Floating IP needs to be unassigned before it can be deleted.

        **Operation specific errors**

        - `422` - `must_be_unassigned` - Error when IP is still assigned to a Resource. This error
          will appear as of 1 May 2026.

        ``DELETE /floating_ips/{id}``

        Args:
            floating_ip_id: ID of the Floating IP.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, floating_ip_id=floating_ip_id)
        await self._transport.request(
            "DELETE",
            f"/floating_ips/{encode_path(floating_ip_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
