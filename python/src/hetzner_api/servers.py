"""Servers of the API: base URLs for the ``*_base_url`` arguments of the client.

Generated - do not edit by hand.
"""

__all__ = [
    "cloud",
    "hetzner",
]


def cloud() -> str:
    """A server of the API.

    ``https://api.hetzner.cloud/v1``
    """
    return "https://api.hetzner.cloud/v1"


def hetzner() -> str:
    """A server of the API.

    ``https://api.hetzner.com/v1``
    """
    return "https://api.hetzner.com/v1"
