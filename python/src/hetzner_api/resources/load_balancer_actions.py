"""Resource ``load_balancer_actions`` (generated - do not edit by hand)."""

from collections.abc import Mapping, Sequence
from typing import Final
from warnings import deprecated

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
    ActionListResponseWithMeta,
    ActionResponse,
    ActionSort,
    ActionStatus,
    ErrorResponse,
    LoadBalancerAlgorithmType,
    LoadBalancerServiceProtocol,
    LoadBalancerTargetType,
)
from hetzner_api.params import (
    LoadBalancerServiceHealthCheck2Param,
    LoadBalancerServiceHTTPParam,
    LoadBalancerTargetIPParam,
    LoadBalancerTargetLabelSelectorParam,
    LoadBalancerTargetServerRequestParam,
    UpdateLoadBalancerServiceHealthCheckParam,
    UpdateLoadBalancerServiceHttpParam,
)
from hetzner_api.rules import (
    LOAD_BALANCER_SERVICE_HEALTH_CHECK2_FIELDS,
    LOAD_BALANCER_SERVICE_HTTP_FIELDS,
    LOAD_BALANCER_TARGET_LABEL_SELECTOR_FIELDS,
    UPDATE_LOAD_BALANCER_SERVICE_HEALTH_CHECK_FIELDS,
    UPDATE_LOAD_BALANCER_SERVICE_HTTP_FIELDS,
)

__all__ = [
    "AsyncLoadBalancerActionsResource",
    "LoadBalancerActionsResource",
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
    "load_balancer_id": Check(minimum=1, maximum=9007199254740991),
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "load_balancer_id": Check(minimum=1, maximum=9007199254740991),
    "health_check": Check(fields_of=lambda: LOAD_BALANCER_SERVICE_HEALTH_CHECK2_FIELDS),
    "http": Check(fields_of=lambda: LOAD_BALANCER_SERVICE_HTTP_FIELDS),
}

_CHECKS_5: Final[Mapping[str, Check]] = {
    "load_balancer_id": Check(minimum=1, maximum=9007199254740991),
    "label_selector": Check(fields_of=lambda: LOAD_BALANCER_TARGET_LABEL_SELECTOR_FIELDS),
}

_CHECKS_6: Final[Mapping[str, Check]] = {
    "load_balancer_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_7: Final[Mapping[str, Check]] = {
    "load_balancer_id": Check(minimum=1, maximum=9007199254740991),
    "health_check": Check(fields_of=lambda: UPDATE_LOAD_BALANCER_SERVICE_HEALTH_CHECK_FIELDS),
    "http": Check(fields_of=lambda: UPDATE_LOAD_BALANCER_SERVICE_HTTP_FIELDS),
}

_CHECKS_8: Final[Mapping[str, Check]] = {
    "load_balancer_id": Check(minimum=1, maximum=9007199254740991),
    "action_id": Check(minimum=1, maximum=9007199254740991),
}


