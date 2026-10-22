"""Examples for ``servers`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import (
    ActionResponse,
    CreateServerResponse,
    ListServersResponse,
    MetricsResponse,
    ServerResponse,
)


def servers_list_servers(client: Hetzner) -> ListServersResponse:
    """List Servers.

    ``GET /servers``

    Optional arguments: name, label_selector, sort, status, page, per_page.
    """
    return client.servers.list_servers()


def servers_create_server(client: Hetzner) -> CreateServerResponse:
    """Create a Server.

    ``POST /servers``

    Optional arguments: location, start_after_create, placement_group, ssh_keys, volumes, networks,
    firewalls, user_data, labels, automount, public_net.
    """
    return client.servers.create_server(name="my-server", server_type="cpx22", image="ubuntu-24.04")


def servers_get_server(client: Hetzner) -> ServerResponse:
    """Get a Server.

    ``GET /servers/{id}``
    """
    return client.servers.get_server(42)


def servers_update_server(client: Hetzner) -> ServerResponse:
    """Update a Server.

    ``PUT /servers/{id}``

    Optional arguments: name, labels.
    """
    return client.servers.update_server(42)


def servers_delete_server(client: Hetzner) -> ActionResponse:
    """Delete a Server.

    ``DELETE /servers/{id}``
    """
    return client.servers.delete_server(42)


def servers_get_server_metrics(client: Hetzner) -> MetricsResponse:
    """Get Metrics for a Server.

    ``GET /servers/{id}/metrics``

    Optional arguments: step.
    """
    return client.servers.get_server_metrics(42, type=["cpu"], start="example", end="example")
