"""Resource ``storage_box_actions`` (generated - do not edit by hand)."""

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

__all__ = [
    "AsyncStorageBoxActionsResource",
    "StorageBoxActionsResource",
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
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
    "action_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_5: Final[Mapping[str, Check]] = {
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_6: Final[Mapping[str, Check]] = {
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
    "max_snapshots": Check(minimum=1),
    "minute": Check(minimum=0, maximum=59),
    "hour": Check(minimum=0, maximum=23),
    "day_of_week": Check(minimum=1, maximum=7),
    "day_of_month": Check(minimum=1, maximum=31),
}


class StorageBoxActionsResource:
    """Operations on ``storage_box_actions`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_storage_boxes_actions(
        self,
        *,
        id: Sequence[int] | None = None,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions.

        Returns all Action objects.

        ``GET /storage_boxes/actions``

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
            "/storage_boxes/actions",
            server="hetzner",
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

    def get_storage_boxes_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action object.

        ``GET /storage_boxes/actions/{id}``

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
            f"/storage_boxes/actions/{encode_path(action_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def list_storage_box_actions(
        self,
        storage_box_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Storage Box.

        List all Actions related to a specific Storage Box.

        ``GET /storage_boxes/{id}/actions``

        Args:
            storage_box_id: ID of the Storage Box.
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
            storage_box_id=storage_box_id,
            page=page,
            per_page=per_page,
        )
        response = self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions",
            server="hetzner",
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

    @deprecated("GET /storage_boxes/{id}/actions/{action_id} is deprecated by the API")
    def get_storage_box_action(self, storage_box_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Storage Box.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action object for a Storage Box.

        ``GET /storage_boxes/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            storage_box_id: ID of the Storage Box.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, storage_box_id=storage_box_id, action_id=action_id)
        response = self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/{encode_path(action_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def change_storage_box_protection(
        self,
        storage_box_id: int,
        /,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Change Protection.

        Changes the protection configuration of a Storage Box.

        ``POST /storage_boxes/{id}/actions/change_protection``

        Args:
            storage_box_id: ID of the Storage Box.
            delete: If true, prevents the snapshot from being deleted. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, storage_box_id=storage_box_id)
        response = self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/change_protection",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_storage_box_type(
        self,
        storage_box_id: int,
        /,
        *,
        storage_box_type: str | int,
    ) -> ActionResponse:
        """Change Type.

        Changes the type of a Storage Box.

        Upgrades or downgrades a Storage Box to another Storage Box Type.

        It is not possible to downgrade to a Storage Box Type that offers less disk space than you
        are currently using.

        ``POST /storage_boxes/{id}/actions/change_type``

        Args:
            storage_box_id: ID of the Storage Box.
            storage_box_type: ID or Name of the Storage Box Type.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, storage_box_id=storage_box_id)
        response = self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/change_type",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "storage_box_type": storage_box_type,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def reset_storage_box_password(
        self,
        storage_box_id: int,
        /,
        *,
        password: str,
    ) -> ActionResponse:
        """Reset Password.

        Reset the password of a Storage Box.

        ``POST /storage_boxes/{id}/actions/reset_password``

        Args:
            storage_box_id: ID of the Storage Box.
            password: Password of the Storage Box. For more details, see the Storage Boxes password
                policy.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, storage_box_id=storage_box_id)
        response = self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/reset_password",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "password": password,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def update_storage_box_access_settings(
        self,
        storage_box_id: int,
        /,
        *,
        reachable_externally: bool | NotGiven = NOT_GIVEN,
        samba_enabled: bool | NotGiven = NOT_GIVEN,
        ssh_enabled: bool | NotGiven = NOT_GIVEN,
        webdav_enabled: bool | NotGiven = NOT_GIVEN,
        zfs_enabled: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Update Access Settings.

        Update access settings of a primary Storage Box account.

        This endpoints supports partial updates. Omitted optional parameters do not result in any
        changes to the respective properties.

        ``POST /storage_boxes/{id}/actions/update_access_settings``

        Args:
            storage_box_id: ID of the Storage Box.
            reachable_externally: Whether access from outside the Hetzner network is allowed.
                Omitted if not given.
            samba_enabled: Whether the Samba subsystem is enabled. Omitted if not given.
            ssh_enabled: Whether the SSH subsystem is enabled. Omitted if not given.
            webdav_enabled: Whether the WebDAV subsystem is enabled. Omitted if not given.
            zfs_enabled: Whether the ZFS snapshot folder is visible. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, storage_box_id=storage_box_id)
        response = self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/update_access_settings",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "reachable_externally": reachable_externally,
                    "samba_enabled": samba_enabled,
                    "ssh_enabled": ssh_enabled,
                    "webdav_enabled": webdav_enabled,
                    "zfs_enabled": zfs_enabled,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def rollback_storage_box_snapshot(
        self,
        storage_box_id: int,
        /,
        *,
        snapshot: str | int,
    ) -> ActionResponse:
        """Rollback Snapshot.

        Rolls back a Storage Box to the given Storage Box Snapshot.

        This will remove all newer Storage Box Snapshot and irrevocably delete all data that was
        since written to the Storage Box.

        ``POST /storage_boxes/{id}/actions/rollback_snapshot``

        Args:
            storage_box_id: ID of the Storage Box.
            snapshot: ID or Name of the Storage Box Snapshot.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, storage_box_id=storage_box_id)
        response = self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/rollback_snapshot",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "snapshot": snapshot,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def disable_storage_box_snapshot_plan(self, storage_box_id: int, /) -> ActionResponse:
        """Disable Snapshot Plan.

        Disables the active Snapshot Plan of a Storage Box.

        Existing Storage Box Snapshots created by the Snapshot Plan will not be delete, they must be
        removed manually.

        ``POST /storage_boxes/{id}/actions/disable_snapshot_plan``

        Args:
            storage_box_id: ID of the Storage Box.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, storage_box_id=storage_box_id)
        response = self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/disable_snapshot_plan",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def enable_storage_box_snapshot_plan(
        self,
        storage_box_id: int,
        /,
        *,
        max_snapshots: int,
        minute: int,
        hour: int,
        day_of_week: int | NotGiven | None = NOT_GIVEN,
        day_of_month: int | NotGiven | None = NOT_GIVEN,
    ) -> ActionResponse:
        """Enable Snapshot Plan.

        Enables a Snapshot Plan for a Storage Box.

        Once enabled, a Snapshot Plan will create Snapshots at predefined intervals. There can only
        ever be one Snapshot Plan. The existing Snapshot Plan will be deleted before a new one is
        set up.

        Automatic Snapshots are retained until explicitly deleted by the user or the maximum
        snapshot count for the plan ("max_snapshots") is exceeded.

        You can choose the specific time (UTC timezone), day of the week, and day of the month. The
        time-related options are cron like. Some typical use cases include:

        - Every day at 3 o'clock - `{"max_snapshots":10,"minute":0,"hour":3}`
        - Every Friday at 3 o'clock - `{"max_snapshots":10,"minute":0,"hour":3,"day_of_week": 5}`
        - On the first of every month at half past 6 -
          `{"max_snapshots":10,"minute":30,"hour":6,"day_of_month": 1}`

        ``POST /storage_boxes/{id}/actions/enable_snapshot_plan``

        Args:
            storage_box_id: ID of the Storage Box.
            max_snapshots: Maximum amount of Snapshots that will be created by this Snapshot Plan.
                Older Snapshots will be deleted.
            minute: Minute when the Snapshot Plan is executed (UTC).
            hour: Hour when the Snapshot Plan is executed (UTC).
            day_of_week: Day of the week when the Snapshot Plan is executed. Starts at 1 for Monday
                til 7 for Sunday. Null means every day. Omitted if not given.
            day_of_month: Day of the month when the Snapshot Plan is executed. Null means every day.
                Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_6,
            storage_box_id=storage_box_id,
            max_snapshots=max_snapshots,
            minute=minute,
            hour=hour,
            day_of_week=day_of_week,
            day_of_month=day_of_month,
        )
        response = self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/enable_snapshot_plan",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "max_snapshots": max_snapshots,
                    "minute": minute,
                    "hour": hour,
                    "day_of_week": day_of_week,
                    "day_of_month": day_of_month,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)


