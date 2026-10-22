"""Examples for ``volume_actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ActionListResponseWithMeta, ActionResponse


def volume_actions_list_volumes_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions.

    ``GET /volumes/actions``

    Optional arguments: id, sort, status, page, per_page.
    """
    return client.volume_actions.list_volumes_actions()


def volume_actions_get_volumes_action(client: Hetzner) -> ActionResponse:
    """Get an Action.

    ``GET /volumes/actions/{id}``
    """
    return client.volume_actions.get_volumes_action(42)


def volume_actions_list_volume_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions for a Volume.

    ``GET /volumes/{id}/actions``

    Optional arguments: sort, status, page, per_page.
    """
    return client.volume_actions.list_volume_actions(42)


def volume_actions_attach_volume(client: Hetzner) -> ActionResponse:
    """Attach Volume to a Server.

    ``POST /volumes/{id}/actions/attach``

    Optional arguments: automount.
    """
    return client.volume_actions.attach_volume(42, server=43)


def volume_actions_change_volume_protection(client: Hetzner) -> ActionResponse:
    """Change Volume Protection.

    ``POST /volumes/{id}/actions/change_protection``

    Optional arguments: delete.
    """
    return client.volume_actions.change_volume_protection(42)


def volume_actions_detach_volume(client: Hetzner) -> ActionResponse:
    """Detach Volume.

    ``POST /volumes/{id}/actions/detach``
    """
    return client.volume_actions.detach_volume(42)


def volume_actions_resize_volume(client: Hetzner) -> ActionResponse:
    """Resize Volume.

    ``POST /volumes/{id}/actions/resize``
    """
    return client.volume_actions.resize_volume(42, size=50)
