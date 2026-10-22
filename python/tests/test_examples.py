"""Every example in ``examples/operations`` runs against a simulated API."""

from examples.operations.actions import actions_get_action, actions_get_actions
from examples.operations.certificate_actions import (
    certificate_actions_get_certificates_action,
    certificate_actions_list_certificate_actions,
    certificate_actions_list_certificates_actions,
    certificate_actions_retry_certificate,
)
from examples.operations.certificates import (
    certificates_create_certificate,
    certificates_delete_certificate,
    certificates_get_certificate,
    certificates_list_certificates,
    certificates_update_certificate,
)
from examples.operations.firewall_actions import (
    firewall_actions_apply_firewall_to_resources,
    firewall_actions_get_firewalls_action,
    firewall_actions_list_firewall_actions,
    firewall_actions_list_firewalls_actions,
    firewall_actions_remove_firewall_from_resources,
    firewall_actions_set_firewall_rules,
)
from examples.operations.firewalls import (
    firewalls_create_firewall,
    firewalls_delete_firewall,
    firewalls_get_firewall,
    firewalls_list_firewalls,
    firewalls_update_firewall,
)
from examples.operations.floating_ip_actions import (
    floating_ip_actions_assign_floating_ip,
    floating_ip_actions_change_floating_ip_dns_ptr,
    floating_ip_actions_change_floating_ip_protection,
    floating_ip_actions_get_floating_ips_action,
    floating_ip_actions_list_floating_ip_actions,
    floating_ip_actions_list_floating_ips_actions,
    floating_ip_actions_unassign_floating_ip,
)
from examples.operations.floating_ips import (
    floating_ips_create_floating_ip,
    floating_ips_delete_floating_ip,
    floating_ips_get_floating_ip,
    floating_ips_list_floating_ips,
    floating_ips_update_floating_ip,
)
from examples.operations.image_actions import (
    image_actions_change_image_protection,
    image_actions_get_images_action,
    image_actions_list_image_actions,
    image_actions_list_images_actions,
)
from examples.operations.images import (
    images_delete_image,
    images_get_image,
    images_list_images,
    images_update_image,
)
from examples.operations.isos import isos_get_iso, isos_list_isos
from examples.operations.load_balancer_actions import (
    load_balancer_actions_add_load_balancer_service,
    load_balancer_actions_add_load_balancer_target,
    load_balancer_actions_attach_load_balancer_to_network,
    load_balancer_actions_change_load_balancer_algorithm,
    load_balancer_actions_change_load_balancer_dns_ptr,
    load_balancer_actions_change_load_balancer_protection,
    load_balancer_actions_change_load_balancer_type,
    load_balancer_actions_delete_load_balancer_service,
    load_balancer_actions_detach_load_balancer_from_network,
    load_balancer_actions_disable_load_balancer_public_interface,
    load_balancer_actions_enable_load_balancer_public_interface,
    load_balancer_actions_get_load_balancers_action,
    load_balancer_actions_list_load_balancer_actions,
    load_balancer_actions_list_load_balancers_actions,
    load_balancer_actions_remove_load_balancer_target,
    load_balancer_actions_update_load_balancer_service,
)
from examples.operations.load_balancer_types import (
    load_balancer_types_get_load_balancer_type,
    load_balancer_types_list_load_balancer_types,
)
from examples.operations.load_balancers import (
    load_balancers_create_load_balancer,
    load_balancers_delete_load_balancer,
    load_balancers_get_load_balancer,
    load_balancers_get_load_balancer_metrics,
    load_balancers_list_load_balancers,
    load_balancers_update_load_balancer,
)
from examples.operations.locations import locations_get_location, locations_list_locations
from examples.operations.network_actions import (
    network_actions_add_network_route,
    network_actions_add_network_subnet,
    network_actions_change_network_ip_range,
    network_actions_change_network_protection,
    network_actions_delete_network_route,
    network_actions_delete_network_subnet,
    network_actions_get_networks_action,
    network_actions_list_network_actions,
    network_actions_list_networks_actions,
)
from examples.operations.networks import (
    networks_create_network,
    networks_delete_network,
    networks_get_network,
    networks_list_network_members,
    networks_list_networks,
    networks_update_network,
)
from examples.operations.placement_groups import (
    placement_groups_create_placement_group,
    placement_groups_delete_placement_group,
    placement_groups_get_placement_group,
    placement_groups_list_placement_groups,
    placement_groups_update_placement_group,
)
from examples.operations.pricing import pricing_get_pricing
from examples.operations.primary_ip_actions import (
    primary_ip_actions_assign_primary_ip,
    primary_ip_actions_change_primary_ip_dns_ptr,
    primary_ip_actions_change_primary_ip_protection,
    primary_ip_actions_get_primary_ips_action,
    primary_ip_actions_list_primary_ip_actions,
    primary_ip_actions_list_primary_ips_actions,
    primary_ip_actions_unassign_primary_ip,
)
from examples.operations.primary_ips import (
    primary_ips_create_primary_ip,
    primary_ips_delete_primary_ip,
    primary_ips_get_primary_ip,
    primary_ips_list_primary_ips,
    primary_ips_update_primary_ip,
)
from examples.operations.server_actions import (
    server_actions_add_server_to_placement_group,
    server_actions_attach_server_iso,
    server_actions_attach_server_to_network,
    server_actions_change_server_alias_ips,
    server_actions_change_server_dns_ptr,
    server_actions_change_server_protection,
    server_actions_change_server_type,
    server_actions_create_server_image,
    server_actions_detach_server_from_network,
    server_actions_detach_server_iso,
    server_actions_disable_server_backup,
    server_actions_disable_server_rescue,
    server_actions_enable_server_backup,
    server_actions_enable_server_rescue,
    server_actions_get_servers_action,
    server_actions_list_server_actions,
    server_actions_list_servers_actions,
    server_actions_poweroff_server,
    server_actions_poweron_server,
    server_actions_reboot_server,
    server_actions_rebuild_server,
    server_actions_remove_server_from_placement_group,
    server_actions_request_server_console,
    server_actions_reset_server,
    server_actions_reset_server_password,
    server_actions_shutdown_server,
)
from examples.operations.server_types import (
    server_types_get_server_type,
    server_types_list_server_types,
)
from examples.operations.servers import (
    servers_create_server,
    servers_delete_server,
    servers_get_server,
    servers_get_server_metrics,
    servers_list_servers,
    servers_update_server,
)
from examples.operations.ssh_keys import (
    ssh_keys_create_ssh_key,
    ssh_keys_delete_ssh_key,
    ssh_keys_get_ssh_key,
    ssh_keys_list_ssh_keys,
    ssh_keys_update_ssh_key,
)
from examples.operations.storage_box_actions import (
    storage_box_actions_change_storage_box_protection,
    storage_box_actions_change_storage_box_type,
    storage_box_actions_disable_storage_box_snapshot_plan,
    storage_box_actions_enable_storage_box_snapshot_plan,
    storage_box_actions_get_storage_boxes_action,
    storage_box_actions_list_storage_box_actions,
    storage_box_actions_list_storage_boxes_actions,
    storage_box_actions_reset_storage_box_password,
    storage_box_actions_rollback_storage_box_snapshot,
    storage_box_actions_update_storage_box_access_settings,
)
from examples.operations.storage_box_snapshots import (
    storage_box_snapshots_create_storage_box_snapshot,
    storage_box_snapshots_delete_storage_box_snapshot,
    storage_box_snapshots_get_storage_box_snapshot,
    storage_box_snapshots_list_storage_box_snapshots,
    storage_box_snapshots_update_storage_box_snapshot,
)
from examples.operations.storage_box_subaccount_actions import (
    storage_box_subaccount_actions_change_storage_box_subaccount_h_97b567b6,
    storage_box_subaccount_actions_reset_storage_box_subaccount_password,
    storage_box_subaccount_actions_update_storage_box_subaccount_a_1dc3d20e,
)
from examples.operations.storage_box_subaccounts import (
    storage_box_subaccounts_create_storage_box_subaccount,
    storage_box_subaccounts_delete_storage_box_subaccount,
    storage_box_subaccounts_get_storage_box_subaccount,
    storage_box_subaccounts_list_storage_box_subaccounts,
    storage_box_subaccounts_update_storage_box_subaccount,
)
from examples.operations.storage_box_types import (
    storage_box_types_get_storage_box_type,
    storage_box_types_list_storage_box_types,
)
from examples.operations.storage_boxes import (
    storage_boxes_create_storage_box,
    storage_boxes_delete_storage_box,
    storage_boxes_get_storage_box,
    storage_boxes_list_storage_box_folders,
    storage_boxes_list_storage_boxes,
    storage_boxes_update_storage_box,
)
from examples.operations.volume_actions import (
    volume_actions_attach_volume,
    volume_actions_change_volume_protection,
    volume_actions_detach_volume,
    volume_actions_get_volumes_action,
    volume_actions_list_volume_actions,
    volume_actions_list_volumes_actions,
    volume_actions_resize_volume,
)
from examples.operations.volumes import (
    volumes_create_volume,
    volumes_delete_volume,
    volumes_get_volume,
    volumes_list_volumes,
    volumes_update_volume,
)
from examples.operations.zone_actions import (
    zone_actions_change_zone_primary_nameservers,
    zone_actions_change_zone_protection,
    zone_actions_change_zone_ttl,
    zone_actions_get_zones_action,
    zone_actions_import_zone_zonefile,
    zone_actions_list_zone_actions,
    zone_actions_list_zones_actions,
)
from examples.operations.zone_rrset_actions import (
    zone_rrset_actions_add_zone_rrset_records,
    zone_rrset_actions_change_zone_rrset_protection,
    zone_rrset_actions_change_zone_rrset_ttl,
    zone_rrset_actions_remove_zone_rrset_records,
    zone_rrset_actions_set_zone_rrset_records,
    zone_rrset_actions_update_zone_rrset_records,
)
from examples.operations.zone_rrsets import (
    zone_rrsets_create_zone_rrset,
    zone_rrsets_delete_zone_rrset,
    zone_rrsets_get_zone_rrset,
    zone_rrsets_list_zone_rrsets,
    zone_rrsets_update_zone_rrset,
)
from examples.operations.zones import (
    zones_create_zone,
    zones_delete_zone,
    zones_get_zone,
    zones_get_zone_zonefile,
    zones_list_zones,
    zones_update_zone,
)
from tests.payloads import (
    ACTION_LIST_RESPONSE,
    ACTION_LIST_RESPONSE_WITH_META,
    ACTION_RESPONSE,
    CERTIFICATE_RESPONSE,
    CERTIFICATES_RESPONSE,
    CREATE_CERTIFICATE_RESPONSE,
    CREATE_FIREWALL_RESPONSE,
    CREATE_FLOATING_IP_RESPONSE,
    CREATE_LOAD_BALANCER_RESPONSE,
    CREATE_PLACEMENT_GROUP_RESPONSE,
    CREATE_PRIMARY_IP_RESPONSE,
    CREATE_SERVER_IMAGE_RESPONSE,
    CREATE_SERVER_RESPONSE,
    CREATE_STORAGE_BOX_RESPONSE,
    CREATE_STORAGE_BOX_SNAPSHOT_RESPONSE,
    CREATE_STORAGE_BOX_SUBACCOUNT_RESPONSE,
    CREATE_VOLUME_RESPONSE,
    CREATE_ZONE_RESPONSE,
    CREATE_ZONE_RRSET_RESPONSE,
    FIREWALL_RESPONSE,
    FIREWALLS_RESPONSE,
    FLOATING_IP_RESPONSE,
    GET_ISO_RESPONSE,
    GET_LOAD_BALANCER_TYPE_RESPONSE,
    GET_LOCATION_RESPONSE,
    GET_PRICING_RESPONSE,
    GET_SERVER_TYPE_RESPONSE,
    GET_STORAGE_BOX_TYPE_RESPONSE,
    IMAGE_RESPONSE,
    LIST_FLOATING_IPS_RESPONSE,
    LIST_IMAGES_RESPONSE,
    LIST_ISOS_RESPONSE,
    LIST_LOAD_BALANCER_TYPES_RESPONSE,
    LIST_LOAD_BALANCERS_RESPONSE,
    LIST_LOCATIONS_RESPONSE,
    LIST_NETWORK_MEMBERS_RESPONSE,
    LIST_NETWORKS_RESPONSE,
    LIST_SERVER_TYPES_RESPONSE,
    LIST_SERVERS_RESPONSE,
    LIST_SSH_KEYS_RESPONSE,
    LIST_STORAGE_BOX_FOLDERS_RESPONSE,
    LIST_STORAGE_BOX_SNAPSHOTS_RESPONSE,
    LIST_STORAGE_BOX_SUBACCOUNTS_RESPONSE,
    LIST_STORAGE_BOX_TYPES_RESPONSE,
    LIST_STORAGE_BOXES_RESPONSE,
    LIST_VOLUMES_RESPONSE,
    LIST_ZONE_RRSETS_RESPONSE,
    LIST_ZONES_RESPONSE,
    LOAD_BALANCER_RESPONSE,
    METRICS_RESPONSE,
    NETWORK_RESPONSE,
    PLACEMENT_GROUP_RESPONSE,
    PLACEMENT_GROUPS_RESPONSE,
    PRIMARY_I_PS_RESPONSE,
    PRIMARY_IP_RESPONSE,
    REBUILD_SERVER_RESPONSE,
    REQUEST_SERVER_CONSOLE_RESPONSE,
    ROOT_PASSWORD_RESPONSE,
    RRSET_RESPONSE,
    SERVER_RESPONSE,
    SNAPSHOT_RESPONSE,
    SSH_KEY_RESPONSE,
    STORAGE_BOX_RESPONSE,
    SUBACCOUNT_RESPONSE,
    VOLUME_RESPONSE,
    ZONE_RESPONSE,
    ZONEFILE,
)
from tests.support import Recorder, sync_client


