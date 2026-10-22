"""Examples for ``storage_box_snapshots`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import (
    ActionResponse,
    CreateStorageBoxSnapshotResponse,
    ListStorageBoxSnapshotsResponse,
    SnapshotResponse,
)


def storage_box_snapshots_list_storage_box_snapshots(
    client: Hetzner,
) -> ListStorageBoxSnapshotsResponse:
    """List Snapshots.

    ``GET /storage_boxes/{id}/snapshots``

    Optional arguments: name, label_selector, sort, is_automatic.
    """
    return client.storage_box_snapshots.list_storage_box_snapshots(42)


def storage_box_snapshots_create_storage_box_snapshot(
    client: Hetzner,
) -> CreateStorageBoxSnapshotResponse:
    """Create a Snapshot.

    ``POST /storage_boxes/{id}/snapshots``

    Optional arguments: description, labels.
    """
    return client.storage_box_snapshots.create_storage_box_snapshot(42)


def storage_box_snapshots_get_storage_box_snapshot(client: Hetzner) -> SnapshotResponse:
    """Get a Snapshot.

    ``GET /storage_boxes/{id}/snapshots/{snapshot_id}``
    """
    return client.storage_box_snapshots.get_storage_box_snapshot(42, 42)


def storage_box_snapshots_update_storage_box_snapshot(client: Hetzner) -> SnapshotResponse:
    """Update a Snapshot.

    ``PUT /storage_boxes/{id}/snapshots/{snapshot_id}``

    Optional arguments: description, labels.
    """
    return client.storage_box_snapshots.update_storage_box_snapshot(42, 42)


def storage_box_snapshots_delete_storage_box_snapshot(client: Hetzner) -> ActionResponse:
    """Delete a Snapshot.

    ``DELETE /storage_boxes/{id}/snapshots/{snapshot_id}``
    """
    return client.storage_box_snapshots.delete_storage_box_snapshot(42, 42)
