"""Resource ``zones`` (generated - do not edit by hand)."""

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
    CreateZoneResponse,
    ErrorResponse,
    ListZonesResponse,
    SortByIdNameCreated,
    Zonefile,
    ZoneMode,
    ZoneResponse,
)
from hetzner_api.params import RRSetRequestParam, ZonePrimaryNameserverParam
from hetzner_api.rules import LABELS_RULES, RR_SET_REQUEST_FIELDS

__all__ = [
    "AsyncZonesResource",
    "ZonesResource",
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
    "name": Check(max_length=255),
    "ttl": Check(minimum=60, maximum=2147483647),
    "labels": LABELS_RULES,
    "rrsets": Check(items=Check(fields_of=lambda: RR_SET_REQUEST_FIELDS)),
}

_CHECKS_3: Final[Mapping[str, Check]] = {
    "labels": LABELS_RULES,
}


class ZonesResource:
    """Operations on ``zones`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_zones(
        self,
        *,
        name: str | None = None,
        mode: ZoneMode | UnknownValue | None = None,
        label_selector: str | None = None,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListZonesResponse:
        """List Zones.

        Returns all Zones.

        Use the provided URI parameters to modify the result.

        ``GET /zones``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            mode: Filter resources by their mode. The response will only contain the resources
                matching exactly the specified mode.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
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
            "/zones",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "mode": mode,
                    "label_selector": label_selector,
                    "sort": sort,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListZonesResponse, response)

    def create_zone(
        self,
        *,
        name: str,
        mode: ZoneMode | UnknownValue,
        ttl: int | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        primary_nameservers: Sequence[ZonePrimaryNameserverParam] | NotGiven = NOT_GIVEN,
        rrsets: Sequence[RRSetRequestParam] | NotGiven = NOT_GIVEN,
        zonefile: str | NotGiven = NOT_GIVEN,
    ) -> CreateZoneResponse:
        """Create a Zone.

        Creates a Zone.

        A default `SOA` and three `NS` resource records with the assigned Hetzner nameservers are
        created automatically.

        ``POST /zones``

        Args:
            name: Name of the Zone. All names with well-known public suffixes
                (https://publicsuffix.org/) (e.g. `.de`, `.com`, `.co.uk`) are supported. Subdomains
                are not supported. The name must be in lower case and must not end with a dot.
                Internationalized domain names
                (https://en.wikipedia.org/wiki/Internationalized_domain_name) must be transcribed to
                Punycode (https://wikipedia.org/wiki/Punycode) representation with ACE prefix, e.g.
                `xn--mnchen-3ya.de` (`münchen.de`).
            mode: Mode of the Zone. For more information, see Zone Modes.
            ttl: Default Time To Live (TTL) of the Zone. Must be in between 60s and 2147483647s.
                This TTL is used for RRSets that do not explicitly define a TTL. Omitted if not
                given. The API default is ``3600``.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            primary_nameservers: Primary nameservers of the Zone. Only applicable for Zones in
                secondary mode. Ignored for Zones in primary mode. Omitted if not given.
            rrsets: RRSets to be added to the Zone. Only applicable for Zones in primary mode.
                Ignored for Zones in secondary mode. Omitted if not given.
            zonefile: Zone file to import. Only applicable for Zones in primary mode. Ignored for
                Zones in secondary mode. If provided, `rrsets` must be empty. See Zone file import
                for more details. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, name=name, ttl=ttl, labels=labels, rrsets=rrsets)
        response = self._transport.request(
            "POST",
            "/zones",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "mode": mode,
                    "ttl": ttl,
                    "labels": labels,
                    "primary_nameservers": primary_nameservers,
                    "rrsets": rrsets,
                    "zonefile": zonefile,
                },
            ),
        )
        return self._transport.parse(CreateZoneResponse, response)

    def get_zone(self, id_or_name: str, /) -> ZoneResponse:
        """Get a Zone.

        Returns a single Zone.

        ``GET /zones/{id_or_name}``

        Args:
            id_or_name: ID or Name of the Zone.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = self._transport.request(
            "GET",
            f"/zones/{encode_path(id_or_name)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ZoneResponse, response)

    def update_zone(
        self,
        id_or_name: str,
        /,
        *,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> ZoneResponse:
        """Update a Zone.

        Updates a Zone.

        To modify resource record sets (RRSets), use the RRSet Actions endpoints.

        ``PUT /zones/{id_or_name}``

        Args:
            id_or_name: ID or Name of the Zone.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, labels=labels)
        response = self._transport.request(
            "PUT",
            f"/zones/{encode_path(id_or_name)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(ZoneResponse, response)

    def delete_zone(self, id_or_name: str, /) -> ActionResponse:
        """Delete a Zone.

        Deletes a Zone.

        ``DELETE /zones/{id_or_name}``

        Args:
            id_or_name: ID or Name of the Zone.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = self._transport.request(
            "DELETE",
            f"/zones/{encode_path(id_or_name)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def get_zone_zonefile(self, id_or_name: str, /) -> Zonefile:
        """Export a Zone file.

        Returns a generated Zone file in BIND (RFC 1034
        (https://datatracker.ietf.org/doc/html/rfc1034)/1035
        (https://datatracker.ietf.org/doc/html/rfc1035)) format.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``GET /zones/{id_or_name}/zonefile``

        Args:
            id_or_name: ID or Name of the Zone.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = self._transport.request(
            "GET",
            f"/zones/{encode_path(id_or_name)}/zonefile",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(Zonefile, response)


class AsyncZonesResource:
    """Operations on ``zones`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_zones(
        self,
        *,
        name: str | None = None,
        mode: ZoneMode | UnknownValue | None = None,
        label_selector: str | None = None,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListZonesResponse:
        """List Zones.

        Returns all Zones.

        Use the provided URI parameters to modify the result.

        ``GET /zones``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            mode: Filter resources by their mode. The response will only contain the resources
                matching exactly the specified mode.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
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
            "/zones",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "mode": mode,
                    "label_selector": label_selector,
                    "sort": sort,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListZonesResponse, response)

    async def create_zone(
        self,
        *,
        name: str,
        mode: ZoneMode | UnknownValue,
        ttl: int | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        primary_nameservers: Sequence[ZonePrimaryNameserverParam] | NotGiven = NOT_GIVEN,
        rrsets: Sequence[RRSetRequestParam] | NotGiven = NOT_GIVEN,
        zonefile: str | NotGiven = NOT_GIVEN,
    ) -> CreateZoneResponse:
        """Create a Zone.

        Creates a Zone.

        A default `SOA` and three `NS` resource records with the assigned Hetzner nameservers are
        created automatically.

        ``POST /zones``

        Args:
            name: Name of the Zone. All names with well-known public suffixes
                (https://publicsuffix.org/) (e.g. `.de`, `.com`, `.co.uk`) are supported. Subdomains
                are not supported. The name must be in lower case and must not end with a dot.
                Internationalized domain names
                (https://en.wikipedia.org/wiki/Internationalized_domain_name) must be transcribed to
                Punycode (https://wikipedia.org/wiki/Punycode) representation with ACE prefix, e.g.
                `xn--mnchen-3ya.de` (`münchen.de`).
            mode: Mode of the Zone. For more information, see Zone Modes.
            ttl: Default Time To Live (TTL) of the Zone. Must be in between 60s and 2147483647s.
                This TTL is used for RRSets that do not explicitly define a TTL. Omitted if not
                given. The API default is ``3600``.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            primary_nameservers: Primary nameservers of the Zone. Only applicable for Zones in
                secondary mode. Ignored for Zones in primary mode. Omitted if not given.
            rrsets: RRSets to be added to the Zone. Only applicable for Zones in primary mode.
                Ignored for Zones in secondary mode. Omitted if not given.
            zonefile: Zone file to import. Only applicable for Zones in primary mode. Ignored for
                Zones in secondary mode. If provided, `rrsets` must be empty. See Zone file import
                for more details. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, name=name, ttl=ttl, labels=labels, rrsets=rrsets)
        response = await self._transport.request(
            "POST",
            "/zones",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "mode": mode,
                    "ttl": ttl,
                    "labels": labels,
                    "primary_nameservers": primary_nameservers,
                    "rrsets": rrsets,
                    "zonefile": zonefile,
                },
            ),
        )
        return self._transport.parse(CreateZoneResponse, response)

    async def get_zone(self, id_or_name: str, /) -> ZoneResponse:
        """Get a Zone.

        Returns a single Zone.

        ``GET /zones/{id_or_name}``

        Args:
            id_or_name: ID or Name of the Zone.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = await self._transport.request(
            "GET",
            f"/zones/{encode_path(id_or_name)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ZoneResponse, response)

    async def update_zone(
        self,
        id_or_name: str,
        /,
        *,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> ZoneResponse:
        """Update a Zone.

        Updates a Zone.

        To modify resource record sets (RRSets), use the RRSet Actions endpoints.

        ``PUT /zones/{id_or_name}``

        Args:
            id_or_name: ID or Name of the Zone.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, labels=labels)
        response = await self._transport.request(
            "PUT",
            f"/zones/{encode_path(id_or_name)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(ZoneResponse, response)

    async def delete_zone(self, id_or_name: str, /) -> ActionResponse:
        """Delete a Zone.

        Deletes a Zone.

        ``DELETE /zones/{id_or_name}``

        Args:
            id_or_name: ID or Name of the Zone.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = await self._transport.request(
            "DELETE",
            f"/zones/{encode_path(id_or_name)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def get_zone_zonefile(self, id_or_name: str, /) -> Zonefile:
        """Export a Zone file.

        Returns a generated Zone file in BIND (RFC 1034
        (https://datatracker.ietf.org/doc/html/rfc1034)/1035
        (https://datatracker.ietf.org/doc/html/rfc1035)) format.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``GET /zones/{id_or_name}/zonefile``

        Args:
            id_or_name: ID or Name of the Zone.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = await self._transport.request(
            "GET",
            f"/zones/{encode_path(id_or_name)}/zonefile",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(Zonefile, response)
