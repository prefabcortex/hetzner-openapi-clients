"""Examples for ``firewall_actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ActionListResponse, ActionListResponseWithMeta, ActionResponse


def firewall_actions_list_firewalls_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions.

    ``GET /firewalls/actions``

    Optional arguments: id, sort, status, page, per_page.
    """
    return client.firewall_actions.list_firewalls_actions()


def firewall_actions_get_firewalls_action(client: Hetzner) -> ActionResponse:
    """Get an Action.

    ``GET /firewalls/actions/{id}``
    """
    return client.firewall_actions.get_firewalls_action(42)


def firewall_actions_list_firewall_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions for a Firewall.

    ``GET /firewalls/{id}/actions``

    Optional arguments: sort, status, page, per_page.
    """
    return client.firewall_actions.list_firewall_actions(42)


def firewall_actions_apply_firewall_to_resources(client: Hetzner) -> ActionListResponse:
    """Apply to Resources.

    ``POST /firewalls/{id}/actions/apply_to_resources``
    """
    return client.firewall_actions.apply_firewall_to_resources(42, apply_to=[{"type": "server"}])


def firewall_actions_remove_firewall_from_resources(client: Hetzner) -> ActionListResponse:
    """Remove from Resources.

    ``POST /firewalls/{id}/actions/remove_from_resources``
    """
    return client.firewall_actions.remove_firewall_from_resources(
        42, remove_from=[{"type": "server"}]
    )


def firewall_actions_set_firewall_rules(client: Hetzner) -> ActionListResponse:
    """Set Rules.

    ``POST /firewalls/{id}/actions/set_rules``
    """
    return client.firewall_actions.set_firewall_rules(
        42, rules=[{"direction": "in", "protocol": "tcp"}]
    )
