"""Read-only tests against the real API (GET requests only).

They hold real responses to the spec (``validation="strict"``: types and rules such as
``maxLength``). Skipped unless a token is set:
``HCLOUD_TOKEN=... uv run pytest -m live``.
"""

import os
from collections.abc import Iterator

import pytest

from hetzner_api import Hetzner

pytestmark = [
    pytest.mark.live,
    pytest.mark.skipif(not os.environ.get("HCLOUD_TOKEN"), reason="no API token"),
]


@pytest.fixture(scope="module")
def client() -> Iterator[Hetzner]:
    token = os.environ["HCLOUD_TOKEN"]
    with Hetzner(token=token, validation="strict") as live_client:
        yield live_client


def test_certificate_actions_list_certificates_actions(client: Hetzner) -> None:
    client.certificate_actions.list_certificates_actions()


def test_certificates_list_certificates(client: Hetzner) -> None:
    client.certificates.list_certificates()


def test_firewall_actions_list_firewalls_actions(client: Hetzner) -> None:
    client.firewall_actions.list_firewalls_actions()


def test_firewalls_list_firewalls(client: Hetzner) -> None:
    client.firewalls.list_firewalls()


def test_floating_ip_actions_list_floating_ips_actions(client: Hetzner) -> None:
    client.floating_ip_actions.list_floating_ips_actions()


def test_floating_ips_list_floating_ips(client: Hetzner) -> None:
    client.floating_ips.list_floating_ips()


def test_image_actions_list_images_actions(client: Hetzner) -> None:
    client.image_actions.list_images_actions()


def test_images_list_images(client: Hetzner) -> None:
    client.images.list_images()


def test_isos_list_isos(client: Hetzner) -> None:
    client.isos.list_isos()


def test_load_balancer_actions_list_load_balancers_actions(client: Hetzner) -> None:
    client.load_balancer_actions.list_load_balancers_actions()


def test_load_balancer_types_list_load_balancer_types(client: Hetzner) -> None:
    client.load_balancer_types.list_load_balancer_types()


def test_load_balancers_list_load_balancers(client: Hetzner) -> None:
    client.load_balancers.list_load_balancers()


def test_locations_list_locations(client: Hetzner) -> None:
    client.locations.list_locations()


def test_network_actions_list_networks_actions(client: Hetzner) -> None:
    client.network_actions.list_networks_actions()


def test_networks_list_networks(client: Hetzner) -> None:
    client.networks.list_networks()


def test_placement_groups_list_placement_groups(client: Hetzner) -> None:
    client.placement_groups.list_placement_groups()


def test_pricing_get_pricing(client: Hetzner) -> None:
    client.pricing.get_pricing()


def test_primary_ip_actions_list_primary_ips_actions(client: Hetzner) -> None:
    client.primary_ip_actions.list_primary_ips_actions()


def test_primary_ips_list_primary_ips(client: Hetzner) -> None:
    client.primary_ips.list_primary_ips()


def test_server_actions_list_servers_actions(client: Hetzner) -> None:
    client.server_actions.list_servers_actions()


def test_server_types_list_server_types(client: Hetzner) -> None:
    client.server_types.list_server_types()


def test_servers_list_servers(client: Hetzner) -> None:
    client.servers.list_servers()


def test_ssh_keys_list_ssh_keys(client: Hetzner) -> None:
    client.ssh_keys.list_ssh_keys()


def test_storage_box_actions_list_storage_boxes_actions(client: Hetzner) -> None:
    client.storage_box_actions.list_storage_boxes_actions()


def test_storage_box_types_list_storage_box_types(client: Hetzner) -> None:
    client.storage_box_types.list_storage_box_types()


def test_storage_boxes_list_storage_boxes(client: Hetzner) -> None:
    client.storage_boxes.list_storage_boxes()


def test_volume_actions_list_volumes_actions(client: Hetzner) -> None:
    client.volume_actions.list_volumes_actions()


def test_volumes_list_volumes(client: Hetzner) -> None:
    client.volumes.list_volumes()


def test_zone_actions_list_zones_actions(client: Hetzner) -> None:
    client.zone_actions.list_zones_actions()


def test_zones_list_zones(client: Hetzner) -> None:
    client.zones.list_zones()
