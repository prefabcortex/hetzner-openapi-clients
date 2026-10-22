"""Resource ``load_balancers`` (generated - do not edit by hand)."""

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
    CreateLoadBalancerResponse,
    ErrorResponse,
    GetLoadBalancerMetricsType,
    ListLoadBalancersResponse,
    LoadBalancerResponse,
    MetricsResponse,
    SortByIdNameCreated,
)
from hetzner_api.params import (
    CreateLoadBalancerRequestServiceParam,
    CreateLoadBalancerRequestTargetParam,
    LoadBalancerAlgorithmParam,
    LoadBalancerCreatePublicNetParam,
)
from hetzner_api.rules import (
    CREATE_LOAD_BALANCER_REQUEST_TARGET_FIELDS,
    LABELS_RULES,
    LOAD_BALANCER_CREATE_PUBLIC_NET_FIELDS,
)

__all__ = [
    "AsyncLoadBalancersResource",
    "LoadBalancersResource",
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
    "name": Check(min_length=1, max_length=128, pattern="^\\S(.*\\S)?$"),
    "targets": Check(items=Check(fields_of=lambda: CREATE_LOAD_BALANCER_REQUEST_TARGET_FIELDS)),
    "labels": LABELS_RULES,
    "public_net": Check(fields_of=lambda: LOAD_BALANCER_CREATE_PUBLIC_NET_FIELDS),
}

_CHECKS_3: Final[Mapping[str, Check]] = {
    "load_balancer_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "load_balancer_id": Check(minimum=1, maximum=9007199254740991),
    "name": Check(min_length=1, max_length=128, pattern="^\\S(.*\\S)?$"),
    "labels": LABELS_RULES,
}


