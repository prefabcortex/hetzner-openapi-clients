"""Examples for ``primary_ip_actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ActionListResponseWithMeta, ActionResponse


def primary_ip_actions_list_primary_ips_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions.

    ``GET /primary_ips/actions``

    Optional arguments: id, sort, status, page, per_page.
    """
    return client.primary_ip_actions.list_primary_ips_actions()


def primary_ip_actions_get_primary_ips_action(client: Hetzner) -> ActionResponse:
    """Get an Action.

    ``GET /primary_ips/actions/{id}``
    """
    return client.primary_ip_actions.get_primary_ips_action(42)


def primary_ip_actions_list_primary_ip_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions for a Primary IP.

    ``GET /primary_ips/{id}/actions``

    Optional arguments: sort, status, page, per_page.
    """
    return client.primary_ip_actions.list_primary_ip_actions(42)


def primary_ip_actions_assign_primary_ip(client: Hetzner) -> ActionResponse:
    """Assign a Primary IP to a resource.

    ``POST /primary_ips/{id}/actions/assign``
    """
    return client.primary_ip_actions.assign_primary_ip(42, assignee_type="server", assignee_id=4711)


def primary_ip_actions_change_primary_ip_dns_ptr(client: Hetzner) -> ActionResponse:
    """Change reverse DNS records for a Primary IP.

    ``POST /primary_ips/{id}/actions/change_dns_ptr``
    """
    return client.primary_ip_actions.change_primary_ip_dns_ptr(
        42, ip="2001:db8::1", dns_ptr="server.example.com"
    )


def primary_ip_actions_change_primary_ip_protection(client: Hetzner) -> ActionResponse:
    """Change Primary IP Protection.

    ``POST /primary_ips/{id}/actions/change_protection``
    """
    return client.primary_ip_actions.change_primary_ip_protection(42, delete=False)


def primary_ip_actions_unassign_primary_ip(client: Hetzner) -> ActionResponse:
    """Unassign a Primary IP from a resource.

    ``POST /primary_ips/{id}/actions/unassign``
    """
    return client.primary_ip_actions.unassign_primary_ip(42)
