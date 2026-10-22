"""Resource ``storage_box_subaccounts`` (generated - do not edit by hand)."""

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
    ActionResponse,
    CreateStorageBoxSubaccountResponse,
    ErrorResponse,
    ListStorageBoxSubaccountsResponse,
    SortByIdCreated,
    SubaccountResponse,
)
from hetzner_api.params import CreateStorageBoxSubaccountAccessSettingsParam
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncStorageBoxSubaccountsResource",
    "StorageBoxSubaccountsResource",
]

_SECURITY_1: Final[Security] = (("APIToken",),)

_ERRORS_1: Final[ErrorModels] = {
    "4XX": ErrorResponse,
    "5XX": ErrorResponse,
}

_CHECKS_1: Final[Mapping[str, Check]] = {
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_2: Final[Mapping[str, Check]] = {
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
    "home_directory": Check(min_length=1, max_length=999, pattern="^[a-zA-Z0-9\x20./_-]+$"),
    "name": Check(min_length=1, max_length=50),
    "description": Check(max_length=1000),
    "labels": LABELS_RULES,
}

_CHECKS_3: Final[Mapping[str, Check]] = {
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
    "subaccount_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
    "subaccount_id": Check(minimum=1, maximum=9007199254740991),
    "name": Check(min_length=1, max_length=50),
    "description": Check(max_length=1000),
    "labels": LABELS_RULES,
}


class StorageBoxSubaccountsResource:
    """Operations on ``storage_box_subaccounts`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_storage_box_subaccounts(
        self,
        storage_box_id: int,
        /,
        *,
        name: str | None = None,
        label_selector: str | None = None,
        sort: Sequence[SortByIdCreated | UnknownValue] | None = None,
        username: str | None = None,
    ) -> ListStorageBoxSubaccountsResponse:
        """List Subaccounts.

        Returns a list of Storage Box Subaccount.

        ``GET /storage_boxes/{id}/subaccounts``

        Args:
            storage_box_id: ID of the Storage Box.
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            username: Filter Storage Box Subaccounts by username. The response will only contain the
                resources matching exactly the specified username.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, storage_box_id=storage_box_id)
        response = self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "label_selector": label_selector,
                    "sort": sort,
                    "username": username,
                },
            ),
        )
        return self._transport.parse(ListStorageBoxSubaccountsResponse, response)

    def create_storage_box_subaccount(
        self,
        storage_box_id: int,
        /,
        *,
        home_directory: str,
        password: str,
        access_settings: CreateStorageBoxSubaccountAccessSettingsParam | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CreateStorageBoxSubaccountResponse:
        """Create a Subaccount.

        Creates a Storage Box Subaccount.

        A Storage Box Subaccount will use a separate home directory.

        ``POST /storage_boxes/{id}/subaccounts``

        Args:
            storage_box_id: ID of the Storage Box.
            home_directory: Home directory of the Storage Box Subaccount. The directory will be
                created if it doesn't exist yet.
            password: Password of the Storage Box Subaccount. For more details, see the Storage
                Boxes password policy.
            access_settings: ``access_settings``. Omitted if not given.
            name: Name of the Storage Box Subaccount. Defaults to the Storage Box Subaccount
                `username`. Omitted if not given.
            description: A description of Storage Box Subaccount. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_2,
            storage_box_id=storage_box_id,
            home_directory=home_directory,
            name=name,
            description=description,
            labels=labels,
        )
        response = self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "home_directory": home_directory,
                    "password": password,
                    "access_settings": access_settings,
                    "name": name,
                    "description": description,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(CreateStorageBoxSubaccountResponse, response)

    def get_storage_box_subaccount(
        self,
        storage_box_id: int,
        subaccount_id: int,
        /,
    ) -> SubaccountResponse:
        """Get a Subaccount.

        Returns a specific Storage Box Subaccount.

        ``GET /storage_boxes/{id}/subaccounts/{subaccount_id}``

        Args:
            storage_box_id: ID of the Storage Box.
            subaccount_id: ID of the Storage Box Subaccount.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_3,
            storage_box_id=storage_box_id,
            subaccount_id=subaccount_id,
        )
        response = self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts/{encode_path(subaccount_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(SubaccountResponse, response)

    def update_storage_box_subaccount(
        self,
        storage_box_id: int,
        subaccount_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> SubaccountResponse:
        """Update a Subaccount.

        Updates a Storage Box Subaccount.

        ``PUT /storage_boxes/{id}/subaccounts/{subaccount_id}``

        Args:
            storage_box_id: ID of the Storage Box.
            subaccount_id: ID of the Storage Box Subaccount.
            name: Name of the Storage Box Subaccount. Omitted if not given.
            description: A description of Storage Box Subaccount. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_4,
            storage_box_id=storage_box_id,
            subaccount_id=subaccount_id,
            name=name,
            description=description,
            labels=labels,
        )
        response = self._transport.request(
            "PUT",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts/{encode_path(subaccount_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "description": description,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(SubaccountResponse, response)

    def delete_storage_box_subaccount(
        self,
        storage_box_id: int,
        subaccount_id: int,
        /,
    ) -> ActionResponse:
        """Delete a Subaccount.

        Deletes a Storage Box Subaccount.

        ``DELETE /storage_boxes/{id}/subaccounts/{subaccount_id}``

        Args:
            storage_box_id: ID of the Storage Box.
            subaccount_id: ID of the Storage Box Subaccount.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_3,
            storage_box_id=storage_box_id,
            subaccount_id=subaccount_id,
        )
        response = self._transport.request(
            "DELETE",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts/{encode_path(subaccount_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)


class AsyncStorageBoxSubaccountsResource:
    """Operations on ``storage_box_subaccounts`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_storage_box_subaccounts(
        self,
        storage_box_id: int,
        /,
        *,
        name: str | None = None,
        label_selector: str | None = None,
        sort: Sequence[SortByIdCreated | UnknownValue] | None = None,
        username: str | None = None,
    ) -> ListStorageBoxSubaccountsResponse:
        """List Subaccounts.

        Returns a list of Storage Box Subaccount.

        ``GET /storage_boxes/{id}/subaccounts``

        Args:
            storage_box_id: ID of the Storage Box.
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            username: Filter Storage Box Subaccounts by username. The response will only contain the
                resources matching exactly the specified username.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, storage_box_id=storage_box_id)
        response = await self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "label_selector": label_selector,
                    "sort": sort,
                    "username": username,
                },
            ),
        )
        return self._transport.parse(ListStorageBoxSubaccountsResponse, response)

    async def create_storage_box_subaccount(
        self,
        storage_box_id: int,
        /,
        *,
        home_directory: str,
        password: str,
        access_settings: CreateStorageBoxSubaccountAccessSettingsParam | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CreateStorageBoxSubaccountResponse:
        """Create a Subaccount.

        Creates a Storage Box Subaccount.

        A Storage Box Subaccount will use a separate home directory.

        ``POST /storage_boxes/{id}/subaccounts``

        Args:
            storage_box_id: ID of the Storage Box.
            home_directory: Home directory of the Storage Box Subaccount. The directory will be
                created if it doesn't exist yet.
            password: Password of the Storage Box Subaccount. For more details, see the Storage
                Boxes password policy.
            access_settings: ``access_settings``. Omitted if not given.
            name: Name of the Storage Box Subaccount. Defaults to the Storage Box Subaccount
                `username`. Omitted if not given.
            description: A description of Storage Box Subaccount. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_2,
            storage_box_id=storage_box_id,
            home_directory=home_directory,
            name=name,
            description=description,
            labels=labels,
        )
        response = await self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "home_directory": home_directory,
                    "password": password,
                    "access_settings": access_settings,
                    "name": name,
                    "description": description,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(CreateStorageBoxSubaccountResponse, response)

    async def get_storage_box_subaccount(
        self,
        storage_box_id: int,
        subaccount_id: int,
        /,
    ) -> SubaccountResponse:
        """Get a Subaccount.

        Returns a specific Storage Box Subaccount.

        ``GET /storage_boxes/{id}/subaccounts/{subaccount_id}``

        Args:
            storage_box_id: ID of the Storage Box.
            subaccount_id: ID of the Storage Box Subaccount.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_3,
            storage_box_id=storage_box_id,
            subaccount_id=subaccount_id,
        )
        response = await self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts/{encode_path(subaccount_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(SubaccountResponse, response)

    async def update_storage_box_subaccount(
        self,
        storage_box_id: int,
        subaccount_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> SubaccountResponse:
        """Update a Subaccount.

        Updates a Storage Box Subaccount.

        ``PUT /storage_boxes/{id}/subaccounts/{subaccount_id}``

        Args:
            storage_box_id: ID of the Storage Box.
            subaccount_id: ID of the Storage Box Subaccount.
            name: Name of the Storage Box Subaccount. Omitted if not given.
            description: A description of Storage Box Subaccount. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_4,
            storage_box_id=storage_box_id,
            subaccount_id=subaccount_id,
            name=name,
            description=description,
            labels=labels,
        )
        response = await self._transport.request(
            "PUT",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts/{encode_path(subaccount_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "description": description,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(SubaccountResponse, response)

    async def delete_storage_box_subaccount(
        self,
        storage_box_id: int,
        subaccount_id: int,
        /,
    ) -> ActionResponse:
        """Delete a Subaccount.

        Deletes a Storage Box Subaccount.

        ``DELETE /storage_boxes/{id}/subaccounts/{subaccount_id}``

        Args:
            storage_box_id: ID of the Storage Box.
            subaccount_id: ID of the Storage Box Subaccount.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_3,
            storage_box_id=storage_box_id,
            subaccount_id=subaccount_id,
        )
        response = await self._transport.request(
            "DELETE",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts/{encode_path(subaccount_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)
