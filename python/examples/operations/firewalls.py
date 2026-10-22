"""Examples for ``firewalls`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import CreateFirewallResponse, FirewallResponse, FirewallsResponse


def firewalls_list_firewalls(client: Hetzner) -> FirewallsResponse:
    """List Firewalls.

    ``GET /firewalls``

    Optional arguments: sort, name, label_selector, page, per_page.
    """
    return client.firewalls.list_firewalls()


def firewalls_create_firewall(client: Hetzner) -> CreateFirewallResponse:
    """Create a Firewall.

    ``POST /firewalls``

    Optional arguments: labels, rules, apply_to.
    """
    return client.firewalls.create_firewall(name="new-name")


def firewalls_get_firewall(client: Hetzner) -> FirewallResponse:
    """Get a Firewall.

    ``GET /firewalls/{id}``
    """
    return client.firewalls.get_firewall(42)


def firewalls_update_firewall(client: Hetzner) -> FirewallResponse:
    """Update a Firewall.

    ``PUT /firewalls/{id}``

    Optional arguments: name, labels.
    """
    return client.firewalls.update_firewall(42)


def firewalls_delete_firewall(client: Hetzner) -> None:
    """Delete a Firewall.

    ``DELETE /firewalls/{id}``
    """
    client.firewalls.delete_firewall(42)
