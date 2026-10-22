"""Examples for ``network_actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ActionListResponseWithMeta, ActionResponse


def network_actions_list_networks_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions.

    ``GET /networks/actions``

    Optional arguments: id, sort, status, page, per_page.
    """
    return client.network_actions.list_networks_actions()


def network_actions_get_networks_action(client: Hetzner) -> ActionResponse:
    """Get an Action.

    ``GET /networks/actions/{id}``
    """
    return client.network_actions.get_networks_action(42)


def network_actions_list_network_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions for a Network.

    ``GET /networks/{id}/actions``

    Optional arguments: sort, status, page, per_page.
    """
    return client.network_actions.list_network_actions(42)


def network_actions_add_network_route(client: Hetzner) -> ActionResponse:
    """Add a route to a Network.

    ``POST /networks/{id}/actions/add_route``
    """
    return client.network_actions.add_network_route(
        42, destination="10.100.1.0/24", gateway="10.0.1.1"
    )


def network_actions_add_network_subnet(client: Hetzner) -> ActionResponse:
    """Add a subnet to a Network.

    ``POST /networks/{id}/actions/add_subnet``

    Optional arguments: ip_range, vswitch_id.
    """
    return client.network_actions.add_network_subnet(42, type="cloud", network_zone="eu-central")


def network_actions_change_network_ip_range(client: Hetzner) -> ActionResponse:
    """Change IP range of a Network.

    ``POST /networks/{id}/actions/change_ip_range``
    """
    return client.network_actions.change_network_ip_range(42, ip_range="10.0.0.0/16")


def network_actions_change_network_protection(client: Hetzner) -> ActionResponse:
    """Change Network Protection.

    ``POST /networks/{id}/actions/change_protection``

    Optional arguments: delete.
    """
    return client.network_actions.change_network_protection(42)


def network_actions_delete_network_route(client: Hetzner) -> ActionResponse:
    """Delete a route from a Network.

    ``POST /networks/{id}/actions/delete_route``
    """
    return client.network_actions.delete_network_route(
        42, destination="10.100.1.0/24", gateway="10.0.1.1"
    )


def network_actions_delete_network_subnet(client: Hetzner) -> ActionResponse:
    """Delete a subnet from a Network.

    ``POST /networks/{id}/actions/delete_subnet``
    """
    return client.network_actions.delete_network_subnet(42, ip_range="10.0.1.0/24")
