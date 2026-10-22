"""Resource ``volume_actions`` (generated - do not edit by hand)."""

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
    "AsyncVolumeActionsResource",
    "VolumeActionsResource",
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
    "volume_id": Check(minimum=1, maximum=9007199254740991),
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "volume_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_5: Final[Mapping[str, Check]] = {
    "volume_id": Check(minimum=1, maximum=9007199254740991),
    "action_id": Check(minimum=1, maximum=9007199254740991),
}


class VolumeActionsResource:
    """Operations on ``volume_actions`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_volumes_actions(
        self,
        *,
        id: Sequence[int] | None = None,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions.

        Returns all Action objects. You can `sort` the results by using the sort URI parameter, and
        filter them with the `status` and `id` parameter.

        ``GET /volumes/actions``

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
            "/volumes/actions",
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

    def get_volumes_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action object.

        ``GET /volumes/actions/{id}``

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
            f"/volumes/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def list_volume_actions(
        self,
        volume_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Volume.

        Returns all Action objects for a Volume. You can `sort` the results by using the sort URI
        parameter, and filter them with the `status` parameter.

        ``GET /volumes/{id}/actions``

        Args:
            volume_id: ID of the Volume.
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
        self._transport.validate(_CHECKS_3, volume_id=volume_id, page=page, per_page=per_page)
        response = self._transport.request(
            "GET",
            f"/volumes/{encode_path(volume_id)}/actions",
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

    def attach_volume(
        self,
        volume_id: int,
        /,
        *,
        server: int,
        automount: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Attach Volume to a Server.

        Attaches a Volume to a Server. Works only if the Server is in the same Location as the
        Volume.

        ``POST /volumes/{id}/actions/attach``

        Args:
            volume_id: ID of the Volume.
            server: ID of the Server the Volume will be attached to.
            automount: Auto-mount the Volume after attaching it. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, volume_id=volume_id)
        response = self._transport.request(
            "POST",
            f"/volumes/{encode_path(volume_id)}/actions/attach",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "server": server,
                    "automount": automount,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_volume_protection(
        self,
        volume_id: int,
        /,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Change Volume Protection.

        Changes the protection configuration of a Volume.

        ``POST /volumes/{id}/actions/change_protection``

        Args:
            volume_id: ID of the Volume.
            delete: If true, prevents the snapshot from being deleted. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, volume_id=volume_id)
        response = self._transport.request(
            "POST",
            f"/volumes/{encode_path(volume_id)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def detach_volume(self, volume_id: int, /) -> ActionResponse:
        """Detach Volume.

        Detaches a Volume from the Server it's attached to. You may attach it to a Server again at a
        later time.

        ``POST /volumes/{id}/actions/detach``

        Args:
            volume_id: ID of the Volume.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, volume_id=volume_id)
        response = self._transport.request(
            "POST",
            f"/volumes/{encode_path(volume_id)}/actions/detach",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def resize_volume(self, volume_id: int, /, *, size: float) -> ActionResponse:
        """Resize Volume.

        Changes the size of a Volume. Note that downsizing a Volume is not possible.

        ``POST /volumes/{id}/actions/resize``

        Args:
            volume_id: ID of the Volume.
            size: New Volume size in GB (must be greater than current size).

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, volume_id=volume_id)
        response = self._transport.request(
            "POST",
            f"/volumes/{encode_path(volume_id)}/actions/resize",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "size": size,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    @deprecated("GET /volumes/{id}/actions/{action_id} is deprecated by the API")
    def get_volume_action(self, volume_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Volume.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Volume.

        ``GET /volumes/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            volume_id: ID of the Volume.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, volume_id=volume_id, action_id=action_id)
        response = self._transport.request(
            "GET",
            f"/volumes/{encode_path(volume_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)


class AsyncVolumeActionsResource:
    """Operations on ``volume_actions`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_volumes_actions(
        self,
        *,
        id: Sequence[int] | None = None,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions.

        Returns all Action objects. You can `sort` the results by using the sort URI parameter, and
        filter them with the `status` and `id` parameter.

        ``GET /volumes/actions``

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
            "/volumes/actions",
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

    async def get_volumes_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action object.

        ``GET /volumes/actions/{id}``

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
            f"/volumes/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def list_volume_actions(
        self,
        volume_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Volume.

        Returns all Action objects for a Volume. You can `sort` the results by using the sort URI
        parameter, and filter them with the `status` parameter.

        ``GET /volumes/{id}/actions``

        Args:
            volume_id: ID of the Volume.
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
        self._transport.validate(_CHECKS_3, volume_id=volume_id, page=page, per_page=per_page)
        response = await self._transport.request(
            "GET",
            f"/volumes/{encode_path(volume_id)}/actions",
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

    async def attach_volume(
        self,
        volume_id: int,
        /,
        *,
        server: int,
        automount: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Attach Volume to a Server.

        Attaches a Volume to a Server. Works only if the Server is in the same Location as the
        Volume.

        ``POST /volumes/{id}/actions/attach``

        Args:
            volume_id: ID of the Volume.
            server: ID of the Server the Volume will be attached to.
            automount: Auto-mount the Volume after attaching it. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, volume_id=volume_id)
        response = await self._transport.request(
            "POST",
            f"/volumes/{encode_path(volume_id)}/actions/attach",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "server": server,
                    "automount": automount,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_volume_protection(
        self,
        volume_id: int,
        /,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Change Volume Protection.

        Changes the protection configuration of a Volume.

        ``POST /volumes/{id}/actions/change_protection``

        Args:
            volume_id: ID of the Volume.
            delete: If true, prevents the snapshot from being deleted. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, volume_id=volume_id)
        response = await self._transport.request(
            "POST",
            f"/volumes/{encode_path(volume_id)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def detach_volume(self, volume_id: int, /) -> ActionResponse:
        """Detach Volume.

        Detaches a Volume from the Server it's attached to. You may attach it to a Server again at a
        later time.

        ``POST /volumes/{id}/actions/detach``

        Args:
            volume_id: ID of the Volume.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, volume_id=volume_id)
        response = await self._transport.request(
            "POST",
            f"/volumes/{encode_path(volume_id)}/actions/detach",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def resize_volume(self, volume_id: int, /, *, size: float) -> ActionResponse:
        """Resize Volume.

        Changes the size of a Volume. Note that downsizing a Volume is not possible.

        ``POST /volumes/{id}/actions/resize``

        Args:
            volume_id: ID of the Volume.
            size: New Volume size in GB (must be greater than current size).

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, volume_id=volume_id)
        response = await self._transport.request(
            "POST",
            f"/volumes/{encode_path(volume_id)}/actions/resize",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "size": size,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    @deprecated("GET /volumes/{id}/actions/{action_id} is deprecated by the API")
    async def get_volume_action(self, volume_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Volume.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Volume.

        ``GET /volumes/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            volume_id: ID of the Volume.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, volume_id=volume_id, action_id=action_id)
        response = await self._transport.request(
            "GET",
            f"/volumes/{encode_path(volume_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)
