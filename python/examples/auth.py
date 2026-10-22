"""Authentication: the credentials the client takes (generated example).

Each operation sends the credentials the spec asks for; pass the ones you have.
"""

from hetzner_api import Hetzner


def with_token() -> Hetzner:
    """``Authorization: Bearer <token>`` - without it, ``$HCLOUD_TOKEN`` is used."""
    return Hetzner(token="your-api-token")
