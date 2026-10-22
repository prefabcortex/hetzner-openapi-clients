"""Examples for ``zone_rrset_actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ActionResponse


def zone_rrset_actions_change_zone_rrset_protection(client: Hetzner) -> ActionResponse:
    """Change an RRSet's Protection.

    ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/change_protection``
    """
    return client.zone_rrset_actions.change_zone_rrset_protection(
        "example", "www", "A", change=False
    )


def zone_rrset_actions_change_zone_rrset_ttl(client: Hetzner) -> ActionResponse:
    """Change an RRSet's TTL.

    ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/change_ttl``
    """
    return client.zone_rrset_actions.change_zone_rrset_ttl("example", "www", "A", ttl=3600)


def zone_rrset_actions_set_zone_rrset_records(client: Hetzner) -> ActionResponse:
    """Set Records of an RRSet.

    ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/set_records``
    """
    return client.zone_rrset_actions.set_zone_rrset_records(
        "example", "www", "A", records=[{"value": "198.51.100.1"}]
    )


def zone_rrset_actions_add_zone_rrset_records(client: Hetzner) -> ActionResponse:
    """Add Records to an RRSet.

    ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/add_records``

    Optional arguments: ttl.
    """
    return client.zone_rrset_actions.add_zone_rrset_records(
        "example", "www", "A", records=[{"value": "198.51.100.1"}]
    )


def zone_rrset_actions_remove_zone_rrset_records(client: Hetzner) -> ActionResponse:
    """Remove Records from an RRSet.

    ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/remove_records``
    """
    return client.zone_rrset_actions.remove_zone_rrset_records(
        "example", "www", "A", records=[{"value": "198.51.100.1"}]
    )


def zone_rrset_actions_update_zone_rrset_records(client: Hetzner) -> ActionResponse:
    """Update Records of an RRSet.

    ``POST /zones/{id_or_name}/rrsets/{rr_name}/{rr_type}/actions/update_records``
    """
    return client.zone_rrset_actions.update_zone_rrset_records(
        "example",
        "www",
        "A",
        records=[{"value": "198.51.100.1", "comment": "My web server at Hetzner Cloud."}],
    )
