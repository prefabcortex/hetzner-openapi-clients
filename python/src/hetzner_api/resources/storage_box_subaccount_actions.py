"""Resource ``storage_box_subaccount_actions`` (generated - do not edit by hand)."""

from collections.abc import Mapping
from typing import Final

from hetzner_api._auth import Security
from hetzner_api._base_client import AsyncTransport, SyncTransport, encode_body, encode_path
from hetzner_api._types import NOT_GIVEN, NotGiven
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import ActionResponse, ErrorResponse

__all__ = [
    "AsyncStorageBoxSubaccountActionsResource",
    "StorageBoxSubaccountActionsResource",
]

_SECURITY_1: Final[Security] = (("APIToken",),)

_ERRORS_1: Final[ErrorModels] = {
    "4XX": ErrorResponse,
    "5XX": ErrorResponse,
}

_CHECKS_1: Final[Mapping[str, Check]] = {
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
    "subaccount_id": Check(minimum=1, maximum=9007199254740991),
    "home_directory": Check(min_length=1, max_length=999, pattern="^[a-zA-Z0-9\x20./_-]+$"),
}

_CHECKS_2: Final[Mapping[str, Check]] = {
    "storage_box_id": Check(minimum=1, maximum=9007199254740991),
    "subaccount_id": Check(minimum=1, maximum=9007199254740991),
}


