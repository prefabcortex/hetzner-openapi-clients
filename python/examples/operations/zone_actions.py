"""Examples for ``zone_actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ActionListResponseWithMeta, ActionResponse


def zone_actions_list_zones_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions.

    ``GET /zones/actions``

    Optional arguments: id, sort, status, page, per_page.
    """
    return client.zone_actions.list_zones_actions()


def zone_actions_get_zones_action(client: Hetzner) -> ActionResponse:
    """Get an Action.

    ``GET /zones/actions/{id}``
    """
    return client.zone_actions.get_zones_action(42)


def zone_actions_list_zone_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions for a Zone.

    ``GET /zones/{id_or_name}/actions``

    Optional arguments: sort, status, page, per_page.
    """
    return client.zone_actions.list_zone_actions("example")


def zone_actions_change_zone_primary_nameservers(client: Hetzner) -> ActionResponse:
    """Change a Zone's Primary Nameservers.

    ``POST /zones/{id_or_name}/actions/change_primary_nameservers``
    """
    return client.zone_actions.change_zone_primary_nameservers(
        "example", primary_nameservers=[{"address": "198.51.100.1"}]
    )


def zone_actions_change_zone_protection(client: Hetzner) -> ActionResponse:
    """Change a Zone's Protection.

    ``POST /zones/{id_or_name}/actions/change_protection``

    Optional arguments: delete.
    """
    return client.zone_actions.change_zone_protection("example")


def zone_actions_change_zone_ttl(client: Hetzner) -> ActionResponse:
    """Change a Zone's Default TTL.

    ``POST /zones/{id_or_name}/actions/change_ttl``
    """
    return client.zone_actions.change_zone_ttl("example", ttl=10800)


def zone_actions_import_zone_zonefile(client: Hetzner) -> ActionResponse:
    """Import a Zone file.

    ``POST /zones/{id_or_name}/actions/import_zonefile``
    """
    return client.zone_actions.import_zone_zonefile("example", zonefile="example")
