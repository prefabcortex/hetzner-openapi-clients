"""Resource ``storage_boxes`` (generated - do not edit by hand)."""

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
from hetzner_api._types import NOT_GIVEN, NotGiven, StrSequence, UnknownValue
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import (
    ActionResponse,
    CreateStorageBoxResponse,
    ErrorResponse,
    ListStorageBoxesResponse,
    ListStorageBoxesSort,
    ListStorageBoxFoldersResponse,
    StorageBoxResponse,
)
from hetzner_api.params import CreateStorageBoxAccessSettingsParam
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncStorageBoxesResource",
    "StorageBoxesResource",
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
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
    "labels": LABELS_RULES,
}


class StorageBoxesResource:
    """Operations on ``storage_boxes`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_storage_boxes(
        self,
        *,
        name: str | None = None,
        label_selector: str | None = None,
        sort: Sequence[ListStorageBoxesSort | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListStorageBoxesResponse:
        """List Storage Boxes.

        Returns a paginated list of Storage Boxes.

        ``GET /storage_boxes``

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
            "/storage_boxes",
            server="hetzner",
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
        return self._transport.parse(ListStorageBoxesResponse, response)

    def create_storage_box(
        self,
        *,
        name: str,
        location: str | int,
        storage_box_type: str | int,
        password: str,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        ssh_keys: StrSequence | NotGiven = NOT_GIVEN,
        access_settings: CreateStorageBoxAccessSettingsParam | NotGiven = NOT_GIVEN,
    ) -> CreateStorageBoxResponse:
        """Create a Storage Box.

        Creates a Storage Box.

        ``POST /storage_boxes``

        Args:
            name: Name of the Storage Box.
            location: ID or Name of Location.
            storage_box_type: ID or Name of the Storage Box Type.
            password: Password of the Storage Box. For more details, see the Storage Boxes password
                policy.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            ssh_keys: SSH public keys in OpenSSH format to inject into the Storage Box. Omitted if
                not given.
            access_settings: Access settings of the Storage Box. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, labels=labels)
        response = self._transport.request(
            "POST",
            "/storage_boxes",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "location": location,
                    "storage_box_type": storage_box_type,
                    "password": password,
                    "labels": labels,
                    "ssh_keys": ssh_keys,
                    "access_settings": access_settings,
                },
            ),
        )
        return self._transport.parse(CreateStorageBoxResponse, response)

    def get_storage_box(self, storage_box_id: int, /) -> StorageBoxResponse:
        """Get a Storage Box.

        Returns a specific Storage Box.

        ``GET /storage_boxes/{id}``

        Args:
            storage_box_id: ID of the Storage Box.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, storage_box_id=storage_box_id)
        response = self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(StorageBoxResponse, response)

    def update_storage_box(
        self,
        storage_box_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> StorageBoxResponse:
        """Update a Storage Box.

        Updates a Storage Box.

        ``PUT /storage_boxes/{id}``

        Args:
            storage_box_id: ID of the Storage Box.
            name: Name of the Storage Box. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, storage_box_id=storage_box_id, labels=labels)
        response = self._transport.request(
            "PUT",
            f"/storage_boxes/{encode_path(storage_box_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(StorageBoxResponse, response)

    def delete_storage_box(self, storage_box_id: int, /) -> ActionResponse:
        """Delete a Storage Box.

        Deletes a Storage Box.

        ``DELETE /storage_boxes/{id}``

        Args:
            storage_box_id: ID of the Storage Box.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, storage_box_id=storage_box_id)
        response = self._transport.request(
            "DELETE",
            f"/storage_boxes/{encode_path(storage_box_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def list_storage_box_folders(
        self,
        storage_box_id: int,
        /,
        *,
        path: str | None = None,
    ) -> ListStorageBoxFoldersResponse:
        """List folders of a Storage Box.

        Returns a list of (sub)folders in a Storage Box.

        The folder location is specified by the `path` query parameter.

        ``GET /storage_boxes/{id}/folders``

        Args:
            storage_box_id: ID of the Storage Box.
            path: Relative path for which the listing is to be made. The API default is ``"."``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, storage_box_id=storage_box_id)
        response = self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/folders",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "path": path,
                },
            ),
        )
        return self._transport.parse(ListStorageBoxFoldersResponse, response)


class AsyncStorageBoxesResource:
    """Operations on ``storage_boxes`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_storage_boxes(
        self,
        *,
        name: str | None = None,
        label_selector: str | None = None,
        sort: Sequence[ListStorageBoxesSort | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListStorageBoxesResponse:
        """List Storage Boxes.

        Returns a paginated list of Storage Boxes.

        ``GET /storage_boxes``

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
            "/storage_boxes",
            server="hetzner",
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
        return self._transport.parse(ListStorageBoxesResponse, response)

    async def create_storage_box(
        self,
        *,
        name: str,
        location: str | int,
        storage_box_type: str | int,
        password: str,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        ssh_keys: StrSequence | NotGiven = NOT_GIVEN,
        access_settings: CreateStorageBoxAccessSettingsParam | NotGiven = NOT_GIVEN,
    ) -> CreateStorageBoxResponse:
        """Create a Storage Box.

        Creates a Storage Box.

        ``POST /storage_boxes``

        Args:
            name: Name of the Storage Box.
            location: ID or Name of Location.
            storage_box_type: ID or Name of the Storage Box Type.
            password: Password of the Storage Box. For more details, see the Storage Boxes password
                policy.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            ssh_keys: SSH public keys in OpenSSH format to inject into the Storage Box. Omitted if
                not given.
            access_settings: Access settings of the Storage Box. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, labels=labels)
        response = await self._transport.request(
            "POST",
            "/storage_boxes",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "location": location,
                    "storage_box_type": storage_box_type,
                    "password": password,
                    "labels": labels,
                    "ssh_keys": ssh_keys,
                    "access_settings": access_settings,
                },
            ),
        )
        return self._transport.parse(CreateStorageBoxResponse, response)

    async def get_storage_box(self, storage_box_id: int, /) -> StorageBoxResponse:
        """Get a Storage Box.

        Returns a specific Storage Box.

        ``GET /storage_boxes/{id}``

        Args:
            storage_box_id: ID of the Storage Box.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, storage_box_id=storage_box_id)
        response = await self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(StorageBoxResponse, response)

    async def update_storage_box(
        self,
        storage_box_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> StorageBoxResponse:
        """Update a Storage Box.

        Updates a Storage Box.

        ``PUT /storage_boxes/{id}``

        Args:
            storage_box_id: ID of the Storage Box.
            name: Name of the Storage Box. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, storage_box_id=storage_box_id, labels=labels)
        response = await self._transport.request(
            "PUT",
            f"/storage_boxes/{encode_path(storage_box_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(StorageBoxResponse, response)

    async def delete_storage_box(self, storage_box_id: int, /) -> ActionResponse:
        """Delete a Storage Box.

        Deletes a Storage Box.

        ``DELETE /storage_boxes/{id}``

        Args:
            storage_box_id: ID of the Storage Box.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, storage_box_id=storage_box_id)
        response = await self._transport.request(
            "DELETE",
            f"/storage_boxes/{encode_path(storage_box_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def list_storage_box_folders(
        self,
        storage_box_id: int,
        /,
        *,
        path: str | None = None,
    ) -> ListStorageBoxFoldersResponse:
        """List folders of a Storage Box.

        Returns a list of (sub)folders in a Storage Box.

        The folder location is specified by the `path` query parameter.

        ``GET /storage_boxes/{id}/folders``

        Args:
            storage_box_id: ID of the Storage Box.
            path: Relative path for which the listing is to be made. The API default is ``"."``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, storage_box_id=storage_box_id)
        response = await self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/folders",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "path": path,
                },
            ),
        )
        return self._transport.parse(ListStorageBoxFoldersResponse, response)