def test_actions_get_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE)
    with sync_client(recorder) as client:
        actions_get_actions(client)
    assert len(recorder.requests) == 1


def test_actions_get_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        actions_get_action(client)
    assert len(recorder.requests) == 1


def test_certificate_actions_list_certificates_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        certificate_actions_list_certificates_actions(client)
    assert len(recorder.requests) == 1


def test_certificate_actions_get_certificates_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        certificate_actions_get_certificates_action(client)
    assert len(recorder.requests) == 1


def test_certificate_actions_list_certificate_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        certificate_actions_list_certificate_actions(client)
    assert len(recorder.requests) == 1


def test_certificate_actions_retry_certificate() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        certificate_actions_retry_certificate(client)
    assert len(recorder.requests) == 1


def test_certificates_list_certificates() -> None:
    recorder = Recorder(200, CERTIFICATES_RESPONSE)
    with sync_client(recorder) as client:
        certificates_list_certificates(client)
    assert len(recorder.requests) == 1


def test_certificates_create_certificate() -> None:
    recorder = Recorder(200, CREATE_CERTIFICATE_RESPONSE)
    with sync_client(recorder) as client:
        certificates_create_certificate(client)
    assert len(recorder.requests) == 1


def test_certificates_get_certificate() -> None:
    recorder = Recorder(200, CERTIFICATE_RESPONSE)
    with sync_client(recorder) as client:
        certificates_get_certificate(client)
    assert len(recorder.requests) == 1


