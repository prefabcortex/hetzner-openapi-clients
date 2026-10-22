"""Resource ``placement_groups`` (generated - do not edit by hand)."""

from collections.abc import Mapping, Sequence
from typing import Final, Literal

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
    CreatePlacementGroupResponse,
    ErrorResponse,
    PlacementGroupResponse,
    PlacementGroupsResponse,
    SortByIdNameCreated,
)
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncPlacementGroupsResource",
    "PlacementGroupsResource",
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
    "labels": LABELS_RULES,
}

_CHECKS_3: Final[Mapping[str, Check]] = {
    "placement_group_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "placement_group_id": Check(minimum=1, maximum=9007199254740991),
    "labels": LABELS_RULES,
}


class PlacementGroupsResource:
    """Operations on ``placement_groups`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_placement_groups(
        self,
        *,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        type: Sequence[Literal["spread"]] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> PlacementGroupsResponse:
        """List Placement Groups.

        Returns all Placement Group objects.

        ``GET /placement_groups``

        Args:
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            type: Filter resources by type. May be used multiple times. The response will only
                contain the resources with the specified type.
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
            "/placement_groups",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "name": name,
                    "label_selector": label_selector,
                    "type": type,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(PlacementGroupsResponse, response)

    def create_placement_group(
        self,
        *,
        name: str,
        type: Literal["spread"],
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CreatePlacementGroupResponse:
        """Create a PlacementGroup.

        Creates a new Placement Group.

        ``POST /placement_groups``

        Args:
            name: Name of the Placement Group.
            type: Define the Placement Group Type.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, labels=labels)
        response = self._transport.request(
            "POST",
            "/placement_groups",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                    "type": type,
                },
            ),
        )
        return self._transport.parse(CreatePlacementGroupResponse, response)

    def get_placement_group(self, placement_group_id: int, /) -> PlacementGroupResponse:
        """Get a PlacementGroup.

        Gets a specific Placement Group object.

        ``GET /placement_groups/{id}``

        Args:
            placement_group_id: ID of the Placement Group.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, placement_group_id=placement_group_id)
        response = self._transport.request(
            "GET",
            f"/placement_groups/{encode_path(placement_group_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(PlacementGroupResponse, response)

    def update_placement_group(
        self,
        placement_group_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> PlacementGroupResponse:
        """Update a PlacementGroup.

        Updates the Placement Group properties.

        Note: if the Placement Group object changes during the request, the response will be a
        "conflict" error.

        ``PUT /placement_groups/{id}``

        Args:
            placement_group_id: ID of the Placement Group.
            name: New Placement Group name. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, placement_group_id=placement_group_id, labels=labels)
        response = self._transport.request(
            "PUT",
            f"/placement_groups/{encode_path(placement_group_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(PlacementGroupResponse, response)

    def delete_placement_group(self, placement_group_id: int, /) -> None:
        """Delete a PlacementGroup.

        Deletes a Placement Group.

        ``DELETE /placement_groups/{id}``

        Args:
            placement_group_id: ID of the Placement Group.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, placement_group_id=placement_group_id)
        self._transport.request(
            "DELETE",
            f"/placement_groups/{encode_path(placement_group_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )


class AsyncPlacementGroupsResource:
    """Operations on ``placement_groups`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_placement_groups(
        self,
        *,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        type: Sequence[Literal["spread"]] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> PlacementGroupsResponse:
        """List Placement Groups.

        Returns all Placement Group objects.

        ``GET /placement_groups``

        Args:
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            type: Filter resources by type. May be used multiple times. The response will only
                contain the resources with the specified type.
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
            "/placement_groups",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "name": name,
                    "label_selector": label_selector,
                    "type": type,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(PlacementGroupsResponse, response)

    async def create_placement_group(
        self,
        *,
        name: str,
        type: Literal["spread"],
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CreatePlacementGroupResponse:
        """Create a PlacementGroup.

        Creates a new Placement Group.

        ``POST /placement_groups``

        Args:
            name: Name of the Placement Group.
            type: Define the Placement Group Type.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, labels=labels)
        response = await self._transport.request(
            "POST",
            "/placement_groups",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                    "type": type,
                },
            ),
        )
        return self._transport.parse(CreatePlacementGroupResponse, response)

    async def get_placement_group(self, placement_group_id: int, /) -> PlacementGroupResponse:
        """Get a PlacementGroup.

        Gets a specific Placement Group object.

        ``GET /placement_groups/{id}``

        Args:
            placement_group_id: ID of the Placement Group.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, placement_group_id=placement_group_id)
        response = await self._transport.request(
            "GET",
            f"/placement_groups/{encode_path(placement_group_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(PlacementGroupResponse, response)

    async def update_placement_group(
        self,
        placement_group_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> PlacementGroupResponse:
        """Update a PlacementGroup.

        Updates the Placement Group properties.

        Note: if the Placement Group object changes during the request, the response will be a
        "conflict" error.

        ``PUT /placement_groups/{id}``

        Args:
            placement_group_id: ID of the Placement Group.
            name: New Placement Group name. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, placement_group_id=placement_group_id, labels=labels)
        response = await self._transport.request(
            "PUT",
            f"/placement_groups/{encode_path(placement_group_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(PlacementGroupResponse, response)

    async def delete_placement_group(self, placement_group_id: int, /) -> None:
        """Delete a PlacementGroup.

        Deletes a Placement Group.

        ``DELETE /placement_groups/{id}``

        Args:
            placement_group_id: ID of the Placement Group.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, placement_group_id=placement_group_id)
        await self._transport.request(
            "DELETE",
            f"/placement_groups/{encode_path(placement_group_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
