"""Examples for ``image_actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ActionListResponseWithMeta, ActionResponse


def image_actions_list_images_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions.

    ``GET /images/actions``

    Optional arguments: id, sort, status, page, per_page.
    """
    return client.image_actions.list_images_actions()


def image_actions_get_images_action(client: Hetzner) -> ActionResponse:
    """Get an Action.

    ``GET /images/actions/{id}``
    """
    return client.image_actions.get_images_action(42)


def image_actions_list_image_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions for an Image.

    ``GET /images/{id}/actions``

    Optional arguments: sort, status, page, per_page.
    """
    return client.image_actions.list_image_actions(42)


def image_actions_change_image_protection(client: Hetzner) -> ActionResponse:
    """Change Image Protection.

    ``POST /images/{id}/actions/change_protection``

    Optional arguments: delete.
    """
    return client.image_actions.change_image_protection(42)
