"""Examples for ``storage_box_subaccount_actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ActionResponse


def storage_box_subaccount_actions_change_storage_box_subaccount_h_97b567b6(
    client: Hetzner,
) -> ActionResponse:
    """Change Home Directory.

    ``POST /storage_boxes/{id}/subaccounts/{subaccount_id}/actions/change_home_directory``
    """
    return client.storage_box_subaccount_actions.change_storage_box_subaccount_home_directory(
        42, 42, home_directory="my-backup/server01"
    )


def storage_box_subaccount_actions_reset_storage_box_subaccount_password(
    client: Hetzner,
) -> ActionResponse:
    """Reset Password.

    ``POST /storage_boxes/{id}/subaccounts/{subaccount_id}/actions/reset_subaccount_password``
    """
    return client.storage_box_subaccount_actions.reset_storage_box_subaccount_password(
        42, 42, password="example"
    )


def storage_box_subaccount_actions_update_storage_box_subaccount_a_1dc3d20e(
    client: Hetzner,
) -> ActionResponse:
    """Update Access Settings.

    ``POST /storage_boxes/{id}/subaccounts/{subaccount_id}/actions/update_access_settings``

    Optional arguments: readonly, reachable_externally, samba_enabled, ssh_enabled, webdav_enabled.
    """
    return client.storage_box_subaccount_actions.update_storage_box_subaccount_access_settings(
        42, 42
    )
