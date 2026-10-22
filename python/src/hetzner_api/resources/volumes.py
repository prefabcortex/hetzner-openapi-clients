"""Resource ``volumes`` (generated - do not edit by hand)."""

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
    CreateVolumeResponse,
    ErrorResponse,
    ListVolumesResponse,
    SortByIdNameCreated,
    VolumeResponse,
    VolumeStatus,
)
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncVolumesResource",
    "VolumesResource",
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
    "volume_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "volume_id": Check(minimum=1, maximum=9007199254740991),
    "labels": LABELS_RULES,
}


class VolumesResource:
    """Operations on ``volumes`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_volumes(
        self,
        *,
        status: Sequence[VolumeStatus | UnknownValue] | None = None,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListVolumesResponse:
        """List Volumes.

        Gets all existing Volumes that you have available.

        ``GET /volumes``

        Args:
            status: Filter resources by status. May be used multiple times. The response will only
                contain the resources with the specified status.
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
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
            "/volumes",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "status": status,
                    "sort": sort,
                    "name": name,
                    "label_selector": label_selector,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListVolumesResponse, response)

    def create_volume(
        self,
        *,
        size: int,
        name: str,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        automount: bool | NotGiven = NOT_GIVEN,
        format: str | NotGiven = NOT_GIVEN,
        location: str | int | NotGiven = NOT_GIVEN,
        server: int | NotGiven = NOT_GIVEN,
    ) -> CreateVolumeResponse:
        """Create a Volume.

        Creates a new Volume attached to a Server. If you want to create a Volume that is not
        attached to a Server, you need to provide the `location` key instead of `server`. This can
        be either the ID or the name of the Location this Volume will be created in. Note that a
        Volume can be attached to a Server only in the same Location as the Volume itself.

        Specifying the Server during Volume creation will automatically attach the Volume to that
        Server after it has been initialized. In that case, the `next_actions` key in the response
        is an array which contains a single `attach_volume` action.

        The minimum Volume size is 10GB and the maximum size is 10TB (10240GB).

        A volume's name can consist of alphanumeric characters, dashes, underscores, and dots, but
        has to start and end with an alphanumeric character. The total length is limited to 64
        characters. Volume names must be unique per Project.

        **Operation specific errors**

        - `422` - `no_space_left_in_location` - There is no volume space left in the given location

        ``POST /volumes``

        Args:
            size: Size of the Volume in GB.
            name: Name of the volume.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            automount: Auto-mount Volume after attach. `server` must be provided. Omitted if not
                given.
            format: Format Volume after creation. One of: `xfs`, `ext4`. Omitted if not given.
            location: Location to create the Volume in (can be omitted if Server is specified).
                Omitted if not given.
            server: Server to which to attach the Volume once it's created (Volume will be created
                in the same Location as the server). Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, labels=labels)
        response = self._transport.request(
            "POST",
            "/volumes",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "size": size,
                    "name": name,
                    "labels": labels,
                    "automount": automount,
                    "format": format,
                    "location": location,
                    "server": server,
                },
            ),
        )
        return self._transport.parse(CreateVolumeResponse, response)

    def get_volume(self, volume_id: int, /) -> VolumeResponse:
        """Get a Volume.

        Gets a specific Volume object.

        ``GET /volumes/{id}``

        Args:
            volume_id: ID of the Volume.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, volume_id=volume_id)
        response = self._transport.request(
            "GET",
            f"/volumes/{encode_path(volume_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(VolumeResponse, response)

    def update_volume(
        self,
        volume_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> VolumeResponse:
        """Update a Volume.

        Updates the Volume properties.

        ``PUT /volumes/{id}``

        Args:
            volume_id: ID of the Volume.
            name: New Volume name. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, volume_id=volume_id, labels=labels)
        response = self._transport.request(
            "PUT",
            f"/volumes/{encode_path(volume_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(VolumeResponse, response)

    def delete_volume(self, volume_id: int, /) -> None:
        """Delete a Volume.

        Deletes a volume. All Volume data is irreversibly destroyed. The Volume must not be attached
        to a Server and it must not have delete protection enabled.

        ``DELETE /volumes/{id}``

        Args:
            volume_id: ID of the Volume.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, volume_id=volume_id)
        self._transport.request(
            "DELETE",
            f"/volumes/{encode_path(volume_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )


class AsyncVolumesResource:
    """Operations on ``volumes`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_volumes(
        self,
        *,
        status: Sequence[VolumeStatus | UnknownValue] | None = None,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListVolumesResponse:
        """List Volumes.

        Gets all existing Volumes that you have available.

        ``GET /volumes``

        Args:
            status: Filter resources by status. May be used multiple times. The response will only
                contain the resources with the specified status.
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
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
            "/volumes",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "status": status,
                    "sort": sort,
                    "name": name,
                    "label_selector": label_selector,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListVolumesResponse, response)

    async def create_volume(
        self,
        *,
        size: int,
        name: str,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        automount: bool | NotGiven = NOT_GIVEN,
        format: str | NotGiven = NOT_GIVEN,
        location: str | int | NotGiven = NOT_GIVEN,
        server: int | NotGiven = NOT_GIVEN,
    ) -> CreateVolumeResponse:
        """Create a Volume.

        Creates a new Volume attached to a Server. If you want to create a Volume that is not
        attached to a Server, you need to provide the `location` key instead of `server`. This can
        be either the ID or the name of the Location this Volume will be created in. Note that a
        Volume can be attached to a Server only in the same Location as the Volume itself.

        Specifying the Server during Volume creation will automatically attach the Volume to that
        Server after it has been initialized. In that case, the `next_actions` key in the response
        is an array which contains a single `attach_volume` action.

        The minimum Volume size is 10GB and the maximum size is 10TB (10240GB).

        A volume's name can consist of alphanumeric characters, dashes, underscores, and dots, but
        has to start and end with an alphanumeric character. The total length is limited to 64
        characters. Volume names must be unique per Project.

        **Operation specific errors**

        - `422` - `no_space_left_in_location` - There is no volume space left in the given location

        ``POST /volumes``

        Args:
            size: Size of the Volume in GB.
            name: Name of the volume.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            automount: Auto-mount Volume after attach. `server` must be provided. Omitted if not
                given.
            format: Format Volume after creation. One of: `xfs`, `ext4`. Omitted if not given.
            location: Location to create the Volume in (can be omitted if Server is specified).
                Omitted if not given.
            server: Server to which to attach the Volume once it's created (Volume will be created
                in the same Location as the server). Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, labels=labels)
        response = await self._transport.request(
            "POST",
            "/volumes",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "size": size,
                    "name": name,
                    "labels": labels,
                    "automount": automount,
                    "format": format,
                    "location": location,
                    "server": server,
                },
            ),
        )
        return self._transport.parse(CreateVolumeResponse, response)

    async def get_volume(self, volume_id: int, /) -> VolumeResponse:
        """Get a Volume.

        Gets a specific Volume object.

        ``GET /volumes/{id}``

        Args:
            volume_id: ID of the Volume.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, volume_id=volume_id)
        response = await self._transport.request(
            "GET",
            f"/volumes/{encode_path(volume_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(VolumeResponse, response)

    async def update_volume(
        self,
        volume_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> VolumeResponse:
        """Update a Volume.

        Updates the Volume properties.

        ``PUT /volumes/{id}``

        Args:
            volume_id: ID of the Volume.
            name: New Volume name. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, volume_id=volume_id, labels=labels)
        response = await self._transport.request(
            "PUT",
            f"/volumes/{encode_path(volume_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(VolumeResponse, response)

    async def delete_volume(self, volume_id: int, /) -> None:
        """Delete a Volume.

        Deletes a volume. All Volume data is irreversibly destroyed. The Volume must not be attached
        to a Server and it must not have delete protection enabled.

        ``DELETE /volumes/{id}``

        Args:
            volume_id: ID of the Volume.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, volume_id=volume_id)
        await self._transport.request(
            "DELETE",
            f"/volumes/{encode_path(volume_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
