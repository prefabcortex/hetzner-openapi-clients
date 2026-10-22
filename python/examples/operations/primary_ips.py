"""Examples for ``primary_ips`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import CreatePrimaryIPResponse, PrimaryIPResponse, PrimaryIPsResponse


def primary_ips_list_primary_ips(client: Hetzner) -> PrimaryIPsResponse:
    """List Primary IPs.

    ``GET /primary_ips``

    Optional arguments: name, label_selector, ip, page, per_page, sort.
    """
    return client.primary_ips.list_primary_ips()


def primary_ips_create_primary_ip(client: Hetzner) -> CreatePrimaryIPResponse:
    """Create a Primary IP.

    ``POST /primary_ips``

    Optional arguments: labels, location, assignee_type, assignee_id, auto_delete.
    """
    return client.primary_ips.create_primary_ip(name="my-resource", type="ipv6")


def primary_ips_get_primary_ip(client: Hetzner) -> PrimaryIPResponse:
    """Get a Primary IP.

    ``GET /primary_ips/{id}``
    """
    return client.primary_ips.get_primary_ip(42)


def primary_ips_update_primary_ip(client: Hetzner) -> PrimaryIPResponse:
    """Update a Primary IP.

    ``PUT /primary_ips/{id}``

    Optional arguments: name, labels, auto_delete.
    """
    return client.primary_ips.update_primary_ip(42)


def primary_ips_delete_primary_ip(client: Hetzner) -> None:
    """Delete a Primary IP.

    ``DELETE /primary_ips/{id}``
    """
    client.primary_ips.delete_primary_ip(42)
