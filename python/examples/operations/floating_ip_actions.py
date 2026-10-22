"""Examples for ``floating_ip_actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ActionListResponseWithMeta, ActionResponse


def floating_ip_actions_list_floating_ips_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions.

    ``GET /floating_ips/actions``

    Optional arguments: id, sort, status, page, per_page.
    """
    return client.floating_ip_actions.list_floating_ips_actions()


def floating_ip_actions_get_floating_ips_action(client: Hetzner) -> ActionResponse:
    """Get an Action.

    ``GET /floating_ips/actions/{id}``
    """
    return client.floating_ip_actions.get_floating_ips_action(42)


def floating_ip_actions_list_floating_ip_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions for a Floating IP.

    ``GET /floating_ips/{id}/actions``

    Optional arguments: sort, status, page, per_page.
    """
    return client.floating_ip_actions.list_floating_ip_actions(42)


def floating_ip_actions_assign_floating_ip(client: Hetzner) -> ActionResponse:
    """Assign a Floating IP to a Server.

    ``POST /floating_ips/{id}/actions/assign``
    """
    return client.floating_ip_actions.assign_floating_ip(42, server=42)


def floating_ip_actions_change_floating_ip_dns_ptr(client: Hetzner) -> ActionResponse:
    """Change reverse DNS records for a Floating IP.

    ``POST /floating_ips/{id}/actions/change_dns_ptr``
    """
    return client.floating_ip_actions.change_floating_ip_dns_ptr(
        42, ip="2001:db8::1", dns_ptr="server.example.com"
    )


def floating_ip_actions_change_floating_ip_protection(client: Hetzner) -> ActionResponse:
    """Change Floating IP Protection.

    ``POST /floating_ips/{id}/actions/change_protection``
    """
    return client.floating_ip_actions.change_floating_ip_protection(42, delete=False)


def floating_ip_actions_unassign_floating_ip(client: Hetzner) -> ActionResponse:
    """Unassign a Floating IP.

    ``POST /floating_ips/{id}/actions/unassign``
    """
    return client.floating_ip_actions.unassign_floating_ip(42)