class LoadBalancerActionsResource:
    """Operations on ``load_balancer_actions`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_load_balancers_actions(
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

        ``GET /load_balancers/actions``

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
            "/load_balancers/actions",
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

    def get_load_balancers_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action object.

        ``GET /load_balancers/actions/{id}``

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
            f"/load_balancers/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def list_load_balancer_actions(
        self,
        load_balancer_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Load Balancer.

        Returns all Action objects for a Load Balancer. You can sort the results by using the `sort`
        URI parameter, and filter them with the `status` parameter.

        ``GET /load_balancers/{id}/actions``

        Args:
            load_balancer_id: ID of the Load Balancer.
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
            load_balancer_id=load_balancer_id,
            page=page,
            per_page=per_page,
        )
        response = self._transport.request(
            "GET",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions",
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

    def add_load_balancer_service(
        self,
        load_balancer_id: int,
        /,
        *,
        protocol: LoadBalancerServiceProtocol | UnknownValue,
        listen_port: int,
        destination_port: int,
        proxyprotocol: bool,
        health_check: LoadBalancerServiceHealthCheck2Param,
        http: LoadBalancerServiceHTTPParam | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Add Service.

        Adds a service to a Load Balancer.

        **Operation specific errors**

        - `412` - `source_port_already_used` - The source port you are trying to add is already in
          use

        ``POST /load_balancers/{id}/actions/add_service``

        Args:
            load_balancer_id: ID of the Load Balancer.
            protocol: Protocol of the Load Balancer.
            listen_port: Port the Load Balancer listens on.
            destination_port: Port the Load Balancer will balance to.
            proxyprotocol: Is Proxyprotocol enabled or not.
            health_check: ``health_check``.
            http: Configuration option for protocols http and https. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_4,
            load_balancer_id=load_balancer_id,
            health_check=health_check,
            http=http,
        )
        response = self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/add_service",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "protocol": protocol,
                    "listen_port": listen_port,
                    "destination_port": destination_port,
                    "proxyprotocol": proxyprotocol,
                    "health_check": health_check,
                    "http": http,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def add_load_balancer_target(
        self,
        load_balancer_id: int,
        /,
        *,
        type: LoadBalancerTargetType | UnknownValue,
        server: LoadBalancerTargetServerRequestParam | NotGiven = NOT_GIVEN,
        label_selector: LoadBalancerTargetLabelSelectorParam | NotGiven = NOT_GIVEN,
        ip: LoadBalancerTargetIPParam | NotGiven = NOT_GIVEN,
        use_private_ip: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Add Target.

        Adds a target to a Load Balancer.

        **Operation specific errors**

        - `422` - `ip_not_in_vswitch_subnet` - The IP you are trying to add does not belong to the
          vswitch subnet of the attached network
        - `422` - `ip_not_owned` - The IP you are trying to add as a target is not owned by the
          Project owner
        - `422` - `ip_not_assigned_to_server` - The specified IP is neither the Primary IPv4 address
          nor in the IPv6 subnet of the given Server
        - `422` - `load_balancer_public_interface_disabled` - The Load Balancer's public network
          interface is disabled
        - `422` - `load_balancer_not_attached_to_network` - The Load Balancer is not attached to a
          network
        - `422` - `network_has_no_vswitch_subnet` - The given IP is private but attached network
          does not have a vswitch subnet
        - `422` - `resolve_cloud_private_targets_error` - The server you are trying to add as a
          target is not attached to the same network as the Load Balancer
        - `422` - `resolve_cloud_public_targets_error` - The server that you are trying to add as a
          public target does not have a public IPv4 address
        - `422` - `target_already_defined` - The Load Balancer target you are trying to define is
          already defined

        ``POST /load_balancers/{id}/actions/add_target``

        Args:
            load_balancer_id: ID of the Load Balancer.
            type: Type of the resource.
            server: Configuration for type Server, only valid and required if type is `server`.
                Omitted if not given.
            label_selector: Configuration for label selector targets, only valid and required if
                type is `label_selector`. Omitted if not given.
            ip: Configuration for an IP target. It is only possible to use the (Public or vSwitch)
                IPs of Hetzner Online Root Servers belonging to the project owner. IPs belonging to
                other users are blocked. Additionally IPs belonging to services provided by Hetzner
                Cloud (Servers, Load Balancers, ...) are blocked as well. Only valid and required if
                type is `ip`. Omitted if not given.
            use_private_ip: Use the private network IP instead of the public IP of the Server,
                requires the Server and Load Balancer to be in the same network. Only valid for
                target types `server` and `label_selector`. Omitted if not given. The API default is
                ``False``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_5,
            load_balancer_id=load_balancer_id,
            label_selector=label_selector,
        )
        response = self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/add_target",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "type": type,
                    "server": server,
                    "label_selector": label_selector,
                    "ip": ip,
                    "use_private_ip": use_private_ip,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def attach_load_balancer_to_network(
        self,
        load_balancer_id: int,
        /,
        *,
        network: int,
        ip: str | NotGiven = NOT_GIVEN,
        ip_range: str | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Attach a Load Balancer to a Network.

        ``POST /load_balancers/{id}/actions/attach_to_network``

        Args:
            load_balancer_id: ID of the Load Balancer.
            network: ID of an existing network to attach the Load Balancer to.
            ip: IP to request to be assigned to this Load Balancer; if you do not provide this then
                you will be auto assigned an IP address. Omitted if not given.
            ip_range: IP range in CIDR block notation of the subnet to attach to. This allows for
                auto assigning an IP address for a specific subnet. Providing `ip` that is not part
                of `ip_range` will result in an error. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/attach_to_network",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "network": network,
                    "ip": ip,
                    "ip_range": ip_range,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_load_balancer_algorithm(
        self,
        load_balancer_id: int,
        /,
        *,
        type: LoadBalancerAlgorithmType | UnknownValue,
    ) -> ActionResponse:
        """Change Algorithm.

        Change the algorithm that determines to which target new requests are sent.

        ``POST /load_balancers/{id}/actions/change_algorithm``

        Args:
            load_balancer_id: ID of the Load Balancer.
            type: Type of the algorithm.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/change_algorithm",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "type": type,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_load_balancer_dns_ptr(
        self,
        load_balancer_id: int,
        /,
        *,
        ip: str,
        dns_ptr: str | None,
    ) -> ActionResponse:
        """Change reverse DNS entry for this Load Balancer.

        Changes the hostname that will appear when getting the hostname belonging to the public IPs
        (IPv4 and IPv6) of this Load Balancer.

        Floating IPs assigned to the Server are not affected by this.

        ``POST /load_balancers/{id}/actions/change_dns_ptr``

        Args:
            load_balancer_id: ID of the Load Balancer.
            ip: Single IPv4 or IPv6 address to create pointer for.
            dns_ptr: Domain Name to point to. PTR record content used for reverse DNS. Set to null
                to reset (IPv4) to the default value or remove (IPv6) the record.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/change_dns_ptr",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ip": ip,
                    "dns_ptr": dns_ptr,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_load_balancer_protection(
        self,
        load_balancer_id: int,
        /,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Change Load Balancer Protection.

        Changes the protection configuration of a Load Balancer.

        ``POST /load_balancers/{id}/actions/change_protection``

        Args:
            load_balancer_id: ID of the Load Balancer.
            delete: If true, prevents the snapshot from being deleted. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_load_balancer_type(
        self,
        load_balancer_id: int,
        /,
        *,
        load_balancer_type: str | int,
    ) -> ActionResponse:
        """Change the Type of a Load Balancer.

        Changes the type (Max Services, Max Targets and Max Connections) of a Load Balancer.

        **Operation specific errors**

        - `422` - `invalid_load_balancer_type` - The Load Balancer type does not fit for the given
          Load Balancer

        ``POST /load_balancers/{id}/actions/change_type``

        Args:
            load_balancer_id: ID of the Load Balancer.
            load_balancer_type: ID or name of Load Balancer type the Load Balancer should migrate
                to.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/change_type",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "load_balancer_type": load_balancer_type,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def delete_load_balancer_service(
        self,
        load_balancer_id: int,
        /,
        *,
        listen_port: int,
    ) -> ActionResponse:
        """Delete Service.

        Delete a service of a Load Balancer.

        ``POST /load_balancers/{id}/actions/delete_service``

        Args:
            load_balancer_id: ID of the Load Balancer.
            listen_port: The listen port of the service you want to delete.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/delete_service",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "listen_port": listen_port,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def detach_load_balancer_from_network(
        self,
        load_balancer_id: int,
        /,
        *,
        network: int,
    ) -> ActionResponse:
        """Detach a Load Balancer from a Network.

        Detaches a Load Balancer from a network.

        ``POST /load_balancers/{id}/actions/detach_from_network``

        Args:
            load_balancer_id: ID of the Load Balancer.
            network: ID of an existing network to detach the Load Balancer from.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/detach_from_network",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "network": network,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def disable_load_balancer_public_interface(self, load_balancer_id: int, /) -> ActionResponse:
        """Disable the public interface of a Load Balancer.

        Disable the public interface of a Load Balancer. The Load Balancer will be not accessible
        from the internet via its public IPs.

        **Operation specific errors**

        - `422` - `load_balancer_not_attached_to_network` - The Load Balancer is not attached to a
          network
        - `422` - `targets_without_use_private_ip` - The Load Balancer has targets that use the
          public IP instead of the private IP

        ``POST /load_balancers/{id}/actions/disable_public_interface``

        Args:
            load_balancer_id: ID of the Load Balancer.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/disable_public_interface",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def enable_load_balancer_public_interface(self, load_balancer_id: int, /) -> ActionResponse:
        """Enable the public interface of a Load Balancer.

        Enable the public interface of a Load Balancer. The Load Balancer will be accessible from
        the internet via its public IPs.

        ``POST /load_balancers/{id}/actions/enable_public_interface``

        Args:
            load_balancer_id: ID of the Load Balancer.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/enable_public_interface",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def remove_load_balancer_target(
        self,
        load_balancer_id: int,
        /,
        *,
        type: LoadBalancerTargetType | UnknownValue,
        server: LoadBalancerTargetServerRequestParam | NotGiven = NOT_GIVEN,
        label_selector: LoadBalancerTargetLabelSelectorParam | NotGiven = NOT_GIVEN,
        ip: LoadBalancerTargetIPParam | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Remove Target.

        Removes a target from a Load Balancer.

        ``POST /load_balancers/{id}/actions/remove_target``

        Args:
            load_balancer_id: ID of the Load Balancer.
            type: Type of the resource.
            server: Configuration for type Server, only valid and required if type is `server`.
                Omitted if not given.
            label_selector: Configuration for label selector targets, only valid and required if
                type is `label_selector`. Omitted if not given.
            ip: Configuration for an IP target. It is only possible to use the (Public or vSwitch)
                IPs of Hetzner Online Root Servers belonging to the project owner. IPs belonging to
                other users are blocked. Additionally IPs belonging to services provided by Hetzner
                Cloud (Servers, Load Balancers, ...) are blocked as well. Only valid and required if
                type is `ip`. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_5,
            load_balancer_id=load_balancer_id,
            label_selector=label_selector,
        )
        response = self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/remove_target",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "type": type,
                    "server": server,
                    "label_selector": label_selector,
                    "ip": ip,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def update_load_balancer_service(
        self,
        load_balancer_id: int,
        /,
        *,
        listen_port: int,
        protocol: LoadBalancerServiceProtocol | UnknownValue | NotGiven = NOT_GIVEN,
        destination_port: int | NotGiven = NOT_GIVEN,
        proxyprotocol: bool | NotGiven = NOT_GIVEN,
        health_check: UpdateLoadBalancerServiceHealthCheckParam | NotGiven = NOT_GIVEN,
        http: UpdateLoadBalancerServiceHttpParam | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Update Service.

        Updates a Load Balancer Service.

        **Operation specific errors**

        - `422` - `source_port_already_used` - The source port you are trying to add is already in
          use

        ``POST /load_balancers/{id}/actions/update_service``

        Args:
            load_balancer_id: ID of the Load Balancer.
            listen_port: Port the Load Balancer listens on.
            protocol: Protocol of the Load Balancer. Omitted if not given.
            destination_port: Port the Load Balancer will balance to. Omitted if not given.
            proxyprotocol: Is Proxyprotocol enabled or not. Omitted if not given.
            health_check: Service health check. Omitted if not given.
            http: Configuration option for protocols http and https. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_7,
            load_balancer_id=load_balancer_id,
            health_check=health_check,
            http=http,
        )
        response = self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/update_service",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "protocol": protocol,
                    "listen_port": listen_port,
                    "destination_port": destination_port,
                    "proxyprotocol": proxyprotocol,
                    "health_check": health_check,
                    "http": http,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    @deprecated("GET /load_balancers/{id}/actions/{action_id} is deprecated by the API")
    def get_load_balancer_action(self, load_balancer_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Load Balancer.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Load Balancer.

        ``GET /load_balancers/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            load_balancer_id: ID of the Load Balancer.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_8, load_balancer_id=load_balancer_id, action_id=action_id)
        response = self._transport.request(
            "GET",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)


