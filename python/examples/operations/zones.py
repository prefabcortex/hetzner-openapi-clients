"""Examples for ``zones`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import (
    ActionResponse,
    CreateZoneResponse,
    ListZonesResponse,
    Zonefile,
    ZoneResponse,
)


def zones_list_zones(client: Hetzner) -> ListZonesResponse:
    """List Zones.

    ``GET /zones``

    Optional arguments: name, mode, label_selector, sort, page, per_page.
    """
    return client.zones.list_zones()


def zones_create_zone(client: Hetzner) -> CreateZoneResponse:
    """Create a Zone.

    ``POST /zones``

    Optional arguments: ttl, labels, primary_nameservers, rrsets, zonefile.
    """
    return client.zones.create_zone(name="example.com", mode="primary")


def zones_get_zone(client: Hetzner) -> ZoneResponse:
    """Get a Zone.

    ``GET /zones/{id_or_name}``
    """
    return client.zones.get_zone("example")


def zones_update_zone(client: Hetzner) -> ZoneResponse:
    """Update a Zone.

    ``PUT /zones/{id_or_name}``

    Optional arguments: labels.
    """
    return client.zones.update_zone("example")


def zones_delete_zone(client: Hetzner) -> ActionResponse:
    """Delete a Zone.

    ``DELETE /zones/{id_or_name}``
    """
    return client.zones.delete_zone("example")


def zones_get_zone_zonefile(client: Hetzner) -> Zonefile:
    """Export a Zone file.

    ``GET /zones/{id_or_name}/zonefile``
    """
    return client.zones.get_zone_zonefile("example")
