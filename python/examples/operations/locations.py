"""Examples for ``locations`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import GetLocationResponse, ListLocationsResponse


def locations_list_locations(client: Hetzner) -> ListLocationsResponse:
    """List Locations.

    ``GET /locations``

    Optional arguments: name, sort, page, per_page.
    """
    return client.locations.list_locations()


def locations_get_location(client: Hetzner) -> GetLocationResponse:
    """Get a Location.

    ``GET /locations/{id}``
    """
    return client.locations.get_location(42)
