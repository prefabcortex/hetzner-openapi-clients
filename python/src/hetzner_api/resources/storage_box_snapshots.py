"""Resource ``storage_box_snapshots`` (generated - do not edit by hand)."""

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
    CreateStorageBoxSnapshotResponse,
    ErrorResponse,
    ListStorageBoxSnapshotsResponse,
    SnapshotResponse,
    SortByIdNameCreated,
)
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncStorageBoxSnapshotsResource",
    "StorageBoxSnapshotsResource",
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
    "description": Check(max_length=1000, pattern="[a-zA-Z0-9-_,:<>+#!\\(\\)\\[\\]\\{\\}\x20]*"),
    "labels": LABELS_RULES,
}

_CHECKS_3: Final[Mapping[str, Check]] = {
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
    "snapshot_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
    "snapshot_id": Check(minimum=1, maximum=9007199254740991),
    "description": Check(max_length=1000, pattern="[a-zA-Z0-9-_,:<>+#!\\(\\)\\[\\]\\{\\}\x20]*"),
    "labels": LABELS_RULES,
}


class StorageBoxSnapshotsResource:
    """Operations on ``storage_box_snapshots`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_storage_box_snapshots(
        self,
        storage_box_id: int,
        /,
        *,
        name: str | None = None,
        label_selector: str | None = None,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        is_automatic: bool | None = None,
    ) -> ListStorageBoxSnapshotsResponse:
        """List Snapshots.

        Returns a list of Storage Box Snapshot.

        Both snapshots created manually and by the snapshot plan are returned.

        ``GET /storage_boxes/{id}/snapshots``

        Args:
            storage_box_id: ID of the Storage Box.
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            is_automatic: Filter wether a Storage Box Snapshot is automatic.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, storage_box_id=storage_box_id)
        response = self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/snapshots",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "label_selector": label_selector,
                    "sort": sort,
                    "is_automatic": is_automatic,
                },
            ),
        )
        return self._transport.parse(ListStorageBoxSnapshotsResponse, response)

    def create_storage_box_snapshot(
        self,
        storage_box_id: int,
        /,
        *,
        description: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CreateStorageBoxSnapshotResponse:
        """Create a Snapshot.

        Creates a Storage Box Snapshot.

        ``POST /storage_boxes/{id}/snapshots``

        Args:
            storage_box_id: ID of the Storage Box.
            description: Description of the Storage Box Snapshot. Omitted if not given.
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
            description=description,
            labels=labels,
        )
        response = self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/snapshots",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "description": description,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(CreateStorageBoxSnapshotResponse, response)

    def get_storage_box_snapshot(
        self,
        storage_box_id: int,
        snapshot_id: int,
        /,
    ) -> SnapshotResponse:
        """Get a Snapshot.

        Returns a specific Storage Box Snapshot.

        ``GET /storage_boxes/{id}/snapshots/{snapshot_id}``

        Args:
            storage_box_id: ID of the Storage Box.
            snapshot_id: ID of the Storage Box Snapshot.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, storage_box_id=storage_box_id, snapshot_id=snapshot_id)
        response = self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/snapshots/{encode_path(snapshot_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(SnapshotResponse, response)

    def update_storage_box_snapshot(
        self,
        storage_box_id: int,
        snapshot_id: int,
        /,
        *,
        description: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> SnapshotResponse:
        """Update a Snapshot.

        Updates a Storage Box Snapshot.

        ``PUT /storage_boxes/{id}/snapshots/{snapshot_id}``

        Args:
            storage_box_id: ID of the Storage Box.
            snapshot_id: ID of the Storage Box Snapshot.
            description: Description of the Storage Box Snapshot. Omitted if not given.
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
            snapshot_id=snapshot_id,
            description=description,
            labels=labels,
        )
        response = self._transport.request(
            "PUT",
            f"/storage_boxes/{encode_path(storage_box_id)}/snapshots/{encode_path(snapshot_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "description": description,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(SnapshotResponse, response)

    def delete_storage_box_snapshot(
        self,
        storage_box_id: int,
        snapshot_id: int,
        /,
    ) -> ActionResponse:
        """Delete a Snapshot.

        Deletes a Storage Box Snapshot.

        ``DELETE /storage_boxes/{id}/snapshots/{snapshot_id}``

        Args:
            storage_box_id: ID of the Storage Box.
            snapshot_id: ID of the Storage Box Snapshot.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, storage_box_id=storage_box_id, snapshot_id=snapshot_id)
        response = self._transport.request(
            "DELETE",
            f"/storage_boxes/{encode_path(storage_box_id)}/snapshots/{encode_path(snapshot_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)


class AsyncStorageBoxSnapshotsResource:
    """Operations on ``storage_box_snapshots`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_storage_box_snapshots(
        self,
        storage_box_id: int,
        /,
        *,
        name: str | None = None,
        label_selector: str | None = None,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        is_automatic: bool | None = None,
    ) -> ListStorageBoxSnapshotsResponse:
        """List Snapshots.

        Returns a list of Storage Box Snapshot.

        Both snapshots created manually and by the snapshot plan are returned.

        ``GET /storage_boxes/{id}/snapshots``

        Args:
            storage_box_id: ID of the Storage Box.
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            is_automatic: Filter wether a Storage Box Snapshot is automatic.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, storage_box_id=storage_box_id)
        response = await self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/snapshots",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "label_selector": label_selector,
                    "sort": sort,
                    "is_automatic": is_automatic,
                },
            ),
        )
        return self._transport.parse(ListStorageBoxSnapshotsResponse, response)

    async def create_storage_box_snapshot(
        self,
        storage_box_id: int,
        /,
        *,
        description: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CreateStorageBoxSnapshotResponse:
        """Create a Snapshot.

        Creates a Storage Box Snapshot.

        ``POST /storage_boxes/{id}/snapshots``

        Args:
            storage_box_id: ID of the Storage Box.
            description: Description of the Storage Box Snapshot. Omitted if not given.
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
            description=description,
            labels=labels,
        )
        response = await self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/snapshots",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "description": description,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(CreateStorageBoxSnapshotResponse, response)

    async def get_storage_box_snapshot(
        self,
        storage_box_id: int,
        snapshot_id: int,
        /,
    ) -> SnapshotResponse:
        """Get a Snapshot.

        Returns a specific Storage Box Snapshot.

        ``GET /storage_boxes/{id}/snapshots/{snapshot_id}``

        Args:
            storage_box_id: ID of the Storage Box.
            snapshot_id: ID of the Storage Box Snapshot.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, storage_box_id=storage_box_id, snapshot_id=snapshot_id)
        response = await self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/snapshots/{encode_path(snapshot_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(SnapshotResponse, response)

    async def update_storage_box_snapshot(
        self,
        storage_box_id: int,
        snapshot_id: int,
        /,
        *,
        description: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> SnapshotResponse:
        """Update a Snapshot.

        Updates a Storage Box Snapshot.

        ``PUT /storage_boxes/{id}/snapshots/{snapshot_id}``

        Args:
            storage_box_id: ID of the Storage Box.
            snapshot_id: ID of the Storage Box Snapshot.
            description: Description of the Storage Box Snapshot. Omitted if not given.
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
            snapshot_id=snapshot_id,
            description=description,
            labels=labels,
        )
        response = await self._transport.request(
            "PUT",
            f"/storage_boxes/{encode_path(storage_box_id)}/snapshots/{encode_path(snapshot_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "description": description,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(SnapshotResponse, response)

    async def delete_storage_box_snapshot(
        self,
        storage_box_id: int,
        snapshot_id: int,
        /,
    ) -> ActionResponse:
        """Delete a Snapshot.

        Deletes a Storage Box Snapshot.

        ``DELETE /storage_boxes/{id}/snapshots/{snapshot_id}``

        Args:
            storage_box_id: ID of the Storage Box.
            snapshot_id: ID of the Storage Box Snapshot.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, storage_box_id=storage_box_id, snapshot_id=snapshot_id)
        response = await self._transport.request(
            "DELETE",
            f"/storage_boxes/{encode_path(storage_box_id)}/snapshots/{encode_path(snapshot_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)
