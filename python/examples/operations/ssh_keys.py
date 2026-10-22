"""Examples for ``ssh_keys`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import ListSshKeysResponse, SshKeyResponse


def ssh_keys_list_ssh_keys(client: Hetzner) -> ListSshKeysResponse:
    """List SSH keys.

    ``GET /ssh_keys``

    Optional arguments: sort, name, fingerprint, label_selector, page, per_page.
    """
    return client.ssh_keys.list_ssh_keys()


def ssh_keys_create_ssh_key(client: Hetzner) -> SshKeyResponse:
    """Create an SSH key.

    ``POST /ssh_keys``

    Optional arguments: labels.
    """
    return client.ssh_keys.create_ssh_key(name="My ssh key", public_key="ssh-rsa AAAjjk76kgf...Xt")


def ssh_keys_get_ssh_key(client: Hetzner) -> SshKeyResponse:
    """Get a SSH key.

    ``GET /ssh_keys/{id}``
    """
    return client.ssh_keys.get_ssh_key(42)


def ssh_keys_update_ssh_key(client: Hetzner) -> SshKeyResponse:
    """Update an SSH key.

    ``PUT /ssh_keys/{id}``

    Optional arguments: name, labels.
    """
    return client.ssh_keys.update_ssh_key(42)


def ssh_keys_delete_ssh_key(client: Hetzner) -> None:
    """Delete an SSH key.

    ``DELETE /ssh_keys/{id}``
    """
    client.ssh_keys.delete_ssh_key(42)
