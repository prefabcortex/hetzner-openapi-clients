"""Resource ``ssh_keys`` (generated - do not edit by hand)."""

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
from hetzner_api.models import ErrorResponse, ListSshKeysResponse, SortByIdName, SshKeyResponse
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncSshKeysResource",
    "SshKeysResource",
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
    "ssh_key_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "ssh_key_id": Check(minimum=1, maximum=9007199254740991),
    "labels": LABELS_RULES,
}


class SshKeysResource:
    """Operations on ``ssh_keys`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_ssh_keys(
        self,
        *,
        sort: Sequence[SortByIdName | UnknownValue] | None = None,
        name: str | None = None,
        fingerprint: str | None = None,
        label_selector: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListSshKeysResponse:
        """List SSH keys.

        Returns all SSH key objects.

        ``GET /ssh_keys``

        Args:
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            fingerprint: May be used to filter SSH keys by their fingerprint. The response will only
                contain the SSH key matching the specified fingerprint.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
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
            "/ssh_keys",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "name": name,
                    "fingerprint": fingerprint,
                    "label_selector": label_selector,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListSshKeysResponse, response)

    def create_ssh_key(
        self,
        *,
        name: str,
        public_key: str,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> SshKeyResponse:
        """Create an SSH key.

        Creates a new SSH key with the given `name` and `public_key`. Once an SSH key is created, it
        can be used in other calls such as creating Servers.

        ``POST /ssh_keys``

        Args:
            name: Name of the SSH key.
            public_key: Public key.
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
            "/ssh_keys",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "public_key": public_key,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(SshKeyResponse, response)

    def get_ssh_key(self, ssh_key_id: int, /) -> SshKeyResponse:
        """Get a SSH key.

        Returns a specific SSH key object.

        ``GET /ssh_keys/{id}``

        Args:
            ssh_key_id: ID of the SSH Key.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, ssh_key_id=ssh_key_id)
        response = self._transport.request(
            "GET",
            f"/ssh_keys/{encode_path(ssh_key_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(SshKeyResponse, response)

    def update_ssh_key(
        self,
        ssh_key_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> SshKeyResponse:
        """Update an SSH key.

        Updates an SSH key. You can update an SSH key name and an SSH key labels.

        ``PUT /ssh_keys/{id}``

        Args:
            ssh_key_id: ID of the SSH Key.
            name: New name Name to set. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, ssh_key_id=ssh_key_id, labels=labels)
        response = self._transport.request(
            "PUT",
            f"/ssh_keys/{encode_path(ssh_key_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(SshKeyResponse, response)

    def delete_ssh_key(self, ssh_key_id: int, /) -> None:
        """Delete an SSH key.

        Deletes an SSH key. It cannot be used anymore.

        ``DELETE /ssh_keys/{id}``

        Args:
            ssh_key_id: ID of the SSH Key.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, ssh_key_id=ssh_key_id)
        self._transport.request(
            "DELETE",
            f"/ssh_keys/{encode_path(ssh_key_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )


class AsyncSshKeysResource:
    """Operations on ``ssh_keys`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_ssh_keys(
        self,
        *,
        sort: Sequence[SortByIdName | UnknownValue] | None = None,
        name: str | None = None,
        fingerprint: str | None = None,
        label_selector: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListSshKeysResponse:
        """List SSH keys.

        Returns all SSH key objects.

        ``GET /ssh_keys``

        Args:
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            fingerprint: May be used to filter SSH keys by their fingerprint. The response will only
                contain the SSH key matching the specified fingerprint.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
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
            "/ssh_keys",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "name": name,
                    "fingerprint": fingerprint,
                    "label_selector": label_selector,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListSshKeysResponse, response)

    async def create_ssh_key(
        self,
        *,
        name: str,
        public_key: str,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> SshKeyResponse:
        """Create an SSH key.

        Creates a new SSH key with the given `name` and `public_key`. Once an SSH key is created, it
        can be used in other calls such as creating Servers.

        ``POST /ssh_keys``

        Args:
            name: Name of the SSH key.
            public_key: Public key.
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
            "/ssh_keys",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "public_key": public_key,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(SshKeyResponse, response)

    async def get_ssh_key(self, ssh_key_id: int, /) -> SshKeyResponse:
        """Get a SSH key.

        Returns a specific SSH key object.

        ``GET /ssh_keys/{id}``

        Args:
            ssh_key_id: ID of the SSH Key.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, ssh_key_id=ssh_key_id)
        response = await self._transport.request(
            "GET",
            f"/ssh_keys/{encode_path(ssh_key_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(SshKeyResponse, response)

    async def update_ssh_key(
        self,
        ssh_key_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> SshKeyResponse:
        """Update an SSH key.

        Updates an SSH key. You can update an SSH key name and an SSH key labels.

        ``PUT /ssh_keys/{id}``

        Args:
            ssh_key_id: ID of the SSH Key.
            name: New name Name to set. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, ssh_key_id=ssh_key_id, labels=labels)
        response = await self._transport.request(
            "PUT",
            f"/ssh_keys/{encode_path(ssh_key_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(SshKeyResponse, response)

    async def delete_ssh_key(self, ssh_key_id: int, /) -> None:
        """Delete an SSH key.

        Deletes an SSH key. It cannot be used anymore.

        ``DELETE /ssh_keys/{id}``

        Args:
            ssh_key_id: ID of the SSH Key.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, ssh_key_id=ssh_key_id)
        await self._transport.request(
            "DELETE",
            f"/ssh_keys/{encode_path(ssh_key_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
