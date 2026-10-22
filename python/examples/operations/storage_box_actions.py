"""Examples for ``storage_box_actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ActionListResponseWithMeta, ActionResponse


def storage_box_actions_list_storage_boxes_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions.

    ``GET /storage_boxes/actions``

    Optional arguments: id, sort, status, page, per_page.
    """
    return client.storage_box_actions.list_storage_boxes_actions()


def storage_box_actions_get_storage_boxes_action(client: Hetzner) -> ActionResponse:
    """Get an Action.

    ``GET /storage_boxes/actions/{id}``
    """
    return client.storage_box_actions.get_storage_boxes_action(42)


def storage_box_actions_list_storage_box_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions for a Storage Box.

    ``GET /storage_boxes/{id}/actions``

    Optional arguments: sort, status, page, per_page.
    """
    return client.storage_box_actions.list_storage_box_actions(42)


def storage_box_actions_change_storage_box_protection(client: Hetzner) -> ActionResponse:
    """Change Protection.

    ``POST /storage_boxes/{id}/actions/change_protection``

    Optional arguments: delete.
    """
    return client.storage_box_actions.change_storage_box_protection(42)


def storage_box_actions_change_storage_box_type(client: Hetzner) -> ActionResponse:
    """Change Type.

    ``POST /storage_boxes/{id}/actions/change_type``
    """
    return client.storage_box_actions.change_storage_box_type(42, storage_box_type="bx20")


def storage_box_actions_reset_storage_box_password(client: Hetzner) -> ActionResponse:
    """Reset Password.

    ``POST /storage_boxes/{id}/actions/reset_password``
    """
    return client.storage_box_actions.reset_storage_box_password(42, password="example")


def storage_box_actions_update_storage_box_access_settings(client: Hetzner) -> ActionResponse:
    """Update Access Settings.

    ``POST /storage_boxes/{id}/actions/update_access_settings``

    Optional arguments: reachable_externally, samba_enabled, ssh_enabled, webdav_enabled,
    zfs_enabled.
    """
    return client.storage_box_actions.update_storage_box_access_settings(42)


def storage_box_actions_rollback_storage_box_snapshot(client: Hetzner) -> ActionResponse:
    """Rollback Snapshot.

    ``POST /storage_boxes/{id}/actions/rollback_snapshot``
    """
    return client.storage_box_actions.rollback_storage_box_snapshot(42, snapshot="my-snapshot")


def storage_box_actions_disable_storage_box_snapshot_plan(client: Hetzner) -> ActionResponse:
    """Disable Snapshot Plan.

    ``POST /storage_boxes/{id}/actions/disable_snapshot_plan``
    """
    return client.storage_box_actions.disable_storage_box_snapshot_plan(42)


def storage_box_actions_enable_storage_box_snapshot_plan(client: Hetzner) -> ActionResponse:
    """Enable Snapshot Plan.

    ``POST /storage_boxes/{id}/actions/enable_snapshot_plan``

    Optional arguments: day_of_week, day_of_month.
    """
    return client.storage_box_actions.enable_storage_box_snapshot_plan(
        42, max_snapshots=10, minute=30, hour=3
    )
