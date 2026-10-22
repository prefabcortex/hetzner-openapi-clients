"""Resource ``zone_rrset_actions`` (generated - do not edit by hand)."""

from collections.abc import Mapping, Sequence
from typing import Final

from hetzner_api._auth import Security
from hetzner_api._base_client import AsyncTransport, SyncTransport, encode_body, encode_path
from hetzner_api._types import NOT_GIVEN, NotGiven, UnknownValue
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import ActionResponse, ErrorResponse, RRSetType
from hetzner_api.params import RecordParam, UpdateZoneRrsetRecordsRecordParam

__all__ = [
    "AsyncZoneRrsetActionsResource",
    "ZoneRrsetActionsResource",
]

_SECURITY_1: Final[Security] = (("APIToken",),)

_ERRORS_1: Final[ErrorModels] = {
    "4XX": ErrorResponse,
    "5XX": ErrorResponse,
}

_CHECKS_1: Final[Mapping[str, Check]] = {
    "ttl": Check(minimum=60, maximum=2147483647),
}

_CHECKS_2: Final[Mapping[str, Check]] = {
    "records": Check(min_items=1, max_items=50),
}

_CHECKS_3: Final[Mapping[str, Check]] = {
    "ttl": Check(minimum=60, maximum=2147483647),
    "records": Check(min_items=1, max_items=50),
}


class ZoneRrsetActionsResource:
    """Operations on ``zone_rrset_actions`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def change_zone_rrset_protection(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        change: bool,
    ) -> ActionResponse:
        """Change an RRSet's Protection.

        Changes the protection of an RRSet in the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/change_protection``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
            change: Prevent the Resource from being changed.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "change": change,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_zone_rrset_ttl(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        ttl: int | None,
    ) -> ActionResponse:
        """Change an RRSet's TTL.

        Changes the Time To Live (TTL) of an RRSet in the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/change_ttl``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
            ttl: Time To Live (TTL) of the RRSet. Must be in between 60s and 2147483647s. If not
                set, the Zone's Default TTL is used.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, ttl=ttl)
        response = self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}/actions/change_ttl",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ttl": ttl,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def set_zone_rrset_records(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        records: Sequence[RecordParam],
    ) -> ActionResponse:
        """Set Records of an RRSet.

        Overwrites the resource records (RRs) of an existing RRSet in the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/set_records``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
            records: Records to set in the RRSet. Must not be empty and must only contain distinct
                record values.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, records=records)
        response = self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}/actions/set_records",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "records": records,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def add_zone_rrset_records(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        records: Sequence[RecordParam],
        ttl: int | NotGiven | None = NOT_GIVEN,
    ) -> ActionResponse:
        """Add Records to an RRSet.

        Adds resource records (RRs) to an RRSet in the Zone.

        For convenience, the RRSet will be automatically created if it doesn't exist. Otherwise, the
        new records are appended to the existing RRSet.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/add_records``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
            records: Records to add to the RRSet. Must not be empty and must only contain distinct
                record values.
            ttl: Time To Live (TTL) of the RRSet. If not set, the Zone's Default TTL is used. If
                set, and the RRSet being updated already has a TTL, the values must be the same.
                Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, ttl=ttl, records=records)
        response = self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}/actions/add_records",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ttl": ttl,
                    "records": records,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def remove_zone_rrset_records(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        records: Sequence[RecordParam],
    ) -> ActionResponse:
        """Remove Records from an RRSet.

        Removes resource records (RRs) from an existing RRSet in the Zone.

        For convenience, the RRSet will be automatically deleted if it doesn't contain any RRs
        afterwards.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/remove_records``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
            records: Records to set in the RRSet. Must not be empty and must only contain distinct
                record values.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, records=records)
        response = self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}/actions/remove_records",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "records": records,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def update_zone_rrset_records(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        records: Sequence[UpdateZoneRrsetRecordsRecordParam],
    ) -> ActionResponse:
        """Update Records of an RRSet.

        Updates resource records' (RRs) comments of an existing RRSet in the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/update_records``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
            records: Records to update in the RRSet. Must not be empty and must only contain
                distinct record values.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, records=records)
        response = self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}/actions/update_records",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "records": records,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)


class AsyncZoneRrsetActionsResource:
    """Operations on ``zone_rrset_actions`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def change_zone_rrset_protection(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        change: bool,
    ) -> ActionResponse:
        """Change an RRSet's Protection.

        Changes the protection of an RRSet in the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/change_protection``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
            change: Prevent the Resource from being changed.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        response = await self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "change": change,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_zone_rrset_ttl(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        ttl: int | None,
    ) -> ActionResponse:
        """Change an RRSet's TTL.

        Changes the Time To Live (TTL) of an RRSet in the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/change_ttl``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
            ttl: Time To Live (TTL) of the RRSet. Must be in between 60s and 2147483647s. If not
                set, the Zone's Default TTL is used.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, ttl=ttl)
        response = await self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}/actions/change_ttl",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ttl": ttl,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def set_zone_rrset_records(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        records: Sequence[RecordParam],
    ) -> ActionResponse:
        """Set Records of an RRSet.

        Overwrites the resource records (RRs) of an existing RRSet in the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/set_records``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
            records: Records to set in the RRSet. Must not be empty and must only contain distinct
                record values.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, records=records)
        response = await self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}/actions/set_records",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "records": records,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def add_zone_rrset_records(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        records: Sequence[RecordParam],
        ttl: int | NotGiven | None = NOT_GIVEN,
    ) -> ActionResponse:
        """Add Records to an RRSet.

        Adds resource records (RRs) to an RRSet in the Zone.

        For convenience, the RRSet will be automatically created if it doesn't exist. Otherwise, the
        new records are appended to the existing RRSet.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/add_records``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
            records: Records to add to the RRSet. Must not be empty and must only contain distinct
                record values.
            ttl: Time To Live (TTL) of the RRSet. If not set, the Zone's Default TTL is used. If
                set, and the RRSet being updated already has a TTL, the values must be the same.
                Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, ttl=ttl, records=records)
        response = await self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}/actions/add_records",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ttl": ttl,
                    "records": records,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def remove_zone_rrset_records(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        records: Sequence[RecordParam],
    ) -> ActionResponse:
        """Remove Records from an RRSet.

        Removes resource records (RRs) from an existing RRSet in the Zone.

        For convenience, the RRSet will be automatically deleted if it doesn't contain any RRs
        afterwards.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/remove_records``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
            records: Records to set in the RRSet. Must not be empty and must only contain distinct
                record values.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, records=records)
        response = await self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}/actions/remove_records",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "records": records,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def update_zone_rrset_records(
        self,
        id_or_name: str,
        rr_name: str,
        rr_type: RRSetType | UnknownValue,
        /,
        *,
        records: Sequence[UpdateZoneRrsetRecordsRecordParam],
    ) -> ActionResponse:
        """Update Records of an RRSet.

        Updates resource records' (RRs) comments of an existing RRSet in the Zone.

        Only applicable for Zones in primary mode.

        **Operation specific errors**

        - `422` - `incorrect_zone_mode` - This operation is not supported for this Zone's `mode`.

        ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/update_records``

        Args:
            id_or_name: ID or Name of the Zone.
            rr_name: ``rr_name``.
            rr_type: ``rr_type``.
            records: Records to update in the RRSet. Must not be empty and must only contain
                distinct record values.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, records=records)
        response = await self._transport.request(
            "POST",
            f"/zones/{encode_path(id_or_name)}/rrsets/{encode_path(rr_name)}/{encode_path(rr_type)}/actions/update_records",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "records": records,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)