def test_certificates_update_certificate() -> None:
    recorder = Recorder(200, CERTIFICATE_RESPONSE)
    with sync_client(recorder) as client:
        certificates_update_certificate(client)
    assert len(recorder.requests) == 1


def test_certificates_delete_certificate() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        certificates_delete_certificate(client)
    assert len(recorder.requests) == 1


def test_firewall_actions_list_firewalls_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        firewall_actions_list_firewalls_actions(client)
    assert len(recorder.requests) == 1


def test_firewall_actions_get_firewalls_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        firewall_actions_get_firewalls_action(client)
    assert len(recorder.requests) == 1


def test_firewall_actions_list_firewall_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        firewall_actions_list_firewall_actions(client)
    assert len(recorder.requests) == 1


def test_firewall_actions_apply_firewall_to_resources() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE)
    with sync_client(recorder) as client:
        firewall_actions_apply_firewall_to_resources(client)
    assert len(recorder.requests) == 1


def test_firewall_actions_remove_firewall_from_resources() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE)
    with sync_client(recorder) as client:
        firewall_actions_remove_firewall_from_resources(client)
    assert len(recorder.requests) == 1


def test_firewall_actions_set_firewall_rules() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE)
    with sync_client(recorder) as client:
        firewall_actions_set_firewall_rules(client)
    assert len(recorder.requests) == 1


def test_firewalls_list_firewalls() -> None:
    recorder = Recorder(200, FIREWALLS_RESPONSE)
    with sync_client(recorder) as client:
        firewalls_list_firewalls(client)
    assert len(recorder.requests) == 1


def test_firewalls_create_firewall() -> None:
    recorder = Recorder(200, CREATE_FIREWALL_RESPONSE)
    with sync_client(recorder) as client:
        firewalls_create_firewall(client)
    assert len(recorder.requests) == 1


def test_firewalls_get_firewall() -> None:
    recorder = Recorder(200, FIREWALL_RESPONSE)
    with sync_client(recorder) as client:
        firewalls_get_firewall(client)
    assert len(recorder.requests) == 1


def test_firewalls_update_firewall() -> None:
    recorder = Recorder(200, FIREWALL_RESPONSE)
    with sync_client(recorder) as client:
        firewalls_update_firewall(client)
    assert len(recorder.requests) == 1


def test_firewalls_delete_firewall() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        firewalls_delete_firewall(client)
    assert len(recorder.requests) == 1


def test_floating_ip_actions_list_floating_ips_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        floating_ip_actions_list_floating_ips_actions(client)
    assert len(recorder.requests) == 1


def test_floating_ip_actions_get_floating_ips_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        floating_ip_actions_get_floating_ips_action(client)
    assert len(recorder.requests) == 1


def test_floating_ip_actions_list_floating_ip_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        floating_ip_actions_list_floating_ip_actions(client)
    assert len(recorder.requests) == 1


def test_floating_ip_actions_assign_floating_ip() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        floating_ip_actions_assign_floating_ip(client)
    assert len(recorder.requests) == 1


