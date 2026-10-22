"""Every server function returns its base URL."""

from hetzner_api import servers


def test_servers() -> None:
    assert servers.cloud() == "https://api.hetzner.cloud/v1"
    assert servers.hetzner() == "https://api.hetzner.com/v1"
