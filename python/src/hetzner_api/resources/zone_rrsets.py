"""Resource ``zone_rrsets`` (generated - do not edit by hand)."""

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
    CreateZoneRrsetResponse,
    ErrorResponse,
    ListZoneRrsetsResponse,
    RrsetResponse,
    RRSetType,
    SortByIdNameCreated,
)
from hetzner_api.params import RecordParam
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncZoneRrsetsResource",
    "ZoneRrsetsResource",
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
    "ttl": Check(minimum=60, maximum=2147483647),
    "labels": LABELS_RULES,
}

_CHECKS_3: Final[Mapping[str, Check]] = {
    "labels": LABELS_RULES,
}


class ZoneRrsetsResource:
    """Operations on ``zone_rrsets`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_zone_rrsets(
        self,
        id_or_name: str,
        /,
        *,
        name: str | None = None,
        type: Sequence[RRSetType | UnknownValue] | None = None,
        label_selector: str | None = None,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListZoneRrsetsResponse:
        """List RRSets.

        Returns all RRSets in the Zone.

        Use the provided URI parameters to modify the result.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``GET /zones/{id_or_name}/rrsets``

        Args:
            id_or_name: ID or Name of the Zone.
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            type: Filter resources by their type. May be used multiple times. The response will only
                contain resources matching the specified types.
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
            f"/zones/{encode_path(id_or_name)}/rrsets",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "type": type,
                    "label_selector": label_selector,
                    "sort": sort,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListZoneRrsetsResponse, response)

    def create_zone_rrset(
        self,
        id_or_name: str,
        /,
        *,
        name: str,
        type: RRSetType | UnknownValue,
        records: Sequence[RecordParam],
        ttl: int | NotGiven | None = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CreateZoneRrsetResponse:
        """Create an RRSet.

        Create an RRSet in the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets``

        Args:
            id_or_name: ID or Name of the Zone.
            name: Name of the RRSet. The name must be in lower case, and must not end with a dot or
                the Zone name. Names containing non-ASCII characters must be transcribed to Punycode
                (https://wikipedia.org/wiki/Punycode) representation with ACE prefix, e.g. `xn--4bi`
                (️). For the Zone apex, use `@`.
            type: Type of the RRSet.
            records: Records of the RRSet. Must not be empty and must only contain distinct record
                values. The order of records returned in responses is not guaranteed to be
                consistent.
            ttl: Time To Live (TTL) of the RRSet. Must be in between 60s and 2147483647s. If not
                set, the Zone's Default TTL is used. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, ttl=ttl, labels=labels)
        response = self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "type": type,
                    "ttl": ttl,
                    "records": records,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(CreateZoneRrsetResponse, response)

    def get_zone_rrset(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
    ) -> RrsetResponse:
        """Get an RRSet.

        Returns a single RRSet from the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``GET /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = self._transport.request(
            "GET",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(RrsetResponse, response)

    def update_zone_rrset(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> RrsetResponse:
        """Update an RRSet.

        Updates an RRSet in the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``PUT /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
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
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(RrsetResponse, response)

    def delete_zone_rrset(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
    ) -> ActionResponse:
        """Delete an RRSet.

        Deletes an RRSet from the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``DELETE /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = self._transport.request(
            "DELETE",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)


class AsyncZoneRrsetsResource:
    """Operations on ``zone_rrsets`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_zone_rrsets(
        self,
        id_or_name: str,
        /,
        *,
        name: str | None = None,
        type: Sequence[RRSetType | UnknownValue] | None = None,
        label_selector: str | None = None,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListZoneRrsetsResponse:
        """List RRSets.

        Returns all RRSets in the Zone.

        Use the provided URI parameters to modify the result.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``GET /zones/{id_or_name}/rrsets``

        Args:
            id_or_name: ID or Name of the Zone.
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            type: Filter resources by their type. May be used multiple times. The response will only
                contain resources matching the specified types.
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
            f"/zones/{encode_path(id_or_name)}/rrsets",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "type": type,
                    "label_selector": label_selector,
                    "sort": sort,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListZoneRrsetsResponse, response)

    async def create_zone_rrset(
        self,
        id_or_name: str,
        /,
        *,
        name: str,
        type: RRSetType | UnknownValue,
        records: Sequence[RecordParam],
        ttl: int | NotGiven | None = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CreateZoneRrsetResponse:
        """Create an RRSet.

        Create an RRSet in the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets``

        Args:
            id_or_name: ID or Name of the Zone.
            name: Name of the RRSet. The name must be in lower case, and must not end with a dot or
                the Zone name. Names containing non-ASCII characters must be transcribed to Punycode
                (https://wikipedia.org/wiki/Punycode) representation with ACE prefix, e.g. `xn--4bi`
                (️). For the Zone apex, use `@`.
            type: Type of the RRSet.
            records: Records of the RRSet. Must not be empty and must only contain distinct record
                values. The order of records returned in responses is not guaranteed to be
                consistent.
            ttl: Time To Live (TTL) of the RRSet. Must be in between 60s and 2147483647s. If not
                set, the Zone's Default TTL is used. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, ttl=ttl, labels=labels)
        response = await self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "type": type,
                    "ttl": ttl,
                    "records": records,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(CreateZoneRrsetResponse, response)

    async def get_zone_rrset(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
    ) -> RrsetResponse:
        """Get an RRSet.

        Returns a single RRSet from the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``GET /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = await self._transport.request(
            "GET",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(RrsetResponse, response)

    async def update_zone_rrset(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> RrsetResponse:
        """Update an RRSet.

        Updates an RRSet in the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``PUT /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
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
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(RrsetResponse, response)

    async def delete_zone_rrset(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
    ) -> ActionResponse:
        """Delete an RRSet.

        Deletes an RRSet from the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``DELETE /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = await self._transport.request(
            "DELETE",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)