def test_floating_ip_actions_change_floating_ip_dns_ptr() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        floating_ip_actions_change_floating_ip_dns_ptr(client)
    assert len(recorder.requests) == 1


def test_floating_ip_actions_change_floating_ip_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        floating_ip_actions_change_floating_ip_protection(client)
    assert len(recorder.requests) == 1


def test_floating_ip_actions_unassign_floating_ip() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        floating_ip_actions_unassign_floating_ip(client)
    assert len(recorder.requests) == 1


def test_floating_ips_list_floating_ips() -> None:
    recorder = Recorder(200, LIST_FLOATING_IPS_RESPONSE)
    with sync_client(recorder) as client:
        floating_ips_list_floating_ips(client)
    assert len(recorder.requests) == 1


def test_floating_ips_create_floating_ip() -> None:
    recorder = Recorder(200, CREATE_FLOATING_IP_RESPONSE)
    with sync_client(recorder) as client:
        floating_ips_create_floating_ip(client)
    assert len(recorder.requests) == 1


def test_floating_ips_get_floating_ip() -> None:
    recorder = Recorder(200, FLOATING_IP_RESPONSE)
    with sync_client(recorder) as client:
        floating_ips_get_floating_ip(client)
    assert len(recorder.requests) == 1


def test_floating_ips_update_floating_ip() -> None:
    recorder = Recorder(200, FLOATING_IP_RESPONSE)
    with sync_client(recorder) as client:
        floating_ips_update_floating_ip(client)
    assert len(recorder.requests) == 1


def test_floating_ips_delete_floating_ip() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        floating_ips_delete_floating_ip(client)
    assert len(recorder.requests) == 1


def test_image_actions_list_images_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        image_actions_list_images_actions(client)
    assert len(recorder.requests) == 1


def test_image_actions_get_images_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        image_actions_get_images_action(client)
    assert len(recorder.requests) == 1


def test_image_actions_list_image_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        image_actions_list_image_actions(client)
    assert len(recorder.requests) == 1


def test_image_actions_change_image_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        image_actions_change_image_protection(client)
    assert len(recorder.requests) == 1


def test_images_list_images() -> None:
    recorder = Recorder(200, LIST_IMAGES_RESPONSE)
    with sync_client(recorder) as client:
        images_list_images(client)
    assert len(recorder.requests) == 1


def test_images_get_image() -> None:
    recorder = Recorder(200, IMAGE_RESPONSE)
    with sync_client(recorder) as client:
        images_get_image(client)
    assert len(recorder.requests) == 1


def test_images_update_image() -> None:
    recorder = Recorder(200, IMAGE_RESPONSE)
    with sync_client(recorder) as client:
        images_update_image(client)
    assert len(recorder.requests) == 1


def test_images_delete_image() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        images_delete_image(client)
    assert len(recorder.requests) == 1


def test_isos_list_isos() -> None:
    recorder = Recorder(200, LIST_ISOS_RESPONSE)
    with sync_client(recorder) as client:
        isos_list_isos(client)
    assert len(recorder.requests) == 1


