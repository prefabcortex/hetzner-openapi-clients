"""Resource ``images`` (generated - do not edit by hand)."""

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
from hetzner_api._types import NOT_GIVEN, NotGiven, StrSequence, UnknownValue
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import (
    Architecture,
    ErrorResponse,
    ImageResponse,
    ImageStatus,
    ImageType,
    ListImagesResponse,
    SortByIdNameCreated,
)
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncImagesResource",
    "ImagesResource",
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
    "image_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_3: Final[Mapping[str, Check]] = {
    "image_id": Check(minimum=1, maximum=9007199254740991),
    "labels": LABELS_RULES,
}


class ImagesResource:
    """Operations on ``images`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_images(
        self,
        *,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        type: Sequence[ImageType | UnknownValue] | None = None,
        status: Sequence[ImageStatus | UnknownValue] | None = None,
        bound_to: StrSequence | None = None,
        include_deprecated: bool | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        architecture: Architecture | UnknownValue | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListImagesResponse:
        """List Images.

        Returns all Image objects. You can select specific Image types only and sort the results by
        using URI parameters.

        ``GET /images``

        Args:
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            type: Filter resources by type. May be used multiple times. The response will only
                contain the resources with the specified type.
            status: Filter resources by status. May be used multiple times. The response will only
                contain the resources with the specified status.
            bound_to: Filter Images by their linked Server ID. May be used multiple times. Only
                available for Images of type `backup`.
            include_deprecated: Include deprecated Images.
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            architecture: Filter resources by cpu architecture. The response will only contain the
                resources with the specified cpu architecture.
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
            "/images",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "type": type,
                    "status": status,
                    "bound_to": bound_to,
                    "include_deprecated": include_deprecated,
                    "name": name,
                    "label_selector": label_selector,
                    "architecture": architecture,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListImagesResponse, response)

    def get_image(self, image_id: int, /) -> ImageResponse:
        """Get an Image.

        Returns a specific Image object.

        ``GET /images/{id}``

        Args:
            image_id: ID of the Image.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, image_id=image_id)
        response = self._transport.request(
            "GET",
            f"/images/{encode_path(image_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ImageResponse, response)

    def update_image(
        self,
        image_id: int,
        /,
        *,
        description: str | NotGiven = NOT_GIVEN,
        type: Literal["snapshot"] | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> ImageResponse:
        """Update an Image.

        Updates the Image. You may change the description, convert a Backup Image to a Snapshot
        Image or change the Image labels. Only Images of type `snapshot` and `backup` can be
        updated.

        ``PUT /images/{id}``

        Args:
            image_id: ID of the Image.
            description: New description of Image. Omitted if not given.
            type: Destination Image type to convert to. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, image_id=image_id, labels=labels)
        response = self._transport.request(
            "PUT",
            f"/images/{encode_path(image_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "description": description,
                    "type": type,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(ImageResponse, response)

    def delete_image(self, image_id: int, /) -> None:
        """Delete an Image.

        Deletes an Image. Only Images of type `snapshot` and `backup` can be deleted.

        ``DELETE /images/{id}``

        Args:
            image_id: ID of the Image.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, image_id=image_id)
        self._transport.request(
            "DELETE",
            f"/images/{encode_path(image_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )


class AsyncImagesResource:
    """Operations on ``images`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_images(
        self,
        *,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        type: Sequence[ImageType | UnknownValue] | None = None,
        status: Sequence[ImageStatus | UnknownValue] | None = None,
        bound_to: StrSequence | None = None,
        include_deprecated: bool | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        architecture: Architecture | UnknownValue | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListImagesResponse:
        """List Images.

        Returns all Image objects. You can select specific Image types only and sort the results by
        using URI parameters.

        ``GET /images``

        Args:
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            type: Filter resources by type. May be used multiple times. The response will only
                contain the resources with the specified type.
            status: Filter resources by status. May be used multiple times. The response will only
                contain the resources with the specified status.
            bound_to: Filter Images by their linked Server ID. May be used multiple times. Only
                available for Images of type `backup`.
            include_deprecated: Include deprecated Images.
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            architecture: Filter resources by cpu architecture. The response will only contain the
                resources with the specified cpu architecture.
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
            "/images",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "type": type,
                    "status": status,
                    "bound_to": bound_to,
                    "include_deprecated": include_deprecated,
                    "name": name,
                    "label_selector": label_selector,
                    "architecture": architecture,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListImagesResponse, response)

    async def get_image(self, image_id: int, /) -> ImageResponse:
        """Get an Image.

        Returns a specific Image object.

        ``GET /images/{id}``

        Args:
            image_id: ID of the Image.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, image_id=image_id)
        response = await self._transport.request(
            "GET",
            f"/images/{encode_path(image_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ImageResponse, response)

    async def update_image(
        self,
        image_id: int,
        /,
        *,
        description: str | NotGiven = NOT_GIVEN,
        type: Literal["snapshot"] | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> ImageResponse:
        """Update an Image.

        Updates the Image. You may change the description, convert a Backup Image to a Snapshot
        Image or change the Image labels. Only Images of type `snapshot` and `backup` can be
        updated.

        ``PUT /images/{id}``

        Args:
            image_id: ID of the Image.
            description: New description of Image. Omitted if not given.
            type: Destination Image type to convert to. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, image_id=image_id, labels=labels)
        response = await self._transport.request(
            "PUT",
            f"/images/{encode_path(image_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "description": description,
                    "type": type,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(ImageResponse, response)

    async def delete_image(self, image_id: int, /) -> None:
        """Delete an Image.

        Deletes an Image. Only Images of type `snapshot` and `backup` can be deleted.

        ``DELETE /images/{id}``

        Args:
            image_id: ID of the Image.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, image_id=image_id)
        await self._transport.request(
            "DELETE",
            f"/images/{encode_path(image_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
