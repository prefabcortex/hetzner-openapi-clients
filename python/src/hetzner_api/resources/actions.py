"""Resource ``actions`` (generated - do not edit by hand)."""

from collections.abc import Mapping, Sequence
from typing import Final

from hetzner_api._auth import Security
from hetzner_api._base_client import AsyncTransport, SyncTransport, encode_path, encode_query
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import ActionListResponse, ActionResponse, ErrorResponse

__all__ = [
    "ActionsResource",
    "AsyncActionsResource",
]

_SECURITY_1: Final[Security] = (("APIToken",),)

_ERRORS_1: Final[ErrorModels] = {
    "4XX": ErrorResponse,
    "5XX": ErrorResponse,
}

_CHECKS_1: Final[Mapping[str, Check]] = {
    "id": Check(items=Check(minimum=1, maximum=9007199254740991)),
}

_CHECKS_2: Final[Mapping[str, Check]] = {
    "action_id": Check(minimum=1, maximum=9007199254740991),
}


class ActionsResource:
    """Operations on ``actions`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def get_actions(self, *, id: Sequence[int]) -> ActionListResponse:
        """Get multiple Actions.

        Returns multiple Action objects specified by the `id` parameter.

        **Note**: This endpoint previously allowed listing all actions in the project. This
        functionality was deprecated in July 2023 and removed on 30 January 2025.

        - Announcement:
          https://docs.hetzner.cloud/changelog#2023-07-20-actions-list-endpoint-is-deprecated
        - Removal:
          https://docs.hetzner.cloud/changelog#2025-01-30-listing-arbitrary-actions-in-the-actions-list-endpoint-is-removed

        ``GET /actions``

        Args:
            id: Filter the actions by ID. May be used multiple times. The response will only contain
                actions matching the specified IDs.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, id=id)
        response = self._transport.request(
            "GET",
            "/actions",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "id": id,
                },
            ),
        )
        return self._transport.parse(ActionListResponse, response)

    def get_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action object.

        ``GET /actions/{id}``

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
            f"/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)


class AsyncActionsResource:
    """Operations on ``actions`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def get_actions(self, *, id: Sequence[int]) -> ActionListResponse:
        """Get multiple Actions.

        Returns multiple Action objects specified by the `id` parameter.

        **Note**: This endpoint previously allowed listing all actions in the project. This
        functionality was deprecated in July 2023 and removed on 30 January 2025.

        - Announcement:
          https://docs.hetzner.cloud/changelog#2023-07-20-actions-list-endpoint-is-deprecated
        - Removal:
          https://docs.hetzner.cloud/changelog#2025-01-30-listing-arbitrary-actions-in-the-actions-list-endpoint-is-removed

        ``GET /actions``

        Args:
            id: Filter the actions by ID. May be used multiple times. The response will only contain
                actions matching the specified IDs.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, id=id)
        response = await self._transport.request(
            "GET",
            "/actions",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "id": id,
                },
            ),
        )
        return self._transport.parse(ActionListResponse, response)

    async def get_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action object.

        ``GET /actions/{id}``

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
            f"/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)
