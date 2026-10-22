"""Examples for ``floating_ips`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import CreateFloatingIpResponse, FloatingIpResponse, ListFloatingIpsResponse


def floating_ips_list_floating_ips(client: Hetzner) -> ListFloatingIpsResponse:
    """List Floating IPs.

    ``GET /floating_ips``

    Optional arguments: name, label_selector, sort, page, per_page.
    """
    return client.floating_ips.list_floating_ips()


def floating_ips_create_floating_ip(client: Hetzner) -> CreateFloatingIpResponse:
    """Create a Floating IP.

    ``POST /floating_ips``

    Optional arguments: server, home_location, description, name, labels.
    """
    return client.floating_ips.create_floating_ip(type="ipv6")


def floating_ips_get_floating_ip(client: Hetzner) -> FloatingIpResponse:
    """Get a Floating IP.

    ``GET /floating_ips/{id}``
    """
    return client.floating_ips.get_floating_ip(42)


def floating_ips_update_floating_ip(client: Hetzner) -> FloatingIpResponse:
    """Update a Floating IP.

    ``PUT /floating_ips/{id}``

    Optional arguments: description, name, labels.
    """
    return client.floating_ips.update_floating_ip(42)


def floating_ips_delete_floating_ip(client: Hetzner) -> None:
    """Delete a Floating IP.

    ``DELETE /floating_ips/{id}``
    """
    client.floating_ips.delete_floating_ip(42)
