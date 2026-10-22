"""Resource ``certificate_actions`` (generated - do not edit by hand)."""

from collections.abc import Mapping, Sequence
from typing import Final
from warnings import deprecated

from hetzner_api._auth import Security
from hetzner_api._base_client import AsyncTransport, SyncTransport, encode_path, encode_query
from hetzner_api._types import UnknownValue
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
    "AsyncCertificateActionsResource",
    "CertificateActionsResource",
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
    "certificate_id": Check(minimum=1, maximum=9007199254740991),
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "certificate_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_5: Final[Mapping[str, Check]] = {
    "certificate_id": Check(minimum=1, maximum=9007199254740991),
    "action_id": Check(minimum=1, maximum=9007199254740991),
}


class CertificateActionsResource:
    """Operations on ``certificate_actions`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_certificates_actions(
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

        ``GET /certificates/actions``

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
            "/certificates/actions",
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

    def get_certificates_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action object.

        ``GET /certificates/actions/{id}``

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
            f"/certificates/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def list_certificate_actions(
        self,
        certificate_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Certificate.

        Returns all Action objects for a Certificate. You can sort the results by using the `sort`
        URI parameter, and filter them with the `status` parameter.

        Only type `managed` Certificates can have Actions. For type `uploaded` Certificates the
        `actions` key will always contain an empty array.

        ``GET /certificates/{id}/actions``

        Args:
            certificate_id: ID of the Certificate.
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
            certificate_id=certificate_id,
            page=page,
            per_page=per_page,
        )
        response = self._transport.request(
            "GET",
            f"/certificates/{encode_path(certificate_id)}/actions",
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

    def retry_certificate(self, certificate_id: int, /) -> ActionResponse:
        """Retry Issuance or Renewal.

        Retry a failed Certificate issuance or renewal.

        Only applicable if the type of the Certificate is `managed` and the issuance or renewal
        status is `failed`.

        **Operation specific errors**

        - `caa_record_does_not_allow_ca` - CAA record does not allow certificate authority
        - `ca_dns_validation_failed` - Certificate Authority: DNS validation failed
        - `ca_too_many_authorizations_failed_recently` - Certificate Authority: Too many
          authorizations failed recently
        - `ca_too_many_certificates_issued_for_registered_domain` - Certificate Authority: Too many
          certificates issued for registered domain
        - `ca_too_many_duplicate_certificates` - Certificate Authority: Too many duplicate
          certificates
        - `could_not_verify_domain_delegated_to_zone` - Could not verify domain delegated to zone
        - `dns_zone_not_found` - DNS zone not found
        - `dns_zone_is_secondary_zone` - DNS zone is a secondary zone

        ``POST /certificates/{id}/actions/retry``

        Args:
            certificate_id: ID of the Certificate.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, certificate_id=certificate_id)
        response = self._transport.request(
            "POST",
            f"/certificates/{encode_path(certificate_id)}/actions/retry",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    @deprecated("GET /certificates/{id}/actions/{action_id} is deprecated by the API")
    def get_certificate_action(self, certificate_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Certificate.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Certificate. Only type `managed` Certificates have Actions.

        ``GET /certificates/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            certificate_id: ID of the Certificate.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, certificate_id=certificate_id, action_id=action_id)
        response = self._transport.request(
            "GET",
            f"/certificates/{encode_path(certificate_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)


class AsyncCertificateActionsResource:
    """Operations on ``certificate_actions`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_certificates_actions(
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

        ``GET /certificates/actions``

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
            "/certificates/actions",
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

    async def get_certificates_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action object.

        ``GET /certificates/actions/{id}``

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
            f"/certificates/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def list_certificate_actions(
        self,
        certificate_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Certificate.

        Returns all Action objects for a Certificate. You can sort the results by using the `sort`
        URI parameter, and filter them with the `status` parameter.

        Only type `managed` Certificates can have Actions. For type `uploaded` Certificates the
        `actions` key will always contain an empty array.

        ``GET /certificates/{id}/actions``

        Args:
            certificate_id: ID of the Certificate.
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
            certificate_id=certificate_id,
            page=page,
            per_page=per_page,
        )
        response = await self._transport.request(
            "GET",
            f"/certificates/{encode_path(certificate_id)}/actions",
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

    async def retry_certificate(self, certificate_id: int, /) -> ActionResponse:
        """Retry Issuance or Renewal.

        Retry a failed Certificate issuance or renewal.

        Only applicable if the type of the Certificate is `managed` and the issuance or renewal
        status is `failed`.

        **Operation specific errors**

        - `caa_record_does_not_allow_ca` - CAA record does not allow certificate authority
        - `ca_dns_validation_failed` - Certificate Authority: DNS validation failed
        - `ca_too_many_authorizations_failed_recently` - Certificate Authority: Too many
          authorizations failed recently
        - `ca_too_many_certificates_issued_for_registered_domain` - Certificate Authority: Too many
          certificates issued for registered domain
        - `ca_too_many_duplicate_certificates` - Certificate Authority: Too many duplicate
          certificates
        - `could_not_verify_domain_delegated_to_zone` - Could not verify domain delegated to zone
        - `dns_zone_not_found` - DNS zone not found
        - `dns_zone_is_secondary_zone` - DNS zone is a secondary zone

        ``POST /certificates/{id}/actions/retry``

        Args:
            certificate_id: ID of the Certificate.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, certificate_id=certificate_id)
        response = await self._transport.request(
            "POST",
            f"/certificates/{encode_path(certificate_id)}/actions/retry",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    @deprecated("GET /certificates/{id}/actions/{action_id} is deprecated by the API")
    async def get_certificate_action(
        self,
        certificate_id: int,
        action_id: int,
        /,
    ) -> ActionResponse:
        """Get an Action for a Certificate.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Certificate. Only type `managed` Certificates have Actions.

        ``GET /certificates/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            certificate_id: ID of the Certificate.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, certificate_id=certificate_id, action_id=action_id)
        response = await self._transport.request(
            "GET",
            f"/certificates/{encode_path(certificate_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)
