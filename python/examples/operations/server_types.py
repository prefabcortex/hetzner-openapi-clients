"""Examples for ``server_types`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import GetServerTypeResponse, ListServerTypesResponse


def server_types_list_server_types(client: Hetzner) -> ListServerTypesResponse:
    """List Server Types.

    ``GET /server_types``

    Optional arguments: name, page, per_page.
    """
    return client.server_types.list_server_types()


def server_types_get_server_type(client: Hetzner) -> GetServerTypeResponse:
    """Get a Server Type.

    ``GET /server_types/{id}``
    """
    return client.server_types.get_server_type(42)