def test_isos_get_iso() -> None:
    recorder = Recorder(200, GET_ISO_RESPONSE)
    with sync_client(recorder) as client:
        isos_get_iso(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_list_load_balancers_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        load_balancer_actions_list_load_balancers_actions(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_get_load_balancers_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_get_load_balancers_action(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_list_load_balancer_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        load_balancer_actions_list_load_balancer_actions(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_add_load_balancer_service() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_add_load_balancer_service(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_add_load_balancer_target() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_add_load_balancer_target(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_attach_load_balancer_to_network() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_attach_load_balancer_to_network(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_change_load_balancer_algorithm() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_change_load_balancer_algorithm(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_change_load_balancer_dns_ptr() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_change_load_balancer_dns_ptr(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_change_load_balancer_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_change_load_balancer_protection(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_change_load_balancer_type() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_change_load_balancer_type(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_delete_load_balancer_service() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_delete_load_balancer_service(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_detach_load_balancer_from_network() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_detach_load_balancer_from_network(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_disable_load_balancer_public_interface() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_disable_load_balancer_public_interface(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_enable_load_balancer_public_interface() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_enable_load_balancer_public_interface(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_remove_load_balancer_target() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_remove_load_balancer_target(client)
    assert len(recorder.requests) == 1


def test_load_balancer_actions_update_load_balancer_service() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_actions_update_load_balancer_service(client)
    assert len(recorder.requests) == 1


def test_load_balancer_types_list_load_balancer_types() -> None:
    recorder = Recorder(200, LIST_LOAD_BALANCER_TYPES_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_types_list_load_balancer_types(client)
    assert len(recorder.requests) == 1


def test_load_balancer_types_get_load_balancer_type() -> None:
    recorder = Recorder(200, GET_LOAD_BALANCER_TYPE_RESPONSE)
    with sync_client(recorder) as client:
        load_balancer_types_get_load_balancer_type(client)
    assert len(recorder.requests) == 1


def test_load_balancers_list_load_balancers() -> None:
    recorder = Recorder(200, LIST_LOAD_BALANCERS_RESPONSE)
    with sync_client(recorder) as client:
        load_balancers_list_load_balancers(client)
    assert len(recorder.requests) == 1


def test_load_balancers_create_load_balancer() -> None:
    recorder = Recorder(200, CREATE_LOAD_BALANCER_RESPONSE)
    with sync_client(recorder) as client:
        load_balancers_create_load_balancer(client)
    assert len(recorder.requests) == 1


def test_load_balancers_get_load_balancer() -> None:
    recorder = Recorder(200, LOAD_BALANCER_RESPONSE)
    with sync_client(recorder) as client:
        load_balancers_get_load_balancer(client)
    assert len(recorder.requests) == 1


def test_load_balancers_update_load_balancer() -> None:
    recorder = Recorder(200, LOAD_BALANCER_RESPONSE)
    with sync_client(recorder) as client:
        load_balancers_update_load_balancer(client)
    assert len(recorder.requests) == 1


def test_load_balancers_delete_load_balancer() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        load_balancers_delete_load_balancer(client)
    assert len(recorder.requests) == 1


def test_load_balancers_get_load_balancer_metrics() -> None:
    recorder = Recorder(200, METRICS_RESPONSE)
    with sync_client(recorder) as client:
        load_balancers_get_load_balancer_metrics(client)
    assert len(recorder.requests) == 1


def test_locations_list_locations() -> None:
    recorder = Recorder(200, LIST_LOCATIONS_RESPONSE)
    with sync_client(recorder) as client:
        locations_list_locations(client)
    assert len(recorder.requests) == 1


def test_locations_get_location() -> None:
    recorder = Recorder(200, GET_LOCATION_RESPONSE)
    with sync_client(recorder) as client:
        locations_get_location(client)
    assert len(recorder.requests) == 1


def test_network_actions_list_networks_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        network_actions_list_networks_actions(client)
    assert len(recorder.requests) == 1


def test_network_actions_get_networks_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        network_actions_get_networks_action(client)
    assert len(recorder.requests) == 1


def test_network_actions_list_network_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        network_actions_list_network_actions(client)
    assert len(recorder.requests) == 1


def test_network_actions_add_network_route() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        network_actions_add_network_route(client)
    assert len(recorder.requests) == 1


def test_network_actions_add_network_subnet() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        network_actions_add_network_subnet(client)
    assert len(recorder.requests) == 1


def test_network_actions_change_network_ip_range() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        network_actions_change_network_ip_range(client)
    assert len(recorder.requests) == 1


def test_network_actions_change_network_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        network_actions_change_network_protection(client)
    assert len(recorder.requests) == 1


def test_network_actions_delete_network_route() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        network_actions_delete_network_route(client)
    assert len(recorder.requests) == 1


def test_network_actions_delete_network_subnet() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        network_actions_delete_network_subnet(client)
    assert len(recorder.requests) == 1


def test_networks_list_networks() -> None:
    recorder = Recorder(200, LIST_NETWORKS_RESPONSE)
    with sync_client(recorder) as client:
        networks_list_networks(client)
    assert len(recorder.requests) == 1


def test_networks_create_network() -> None:
    recorder = Recorder(200, NETWORK_RESPONSE)
    with sync_client(recorder) as client:
        networks_create_network(client)
    assert len(recorder.requests) == 1


def test_networks_get_network() -> None:
    recorder = Recorder(200, NETWORK_RESPONSE)
    with sync_client(recorder) as client:
        networks_get_network(client)
    assert len(recorder.requests) == 1


def test_networks_update_network() -> None:
    recorder = Recorder(200, NETWORK_RESPONSE)
    with sync_client(recorder) as client:
        networks_update_network(client)
    assert len(recorder.requests) == 1


def test_networks_delete_network() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        networks_delete_network(client)
    assert len(recorder.requests) == 1


def test_networks_list_network_members() -> None:
    recorder = Recorder(200, LIST_NETWORK_MEMBERS_RESPONSE)
    with sync_client(recorder) as client:
        networks_list_network_members(client)
    assert len(recorder.requests) == 1


def test_placement_groups_list_placement_groups() -> None:
    recorder = Recorder(200, PLACEMENT_GROUPS_RESPONSE)
    with sync_client(recorder) as client:
        placement_groups_list_placement_groups(client)
    assert len(recorder.requests) == 1


def test_placement_groups_create_placement_group() -> None:
    recorder = Recorder(200, CREATE_PLACEMENT_GROUP_RESPONSE)
    with sync_client(recorder) as client:
        placement_groups_create_placement_group(client)
    assert len(recorder.requests) == 1


def test_placement_groups_get_placement_group() -> None:
    recorder = Recorder(200, PLACEMENT_GROUP_RESPONSE)
    with sync_client(recorder) as client:
        placement_groups_get_placement_group(client)
    assert len(recorder.requests) == 1


def test_placement_groups_update_placement_group() -> None:
    recorder = Recorder(200, PLACEMENT_GROUP_RESPONSE)
    with sync_client(recorder) as client:
        placement_groups_update_placement_group(client)
    assert len(recorder.requests) == 1


def test_placement_groups_delete_placement_group() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        placement_groups_delete_placement_group(client)
    assert len(recorder.requests) == 1


def test_pricing_get_pricing() -> None:
    recorder = Recorder(200, GET_PRICING_RESPONSE)
    with sync_client(recorder) as client:
        pricing_get_pricing(client)
    assert len(recorder.requests) == 1


def test_primary_ip_actions_list_primary_ips_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        primary_ip_actions_list_primary_ips_actions(client)
    assert len(recorder.requests) == 1


def test_primary_ip_actions_get_primary_ips_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        primary_ip_actions_get_primary_ips_action(client)
    assert len(recorder.requests) == 1


def test_primary_ip_actions_list_primary_ip_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        primary_ip_actions_list_primary_ip_actions(client)
    assert len(recorder.requests) == 1


def test_primary_ip_actions_assign_primary_ip() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        primary_ip_actions_assign_primary_ip(client)
    assert len(recorder.requests) == 1


def test_primary_ip_actions_change_primary_ip_dns_ptr() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        primary_ip_actions_change_primary_ip_dns_ptr(client)
    assert len(recorder.requests) == 1


def test_primary_ip_actions_change_primary_ip_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        primary_ip_actions_change_primary_ip_protection(client)
    assert len(recorder.requests) == 1


def test_primary_ip_actions_unassign_primary_ip() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        primary_ip_actions_unassign_primary_ip(client)
    assert len(recorder.requests) == 1


def test_primary_ips_list_primary_ips() -> None:
    recorder = Recorder(200, PRIMARY_I_PS_RESPONSE)
    with sync_client(recorder) as client:
        primary_ips_list_primary_ips(client)
    assert len(recorder.requests) == 1


def test_primary_ips_create_primary_ip() -> None:
    recorder = Recorder(200, CREATE_PRIMARY_IP_RESPONSE)
    with sync_client(recorder) as client:
        primary_ips_create_primary_ip(client)
    assert len(recorder.requests) == 1


def test_primary_ips_get_primary_ip() -> None:
    recorder = Recorder(200, PRIMARY_IP_RESPONSE)
    with sync_client(recorder) as client:
        primary_ips_get_primary_ip(client)
    assert len(recorder.requests) == 1


def test_primary_ips_update_primary_ip() -> None:
    recorder = Recorder(200, PRIMARY_IP_RESPONSE)
    with sync_client(recorder) as client:
        primary_ips_update_primary_ip(client)
    assert len(recorder.requests) == 1


def test_primary_ips_delete_primary_ip() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        primary_ips_delete_primary_ip(client)
    assert len(recorder.requests) == 1


def test_server_actions_list_servers_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        server_actions_list_servers_actions(client)
    assert len(recorder.requests) == 1


def test_server_actions_get_servers_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_get_servers_action(client)
    assert len(recorder.requests) == 1


def test_server_actions_list_server_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        server_actions_list_server_actions(client)
    assert len(recorder.requests) == 1


def test_server_actions_add_server_to_placement_group() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_add_server_to_placement_group(client)
    assert len(recorder.requests) == 1


def test_server_actions_attach_server_iso() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_attach_server_iso(client)
    assert len(recorder.requests) == 1


def test_server_actions_attach_server_to_network() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_attach_server_to_network(client)
    assert len(recorder.requests) == 1


def test_server_actions_change_server_alias_ips() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_change_server_alias_ips(client)
    assert len(recorder.requests) == 1


def test_server_actions_change_server_dns_ptr() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_change_server_dns_ptr(client)
    assert len(recorder.requests) == 1


def test_server_actions_change_server_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_change_server_protection(client)
    assert len(recorder.requests) == 1


def test_server_actions_change_server_type() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_change_server_type(client)
    assert len(recorder.requests) == 1


def test_server_actions_create_server_image() -> None:
    recorder = Recorder(200, CREATE_SERVER_IMAGE_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_create_server_image(client)
    assert len(recorder.requests) == 1


def test_server_actions_detach_server_from_network() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_detach_server_from_network(client)
    assert len(recorder.requests) == 1


def test_server_actions_detach_server_iso() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_detach_server_iso(client)
    assert len(recorder.requests) == 1


def test_server_actions_disable_server_backup() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_disable_server_backup(client)
    assert len(recorder.requests) == 1


def test_server_actions_disable_server_rescue() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_disable_server_rescue(client)
    assert len(recorder.requests) == 1


def test_server_actions_enable_server_backup() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_enable_server_backup(client)
    assert len(recorder.requests) == 1


def test_server_actions_enable_server_rescue() -> None:
    recorder = Recorder(200, ROOT_PASSWORD_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_enable_server_rescue(client)
    assert len(recorder.requests) == 1


def test_server_actions_poweroff_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_poweroff_server(client)
    assert len(recorder.requests) == 1


def test_server_actions_poweron_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_poweron_server(client)
    assert len(recorder.requests) == 1


def test_server_actions_reboot_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_reboot_server(client)
    assert len(recorder.requests) == 1


def test_server_actions_rebuild_server() -> None:
    recorder = Recorder(200, REBUILD_SERVER_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_rebuild_server(client)
    assert len(recorder.requests) == 1


def test_server_actions_remove_server_from_placement_group() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_remove_server_from_placement_group(client)
    assert len(recorder.requests) == 1


def test_server_actions_request_server_console() -> None:
    recorder = Recorder(200, REQUEST_SERVER_CONSOLE_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_request_server_console(client)
    assert len(recorder.requests) == 1


def test_server_actions_reset_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_reset_server(client)
    assert len(recorder.requests) == 1


def test_server_actions_reset_server_password() -> None:
    recorder = Recorder(200, ROOT_PASSWORD_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_reset_server_password(client)
    assert len(recorder.requests) == 1


def test_server_actions_shutdown_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        server_actions_shutdown_server(client)
    assert len(recorder.requests) == 1


def test_server_types_list_server_types() -> None:
    recorder = Recorder(200, LIST_SERVER_TYPES_RESPONSE)
    with sync_client(recorder) as client:
        server_types_list_server_types(client)
    assert len(recorder.requests) == 1


def test_server_types_get_server_type() -> None:
    recorder = Recorder(200, GET_SERVER_TYPE_RESPONSE)
    with sync_client(recorder) as client:
        server_types_get_server_type(client)
    assert len(recorder.requests) == 1


def test_servers_list_servers() -> None:
    recorder = Recorder(200, LIST_SERVERS_RESPONSE)
    with sync_client(recorder) as client:
        servers_list_servers(client)
    assert len(recorder.requests) == 1


def test_servers_create_server() -> None:
    recorder = Recorder(200, CREATE_SERVER_RESPONSE)
    with sync_client(recorder) as client:
        servers_create_server(client)
    assert len(recorder.requests) == 1


def test_servers_get_server() -> None:
    recorder = Recorder(200, SERVER_RESPONSE)
    with sync_client(recorder) as client:
        servers_get_server(client)
    assert len(recorder.requests) == 1


def test_servers_update_server() -> None:
    recorder = Recorder(200, SERVER_RESPONSE)
    with sync_client(recorder) as client:
        servers_update_server(client)
    assert len(recorder.requests) == 1


def test_servers_delete_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        servers_delete_server(client)
    assert len(recorder.requests) == 1


def test_servers_get_server_metrics() -> None:
    recorder = Recorder(200, METRICS_RESPONSE)
    with sync_client(recorder) as client:
        servers_get_server_metrics(client)
    assert len(recorder.requests) == 1


def test_ssh_keys_list_ssh_keys() -> None:
    recorder = Recorder(200, LIST_SSH_KEYS_RESPONSE)
    with sync_client(recorder) as client:
        ssh_keys_list_ssh_keys(client)
    assert len(recorder.requests) == 1


def test_ssh_keys_create_ssh_key() -> None:
    recorder = Recorder(200, SSH_KEY_RESPONSE)
    with sync_client(recorder) as client:
        ssh_keys_create_ssh_key(client)
    assert len(recorder.requests) == 1


def test_ssh_keys_get_ssh_key() -> None:
    recorder = Recorder(200, SSH_KEY_RESPONSE)
    with sync_client(recorder) as client:
        ssh_keys_get_ssh_key(client)
    assert len(recorder.requests) == 1


def test_ssh_keys_update_ssh_key() -> None:
    recorder = Recorder(200, SSH_KEY_RESPONSE)
    with sync_client(recorder) as client:
        ssh_keys_update_ssh_key(client)
    assert len(recorder.requests) == 1


def test_ssh_keys_delete_ssh_key() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        ssh_keys_delete_ssh_key(client)
    assert len(recorder.requests) == 1


def test_storage_box_actions_list_storage_boxes_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        storage_box_actions_list_storage_boxes_actions(client)
    assert len(recorder.requests) == 1


def test_storage_box_actions_get_storage_boxes_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_actions_get_storage_boxes_action(client)
    assert len(recorder.requests) == 1


def test_storage_box_actions_list_storage_box_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        storage_box_actions_list_storage_box_actions(client)
    assert len(recorder.requests) == 1


def test_storage_box_actions_change_storage_box_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_actions_change_storage_box_protection(client)
    assert len(recorder.requests) == 1


def test_storage_box_actions_change_storage_box_type() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_actions_change_storage_box_type(client)
    assert len(recorder.requests) == 1


def test_storage_box_actions_reset_storage_box_password() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_actions_reset_storage_box_password(client)
    assert len(recorder.requests) == 1


def test_storage_box_actions_update_storage_box_access_settings() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_actions_update_storage_box_access_settings(client)
    assert len(recorder.requests) == 1


def test_storage_box_actions_rollback_storage_box_snapshot() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_actions_rollback_storage_box_snapshot(client)
    assert len(recorder.requests) == 1


def test_storage_box_actions_disable_storage_box_snapshot_plan() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_actions_disable_storage_box_snapshot_plan(client)
    assert len(recorder.requests) == 1


def test_storage_box_actions_enable_storage_box_snapshot_plan() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_actions_enable_storage_box_snapshot_plan(client)
    assert len(recorder.requests) == 1


def test_storage_box_snapshots_list_storage_box_snapshots() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOX_SNAPSHOTS_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_snapshots_list_storage_box_snapshots(client)
    assert len(recorder.requests) == 1


def test_storage_box_snapshots_create_storage_box_snapshot() -> None:
    recorder = Recorder(200, CREATE_STORAGE_BOX_SNAPSHOT_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_snapshots_create_storage_box_snapshot(client)
    assert len(recorder.requests) == 1


def test_storage_box_snapshots_get_storage_box_snapshot() -> None:
    recorder = Recorder(200, SNAPSHOT_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_snapshots_get_storage_box_snapshot(client)
    assert len(recorder.requests) == 1


def test_storage_box_snapshots_update_storage_box_snapshot() -> None:
    recorder = Recorder(200, SNAPSHOT_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_snapshots_update_storage_box_snapshot(client)
    assert len(recorder.requests) == 1


def test_storage_box_snapshots_delete_storage_box_snapshot() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_snapshots_delete_storage_box_snapshot(client)
    assert len(recorder.requests) == 1


def test_storage_box_subaccount_actions_change_storage_box_subaccount_h_97b567b6() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_subaccount_actions_change_storage_box_subaccount_h_97b567b6(client)
    assert len(recorder.requests) == 1


def test_storage_box_subaccount_actions_reset_storage_box_subaccount_password() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_subaccount_actions_reset_storage_box_subaccount_password(client)
    assert len(recorder.requests) == 1


def test_storage_box_subaccount_actions_update_storage_box_subaccount_a_1dc3d20e() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_subaccount_actions_update_storage_box_subaccount_a_1dc3d20e(client)
    assert len(recorder.requests) == 1


def test_storage_box_subaccounts_list_storage_box_subaccounts() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOX_SUBACCOUNTS_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_subaccounts_list_storage_box_subaccounts(client)
    assert len(recorder.requests) == 1


def test_storage_box_subaccounts_create_storage_box_subaccount() -> None:
    recorder = Recorder(200, CREATE_STORAGE_BOX_SUBACCOUNT_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_subaccounts_create_storage_box_subaccount(client)
    assert len(recorder.requests) == 1


def test_storage_box_subaccounts_get_storage_box_subaccount() -> None:
    recorder = Recorder(200, SUBACCOUNT_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_subaccounts_get_storage_box_subaccount(client)
    assert len(recorder.requests) == 1


def test_storage_box_subaccounts_update_storage_box_subaccount() -> None:
    recorder = Recorder(200, SUBACCOUNT_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_subaccounts_update_storage_box_subaccount(client)
    assert len(recorder.requests) == 1


def test_storage_box_subaccounts_delete_storage_box_subaccount() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_subaccounts_delete_storage_box_subaccount(client)
    assert len(recorder.requests) == 1


def test_storage_box_types_list_storage_box_types() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOX_TYPES_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_types_list_storage_box_types(client)
    assert len(recorder.requests) == 1


def test_storage_box_types_get_storage_box_type() -> None:
    recorder = Recorder(200, GET_STORAGE_BOX_TYPE_RESPONSE)
    with sync_client(recorder) as client:
        storage_box_types_get_storage_box_type(client)
    assert len(recorder.requests) == 1


def test_storage_boxes_list_storage_boxes() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOXES_RESPONSE)
    with sync_client(recorder) as client:
        storage_boxes_list_storage_boxes(client)
    assert len(recorder.requests) == 1


def test_storage_boxes_create_storage_box() -> None:
    recorder = Recorder(200, CREATE_STORAGE_BOX_RESPONSE)
    with sync_client(recorder) as client:
        storage_boxes_create_storage_box(client)
    assert len(recorder.requests) == 1


def test_storage_boxes_get_storage_box() -> None:
    recorder = Recorder(200, STORAGE_BOX_RESPONSE)
    with sync_client(recorder) as client:
        storage_boxes_get_storage_box(client)
    assert len(recorder.requests) == 1


def test_storage_boxes_update_storage_box() -> None:
    recorder = Recorder(200, STORAGE_BOX_RESPONSE)
    with sync_client(recorder) as client:
        storage_boxes_update_storage_box(client)
    assert len(recorder.requests) == 1


def test_storage_boxes_delete_storage_box() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        storage_boxes_delete_storage_box(client)
    assert len(recorder.requests) == 1


def test_storage_boxes_list_storage_box_folders() -> None:
    recorder = Recorder(200, LIST_STORAGE_BOX_FOLDERS_RESPONSE)
    with sync_client(recorder) as client:
        storage_boxes_list_storage_box_folders(client)
    assert len(recorder.requests) == 1


def test_volume_actions_list_volumes_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        volume_actions_list_volumes_actions(client)
    assert len(recorder.requests) == 1


def test_volume_actions_get_volumes_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        volume_actions_get_volumes_action(client)
    assert len(recorder.requests) == 1


def test_volume_actions_list_volume_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        volume_actions_list_volume_actions(client)
    assert len(recorder.requests) == 1


def test_volume_actions_attach_volume() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        volume_actions_attach_volume(client)
    assert len(recorder.requests) == 1


def test_volume_actions_change_volume_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        volume_actions_change_volume_protection(client)
    assert len(recorder.requests) == 1


def test_volume_actions_detach_volume() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        volume_actions_detach_volume(client)
    assert len(recorder.requests) == 1


def test_volume_actions_resize_volume() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        volume_actions_resize_volume(client)
    assert len(recorder.requests) == 1


def test_volumes_list_volumes() -> None:
    recorder = Recorder(200, LIST_VOLUMES_RESPONSE)
    with sync_client(recorder) as client:
        volumes_list_volumes(client)
    assert len(recorder.requests) == 1


def test_volumes_create_volume() -> None:
    recorder = Recorder(200, CREATE_VOLUME_RESPONSE)
    with sync_client(recorder) as client:
        volumes_create_volume(client)
    assert len(recorder.requests) == 1


def test_volumes_get_volume() -> None:
    recorder = Recorder(200, VOLUME_RESPONSE)
    with sync_client(recorder) as client:
        volumes_get_volume(client)
    assert len(recorder.requests) == 1


def test_volumes_update_volume() -> None:
    recorder = Recorder(200, VOLUME_RESPONSE)
    with sync_client(recorder) as client:
        volumes_update_volume(client)
    assert len(recorder.requests) == 1


def test_volumes_delete_volume() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        volumes_delete_volume(client)
    assert len(recorder.requests) == 1


def test_zone_actions_list_zones_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        zone_actions_list_zones_actions(client)
    assert len(recorder.requests) == 1


def test_zone_actions_get_zones_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        zone_actions_get_zones_action(client)
    assert len(recorder.requests) == 1


def test_zone_actions_list_zone_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        zone_actions_list_zone_actions(client)
    assert len(recorder.requests) == 1


def test_zone_actions_change_zone_primary_nameservers() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        zone_actions_change_zone_primary_nameservers(client)
    assert len(recorder.requests) == 1


def test_zone_actions_change_zone_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        zone_actions_change_zone_protection(client)
    assert len(recorder.requests) == 1


def test_zone_actions_change_zone_ttl() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        zone_actions_change_zone_ttl(client)
    assert len(recorder.requests) == 1


def test_zone_actions_import_zone_zonefile() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        zone_actions_import_zone_zonefile(client)
    assert len(recorder.requests) == 1


def test_zone_rrset_actions_change_zone_rrset_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        zone_rrset_actions_change_zone_rrset_protection(client)
    assert len(recorder.requests) == 1


def test_zone_rrset_actions_change_zone_rrset_ttl() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        zone_rrset_actions_change_zone_rrset_ttl(client)
    assert len(recorder.requests) == 1


def test_zone_rrset_actions_set_zone_rrset_records() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        zone_rrset_actions_set_zone_rrset_records(client)
    assert len(recorder.requests) == 1


def test_zone_rrset_actions_add_zone_rrset_records() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        zone_rrset_actions_add_zone_rrset_records(client)
    assert len(recorder.requests) == 1


def test_zone_rrset_actions_remove_zone_rrset_records() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        zone_rrset_actions_remove_zone_rrset_records(client)
    assert len(recorder.requests) == 1


def test_zone_rrset_actions_update_zone_rrset_records() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        zone_rrset_actions_update_zone_rrset_records(client)
    assert len(recorder.requests) == 1


def test_zone_rrsets_list_zone_rrsets() -> None:
    recorder = Recorder(200, LIST_ZONE_RRSETS_RESPONSE)
    with sync_client(recorder) as client:
        zone_rrsets_list_zone_rrsets(client)
    assert len(recorder.requests) == 1


def test_zone_rrsets_create_zone_rrset() -> None:
    recorder = Recorder(200, CREATE_ZONE_RRSET_RESPONSE)
    with sync_client(recorder) as client:
        zone_rrsets_create_zone_rrset(client)
    assert len(recorder.requests) == 1


def test_zone_rrsets_get_zone_rrset() -> None:
    recorder = Recorder(200, RRSET_RESPONSE)
    with sync_client(recorder) as client:
        zone_rrsets_get_zone_rrset(client)
    assert len(recorder.requests) == 1


def test_zone_rrsets_update_zone_rrset() -> None:
    recorder = Recorder(200, RRSET_RESPONSE)
    with sync_client(recorder) as client:
        zone_rrsets_update_zone_rrset(client)
    assert len(recorder.requests) == 1


def test_zone_rrsets_delete_zone_rrset() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        zone_rrsets_delete_zone_rrset(client)
    assert len(recorder.requests) == 1


def test_zones_list_zones() -> None:
    recorder = Recorder(200, LIST_ZONES_RESPONSE)
    with sync_client(recorder) as client:
        zones_list_zones(client)
    assert len(recorder.requests) == 1


def test_zones_create_zone() -> None:
    recorder = Recorder(200, CREATE_ZONE_RESPONSE)
    with sync_client(recorder) as client:
        zones_create_zone(client)
    assert len(recorder.requests) == 1


def test_zones_get_zone() -> None:
    recorder = Recorder(200, ZONE_RESPONSE)
    with sync_client(recorder) as client:
        zones_get_zone(client)
    assert len(recorder.requests) == 1


def test_zones_update_zone() -> None:
    recorder = Recorder(200, ZONE_RESPONSE)
    with sync_client(recorder) as client:
        zones_update_zone(client)
    assert len(recorder.requests) == 1


def test_zones_delete_zone() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        zones_delete_zone(client)
    assert len(recorder.requests) == 1


def test_zones_get_zone_zonefile() -> None:
    recorder = Recorder(200, ZONEFILE)
    with sync_client(recorder) as client:
        zones_get_zone_zonefile(client)
    assert len(recorder.requests) == 1
