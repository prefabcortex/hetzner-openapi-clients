"""Examples for ``isos`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import GetIsoResponse, ListIsosResponse


def isos_list_isos(client: Hetzner) -> ListIsosResponse:
    """List ISOs.

    ``GET /isos``

    Optional arguments: name, architecture, include_architecture_wildcard, page, per_page.
    """
    return client.isos.list_isos()


def isos_get_iso(client: Hetzner) -> GetIsoResponse:
    """Get an ISO.

    ``GET /isos/{id}``
    """
    return client.isos.get_iso(42)
