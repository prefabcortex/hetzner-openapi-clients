"""Examples for ``certificate_actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ActionListResponseWithMeta, ActionResponse


def certificate_actions_list_certificates_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions.

    ``GET /certificates/actions``

    Optional arguments: id, sort, status, page, per_page.
    """
    return client.certificate_actions.list_certificates_actions()


def certificate_actions_get_certificates_action(client: Hetzner) -> ActionResponse:
    """Get an Action.

    ``GET /certificates/actions/{id}``
    """
    return client.certificate_actions.get_certificates_action(42)


def certificate_actions_list_certificate_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions for a Certificate.

    ``GET /certificates/{id}/actions``

    Optional arguments: sort, status, page, per_page.
    """
    return client.certificate_actions.list_certificate_actions(42)


def certificate_actions_retry_certificate(client: Hetzner) -> ActionResponse:
    """Retry Issuance or Renewal.

    ``POST /certificates/{id}/actions/retry``
    """
    return client.certificate_actions.retry_certificate(42)
