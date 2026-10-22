"""Examples for ``volumes`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import CreateVolumeResponse, ListVolumesResponse, VolumeResponse


def volumes_list_volumes(client: Hetzner) -> ListVolumesResponse:
    """List Volumes.

    ``GET /volumes``

    Optional arguments: status, sort, name, label_selector, page, per_page.
    """
    return client.volumes.list_volumes()


def volumes_create_volume(client: Hetzner) -> CreateVolumeResponse:
    """Create a Volume.

    ``POST /volumes``

    Optional arguments: labels, automount, format, location, server.
    """
    return client.volumes.create_volume(size=42, name="databases-storage")


def volumes_get_volume(client: Hetzner) -> VolumeResponse:
    """Get a Volume.

    ``GET /volumes/{id}``
    """
    return client.volumes.get_volume(42)


def volumes_update_volume(client: Hetzner) -> VolumeResponse:
    """Update a Volume.

    ``PUT /volumes/{id}``

    Optional arguments: name, labels.
    """
    return client.volumes.update_volume(42)


def volumes_delete_volume(client: Hetzner) -> None:
    """Delete a Volume.

    ``DELETE /volumes/{id}``
    """
    client.volumes.delete_volume(42)
