"""Examples for ``storage_boxes`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import (
    ActionResponse,
    CreateStorageBoxResponse,
    ListStorageBoxesResponse,
    ListStorageBoxFoldersResponse,
    StorageBoxResponse,
)


def storage_boxes_list_storage_boxes(client: Hetzner) -> ListStorageBoxesResponse:
    """List Storage Boxes.

    ``GET /storage_boxes``

    Optional arguments: name, label_selector, sort, page, per_page.
    """
    return client.storage_boxes.list_storage_boxes()


def storage_boxes_create_storage_box(client: Hetzner) -> CreateStorageBoxResponse:
    """Create a Storage Box.

    ``POST /storage_boxes``

    Optional arguments: labels, ssh_keys, access_settings.
    """
    return client.storage_boxes.create_storage_box(
        name="example", location="fsn1", storage_box_type="bx20", password="example"
    )


def storage_boxes_get_storage_box(client: Hetzner) -> StorageBoxResponse:
    """Get a Storage Box.

    ``GET /storage_boxes/{id}``
    """
    return client.storage_boxes.get_storage_box(42)


def storage_boxes_update_storage_box(client: Hetzner) -> StorageBoxResponse:
    """Update a Storage Box.

    ``PUT /storage_boxes/{id}``

    Optional arguments: name, labels.
    """
    return client.storage_boxes.update_storage_box(42)


def storage_boxes_delete_storage_box(client: Hetzner) -> ActionResponse:
    """Delete a Storage Box.

    ``DELETE /storage_boxes/{id}``
    """
    return client.storage_boxes.delete_storage_box(42)


def storage_boxes_list_storage_box_folders(client: Hetzner) -> ListStorageBoxFoldersResponse:
    """List folders of a Storage Box.

    ``GET /storage_boxes/{id}/folders``

    Optional arguments: path.
    """
    return client.storage_boxes.list_storage_box_folders(42)
