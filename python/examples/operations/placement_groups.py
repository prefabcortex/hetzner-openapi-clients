"""Examples for ``placement_groups`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import (
    CreatePlacementGroupResponse,
    PlacementGroupResponse,
    PlacementGroupsResponse,
)


def placement_groups_list_placement_groups(client: Hetzner) -> PlacementGroupsResponse:
    """List Placement Groups.

    ``GET /placement_groups``

    Optional arguments: sort, name, label_selector, type, page, per_page.
    """
    return client.placement_groups.list_placement_groups()


def placement_groups_create_placement_group(client: Hetzner) -> CreatePlacementGroupResponse:
    """Create a PlacementGroup.

    ``POST /placement_groups``

    Optional arguments: labels.
    """
    return client.placement_groups.create_placement_group(name="my Placement Group", type="spread")


def placement_groups_get_placement_group(client: Hetzner) -> PlacementGroupResponse:
    """Get a PlacementGroup.

    ``GET /placement_groups/{id}``
    """
    return client.placement_groups.get_placement_group(42)


def placement_groups_update_placement_group(client: Hetzner) -> PlacementGroupResponse:
    """Update a PlacementGroup.

    ``PUT /placement_groups/{id}``

    Optional arguments: name, labels.
    """
    return client.placement_groups.update_placement_group(42)


def placement_groups_delete_placement_group(client: Hetzner) -> None:
    """Delete a PlacementGroup.

    ``DELETE /placement_groups/{id}``
    """
    client.placement_groups.delete_placement_group(42)
