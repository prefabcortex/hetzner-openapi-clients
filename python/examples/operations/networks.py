"""Examples for ``networks`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ListNetworkMembersResponse, ListNetworksResponse, NetworkResponse


def networks_list_networks(client: Hetzner) -> ListNetworksResponse:
    """List Networks.

    ``GET /networks``

    Optional arguments: sort, name, label_selector, page, per_page.
    """
    return client.networks.list_networks()


def networks_create_network(client: Hetzner) -> NetworkResponse:
    """Create a Network.

    ``POST /networks``

    Optional arguments: labels, subnets, routes, expose_routes_to_vswitch.
    """
    return client.networks.create_network(name="mynet", ip_range="10.0.0.0/16")


def networks_get_network(client: Hetzner) -> NetworkResponse:
    """Get a Network.

    ``GET /networks/{id}``
    """
    return client.networks.get_network(42)


def networks_update_network(client: Hetzner) -> NetworkResponse:
    """Update a Network.

    ``PUT /networks/{id}``

    Optional arguments: name, labels, expose_routes_to_vswitch.
    """
    return client.networks.update_network(42)


def networks_delete_network(client: Hetzner) -> None:
    """Delete a Network.

    ``DELETE /networks/{id}``
    """
    client.networks.delete_network(42)


def networks_list_network_members(client: Hetzner) -> ListNetworkMembersResponse:
    """List Members of a Network.

    ``GET /networks/{id}/members``

    Optional arguments: type, subnet, status, sort, page, per_page.
    """
    return client.networks.list_network_members(42)
