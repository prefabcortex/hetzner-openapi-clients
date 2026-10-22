"""Examples for ``load_balancer_actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ActionListResponseWithMeta, ActionResponse


def load_balancer_actions_list_load_balancers_actions(
    client: Hetzner,
) -> ActionListResponseWithMeta:
    """List Actions.

    ``GET /load_balancers/actions``

    Optional arguments: id, sort, status, page, per_page.
    """
    return client.load_balancer_actions.list_load_balancers_actions()


def load_balancer_actions_get_load_balancers_action(client: Hetzner) -> ActionResponse:
    """Get an Action.

    ``GET /load_balancers/actions/{id}``
    """
    return client.load_balancer_actions.get_load_balancers_action(42)


def load_balancer_actions_list_load_balancer_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions for a Load Balancer.

    ``GET /load_balancers/{id}/actions``

    Optional arguments: sort, status, page, per_page.
    """
    return client.load_balancer_actions.list_load_balancer_actions(42)


def load_balancer_actions_add_load_balancer_service(client: Hetzner) -> ActionResponse:
    """Add Service.

    ``POST /load_balancers/{id}/actions/add_service``

    Optional arguments: http.
    """
    return client.load_balancer_actions.add_load_balancer_service(
        42,
        protocol="https",
        listen_port=443,
        destination_port=80,
        proxyprotocol=False,
        health_check={
            "protocol": "http",
            "port": 4711,
            "interval": 15,
            "timeout": 10,
            "retries": 3,
        },
    )


def load_balancer_actions_add_load_balancer_target(client: Hetzner) -> ActionResponse:
    """Add Target.

    ``POST /load_balancers/{id}/actions/add_target``

    Optional arguments: server, label_selector, ip, use_private_ip.
    """
    return client.load_balancer_actions.add_load_balancer_target(42, type="server")


def load_balancer_actions_attach_load_balancer_to_network(client: Hetzner) -> ActionResponse:
    """Attach a Load Balancer to a Network.

    ``POST /load_balancers/{id}/actions/attach_to_network``

    Optional arguments: ip, ip_range.
    """
    return client.load_balancer_actions.attach_load_balancer_to_network(42, network=123)


def load_balancer_actions_change_load_balancer_algorithm(client: Hetzner) -> ActionResponse:
    """Change Algorithm.

    ``POST /load_balancers/{id}/actions/change_algorithm``
    """
    return client.load_balancer_actions.change_load_balancer_algorithm(42, type="round_robin")


def load_balancer_actions_change_load_balancer_dns_ptr(client: Hetzner) -> ActionResponse:
    """Change reverse DNS entry for this Load Balancer.

    ``POST /load_balancers/{id}/actions/change_dns_ptr``
    """
    return client.load_balancer_actions.change_load_balancer_dns_ptr(
        42, ip="2001:db8::1", dns_ptr="server.example.com"
    )


def load_balancer_actions_change_load_balancer_protection(client: Hetzner) -> ActionResponse:
    """Change Load Balancer Protection.

    ``POST /load_balancers/{id}/actions/change_protection``

    Optional arguments: delete.
    """
    return client.load_balancer_actions.change_load_balancer_protection(42)


def load_balancer_actions_change_load_balancer_type(client: Hetzner) -> ActionResponse:
    """Change the Type of a Load Balancer.

    ``POST /load_balancers/{id}/actions/change_type``
    """
    return client.load_balancer_actions.change_load_balancer_type(42, load_balancer_type="lb11")


def load_balancer_actions_delete_load_balancer_service(client: Hetzner) -> ActionResponse:
    """Delete Service.

    ``POST /load_balancers/{id}/actions/delete_service``
    """
    return client.load_balancer_actions.delete_load_balancer_service(42, listen_port=443)


def load_balancer_actions_detach_load_balancer_from_network(client: Hetzner) -> ActionResponse:
    """Detach a Load Balancer from a Network.

    ``POST /load_balancers/{id}/actions/detach_from_network``
    """
    return client.load_balancer_actions.detach_load_balancer_from_network(42, network=4711)


def load_balancer_actions_disable_load_balancer_public_interface(client: Hetzner) -> ActionResponse:
    """Disable the public interface of a Load Balancer.

    ``POST /load_balancers/{id}/actions/disable_public_interface``
    """
    return client.load_balancer_actions.disable_load_balancer_public_interface(42)


def load_balancer_actions_enable_load_balancer_public_interface(client: Hetzner) -> ActionResponse:
    """Enable the public interface of a Load Balancer.

    ``POST /load_balancers/{id}/actions/enable_public_interface``
    """
    return client.load_balancer_actions.enable_load_balancer_public_interface(42)


def load_balancer_actions_remove_load_balancer_target(client: Hetzner) -> ActionResponse:
    """Remove Target.

    ``POST /load_balancers/{id}/actions/remove_target``

    Optional arguments: server, label_selector, ip.
    """
    return client.load_balancer_actions.remove_load_balancer_target(42, type="server")


def load_balancer_actions_update_load_balancer_service(client: Hetzner) -> ActionResponse:
    """Update Service.

    ``POST /load_balancers/{id}/actions/update_service``

    Optional arguments: protocol, destination_port, proxyprotocol, health_check, http.
    """
    return client.load_balancer_actions.update_load_balancer_service(42, listen_port=443)
