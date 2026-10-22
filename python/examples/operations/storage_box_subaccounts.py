"""Examples for ``storage_box_subaccounts`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import (
    ActionResponse,
    CreateStorageBoxSubaccountResponse,
    ListStorageBoxSubaccountsResponse,
    SubaccountResponse,
)


def storage_box_subaccounts_list_storage_box_subaccounts(
    client: Hetzner,
) -> ListStorageBoxSubaccountsResponse:
    """List Subaccounts.

    ``GET /storage_boxes/{id}/subaccounts``

    Optional arguments: name, label_selector, sort, username.
    """
    return client.storage_box_subaccounts.list_storage_box_subaccounts(42)


def storage_box_subaccounts_create_storage_box_subaccount(
    client: Hetzner,
) -> CreateStorageBoxSubaccountResponse:
    """Create a Subaccount.

    ``POST /storage_boxes/{id}/subaccounts``

    Optional arguments: access_settings, name, description, labels.
    """
    return client.storage_box_subaccounts.create_storage_box_subaccount(
        42, home_directory="my-backup/server01", password="example"
    )


def storage_box_subaccounts_get_storage_box_subaccount(client: Hetzner) -> SubaccountResponse:
    """Get a Subaccount.

    ``GET /storage_boxes/{id}/subaccounts/{subaccount_id}``
    """
    return client.storage_box_subaccounts.get_storage_box_subaccount(42, 42)


def storage_box_subaccounts_update_storage_box_subaccount(client: Hetzner) -> SubaccountResponse:
    """Update a Subaccount.

    ``PUT /storage_boxes/{id}/subaccounts/{subaccount_id}``

    Optional arguments: name, description, labels.
    """
    return client.storage_box_subaccounts.update_storage_box_subaccount(42, 42)


def storage_box_subaccounts_delete_storage_box_subaccount(client: Hetzner) -> ActionResponse:
    """Delete a Subaccount.

    ``DELETE /storage_boxes/{id}/subaccounts/{subaccount_id}``
    """
    return client.storage_box_subaccounts.delete_storage_box_subaccount(42, 42)
