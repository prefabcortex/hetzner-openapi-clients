"""Resource ``certificates`` (generated - do not edit by hand)."""

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
    CertificateResponse,
    CertificatesResponse,
    CertificateType,
    CreateCertificateResponse,
    ErrorResponse,
    SortByIdNameCreated,
)
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncCertificatesResource",
    "CertificatesResource",
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
    "certificate_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "certificate_id": Check(minimum=1, maximum=9007199254740991),
    "labels": LABELS_RULES,
}


class CertificatesResource:
    """Operations on ``certificates`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_certificates(
        self,
        *,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        type: Sequence[CertificateType | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> CertificatesResponse:
        """List Certificates.

        Returns all Certificate objects.

        ``GET /certificates``

        Args:
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            type: Filter resources by type. May be used multiple times. The response will only
                contain the resources with the specified type.
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
            "/certificates",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "name": name,
                    "label_selector": label_selector,
                    "type": type,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(CertificatesResponse, response)

    def create_certificate(
        self,
        *,
        name: str,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        type: CertificateType | UnknownValue | NotGiven = NOT_GIVEN,
        certificate: str | NotGiven = NOT_GIVEN,
        private_key: str | NotGiven = NOT_GIVEN,
        domain_names: StrSequence | NotGiven = NOT_GIVEN,
    ) -> CreateCertificateResponse:
        """Create a Certificate.

        Creates a new Certificate.

        The default type **uploaded** allows for uploading your existing `certificate` and
        `private_key` in PEM format. You have to monitor its expiration date and handle renewal
        yourself.

        In contrast, type **managed** requests a new Certificate from *Let's Encrypt* for the
        specified `domain_names`. Only domains managed by *Hetzner DNS* are supported. We handle
        renewal and timely alert the project owner via email if problems occur.

        For type `managed` Certificates the `action` key of the response contains the Action that
        allows for tracking the issuance process. For type `uploaded` Certificates the `action` is
        always null.

        ``POST /certificates``

        Args:
            name: Name of the Certificate.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            type: Choose between uploading a Certificate in PEM format or requesting a managed
                *Let's Encrypt* Certificate. Omitted if not given. The API default is
                ``"uploaded"``.
            certificate: Certificate and chain in PEM format, in order so that each record directly
                certifies the one preceding. Required for type `uploaded` Certificates. Omitted if
                not given.
            private_key: Certificate key in PEM format. Required for type `uploaded` Certificates.
                Omitted if not given.
            domain_names: Domains and subdomains that should be contained in the Certificate issued
                by *Let's Encrypt*. Required for type `managed` Certificates. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, labels=labels)
        response = self._transport.request(
            "POST",
            "/certificates",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                    "type": type,
                    "certificate": certificate,
                    "private_key": private_key,
                    "domain_names": domain_names,
                },
            ),
        )
        return self._transport.parse(CreateCertificateResponse, response)

    def get_certificate(self, certificate_id: int, /) -> CertificateResponse:
        """Get a Certificate.

        Gets a specific Certificate object.

        ``GET /certificates/{id}``

        Args:
            certificate_id: ID of the Certificate.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, certificate_id=certificate_id)
        response = self._transport.request(
            "GET",
            f"/certificates/{encode_path(certificate_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(CertificateResponse, response)

    def update_certificate(
        self,
        certificate_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CertificateResponse:
        """Update a Certificate.

        Updates the Certificate properties.

        Note: if the Certificate object changes during the request, the response will be a
        "conflict" error.

        ``PUT /certificates/{id}``

        Args:
            certificate_id: ID of the Certificate.
            name: New Certificate name. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, certificate_id=certificate_id, labels=labels)
        response = self._transport.request(
            "PUT",
            f"/certificates/{encode_path(certificate_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(CertificateResponse, response)

    def delete_certificate(self, certificate_id: int, /) -> None:
        """Delete a Certificate.

        Deletes a Certificate.

        ``DELETE /certificates/{id}``

        Args:
            certificate_id: ID of the Certificate.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, certificate_id=certificate_id)
        self._transport.request(
            "DELETE",
            f"/certificates/{encode_path(certificate_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )


class AsyncCertificatesResource:
    """Operations on ``certificates`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_certificates(
        self,
        *,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        type: Sequence[CertificateType | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> CertificatesResponse:
        """List Certificates.

        Returns all Certificate objects.

        ``GET /certificates``

        Args:
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            type: Filter resources by type. May be used multiple times. The response will only
                contain the resources with the specified type.
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
            "/certificates",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "name": name,
                    "label_selector": label_selector,
                    "type": type,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(CertificatesResponse, response)

    async def create_certificate(
        self,
        *,
        name: str,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        type: CertificateType | UnknownValue | NotGiven = NOT_GIVEN,
        certificate: str | NotGiven = NOT_GIVEN,
        private_key: str | NotGiven = NOT_GIVEN,
        domain_names: StrSequence | NotGiven = NOT_GIVEN,
    ) -> CreateCertificateResponse:
        """Create a Certificate.

        Creates a new Certificate.

        The default type **uploaded** allows for uploading your existing `certificate` and
        `private_key` in PEM format. You have to monitor its expiration date and handle renewal
        yourself.

        In contrast, type **managed** requests a new Certificate from *Let's Encrypt* for the
        specified `domain_names`. Only domains managed by *Hetzner DNS* are supported. We handle
        renewal and timely alert the project owner via email if problems occur.

        For type `managed` Certificates the `action` key of the response contains the Action that
        allows for tracking the issuance process. For type `uploaded` Certificates the `action` is
        always null.

        ``POST /certificates``

        Args:
            name: Name of the Certificate.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            type: Choose between uploading a Certificate in PEM format or requesting a managed
                *Let's Encrypt* Certificate. Omitted if not given. The API default is
                ``"uploaded"``.
            certificate: Certificate and chain in PEM format, in order so that each record directly
                certifies the one preceding. Required for type `uploaded` Certificates. Omitted if
                not given.
            private_key: Certificate key in PEM format. Required for type `uploaded` Certificates.
                Omitted if not given.
            domain_names: Domains and subdomains that should be contained in the Certificate issued
                by *Let's Encrypt*. Required for type `managed` Certificates. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, labels=labels)
        response = await self._transport.request(
            "POST",
            "/certificates",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                    "type": type,
                    "certificate": certificate,
                    "private_key": private_key,
                    "domain_names": domain_names,
                },
            ),
        )
        return self._transport.parse(CreateCertificateResponse, response)

    async def get_certificate(self, certificate_id: int, /) -> CertificateResponse:
        """Get a Certificate.

        Gets a specific Certificate object.

        ``GET /certificates/{id}``

        Args:
            certificate_id: ID of the Certificate.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, certificate_id=certificate_id)
        response = await self._transport.request(
            "GET",
            f"/certificates/{encode_path(certificate_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(CertificateResponse, response)

    async def update_certificate(
        self,
        certificate_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CertificateResponse:
        """Update a Certificate.

        Updates the Certificate properties.

        Note: if the Certificate object changes during the request, the response will be a
        "conflict" error.

        ``PUT /certificates/{id}``

        Args:
            certificate_id: ID of the Certificate.
            name: New Certificate name. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, certificate_id=certificate_id, labels=labels)
        response = await self._transport.request(
            "PUT",
            f"/certificates/{encode_path(certificate_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(CertificateResponse, response)

    async def delete_certificate(self, certificate_id: int, /) -> None:
        """Delete a Certificate.

        Deletes a Certificate.

        ``DELETE /certificates/{id}``

        Args:
            certificate_id: ID of the Certificate.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, certificate_id=certificate_id)
        await self._transport.request(
            "DELETE",
            f"/certificates/{encode_path(certificate_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