class LoadBalancersResource:
    """Operations on ``load_balancers`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_load_balancers(
        self,
        *,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListLoadBalancersResponse:
        """List Load Balancers.

        Gets all existing Load Balancers that you have available.

        ``GET /load_balancers``

        Args:
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
            "/load_balancers",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "name": name,
                    "label_selector": label_selector,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListLoadBalancersResponse, response)

    def create_load_balancer(
        self,
        *,
        name: str,
        load_balancer_type: str | int,
        algorithm: LoadBalancerAlgorithmParam | NotGiven = NOT_GIVEN,
        services: Sequence[CreateLoadBalancerRequestServiceParam] | NotGiven = NOT_GIVEN,
        targets: Sequence[CreateLoadBalancerRequestTargetParam] | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        public_interface: bool | NotGiven = NOT_GIVEN,
        public_net: LoadBalancerCreatePublicNetParam | NotGiven = NOT_GIVEN,
        network: int | NotGiven = NOT_GIVEN,
        network_zone: str | NotGiven = NOT_GIVEN,
        location: str | int | NotGiven = NOT_GIVEN,
    ) -> CreateLoadBalancerResponse:
        """Create a Load Balancer.

        Creates a Load Balancer.

        **Operation specific errors**

        - `412` - `source_port_already_used` - The source port you are trying to add is already in
          use
        - `412` - `primary_ip_version_mismatch` - The specified Primary IP has the wrong IP version
        - `422` - `ip_not_owned` - The IP is not owned by the owner of the project of the Load
          Balancer
        - `422` - `load_balancer_not_attached_to_network` - The Load Balancer is not attached to a
          network
        - `422` - `resolve_cloud_private_targets_error` - The server you are trying to add as a
          target is not attached to the same network as the Load Balancer
        - `422` - `resolve_cloud_public_targets_error` - The server that you are trying to add as a
          public target does not have a public IPv4 address
        - `422` - `target_already_defined` - The Load Balancer target you are trying to define is
          already defined
        - `422` - `primary_ip_assigned` - The specified Primary IP is already assigned to a resource
        - `422` - `primary_ip_blocked` - The specified Primary IP is blocked
        - `422` - `primary_ip_location_mismatch` - The specified Primary IP is bound to a different
          Location than the Load Balancer

        ``POST /load_balancers``

        Args:
            name: Name of the Load Balancer.
            load_balancer_type: ID or name of the Load Balancer type this Load Balancer should be
                created with.
            algorithm: Algorithm of the Load Balancer. Omitted if not given. The API default is
                ``{"type": "round_robin"}``.
            services: Array of services. Omitted if not given.
            targets: Array of targets. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            public_interface: Enable or disable the public interface of the Load Balancer. Omitted
                if not given.
            public_net: Public network options of the Load Balancer. Only allowed if the public
                interface is enabled. Omitted if not given.
            network: ID of the network the Load Balancer should be attached to on creation. Omitted
                if not given.
            network_zone: Name of network zone. Omitted if not given.
            location: ID or name of Location to create Load Balancer in. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_2,
            name=name,
            targets=targets,
            labels=labels,
            public_net=public_net,
        )
        response = self._transport.request(
            "POST",
            "/load_balancers",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "load_balancer_type": load_balancer_type,
                    "algorithm": algorithm,
                    "services": services,
                    "targets": targets,
                    "labels": labels,
                    "public_interface": public_interface,
                    "public_net": public_net,
                    "network": network,
                    "network_zone": network_zone,
                    "location": location,
                },
            ),
        )
        return self._transport.parse(CreateLoadBalancerResponse, response)

    def get_load_balancer(self, load_balancer_id: int, /) -> LoadBalancerResponse:
        """Get a Load Balancer.

        Gets a specific Load Balancer object.

        ``GET /load_balancers/{id}``

        Args:
            load_balancer_id: ID of the Load Balancer.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, load_balancer_id=load_balancer_id)
        response = self._transport.request(
            "GET",
            f"/load_balancers/{encode_path(load_balancer_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(LoadBalancerResponse, response)

    def update_load_balancer(
        self,
        load_balancer_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerResponse:
        """Update a Load Balancer.

        Updates a Load Balancer. You can update a Load Balancer's name and a Load Balancer's labels.

        Note: if the Load Balancer object changes during the request, the response will be a
        "conflict" error.

        ``PUT /load_balancers/{id}``

        Args:
            load_balancer_id: ID of the Load Balancer.
            name: New Load Balancer name. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_4,
            load_balancer_id=load_balancer_id,
            name=name,
            labels=labels,
        )
        response = self._transport.request(
            "PUT",
            f"/load_balancers/{encode_path(load_balancer_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(LoadBalancerResponse, response)

    def delete_load_balancer(self, load_balancer_id: int, /) -> ActionResponse:
        """Delete a Load Balancer.

        Deletes a Load Balancer.

        ``DELETE /load_balancers/{id}``

        Args:
            load_balancer_id: ID of the Load Balancer.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, load_balancer_id=load_balancer_id)
        response = self._transport.request(
            "DELETE",
            f"/load_balancers/{encode_path(load_balancer_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def get_load_balancer_metrics(
        self,
        load_balancer_id: int,
        /,
        *,
        type: Sequence[GetLoadBalancerMetricsType | UnknownValue],
        start: str,
        end: str,
        step: str | None = None,
    ) -> MetricsResponse:
        """Get Metrics for a LoadBalancer.

        You must specify the type of metric to get: `open_connections`, `connections_per_second`,
        `requests_per_second` or `bandwidth`. You can also specify more than one type by comma
        separation, e.g. `requests_per_second,bandwidth`.

        Depending on the type you will get different time series data:

        - open_connections - open_connections - number - Open connections
        - connections_per_second - connections_per_second - connections/s - Connections per second
        - requests_per_second - requests_per_second - requests/s - Requests per second
        - bandwidth - bandwidth.in - bytes/s - Ingress bandwidth
        - bandwidth.out - bytes/s - Egress bandwidth

        Metrics are available for the last 30 days only.

        If you do not provide the step argument we will automatically adjust it so that 200 samples
        are returned.

        We limit the number of samples to a maximum of 500 and will adjust the step parameter
        accordingly.

        ``GET /load_balancers/{id}/metrics``

        Args:
            load_balancer_id: ID of the Load Balancer.
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
        self._transport.validate(_CHECKS_3, load_balancer_id=load_balancer_id)
        response = self._transport.request(
            "GET",
            f"/load_balancers/{encode_path(load_balancer_id)}/metrics",
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


class AsyncLoadBalancersResource:
    """Operations on ``load_balancers`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_load_balancers(
        self,
        *,
        sort: Sequence[SortByIdNameCreated | UnknownValue] | None = None,
        name: str | None = None,
        label_selector: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ListLoadBalancersResponse:
        """List Load Balancers.

        Gets all existing Load Balancers that you have available.

        ``GET /load_balancers``

        Args:
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
            "/load_balancers",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "name": name,
                    "label_selector": label_selector,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ListLoadBalancersResponse, response)

    async def create_load_balancer(
        self,
        *,
        name: str,
        load_balancer_type: str | int,
        algorithm: LoadBalancerAlgorithmParam | NotGiven = NOT_GIVEN,
        services: Sequence[CreateLoadBalancerRequestServiceParam] | NotGiven = NOT_GIVEN,
        targets: Sequence[CreateLoadBalancerRequestTargetParam] | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
        public_interface: bool | NotGiven = NOT_GIVEN,
        public_net: LoadBalancerCreatePublicNetParam | NotGiven = NOT_GIVEN,
        network: int | NotGiven = NOT_GIVEN,
        network_zone: str | NotGiven = NOT_GIVEN,
        location: str | int | NotGiven = NOT_GIVEN,
    ) -> CreateLoadBalancerResponse:
        """Create a Load Balancer.

        Creates a Load Balancer.

        **Operation specific errors**

        - `412` - `source_port_already_used` - The source port you are trying to add is already in
          use
        - `412` - `primary_ip_version_mismatch` - The specified Primary IP has the wrong IP version
        - `422` - `ip_not_owned` - The IP is not owned by the owner of the project of the Load
          Balancer
        - `422` - `load_balancer_not_attached_to_network` - The Load Balancer is not attached to a
          network
        - `422` - `resolve_cloud_private_targets_error` - The server you are trying to add as a
          target is not attached to the same network as the Load Balancer
        - `422` - `resolve_cloud_public_targets_error` - The server that you are trying to add as a
          public target does not have a public IPv4 address
        - `422` - `target_already_defined` - The Load Balancer target you are trying to define is
          already defined
        - `422` - `primary_ip_assigned` - The specified Primary IP is already assigned to a resource
        - `422` - `primary_ip_blocked` - The specified Primary IP is blocked
        - `422` - `primary_ip_location_mismatch` - The specified Primary IP is bound to a different
          Location than the Load Balancer

        ``POST /load_balancers``

        Args:
            name: Name of the Load Balancer.
            load_balancer_type: ID or name of the Load Balancer type this Load Balancer should be
                created with.
            algorithm: Algorithm of the Load Balancer. Omitted if not given. The API default is
                ``{"type": "round_robin"}``.
            services: Array of services. Omitted if not given.
            targets: Array of targets. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.
            public_interface: Enable or disable the public interface of the Load Balancer. Omitted
                if not given.
            public_net: Public network options of the Load Balancer. Only allowed if the public
                interface is enabled. Omitted if not given.
            network: ID of the network the Load Balancer should be attached to on creation. Omitted
                if not given.
            network_zone: Name of network zone. Omitted if not given.
            location: ID or name of Location to create Load Balancer in. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_2,
            name=name,
            targets=targets,
            labels=labels,
            public_net=public_net,
        )
        response = await self._transport.request(
            "POST",
            "/load_balancers",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "load_balancer_type": load_balancer_type,
                    "algorithm": algorithm,
                    "services": services,
                    "targets": targets,
                    "labels": labels,
                    "public_interface": public_interface,
                    "public_net": public_net,
                    "network": network,
                    "network_zone": network_zone,
                    "location": location,
                },
            ),
        )
        return self._transport.parse(CreateLoadBalancerResponse, response)

    async def get_load_balancer(self, load_balancer_id: int, /) -> LoadBalancerResponse:
        """Get a Load Balancer.

        Gets a specific Load Balancer object.

        ``GET /load_balancers/{id}``

        Args:
            load_balancer_id: ID of the Load Balancer.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, load_balancer_id=load_balancer_id)
        response = await self._transport.request(
            "GET",
            f"/load_balancers/{encode_path(load_balancer_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(LoadBalancerResponse, response)

    async def update_load_balancer(
        self,
        load_balancer_id: int,
        /,
        *,
        name: str | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> LoadBalancerResponse:
        """Update a Load Balancer.

        Updates a Load Balancer. You can update a Load Balancer's name and a Load Balancer's labels.

        Note: if the Load Balancer object changes during the request, the response will be a
        "conflict" error.

        ``PUT /load_balancers/{id}``

        Args:
            load_balancer_id: ID of the Load Balancer.
            name: New Load Balancer name. Omitted if not given.
            labels: User-defined labels (`key/value` pairs) for the Resource. Note that the set of
                Labels provided in the request will overwrite the existing one. For more
                information, see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_4,
            load_balancer_id=load_balancer_id,
            name=name,
            labels=labels,
        )
        response = await self._transport.request(
            "PUT",
            f"/load_balancers/{encode_path(load_balancer_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "name": name,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(LoadBalancerResponse, response)

    async def delete_load_balancer(self, load_balancer_id: int, /) -> ActionResponse:
        """Delete a Load Balancer.

        Deletes a Load Balancer.

        ``DELETE /load_balancers/{id}``

        Args:
            load_balancer_id: ID of the Load Balancer.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, load_balancer_id=load_balancer_id)
        response = await self._transport.request(
            "DELETE",
            f"/load_balancers/{encode_path(load_balancer_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def get_load_balancer_metrics(
        self,
        load_balancer_id: int,
        /,
        *,
        type: Sequence[GetLoadBalancerMetricsType | UnknownValue],
        start: str,
        end: str,
        step: str | None = None,
    ) -> MetricsResponse:
        """Get Metrics for a LoadBalancer.

        You must specify the type of metric to get: `open_connections`, `connections_per_second`,
        `requests_per_second` or `bandwidth`. You can also specify more than one type by comma
        separation, e.g. `requests_per_second,bandwidth`.

        Depending on the type you will get different time series data:

        - open_connections - open_connections - number - Open connections
        - connections_per_second - connections_per_second - connections/s - Connections per second
        - requests_per_second - requests_per_second - requests/s - Requests per second
        - bandwidth - bandwidth.in - bytes/s - Ingress bandwidth
        - bandwidth.out - bytes/s - Egress bandwidth

        Metrics are available for the last 30 days only.

        If you do not provide the step argument we will automatically adjust it so that 200 samples
        are returned.

        We limit the number of samples to a maximum of 500 and will adjust the step parameter
        accordingly.

        ``GET /load_balancers/{id}/metrics``

        Args:
            load_balancer_id: ID of the Load Balancer.
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
        self._transport.validate(_CHECKS_3, load_balancer_id=load_balancer_id)
        response = await self._transport.request(
            "GET",
            f"/load_balancers/{encode_path(load_balancer_id)}/metrics",
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
