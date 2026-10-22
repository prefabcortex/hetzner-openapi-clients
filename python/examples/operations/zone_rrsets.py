"""Examples for ``zone_rrsets`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import (
    ActionResponse,
    CreateZoneRrsetResponse,
    ListZoneRrsetsResponse,
    RrsetResponse,
)


def zone_rrsets_list_zone_rrsets(client: Hetzner) -> ListZoneRrsetsResponse:
    """List RRSets.

    ``GET /zones/{id_or_name}/rrsets``

    Optional arguments: name, type, label_selector, sort, page, per_page.
    """
    return client.zone_rrsets.list_zone_rrsets("example")


def zone_rrsets_create_zone_rrset(client: Hetzner) -> CreateZoneRrsetResponse:
    """Create an RRSet.

    ``POST /zones/{id_or_name}/rrsets``

    Optional arguments: ttl, labels.
    """
    return client.zone_rrsets.create_zone_rrset(
        "example", name="www", type="A", records=[{"value": "198.51.100.1"}]
    )


def zone_rrsets_get_zone_rrset(client: Hetzner) -> RrsetResponse:
    """Get an RRSet.

    ``GET /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}``
    """
    return client.zone_rrsets.get_zone_rrset("example", "www", "A")


def zone_rrsets_update_zone_rrset(client: Hetzner) -> RrsetResponse:
    """Update an RRSet.

    ``PUT /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}``

    Optional arguments: labels.
    """
    return client.zone_rrsets.update_zone_rrset("example", "www", "A")


def zone_rrsets_delete_zone_rrset(client: Hetzner) -> ActionResponse:
    """Delete an RRSet.

    ``DELETE /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}``
    """
    return client.zone_rrsets.delete_zone_rrset("example", "www", "A")