class StorageBoxSubaccountActionsResource:
    """Operations on ``storage_box_subaccount_actions`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def change_storage_box_subaccount_home_directory(
        self,
        storage_box_id: int,
        subaccount_id: int,
        /,
        *,
        home_directory: str,
    ) -> ActionResponse:
        """Change Home Directory.

        Change the home directory of a Storage Box Subaccount.

        ``POST /storage_boxes/{id}/subaccounts/{subaccount_id}/actions/change_home_directory``

        Args:
            storage_box_id: ID of the Storage Box.
            subaccount_id: ID of the Storage Box Subaccount.
            home_directory: Home directory of the Storage Box Subaccount. The directory will be
                created if it doesn't exist yet.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_1,
            storage_box_id=storage_box_id,
            subaccount_id=subaccount_id,
            home_directory=home_directory,
        )
        response = self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts/{encode_path(subaccount_id)}/actions/change_home_directory",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "home_directory": home_directory,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def reset_storage_box_subaccount_password(
        self,
        storage_box_id: int,
        subaccount_id: int,
        /,
        *,
        password: str,
    ) -> ActionResponse:
        """Reset Password.

        Reset the password of a Storage Box Subaccount.

        ``POST /storage_boxes/{id}/subaccounts/{subaccount_id}/actions/reset_subaccount_password``

        Args:
            storage_box_id: ID of the Storage Box.
            subaccount_id: ID of the Storage Box Subaccount.
            password: Password of the Storage Box. For more details, see the Storage Boxes password
                policy.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_2,
            storage_box_id=storage_box_id,
            subaccount_id=subaccount_id,
        )
        response = self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts/{encode_path(subaccount_id)}/actions/reset_subaccount_password",
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

    def update_storage_box_subaccount_access_settings(
        self,
        storage_box_id: int,
        subaccount_id: int,
        /,
        *,
        readonly: bool | NotGiven = NOT_GIVEN,
        reachable_externally: bool | NotGiven = NOT_GIVEN,
        samba_enabled: bool | NotGiven = NOT_GIVEN,
        ssh_enabled: bool | NotGiven = NOT_GIVEN,
        webdav_enabled: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Update Access Settings.

        Updates the access settings of a Storage Box Subaccount.

        This endpoints supports partial updates. Omitted optional parameters do not result in any
        changes to the respective properties.

        ``POST /storage_boxes/{id}/subaccounts/{subaccount_id}/actions/update_access_settings``

        Args:
            storage_box_id: ID of the Storage Box.
            subaccount_id: ID of the Storage Box Subaccount.
            readonly: Whether the Subaccount is read-only. Omitted if not given.
            reachable_externally: Whether access from outside the Hetzner network is allowed.
                Omitted if not given.
            samba_enabled: Whether the Samba subsystem is enabled. Omitted if not given.
            ssh_enabled: Whether the SSH subsystem is enabled. Omitted if not given.
            webdav_enabled: Whether the WebDAV subsystem is enabled. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_2,
            storage_box_id=storage_box_id,
            subaccount_id=subaccount_id,
        )
        response = self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts/{encode_path(subaccount_id)}/actions/update_access_settings",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "readonly": readonly,
                    "reachable_externally": reachable_externally,
                    "samba_enabled": samba_enabled,
                    "ssh_enabled": ssh_enabled,
                    "webdav_enabled": webdav_enabled,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)


class AsyncStorageBoxSubaccountActionsResource:
    """Operations on ``storage_box_subaccount_actions`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def change_storage_box_subaccount_home_directory(
        self,
        storage_box_id: int,
        subaccount_id: int,
        /,
        *,
        home_directory: str,
    ) -> ActionResponse:
        """Change Home Directory.

        Change the home directory of a Storage Box Subaccount.

        ``POST /storage_boxes/{id}/subaccounts/{subaccount_id}/actions/change_home_directory``

        Args:
            storage_box_id: ID of the Storage Box.
            subaccount_id: ID of the Storage Box Subaccount.
            home_directory: Home directory of the Storage Box Subaccount. The directory will be
                created if it doesn't exist yet.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_1,
            storage_box_id=storage_box_id,
            subaccount_id=subaccount_id,
            home_directory=home_directory,
        )
        response = await self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts/{encode_path(subaccount_id)}/actions/change_home_directory",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "home_directory": home_directory,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def reset_storage_box_subaccount_password(
        self,
        storage_box_id: int,
        subaccount_id: int,
        /,
        *,
        password: str,
    ) -> ActionResponse:
        """Reset Password.

        Reset the password of a Storage Box Subaccount.

        ``POST /storage_boxes/{id}/subaccounts/{subaccount_id}/actions/reset_subaccount_password``

        Args:
            storage_box_id: ID of the Storage Box.
            subaccount_id: ID of the Storage Box Subaccount.
            password: Password of the Storage Box. For more details, see the Storage Boxes password
                policy.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_2,
            storage_box_id=storage_box_id,
            subaccount_id=subaccount_id,
        )
        response = await self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts/{encode_path(subaccount_id)}/actions/reset_subaccount_password",
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

    async def update_storage_box_subaccount_access_settings(
        self,
        storage_box_id: int,
        subaccount_id: int,
        /,
        *,
        readonly: bool | NotGiven = NOT_GIVEN,
        reachable_externally: bool | NotGiven = NOT_GIVEN,
        samba_enabled: bool | NotGiven = NOT_GIVEN,
        ssh_enabled: bool | NotGiven = NOT_GIVEN,
        webdav_enabled: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Update Access Settings.

        Updates the access settings of a Storage Box Subaccount.

        This endpoints supports partial updates. Omitted optional parameters do not result in any
        changes to the respective properties.

        ``POST /storage_boxes/{id}/subaccounts/{subaccount_id}/actions/update_access_settings``

        Args:
            storage_box_id: ID of the Storage Box.
            subaccount_id: ID of the Storage Box Subaccount.
            readonly: Whether the Subaccount is read-only. Omitted if not given.
            reachable_externally: Whether access from outside the Hetzner network is allowed.
                Omitted if not given.
            samba_enabled: Whether the Samba subsystem is enabled. Omitted if not given.
            ssh_enabled: Whether the SSH subsystem is enabled. Omitted if not given.
            webdav_enabled: Whether the WebDAV subsystem is enabled. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_2,
            storage_box_id=storage_box_id,
            subaccount_id=subaccount_id,
        )
        response = await self._transport.request(
            "POST",
            f"/storage_boxes/{encode_path(storage_box_id)}/subaccounts/{encode_path(subaccount_id)}/actions/update_access_settings",
            server="hetzner",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "readonly": readonly,
                    "reachable_externally": reachable_externally,
                    "samba_enabled": samba_enabled,
                    "ssh_enabled": ssh_enabled,
                    "webdav_enabled": webdav_enabled,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)
