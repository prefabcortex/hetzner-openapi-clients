"""Resource ``primary_ips`` (generated - do not edit by hand)."""

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
    AssigneeType,
    CreatePrimaryIPResponse,
    ErrorResponse,
    IpType,
    PrimaryIPResponse,
    PrimaryIPsResponse,
    SortByIdCreated,
)
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncPrimaryIpsResource",
    "PrimaryIpsResource",
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
    "primary_ip_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "primary_ip_id": Check(minimum=1, maximum=9007199254740991),
    "name": Check(min_length=1, max_length=255),
    "labels": LABELS_RULES,
}


class PrimaryIpsResource:
    """Operations on ``primary_ips`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_primary_ips(
        self,
        *,
        name: str | None = None,
        label_selector: str | None = None,
        ip: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        sort: Sequence[SortByIdCreated | UnknownValue] | None = None,
    ) -> PrimaryIPsResponse:
        """List Primary IPs.

        List multiple Primary IPs.

        Use the provided URI parameters to modify the result.

        ``GET /primary_ips``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            ip: Filter results by IP address.
            page: Page number to return. For more information, see "Pagination". The API default is
                ``1``.
            per_page: Maximum number of entries returned per page. For more information, see
                "Pagination". The API default is ``25``.
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, page=page, per_page=per_page)
        response = self._transport.request(
            "GET",
            "/primary_ips",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "label_selector": label_selector,
                    "ip": ip,
                    "page": page,
                    "per_page": per_page,
                    "sort": sort,
                },
            ),
        )
        return self._transport.parse(PrimaryIPsResponse, response)

    def create_primary_ip(
        self,
        *,
        name: str,
        type: IpType | UnknownValue,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        location: str | int | NotGiven = NOT_GIVEN,
        assignee_type: AssigneeType | UnknownValue | NotGiven = NOT_GIVEN,
        assignee_id: int | NotGiven | None = NOT_GIVEN,
        auto_delete: bool | NotGiven = NOT_GIVEN,
    ) -> CreatePrimaryIPResponse:
        """Create a Primary IP.

        Create a new Primary IP.

        Can optionally be assigned to a resource by providing an `assignee_id` and `assignee_type`.

        If not assigned to a resource the `location` key needs to be provided. This can be either
        the ID or the name of the Location this Primary IP shall be created in.

        A Primary IP can only be assigned to resource in the same Location later on.

        **Operation specific errors**

        - `422` - `server_not_stopped` - The specified Server is running, but needs to be powered
          off
        - `422` - `server_has_ipv4` - The Server already has an ipv4 address
        - `422` - `server_has_ipv6` - The Server already has an ipv6 address

        ``POST /primary_ips``

        Args:
            name: Name of the Resource. Must be unique per Project.
            type: Primary IP type.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            location: Location ID or name the Primary IP will be bound to. Omit if
                `assignee_id`/`assignee_type` or `datacenter` are provided. Omitted if not given.
            assignee_type: Type of resource to assign the Primary IP to. Omitted if the Primary IP
                should not get assigned. Omitted if not given.
            assignee_id: ID of resource to assign the Primary IP to. Omitted if the Primary IP
                should not get assigned. Omitted if not given.
            auto_delete: Auto deletion state. If enabled the Primary IP will be deleted once the
                assigned resource gets deleted. Omitted if not given. The API default is ``False``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, name=name, labels=labels)
        response = self._transport.request(
            "POST",
            "/primary_ips",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                    "type": type,
                    "location": location,
                    "assignee_type": assignee_type,
                    "assignee_id": assignee_id,
                    "auto_delete": auto_delete,
                },
            ),
        )
        return self._transport.parse(CreatePrimaryIPResponse, response)

    def get_primary_ip(self, primary_ip_id: int, /) -> PrimaryIPResponse:
        """Get a Primary IP.

        Returns a Primary IP.

        ``GET /primary_ips/{id}``

        Args:
            primary_ip_id: ID of the Primary IP.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, primary_ip_id=primary_ip_id)
        response = self._transport.request(
            "GET",
            f"/primary_ips/{encode_path(primary_ip_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(PrimaryIPResponse, response)

    def update_primary_ip(
        self,
        primary_ip_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        auto_delete: bool | NotGiven = NOT_GIVEN,
    ) -> PrimaryIPResponse:
        """Update a Primary IP.

        ``PUT /primary_ips/{id}``

        Args:
            primary_ip_id: ID of the Primary IP.
            name: Name of the Resource. Must be unique per Project. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.
            auto_delete: Auto deletion state. If enabled the Primary IP will be deleted once the
                assigned resource gets deleted. Omitted if not given. The API default is ``False``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, primary_ip_id=primary_ip_id, name=name, labels=labels)
        response = self._transport.request(
            "PUT",
            f"/primary_ips/{encode_path(primary_ip_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                    "auto_delete": auto_delete,
                },
            ),
        )
        return self._transport.parse(PrimaryIPResponse, response)

    def delete_primary_ip(self, primary_ip_id: int, /) -> None:
        """Delete a Primary IP.

        Deletes a Primary IP.

        The Server must be powered off (status `off`) in order for this operation to succeed. If
        assigned to a Server the Primary IP will be unassigned automatically until 1 May 2026. After
        this date, the Primary IP needs to be unassigned before it can be deleted.

        **Operation specific errors**

        - `422` - `must_be_unassigned` - Error when IP is still assigned to a Resource. This error
          will appear as of 1 May 2026.

        ``DELETE /primary_ips/{id}``

        Args:
            primary_ip_id: ID of the Primary IP.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, primary_ip_id=primary_ip_id)
        self._transport.request(
            "DELETE",
            f"/primary_ips/{encode_path(primary_ip_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )


class AsyncPrimaryIpsResource:
    """Operations on ``primary_ips`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_primary_ips(
        self,
        *,
        name: str | None = None,
        label_selector: str | None = None,
        ip: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
        sort: Sequence[SortByIdCreated | UnknownValue] | None = None,
    ) -> PrimaryIPsResponse:
        """List Primary IPs.

        List multiple Primary IPs.

        Use the provided URI parameters to modify the result.

        ``GET /primary_ips``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            ip: Filter results by IP address.
            page: Page number to return. For more information, see "Pagination". The API default is
                ``1``.
            per_page: Maximum number of entries returned per page. For more information, see
                "Pagination". The API default is ``25``.
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, page=page, per_page=per_page)
        response = await self._transport.request(
            "GET",
            "/primary_ips",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "label_selector": label_selector,
                    "ip": ip,
                    "page": page,
                    "per_page": per_page,
                    "sort": sort,
                },
            ),
        )
        return self._transport.parse(PrimaryIPsResponse, response)

    async def create_primary_ip(
        self,
        *,
        name: str,
        type: IpType | UnknownValue,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        location: str | int | NotGiven = NOT_GIVEN,
        assignee_type: AssigneeType | UnknownValue | NotGiven = NOT_GIVEN,
        assignee_id: int | NotGiven | None = NOT_GIVEN,
        auto_delete: bool | NotGiven = NOT_GIVEN,
    ) -> CreatePrimaryIPResponse:
        """Create a Primary IP.

        Create a new Primary IP.

        Can optionally be assigned to a resource by providing an `assignee_id` and `assignee_type`.

        If not assigned to a resource the `location` key needs to be provided. This can be either
        the ID or the name of the Location this Primary IP shall be created in.

        A Primary IP can only be assigned to resource in the same Location later on.

        **Operation specific errors**

        - `422` - `server_not_stopped` - The specified Server is running, but needs to be powered
          off
        - `422` - `server_has_ipv4` - The Server already has an ipv4 address
        - `422` - `server_has_ipv6` - The Server already has an ipv6 address

        ``POST /primary_ips``

        Args:
            name: Name of the Resource. Must be unique per Project.
            type: Primary IP type.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            location: Location ID or name the Primary IP will be bound to. Omit if
                `assignee_id`/`assignee_type` or `datacenter` are provided. Omitted if not given.
            assignee_type: Type of resource to assign the Primary IP to. Omitted if the Primary IP
                should not get assigned. Omitted if not given.
            assignee_id: ID of resource to assign the Primary IP to. Omitted if the Primary IP
                should not get assigned. Omitted if not given.
            auto_delete: Auto deletion state. If enabled the Primary IP will be deleted once the
                assigned resource gets deleted. Omitted if not given. The API default is ``False``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, name=name, labels=labels)
        response = await self._transport.request(
            "POST",
            "/primary_ips",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                    "type": type,
                    "location": location,
                    "assignee_type": assignee_type,
                    "assignee_id": assignee_id,
                    "auto_delete": auto_delete,
                },
            ),
        )
        return self._transport.parse(CreatePrimaryIPResponse, response)

    async def get_primary_ip(self, primary_ip_id: int, /) -> PrimaryIPResponse:
        """Get a Primary IP.

        Returns a Primary IP.

        ``GET /primary_ips/{id}``

        Args:
            primary_ip_id: ID of the Primary IP.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, primary_ip_id=primary_ip_id)
        response = await self._transport.request(
            "GET",
            f"/primary_ips/{encode_path(primary_ip_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(PrimaryIPResponse, response)

    async def update_primary_ip(
        self,
        primary_ip_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        auto_delete: bool | NotGiven = NOT_GIVEN,
    ) -> PrimaryIPResponse:
        """Update a Primary IP.

        ``PUT /primary_ips/{id}``

        Args:
            primary_ip_id: ID of the Primary IP.
            name: Name of the Resource. Must be unique per Project. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.
            auto_delete: Auto deletion state. If enabled the Primary IP will be deleted once the
                assigned resource gets deleted. Omitted if not given. The API default is ``False``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, primary_ip_id=primary_ip_id, name=name, labels=labels)
        response = await self._transport.request(
            "PUT",
            f"/primary_ips/{encode_path(primary_ip_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                    "auto_delete": auto_delete,
                },
            ),
        )
        return self._transport.parse(PrimaryIPResponse, response)

    async def delete_primary_ip(self, primary_ip_id: int, /) -> None:
        """Delete a Primary IP.

        Deletes a Primary IP.

        The Server must be powered off (status `off`) in order for this operation to succeed. If
        assigned to a Server the Primary IP will be unassigned automatically until 1 May 2026. After
        this date, the Primary IP needs to be unassigned before it can be deleted.

        **Operation specific errors**

        - `422` - `must_be_unassigned` - Error when IP is still assigned to a Resource. This error
          will appear as of 1 May 2026.

        ``DELETE /primary_ips/{id}``

        Args:
            primary_ip_id: ID of the Primary IP.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, primary_ip_id=primary_ip_id)
        await self._transport.request(
            "DELETE",
            f"/primary_ips/{encode_path(primary_ip_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
