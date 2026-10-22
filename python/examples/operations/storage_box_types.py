"""Examples for ``storage_box_types`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import GetStorageBoxTypeResponse, ListStorageBoxTypesResponse


def storage_box_types_list_storage_box_types(client: Hetzner) -> ListStorageBoxTypesResponse:
    """List Storage Box Types.

    ``GET /storage_box_types``

    Optional arguments: name, page, per_page.
    """
    return client.storage_box_types.list_storage_box_types()


def storage_box_types_get_storage_box_type(client: Hetzner) -> GetStorageBoxTypeResponse:
    """Get a Storage Box Type.

    ``GET /storage_box_types/{id}``
    """
    return client.storage_box_types.get_storage_box_type(42)