class AsyncStorageBoxActionsResource:
    """Operations on ``storage_box_actions`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_storage_boxes_actions(
        self,
        *,
        id: Sequence[int] | None = None,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions.

        Returns all Action objects.

        ``GET /storage_boxes/actions``

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
            "/storage_boxes/actions",
            server="hetzner",
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

    async def get_storage_boxes_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action object.

        ``GET /storage_boxes/actions/{id}``

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
            f"/storage_boxes/actions/{encode_path(action_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def list_storage_box_actions(
        self,
        storage_box_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Storage Box.

        List all Actions related to a specific Storage Box.

        ``GET /storage_boxes/{id}/actions``

        Args:
            storage_box_id: ID of the Storage Box.
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
            storage_box_id=storage_box_id,
            page=page,
            per_page=per_page,
        )
        response = await self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions",
            server="hetzner",
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

    @deprecated("GET /storage_boxes/{id}/actions/{action_id} is deprecated by the API")
    async def get_storage_box_action(
        self,
        storage_box_id: int,
        action_id: int,
        /,
    ) -> ActionResponse:
        """Get an Action for a Storage Box.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action object for a Storage Box.

        ``GET /storage_boxes/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            storage_box_id: ID of the Storage Box.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, storage_box_id=storage_box_id, action_id=action_id)
        response = await self._transport.request(
            "GET",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/{encode_path(action_id)}",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def change_storage_box_protection(
        self,
        storage_box_id: int,
        /,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Change Protection.

        Changes the protection configuration of a Storage Box.

        ``POST /storage_boxes/{id}/actions/change_protection``

        Args:
            storage_box_id: ID of the Storage Box.
            delete: If true, prevents the snapshot from being deleted. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, storage_box_id=storage_box_id)
        response = await self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/change_protection",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_storage_box_type(
        self,
        storage_box_id: int,
        /,
        *,
        storage_box_type: str | int,
    ) -> ActionResponse:
        """Change Type.

        Changes the type of a Storage Box.

        Upgrades or downgrades a Storage Box to another Storage Box Type.

        It is not possible to downgrade to a Storage Box Type that offers less disk space than you
        are currently using.

        ``POST /storage_boxes/{id}/actions/change_type``

        Args:
            storage_box_id: ID of the Storage Box.
            storage_box_type: ID or Name of the Storage Box Type.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, storage_box_id=storage_box_id)
        response = await self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/change_type",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "storage_box_type": storage_box_type,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def reset_storage_box_password(
        self,
        storage_box_id: int,
        /,
        *,
        password: str,
    ) -> ActionResponse:
        """Reset Password.

        Reset the password of a Storage Box.

        ``POST /storage_boxes/{id}/actions/reset_password``

        Args:
            storage_box_id: ID of the Storage Box.
            password: Password of the Storage Box. For more details, see the Storage Boxes password
                policy.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, storage_box_id=storage_box_id)
        response = await self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/reset_password",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "password": password,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def update_storage_box_access_settings(
        self,
        storage_box_id: int,
        /,
        *,
        reachable_externally: bool | NotGiven = NOT_GIVEN,
        samba_enabled: bool | NotGiven = NOT_GIVEN,
        ssh_enabled: bool | NotGiven = NOT_GIVEN,
        webdav_enabled: bool | NotGiven = NOT_GIVEN,
        zfs_enabled: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Update Access Settings.

        Update access settings of a primary Storage Box account.

        This endpoints supports partial updates. Omitted optional parameters do not result in any
        changes to the respective properties.

        ``POST /storage_boxes/{id}/actions/update_access_settings``

        Args:
            storage_box_id: ID of the Storage Box.
            reachable_externally: Whether access from outside the Hetzner network is allowed.
                Omitted if not given.
            samba_enabled: Whether the Samba subsystem is enabled. Omitted if not given.
            ssh_enabled: Whether the SSH subsystem is enabled. Omitted if not given.
            webdav_enabled: Whether the WebDAV subsystem is enabled. Omitted if not given.
            zfs_enabled: Whether the ZFS snapshot folder is visible. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, storage_box_id=storage_box_id)
        response = await self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/update_access_settings",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "reachable_externally": reachable_externally,
                    "samba_enabled": samba_enabled,
                    "ssh_enabled": ssh_enabled,
                    "webdav_enabled": webdav_enabled,
                    "zfs_enabled": zfs_enabled,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def rollback_storage_box_snapshot(
        self,
        storage_box_id: int,
        /,
        *,
        snapshot: str | int,
    ) -> ActionResponse:
        """Rollback Snapshot.

        Rolls back a Storage Box to the given Storage Box Snapshot.

        This will remove all newer Storage Box Snapshot and irrevocably delete all data that was
        since written to the Storage Box.

        ``POST /storage_boxes/{id}/actions/rollback_snapshot``

        Args:
            storage_box_id: ID of the Storage Box.
            snapshot: ID or Name of the Storage Box Snapshot.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, storage_box_id=storage_box_id)
        response = await self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/rollback_snapshot",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "snapshot": snapshot,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def disable_storage_box_snapshot_plan(self, storage_box_id: int, /) -> ActionResponse:
        """Disable Snapshot Plan.

        Disables the active Snapshot Plan of a Storage Box.

        Existing Storage Box Snapshots created by the Snapshot Plan will not be delete, they must be
        removed manually.

        ``POST /storage_boxes/{id}/actions/disable_snapshot_plan``

        Args:
            storage_box_id: ID of the Storage Box.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, storage_box_id=storage_box_id)
        response = await self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/disable_snapshot_plan",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def enable_storage_box_snapshot_plan(
        self,
        storage_box_id: int,
        /,
        *,
        max_snapshots: int,
        minute: int,
        hour: int,
        day_of_week: int | NotGiven | None = NOT_GIVEN,
        day_of_month: int | NotGiven | None = NOT_GIVEN,
    ) -> ActionResponse:
        """Enable Snapshot Plan.

        Enables a Snapshot Plan for a Storage Box.

        Once enabled, a Snapshot Plan will create Snapshots at predefined intervals. There can only
        ever be one Snapshot Plan. The existing Snapshot Plan will be deleted before a new one is
        set up.

        Automatic Snapshots are retained until explicitly deleted by the user or the maximum
        snapshot count for the plan ("max_snapshots") is exceeded.

        You can choose the specific time (UTC timezone), day of the week, and day of the month. The
        time-related options are cron like. Some typical use cases include:

        - Every day at 3 o'clock - `{"max_snapshots":10,"minute":0,"hour":3}`
        - Every Friday at 3 o'clock - `{"max_snapshots":10,"minute":0,"hour":3,"day_of_week": 5}`
        - On the first of every month at half past 6 -
          `{"max_snapshots":10,"minute":30,"hour":6,"day_of_month": 1}`

        ``POST /storage_boxes/{id}/actions/enable_snapshot_plan``

        Args:
            storage_box_id: ID of the Storage Box.
            max_snapshots: Maximum amount of Snapshots that will be created by this Snapshot Plan.
                Older Snapshots will be deleted.
            minute: Minute when the Snapshot Plan is executed (UTC).
            hour: Hour when the Snapshot Plan is executed (UTC).
            day_of_week: Day of the week when the Snapshot Plan is executed. Starts at 1 for Monday
                til 7 for Sunday. Null means every day. Omitted if not given.
            day_of_month: Day of the month when the Snapshot Plan is executed. Null means every day.
                Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_6,
            storage_box_id=storage_box_id,
            max_snapshots=max_snapshots,
            minute=minute,
            hour=hour,
            day_of_week=day_of_week,
            day_of_month=day_of_month,
        )
        response = await self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/actions/enable_snapshot_plan",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "max_snapshots": max_snapshots,
                    "minute": minute,
                    "hour": hour,
                    "day_of_week": day_of_week,
                    "day_of_month": day_of_month,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)
