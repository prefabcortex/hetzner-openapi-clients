"""Examples for ``actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ActionListResponse, ActionResponse


def actions_get_actions(client: Hetzner) -> ActionListResponse:
    """Get multiple Actions.

    ``GET /actions``
    """
    return client.actions.get_actions(id=[1])


def actions_get_action(client: Hetzner) -> ActionResponse:
    """Get an Action.

    ``GET /actions/{id}``
    """
    return client.actions.get_action(42)
