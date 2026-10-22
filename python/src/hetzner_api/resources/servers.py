"""Resource ``servers`` (generated - do not edit by hand)."""

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
    CreateServerResponse,
    ErrorResponse,
    GetServerMetricsType,
    ListServersResponse,
    MetricsResponse,
    ServerResponse,
    ServerStatus,
    SortByIdNameCreated,
)
from hetzner_api.params import CreateServerRequestFirewallParam, CreateServerRequestPublicNetParam
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncServersResource",
    "ServersResource",
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
    "server_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "server_id": Check(minimum=1, maximum=9007199254740991),
    "labels": LABELS_RULES,
}


class ServersResource:
    """Operations on ``servers`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_servers(
        self,
        *,
        name: str | None = None,
        label_selector: str | None = None,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        status: Sequence[ServerStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListServersResponse:
        """List Servers.

        Returns all existing Server objects.

        ``GET /servers``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            status: Filter resources by status. May be used multiple times. The response will only
                contain the resources with the specified status.
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
            "/servers",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "label_selector": label_selector,
                    "sort": sort,
                    "status": status,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListServersResponse, response)

    def create_server(
        self,
        *,
        name: str,
        server_type: str | int,
        image: str | int,
        location: str | int | NotGiven = NOT_GIVEN,
        start_after_create: bool | NotGiven = NOT_GIVEN,
        placement_group: int | NotGiven = NOT_GIVEN,
        ssh_keys: Sequence[str | int] | NotGiven = NOT_GIVEN,
        volumes: Sequence[int] | NotGiven = NOT_GIVEN,
        networks: Sequence[int] | NotGiven = NOT_GIVEN,
        firewalls: Sequence[CreateServerRequestFirewallParam] | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        automount: bool | NotGiven = NOT_GIVEN,
        public_net: CreateServerRequestPublicNetParam | NotGiven = NOT_GIVEN,
    ) -> CreateServerResponse:
        """Create a Server.

        Creates a new Server. Returns preliminary information about the Server as well as an Action
        that covers progress of creation.

        **Operation specific errors**

        - `412` - `primary_ip_version_mismatch` - The specified Primary IP has the wrong IP Version
        - `422` - `placement_error` - An error during the placement occurred
        - `422` - `primary_ip_assigned` - The specified Primary IP is already assigned to a server
        - `422` - `primary_ip_datacenter_mismatch` - The specified Primary IP is in a different
          location

        ``POST /servers``

        Args:
            name: Name of the Server to create (must be unique per Project and a valid hostname as
                per RFC 1123).
            server_type: ID or name of the Server type this Server should be created with.
            image: ID or name of the Image the Server is created from.
            location: ID or name of the Location to create the Server in. Omitted if not given.
            start_after_create: This automatically triggers a Power on a Server-Server Action after
                the creation is finished and is returned in the `next_actions` response object.
                Omitted if not given. The API default is ``True``.
            placement_group: ID of the Placement Group the Server should be in. Omitted if not
                given.
            ssh_keys: SSH key IDs (`integer`) or names (`string`) which should be injected into the
                Server at creation time. Omitted if not given.
            volumes: Volume IDs which should be attached to the Server at the creation time. Volumes
                must be in the same Location. Omitted if not given.
            networks: Network IDs which should be attached to the Server private network interface
                at the creation time. Omitted if not given.
            firewalls: Firewalls which should be applied on the Server's public network interface at
                creation time. Omitted if not given.
            user_data: Cloud-Init user data to use during Server creation. This field is limited to
                32KiB. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            automount: Auto-mount Volumes after attach. Omitted if not given.
            public_net: Public Network options. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, labels=labels)
        response = self._transport.request(
            "POST",
            "/servers",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "location": location,
                    "server_type": server_type,
                    "start_after_create": start_after_create,
                    "image": image,
                    "placement_group": placement_group,
                    "ssh_keys": ssh_keys,
                    "volumes": volumes,
                    "networks": networks,
                    "firewalls": firewalls,
                    "user_data": user_data,
                    "labels": labels,
                    "automount": automount,
                    "public_net": public_net,
                },
            ),
        )
        return self._transport.parse(CreateServerResponse, response)

    def get_server(self, server_id: int, /) -> ServerResponse:
        """Get a Server.

        Returns a specific Server object. The Server must exist inside the Project.

        ``GET /servers/{id}``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, server_id=server_id)
        response = self._transport.request(
            "GET",
            f"/servers/{encode_path(server_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ServerResponse, response)

    def update_server(
        self,
        server_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> ServerResponse:
        """Update a Server.

        Updates a Server. You can update a Server's name and a Server's labels.

        Please note that Server names must be unique per Project and valid hostnames as per RFC 1123
        (i.e. may only contain letters, digits, periods, and dashes).

        ``PUT /servers/{id}``

        Args:
            server_id: ID of the Server.
            name: New name to set. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id, labels=labels)
        response = self._transport.request(
            "PUT",
            f"/servers/{encode_path(server_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(ServerResponse, response)

    def delete_server(self, server_id: int, /) -> ActionResponse:
        """Delete a Server.

        Deletes a Server.

        This immediately removes the Server from your account, and it is no longer accessible. Any
        resources attached to the server (like Volumes, Primary IPs, Floating IPs, Firewalls,
        Placement Groups) are detached while the server is deleted.

        ``DELETE /servers/{id}``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, server_id=server_id)
        response = self._transport.request(
            "DELETE",
            f"/servers/{encode_path(server_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def get_server_metrics(
        self,
        server_id: int,
        /,
        *,
        type: Sequence[GetServerMetricsType | UnknownValue],
        start: str,
        end: str,
        step: str | None = None,
    ) -> MetricsResponse:
        """Get Metrics for a Server.

        Get Metrics for specified Server.

        You must specify the type of metric to get: cpu, disk or network. You can also specify more
        than one type by comma separation, e.g. cpu,disk.

        Depending on the type you will get different time series data

        - cpu - cpu - percent - Percent CPU usage
        - disk - disk.0.iops.read - iop/s - Number of read IO operations per second
        - disk.0.iops.write - iop/s - Number of write IO operations per second
        - disk.0.bandwidth.read - bytes/s - Bytes read per second
        - disk.0.bandwidth.write - bytes/s - Bytes written per second
        - network - network.0.pps.in - packets/s - Public Network interface packets per second
          received
        - network.0.pps.out - packets/s - Public Network interface packets per second sent
        - network.0.bandwidth.in - bytes/s - Public Network interface bytes/s received
        - network.0.bandwidth.out - bytes/s - Public Network interface bytes/s sent

        Note that the CPU value is not normalized to a fixed 0-100% scale. It is calculated per
        vCPU: a value of 100 represents full utilization on a 1-vCPU server, and 25% utilization on
        a 4-vCPU server. To calculate the overall CPU usage, divide the metric value by the number
        of vCPUs.

        Metrics are available for the last 30 days only.

        If you do not provide the step argument we will automatically adjust it so that a maximum of
        200 samples are returned.

        We limit the number of samples returned to a maximum of 500 and will adjust the step
        parameter accordingly.

        ``GET /servers/{id}/metrics``

        Args:
            server_id: ID of the Server.
            type: Type of metrics to get.
            start: Start of period to get Metrics for (must be in RFC3339
                (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
            end: End of period to get Metrics for (must be in RFC3339
                (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
            step: Resolution of results in seconds.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, server_id=server_id)
        response = self._transport.request(
            "GET",
            f"/servers/{encode_path(server_id)}/metrics",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "type": type,
                    "start": start,
                    "end": end,
                    "step": step,
                },
            ),
        )
        return self._transport.parse(MetricsResponse, response)


class AsyncServersResource:
    """Operations on ``servers`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_servers(
        self,
        *,
        name: str | None = None,
        label_selector: str | None = None,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        status: Sequence[ServerStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListServersResponse:
        """List Servers.

        Returns all existing Server objects.

        ``GET /servers``

        Args:
            name: Filter resources by their name. The response will only contain the resources
                matching exactly the specified name.
            label_selector: Filter resources by labels. The response will only contain resources
                matching the label selector. For more information, see "Label Selector".
            sort: Sort resources by field and direction. May be used multiple times. For more
                information, see "Sorting".
            status: Filter resources by status. May be used multiple times. The response will only
                contain the resources with the specified status.
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
            "/servers",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "name": name,
                    "label_selector": label_selector,
                    "sort": sort,
                    "status": status,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListServersResponse, response)

    async def create_server(
        self,
        *,
        name: str,
        server_type: str | int,
        image: str | int,
        location: str | int | NotGiven = NOT_GIVEN,
        start_after_create: bool | NotGiven = NOT_GIVEN,
        placement_group: int | NotGiven = NOT_GIVEN,
        ssh_keys: Sequence[str | int] | NotGiven = NOT_GIVEN,
        volumes: Sequence[int] | NotGiven = NOT_GIVEN,
        networks: Sequence[int] | NotGiven = NOT_GIVEN,
        firewalls: Sequence[CreateServerRequestFirewallParam] | NotGiven = NOT_GIVEN,
        user_data: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        automount: bool | NotGiven = NOT_GIVEN,
        public_net: CreateServerRequestPublicNetParam | NotGiven = NOT_GIVEN,
    ) -> CreateServerResponse:
        """Create a Server.

        Creates a new Server. Returns preliminary information about the Server as well as an Action
        that covers progress of creation.

        **Operation specific errors**

        - `412` - `primary_ip_version_mismatch` - The specified Primary IP has the wrong IP Version
        - `422` - `placement_error` - An error during the placement occurred
        - `422` - `primary_ip_assigned` - The specified Primary IP is already assigned to a server
        - `422` - `primary_ip_datacenter_mismatch` - The specified Primary IP is in a different
          location

        ``POST /servers``

        Args:
            name: Name of the Server to create (must be unique per Project and a valid hostname as
                per RFC 1123).
            server_type: ID or name of the Server type this Server should be created with.
            image: ID or name of the Image the Server is created from.
            location: ID or name of the Location to create the Server in. Omitted if not given.
            start_after_create: This automatically triggers a Power on a Server-Server Action after
                the creation is finished and is returned in the `next_actions` response object.
                Omitted if not given. The API default is ``True``.
            placement_group: ID of the Placement Group the Server should be in. Omitted if not
                given.
            ssh_keys: SSH key IDs (`integer`) or names (`string`) which should be injected into the
                Server at creation time. Omitted if not given.
            volumes: Volume IDs which should be attached to the Server at the creation time. Volumes
                must be in the same Location. Omitted if not given.
            networks: Network IDs which should be attached to the Server private network interface
                at the creation time. Omitted if not given.
            firewalls: Firewalls which should be applied on the Server's public network interface at
                creation time. Omitted if not given.
            user_data: Cloud-Init user data to use during Server creation. This field is limited to
                32KiB. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            automount: Auto-mount Volumes after attach. Omitted if not given.
            public_net: Public Network options. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, labels=labels)
        response = await self._transport.request(
            "POST",
            "/servers",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "location": location,
                    "server_type": server_type,
                    "start_after_create": start_after_create,
                    "image": image,
                    "placement_group": placement_group,
                    "ssh_keys": ssh_keys,
                    "volumes": volumes,
                    "networks": networks,
                    "firewalls": firewalls,
                    "user_data": user_data,
                    "labels": labels,
                    "automount": automount,
                    "public_net": public_net,
                },
            ),
        )
        return self._transport.parse(CreateServerResponse, response)

    async def get_server(self, server_id: int, /) -> ServerResponse:
        """Get a Server.

        Returns a specific Server object. The Server must exist inside the Project.

        ``GET /servers/{id}``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, server_id=server_id)
        response = await self._transport.request(
            "GET",
            f"/servers/{encode_path(server_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ServerResponse, response)

    async def update_server(
        self,
        server_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> ServerResponse:
        """Update a Server.

        Updates a Server. You can update a Server's name and a Server's labels.

        Please note that Server names must be unique per Project and valid hostnames as per RFC 1123
        (i.e. may only contain letters, digits, periods, and dashes).

        ``PUT /servers/{id}``

        Args:
            server_id: ID of the Server.
            name: New name to set. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id, labels=labels)
        response = await self._transport.request(
            "PUT",
            f"/servers/{encode_path(server_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(ServerResponse, response)

    async def delete_server(self, server_id: int, /) -> ActionResponse:
        """Delete a Server.

        Deletes a Server.

        This immediately removes the Server from your account, and it is no longer accessible. Any
        resources attached to the server (like Volumes, Primary IPs, Floating IPs, Firewalls,
        Placement Groups) are detached while the server is deleted.

        ``DELETE /servers/{id}``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, server_id=server_id)
        response = await self._transport.request(
            "DELETE",
            f"/servers/{encode_path(server_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def get_server_metrics(
        self,
        server_id: int,
        /,
        *,
        type: Sequence[GetServerMetricsType | UnknownValue],
        start: str,
        end: str,
        step: str | None = None,
    ) -> MetricsResponse:
        """Get Metrics for a Server.

        Get Metrics for specified Server.

        You must specify the type of metric to get: cpu, disk or network. You can also specify more
        than one type by comma separation, e.g. cpu,disk.

        Depending on the type you will get different time series data

        - cpu - cpu - percent - Percent CPU usage
        - disk - disk.0.iops.read - iop/s - Number of read IO operations per second
        - disk.0.iops.write - iop/s - Number of write IO operations per second
        - disk.0.bandwidth.read - bytes/s - Bytes read per second
        - disk.0.bandwidth.write - bytes/s - Bytes written per second
        - network - network.0.pps.in - packets/s - Public Network interface packets per second
          received
        - network.0.pps.out - packets/s - Public Network interface packets per second sent
        - network.0.bandwidth.in - bytes/s - Public Network interface bytes/s received
        - network.0.bandwidth.out - bytes/s - Public Network interface bytes/s sent

        Note that the CPU value is not normalized to a fixed 0-100% scale. It is calculated per
        vCPU: a value of 100 represents full utilization on a 1-vCPU server, and 25% utilization on
        a 4-vCPU server. To calculate the overall CPU usage, divide the metric value by the number
        of vCPUs.

        Metrics are available for the last 30 days only.

        If you do not provide the step argument we will automatically adjust it so that a maximum of
        200 samples are returned.

        We limit the number of samples returned to a maximum of 500 and will adjust the step
        parameter accordingly.

        ``GET /servers/{id}/metrics``

        Args:
            server_id: ID of the Server.
            type: Type of metrics to get.
            start: Start of period to get Metrics for (must be in RFC3339
                (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
            end: End of period to get Metrics for (must be in RFC3339
                (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
            step: Resolution of results in seconds.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, server_id=server_id)
        response = await self._transport.request(
            "GET",
            f"/servers/{encode_path(server_id)}/metrics",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "type": type,
                    "start": start,
                    "end": end,
                    "step": step,
                },
            ),
        )
        return self._transport.parse(MetricsResponse, response)