class AsyncLoadBalancerActionsResource:
    """Operations on ``load_balancer_actions`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_load_balancers_actions(
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

        ``GET /load_balancers/actions``

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
            "/load_balancers/actions",
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

    async def get_load_balancers_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action object.

        ``GET /load_balancers/actions/{id}``

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
            f"/load_balancers/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def list_load_balancer_actions(
        self,
        load_balancer_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Load Balancer.

        Returns all Action objects for a Load Balancer. You can sort the results by using the `sort`
        URI parameter, and filter them with the `status` parameter.

        ``GET /load_balancers/{id}/actions``

        Args:
            load_balancer_id: ID of the Load Balancer.
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
            load_balancer_id=load_balancer_id,
            page=page,
            per_page=per_page,
        )
        response = await self._transport.request(
            "GET",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions",
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

    async def add_load_balancer_service(
        self,
        load_balancer_id: int,
        /,
        *,
        protocol: LoadBalancerServiceProtocol | UnknownValue,
        listen_port: int,
        destination_port: int,
        proxyprotocol: bool,
        health_check: LoadBalancerServiceHealthCheck2Param,
        http: LoadBalancerServiceHTTPParam | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Add Service.

        Adds a service to a Load Balancer.

        **Operation specific errors**

        - `412` - `source_port_already_used` - The source port you are trying to add is already in
          use

        ``POST /load_balancers/{id}/actions/add_service``

        Args:
            load_balancer_id: ID of the Load Balancer.
            protocol: Protocol of the Load Balancer.
            listen_port: Port the Load Balancer listens on.
            destination_port: Port the Load Balancer will balance to.
            proxyprotocol: Is Proxyprotocol enabled or not.
            health_check: ``health_check``.
            http: Configuration option for protocols http and https. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_4,
            load_balancer_id=load_balancer_id,
            health_check=health_check,
            http=http,
        )
        response = await self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/add_service",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "protocol": protocol,
                    "listen_port": listen_port,
                    "destination_port": destination_port,
                    "proxyprotocol": proxyprotocol,
                    "health_check": health_check,
                    "http": http,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def add_load_balancer_target(
        self,
        load_balancer_id: int,
        /,
        *,
        type: LoadBalancerTargetType | UnknownValue,
        server: LoadBalancerTargetServerRequestParam | NotGiven = NOT_GIVEN,
        label_selector: LoadBalancerTargetLabelSelectorParam | NotGiven = NOT_GIVEN,
        ip: LoadBalancerTargetIPParam | NotGiven = NOT_GIVEN,
        use_private_ip: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Add Target.

        Adds a target to a Load Balancer.

        **Operation specific errors**

        - `422` - `ip_not_in_vswitch_subnet` - The IP you are trying to add does not belong to the
          vswitch subnet of the attached network
        - `422` - `ip_not_owned` - The IP you are trying to add as a target is not owned by the
          Project owner
        - `422` - `ip_not_assigned_to_server` - The specified IP is neither the Primary IPv4 address
          nor in the IPv6 subnet of the given Server
        - `422` - `load_balancer_public_interface_disabled` - The Load Balancer's public network
          interface is disabled
        - `422` - `load_balancer_not_attached_to_network` - The Load Balancer is not attached to a
          network
        - `422` - `network_has_no_vswitch_subnet` - The given IP is private but attached network
          does not have a vswitch subnet
        - `422` - `resolve_cloud_private_targets_error` - The server you are trying to add as a
          target is not attached to the same network as the Load Balancer
        - `422` - `resolve_cloud_public_targets_error` - The server that you are trying to add as a
          public target does not have a public IPv4 address
        - `422` - `target_already_defined` - The Load Balancer target you are trying to define is
          already defined

        ``POST /load_balancers/{id}/actions/add_target``

        Args:
            load_balancer_id: ID of the Load Balancer.
            type: Type of the resource.
            server: Configuration for type Server, only valid and required if type is `server`.
                Omitted if not given.
            label_selector: Configuration for label selector targets, only valid and required if
                type is `label_selector`. Omitted if not given.
            ip: Configuration for an IP target. It is only possible to use the (Public or vSwitch)
                IPs of Hetzner Online Root Servers belonging to the project owner. IPs belonging to
                other users are blocked. Additionally IPs belonging to services provided by Hetzner
                Cloud (Servers, Load Balancers, ...) are blocked as well. Only valid and required if
                type is `ip`. Omitted if not given.
            use_private_ip: Use the private network IP instead of the public IP of the Server,
                requires the Server and Load Balancer to be in the same network. Only valid for
                target types `server` and `label_selector`. Omitted if not given. The API default is
                ``False``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_5,
            load_balancer_id=load_balancer_id,
            label_selector=label_selector,
        )
        response = await self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/add_target",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "type": type,
                    "server": server,
                    "label_selector": label_selector,
                    "ip": ip,
                    "use_private_ip": use_private_ip,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def attach_load_balancer_to_network(
        self,
        load_balancer_id: int,
        /,
        *,
        network: int,
        ip: str | NotGiven = NOT_GIVEN,
        ip_range: str | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Attach a Load Balancer to a Network.

        ``POST /load_balancers/{id}/actions/attach_to_network``

        Args:
            load_balancer_id: ID of the Load Balancer.
            network: ID of an existing network to attach the Load Balancer to.
            ip: IP to request to be assigned to this Load Balancer; if you do not provide this then
                you will be auto assigned an IP address. Omitted if not given.
            ip_range: IP range in CIDR block notation of the subnet to attach to. This allows for
                auto assigning an IP address for a specific subnet. Providing `ip` that is not part
                of `ip_range` will result in an error. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = await self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/attach_to_network",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "network": network,
                    "ip": ip,
                    "ip_range": ip_range,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_load_balancer_algorithm(
        self,
        load_balancer_id: int,
        /,
        *,
        type: LoadBalancerAlgorithmType | UnknownValue,
    ) -> ActionResponse:
        """Change Algorithm.

        Change the algorithm that determines to which target new requests are sent.

        ``POST /load_balancers/{id}/actions/change_algorithm``

        Args:
            load_balancer_id: ID of the Load Balancer.
            type: Type of the algorithm.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = await self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/change_algorithm",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "type": type,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_load_balancer_dns_ptr(
        self,
        load_balancer_id: int,
        /,
        *,
        ip: str,
        dns_ptr: str | None,
    ) -> ActionResponse:
        """Change reverse DNS entry for this Load Balancer.

        Changes the hostname that will appear when getting the hostname belonging to the public IPs
        (IPv4 and IPv6) of this Load Balancer.

        Floating IPs assigned to the Server are not affected by this.

        ``POST /load_balancers/{id}/actions/change_dns_ptr``

        Args:
            load_balancer_id: ID of the Load Balancer.
            ip: Single IPv4 or IPv6 address to create pointer for.
            dns_ptr: Domain Name to point to. PTR record content used for reverse DNS. Set to null
                to reset (IPv4) to the default value or remove (IPv6) the record.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = await self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/change_dns_ptr",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ip": ip,
                    "dns_ptr": dns_ptr,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_load_balancer_protection(
        self,
        load_balancer_id: int,
        /,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Change Load Balancer Protection.

        Changes the protection configuration of a Load Balancer.

        ``POST /load_balancers/{id}/actions/change_protection``

        Args:
            load_balancer_id: ID of the Load Balancer.
            delete: If true, prevents the snapshot from being deleted. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = await self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_load_balancer_type(
        self,
        load_balancer_id: int,
        /,
        *,
        load_balancer_type: str | int,
    ) -> ActionResponse:
        """Change the Type of a Load Balancer.

        Changes the type (Max Services, Max Targets and Max Connections) of a Load Balancer.

        **Operation specific errors**

        - `422` - `invalid_load_balancer_type` - The Load Balancer type does not fit for the given
          Load Balancer

        ``POST /load_balancers/{id}/actions/change_type``

        Args:
            load_balancer_id: ID of the Load Balancer.
            load_balancer_type: ID or name of Load Balancer type the Load Balancer should migrate
                to.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = await self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/change_type",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "load_balancer_type": load_balancer_type,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def delete_load_balancer_service(
        self,
        load_balancer_id: int,
        /,
        *,
        listen_port: int,
    ) -> ActionResponse:
        """Delete Service.

        Delete a service of a Load Balancer.

        ``POST /load_balancers/{id}/actions/delete_service``

        Args:
            load_balancer_id: ID of the Load Balancer.
            listen_port: The listen port of the service you want to delete.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = await self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/delete_service",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "listen_port": listen_port,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def detach_load_balancer_from_network(
        self,
        load_balancer_id: int,
        /,
        *,
        network: int,
    ) -> ActionResponse:
        """Detach a Load Balancer from a Network.

        Detaches a Load Balancer from a network.

        ``POST /load_balancers/{id}/actions/detach_from_network``

        Args:
            load_balancer_id: ID of the Load Balancer.
            network: ID of an existing network to detach the Load Balancer from.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = await self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/detach_from_network",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "network": network,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def disable_load_balancer_public_interface(
        self,
        load_balancer_id: int,
        /,
    ) -> ActionResponse:
        """Disable the public interface of a Load Balancer.

        Disable the public interface of a Load Balancer. The Load Balancer will be not accessible
        from the internet via its public IPs.

        **Operation specific errors**

        - `422` - `load_balancer_not_attached_to_network` - The Load Balancer is not attached to a
          network
        - `422` - `targets_without_use_private_ip` - The Load Balancer has targets that use the
          public IP instead of the private IP

        ``POST /load_balancers/{id}/actions/disable_public_interface``

        Args:
            load_balancer_id: ID of the Load Balancer.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = await self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/disable_public_interface",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def enable_load_balancer_public_interface(
        self,
        load_balancer_id: int,
        /,
    ) -> ActionResponse:
        """Enable the public interface of a Load Balancer.

        Enable the public interface of a Load Balancer. The Load Balancer will be accessible from
        the internet via its public IPs.

        ``POST /load_balancers/{id}/actions/enable_public_interface``

        Args:
            load_balancer_id: ID of the Load Balancer.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, load_balancer_id=load_balancer_id)
        response = await self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/enable_public_interface",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def remove_load_balancer_target(
        self,
        load_balancer_id: int,
        /,
        *,
        type: LoadBalancerTargetType | UnknownValue,
        server: LoadBalancerTargetServerRequestParam | NotGiven = NOT_GIVEN,
        label_selector: LoadBalancerTargetLabelSelectorParam | NotGiven = NOT_GIVEN,
        ip: LoadBalancerTargetIPParam | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Remove Target.

        Removes a target from a Load Balancer.

        ``POST /load_balancers/{id}/actions/remove_target``

        Args:
            load_balancer_id: ID of the Load Balancer.
            type: Type of the resource.
            server: Configuration for type Server, only valid and required if type is `server`.
                Omitted if not given.
            label_selector: Configuration for label selector targets, only valid and required if
                type is `label_selector`. Omitted if not given.
            ip: Configuration for an IP target. It is only possible to use the (Public or vSwitch)
                IPs of Hetzner Online Root Servers belonging to the project owner. IPs belonging to
                other users are blocked. Additionally IPs belonging to services provided by Hetzner
                Cloud (Servers, Load Balancers, ...) are blocked as well. Only valid and required if
                type is `ip`. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_5,
            load_balancer_id=load_balancer_id,
            label_selector=label_selector,
        )
        response = await self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/remove_target",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "type": type,
                    "server": server,
                    "label_selector": label_selector,
                    "ip": ip,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def update_load_balancer_service(
        self,
        load_balancer_id: int,
        /,
        *,
        listen_port: int,
        protocol: LoadBalancerServiceProtocol | UnknownValue | NotGiven = NOT_GIVEN,
        destination_port: int | NotGiven = NOT_GIVEN,
        proxyprotocol: bool | NotGiven = NOT_GIVEN,
        health_check: UpdateLoadBalancerServiceHealthCheckParam | NotGiven = NOT_GIVEN,
        http: UpdateLoadBalancerServiceHttpParam | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Update Service.

        Updates a Load Balancer Service.

        **Operation specific errors**

        - `422` - `source_port_already_used` - The source port you are trying to add is already in
          use

        ``POST /load_balancers/{id}/actions/update_service``

        Args:
            load_balancer_id: ID of the Load Balancer.
            listen_port: Port the Load Balancer listens on.
            protocol: Protocol of the Load Balancer. Omitted if not given.
            destination_port: Port the Load Balancer will balance to. Omitted if not given.
            proxyprotocol: Is Proxyprotocol enabled or not. Omitted if not given.
            health_check: Service health check. Omitted if not given.
            http: Configuration option for protocols http and https. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(
            _CHECKS_7,
            load_balancer_id=load_balancer_id,
            health_check=health_check,
            http=http,
        )
        response = await self._transport.request(
            "POST",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/update_service",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "protocol": protocol,
                    "listen_port": listen_port,
                    "destination_port": destination_port,
                    "proxyprotocol": proxyprotocol,
                    "health_check": health_check,
                    "http": http,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    @deprecated("GET /load_balancers/{id}/actions/{action_id} is deprecated by the API")
    async def get_load_balancer_action(
        self,
        load_balancer_id: int,
        action_id: int,
        /,
    ) -> ActionResponse:
        """Get an Action for a Load Balancer.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action for a Load Balancer.

        ``GET /load_balancers/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            load_balancer_id: ID of the Load Balancer.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_8, load_balancer_id=load_balancer_id, action_id=action_id)
        response = await self._transport.request(
            "GET",
            f"/load_balancers/{encode_path(load_balancer_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)
