"""Examples for ``server_actions`` - one function per operation (generated).

Each function makes one real request with example values from the spec: copy what
you need. ``tests/test_examples.py`` runs them against a simulated API.
"""

from hetzner_api import Hetzner
from hetzner_api.models import (
    ActionListResponseWithMeta,
    ActionResponse,
    CreateServerImageResponse,
    RebuildServerResponse,
    RequestServerConsoleResponse,
    RootPasswordResponse,
)


def server_actions_list_servers_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions.

    ``GET /servers/actions``

    Optional arguments: id, sort, status, page, per_page.
    """
    return client.server_actions.list_servers_actions()


def server_actions_get_servers_action(client: Hetzner) -> ActionResponse:
    """Get an Action.

    ``GET /servers/actions/{id}``
    """
    return client.server_actions.get_servers_action(42)


def server_actions_list_server_actions(client: Hetzner) -> ActionListResponseWithMeta:
    """List Actions for a Server.

    ``GET /servers/{id}/actions``

    Optional arguments: sort, status, page, per_page.
    """
    return client.server_actions.list_server_actions(42)


def server_actions_add_server_to_placement_group(client: Hetzner) -> ActionResponse:
    """Add a Server to a Placement Group.

    ``POST /servers/{id}/actions/add_to_placement_group``
    """
    return client.server_actions.add_server_to_placement_group(42, placement_group=1)


def server_actions_attach_server_iso(client: Hetzner) -> ActionResponse:
    """Attach an ISO to a Server.

    ``POST /servers/{id}/actions/attach_iso``
    """
    return client.server_actions.attach_server_iso(42, iso="FreeBSD-11.0-RELEASE-amd64-dvd1")


def server_actions_attach_server_to_network(client: Hetzner) -> ActionResponse:
    """Attach a Server to a Network.

    ``POST /servers/{id}/actions/attach_to_network``

    Optional arguments: ip, alias_ips, ip_range.
    """
    return client.server_actions.attach_server_to_network(42, network=4711)


def server_actions_change_server_alias_ips(client: Hetzner) -> ActionResponse:
    """Change alias IPs of a Network.

    ``POST /servers/{id}/actions/change_alias_ips``
    """
    return client.server_actions.change_server_alias_ips(42, network=4711, alias_ips=["10.0.1.2"])


def server_actions_change_server_dns_ptr(client: Hetzner) -> ActionResponse:
    """Change reverse DNS entry for this Server.

    ``POST /servers/{id}/actions/change_dns_ptr``
    """
    return client.server_actions.change_server_dns_ptr(
        42, ip="2001:db8::1", dns_ptr="server.example.com"
    )


def server_actions_change_server_protection(client: Hetzner) -> ActionResponse:
    """Change Server Protection.

    ``POST /servers/{id}/actions/change_protection``

    Optional arguments: delete, rebuild.
    """
    return client.server_actions.change_server_protection(42)


def server_actions_change_server_type(client: Hetzner) -> ActionResponse:
    """Change the Type of a Server.

    ``POST /servers/{id}/actions/change_type``
    """
    return client.server_actions.change_server_type(42, upgrade_disk=True, server_type="cpx22")


def server_actions_create_server_image(client: Hetzner) -> CreateServerImageResponse:
    """Create Image from a Server.

    ``POST /servers/{id}/actions/create_image``

    Optional arguments: description, type, labels.
    """
    return client.server_actions.create_server_image(42)


def server_actions_detach_server_from_network(client: Hetzner) -> ActionResponse:
    """Detach a Server from a Network.

    ``POST /servers/{id}/actions/detach_from_network``
    """
    return client.server_actions.detach_server_from_network(42, network=4711)


def server_actions_detach_server_iso(client: Hetzner) -> ActionResponse:
    """Detach an ISO from a Server.

    ``POST /servers/{id}/actions/detach_iso``
    """
    return client.server_actions.detach_server_iso(42)


def server_actions_disable_server_backup(client: Hetzner) -> ActionResponse:
    """Disable Backups for a Server.

    ``POST /servers/{id}/actions/disable_backup``
    """
    return client.server_actions.disable_server_backup(42)


def server_actions_disable_server_rescue(client: Hetzner) -> ActionResponse:
    """Disable Rescue Mode for a Server.

    ``POST /servers/{id}/actions/disable_rescue``
    """
    return client.server_actions.disable_server_rescue(42)


def server_actions_enable_server_backup(client: Hetzner) -> ActionResponse:
    """Enable and Configure Backups for a Server.

    ``POST /servers/{id}/actions/enable_backup``
    """
    return client.server_actions.enable_server_backup(42)


def server_actions_enable_server_rescue(client: Hetzner) -> RootPasswordResponse:
    """Enable Rescue Mode for a Server.

    ``POST /servers/{id}/actions/enable_rescue``

    Optional arguments: type, ssh_keys.
    """
    return client.server_actions.enable_server_rescue(42)


def server_actions_poweroff_server(client: Hetzner) -> ActionResponse:
    """Power off a Server.

    ``POST /servers/{id}/actions/poweroff``
    """
    return client.server_actions.poweroff_server(42)


def server_actions_poweron_server(client: Hetzner) -> ActionResponse:
    """Power on a Server.

    ``POST /servers/{id}/actions/poweron``
    """
    return client.server_actions.poweron_server(42)


def server_actions_reboot_server(client: Hetzner) -> ActionResponse:
    """Soft-reboot a Server.

    ``POST /servers/{id}/actions/reboot``
    """
    return client.server_actions.reboot_server(42)


def server_actions_rebuild_server(client: Hetzner) -> RebuildServerResponse:
    """Rebuild a Server from an Image.

    ``POST /servers/{id}/actions/rebuild``

    Optional arguments: user_data.
    """
    return client.server_actions.rebuild_server(42, image="ubuntu-24.04")


def server_actions_remove_server_from_placement_group(client: Hetzner) -> ActionResponse:
    """Remove from Placement Group.

    ``POST /servers/{id}/actions/remove_from_placement_group``
    """
    return client.server_actions.remove_server_from_placement_group(42)


def server_actions_request_server_console(client: Hetzner) -> RequestServerConsoleResponse:
    """Request Console for a Server.

    ``POST /servers/{id}/actions/request_console``
    """
    return client.server_actions.request_server_console(42)


def server_actions_reset_server(client: Hetzner) -> ActionResponse:
    """Reset a Server.

    ``POST /servers/{id}/actions/reset``
    """
    return client.server_actions.reset_server(42)


def server_actions_reset_server_password(client: Hetzner) -> RootPasswordResponse:
    """Reset root Password of a Server.

    ``POST /servers/{id}/actions/reset_password``
    """
    return client.server_actions.reset_server_password(42)


def server_actions_shutdown_server(client: Hetzner) -> ActionResponse:
    """Shutdown a Server.

    ``POST /servers/{id}/actions/shutdown``
    """
    return client.server_actions.shutdown_server(42)
