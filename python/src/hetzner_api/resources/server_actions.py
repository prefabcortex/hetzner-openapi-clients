"""Resource ``server_actions`` (generated - do not edit by hand)."""

from collections.abc import Mapping, Sequence
from typing import Final, Literal
from warnings import deprecated

from hetzner_api._auth import Security
from hetzner_api._base_client import (
    AsyncTransport,
    SyncTransport,
    encode_body,
    encode_path,
    encode_query,
)
from hetzner_api._types import NOT_GIVEN, NotGiven, StrSequence, UnknownValue
from hetzner_api._validation import Check
from hetzner_api.errors import ErrorModels
from hetzner_api.models import (
    ActionListResponseWithMeta,
    ActionResponse,
    ActionSort,
    ActionStatus,
    CreateImageRequestType,
    CreateServerImageResponse,
    ErrorResponse,
    RebuildServerResponse,
    RequestServerConsoleResponse,
    RootPasswordResponse,
)
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "AsyncServerActionsResource",
    "ServerActionsResource",
]

_SECURITY_1: Final[Security] = (("APIToken",),)

_ERRORS_1: Final[ErrorModels] = {
    "4XX": ErrorResponse,
    "5XX": ErrorResponse,
}

_CHECKS_1: Final[Mapping[str, Check]] = {
    "id": Check(items=Check(minimum=1, maximum=9007199254740991)),
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}

_CHECKS_2: Final[Mapping[str, Check]] = {
    "action_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_3: Final[Mapping[str, Check]] = {
    "server_id": Check(minimum=1, maximum=9007199254740991),
    "page": Check(minimum=1),
    "per_page": Check(minimum=1, maximum=50),
}

_CHECKS_4: Final[Mapping[str, Check]] = {
    "server_id": Check(minimum=1, maximum=9007199254740991),
}

_CHECKS_5: Final[Mapping[str, Check]] = {
    "server_id": Check(minimum=1, maximum=9007199254740991),
    "labels": LABELS_RULES,
}

_CHECKS_6: Final[Mapping[str, Check]] = {
    "server_id": Check(minimum=1, maximum=9007199254740991),
    "action_id": Check(minimum=1, maximum=9007199254740991),
}


class ServerActionsResource:
    """Operations on ``server_actions`` (synchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: SyncTransport) -> None:
        self._transport: Final = transport

    def list_servers_actions(
        self,
        *,
        id: Sequence[int] | None = None,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions.

        Returns all Action objects. You can `sort` the results by using the sort URI parameter, and
        filter them with the `status` and `id` parameter.

        ``GET /servers/actions``

        Args:
            id: Filter the actions by ID. May be used multiple times. The response will only contain
                actions matching the specified IDs.
            sort: Sort actions by field and direction. May be used multiple times. For more
                information, see "Sorting".
            status: Filter the actions by status. May be used multiple times. The response will only
                contain actions matching the specified statuses.
            page: Page number to return. For more information, see "Pagination". The API default is
                ``1``.
            per_page: Maximum number of entries returned per page. For more information, see
                "Pagination". The API default is ``25``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, id=id, page=page, per_page=per_page)
        response = self._transport.request(
            "GET",
            "/servers/actions",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "id": id,
                    "sort": sort,
                    "status": status,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ActionListResponseWithMeta, response)

    def get_servers_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action object.

        ``GET /servers/actions/{id}``

        Args:
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, action_id=action_id)
        response = self._transport.request(
            "GET",
            f"/servers/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def list_server_actions(
        self,
        server_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Server.

        Returns all Action objects for a Server. You can `sort` the results by using the sort URI
        parameter, and filter them with the `status` parameter.

        ``GET /servers/{id}/actions``

        Args:
            server_id: ID of the Server.
            sort: Sort actions by field and direction. May be used multiple times. For more
                information, see "Sorting".
            status: Filter the actions by status. May be used multiple times. The response will only
                contain actions matching the specified statuses.
            page: Page number to return. For more information, see "Pagination". The API default is
                ``1``.
            per_page: Maximum number of entries returned per page. For more information, see
                "Pagination". The API default is ``25``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, server_id=server_id, page=page, per_page=per_page)
        response = self._transport.request(
            "GET",
            f"/servers/{encode_path(server_id)}/actions",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "status": status,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ActionListResponseWithMeta, response)

    def add_server_to_placement_group(
        self,
        server_id: int,
        /,
        *,
        placement_group: int,
    ) -> ActionResponse:
        """Add a Server to a Placement Group.

        Adds a Server to a Placement Group.

        Server must be powered off for this command to succeed.

        **Operation specific errors**

        - `422` - `server_not_stopped` - The action requires a stopped server
        - `422` - `already_in_placement_group` - The server is already part of a placement group

        ``POST /servers/{id}/actions/add_to_placement_group``

        Args:
            server_id: ID of the Server.
            placement_group: ID of Placement Group the Server should be added to.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/add_to_placement_group",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "placement_group": placement_group,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def attach_server_iso(self, server_id: int, /, *, iso: str | int) -> ActionResponse:
        """Attach an ISO to a Server.

        Attaches an ISO to a Server. The Server will immediately see it as a new disk. An already
        attached ISO will automatically be detached before the new ISO is attached.

        Servers with attached ISOs have a modified boot order: They will try to boot from the ISO
        first before falling back to hard disk.

        ``POST /servers/{id}/actions/attach_iso``

        Args:
            server_id: ID of the Server.
            iso: ID or name of ISO to attach to the Server as listed in GET `/isos`.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/attach_iso",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "iso": iso,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def attach_server_to_network(
        self,
        server_id: int,
        /,
        *,
        network: int,
        ip: str | NotGiven = NOT_GIVEN,
        alias_ips: StrSequence | NotGiven = NOT_GIVEN,
        ip_range: str | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Attach a Server to a Network.

        Attaches a Server to a network. This will complement the fixed public Server interface by
        adding an additional ethernet interface to the Server which is connected to the specified
        network.

        The Server will get an IP auto assigned from a subnet of type `server` in the same
        `network_zone`.

        Using the `alias_ips` attribute you can also define one or more additional IPs to the
        Servers. Please note that you will have to configure these IPs by hand on your Server since
        only the primary IP will be given out by DHCP.

        **Operation specific errors**

        - `422` - `server_already_attached` - The server is already attached to the network
        - `422` - `ip_not_available` - The provided Network IP is not available
        - `422` - `no_subnet_available` - No Subnet or IP is available for the Server within the
          network
        - `422` - `networks_overlap` - The network IP range overlaps with one of the server networks

        ``POST /servers/{id}/actions/attach_to_network``

        Args:
            server_id: ID of the Server.
            network: ID of an existing network to attach the Server to.
            ip: IP to request to be assigned to this Server; if you do not provide this then you
                will be auto assigned an IP address. Omitted if not given.
            alias_ips: Additional IPs to be assigned to this Server. Omitted if not given.
            ip_range: IP range in CIDR block notation of the subnet to attach to. This allows for
                auto assigning an IP address for a specific subnet. Providing `ip` that is not part
                of `ip_range` will result in an error. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/attach_to_network",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "network": network,
                    "ip": ip,
                    "alias_ips": alias_ips,
                    "ip_range": ip_range,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_server_alias_ips(
        self,
        server_id: int,
        /,
        *,
        network: int,
        alias_ips: StrSequence,
    ) -> ActionResponse:
        """Change alias IPs of a Network.

        Changes the alias IPs of an already attached Network. Note that the existing aliases for the
        specified Network will be replaced with these provided in the request body. So if you want
        to add an alias IP, you have to provide the existing ones from the Network plus the new
        alias IP in the request body.

        ``POST /servers/{id}/actions/change_alias_ips``

        Args:
            server_id: ID of the Server.
            network: ID of an existing Network already attached to the Server.
            alias_ips: New alias IPs to set for this Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/change_alias_ips",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "network": network,
                    "alias_ips": alias_ips,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_server_dns_ptr(
        self,
        server_id: int,
        /,
        *,
        ip: str,
        dns_ptr: str | None,
    ) -> ActionResponse:
        """Change reverse DNS entry for this Server.

        Changes the hostname that will appear when getting the hostname belonging to the primary IPs
        (IPv4 and IPv6) of this Server.

        Floating IPs assigned to the Server are not affected by this.

        ``POST /servers/{id}/actions/change_dns_ptr``

        Args:
            server_id: ID of the Server.
            ip: Single IPv4 or IPv6 address to create pointer for.
            dns_ptr: Domain Name to point to. PTR record content used for reverse DNS. Set to null
                to reset (IPv4) to the default value or remove (IPv6) the record.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/change_dns_ptr",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ip": ip,
                    "dns_ptr": dns_ptr,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_server_protection(
        self,
        server_id: int,
        /,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
        rebuild: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Change Server Protection.

        Changes the protection configuration of the Server.

        ``POST /servers/{id}/actions/change_protection``

        Args:
            server_id: ID of the Server.
            delete: If true, prevents the Server from being deleted (currently delete and rebuild
                attribute needs to have the same value). Omitted if not given.
            rebuild: If true, prevents the Server from being rebuilt (currently delete and rebuild
                attribute needs to have the same value). Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                    "rebuild": rebuild,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def change_server_type(
        self,
        server_id: int,
        /,
        *,
        upgrade_disk: bool,
        server_type: str | int,
    ) -> ActionResponse:
        """Change the Type of a Server.

        Changes the type (Cores, RAM and disk sizes) of a Server.

        Server must be powered off for this command to succeed.

        This copies the content of its disk, and starts it again.

        You can only migrate to Server types with the same `storage_type` and equal or bigger disks.
        Shrinking disks is not possible as it might destroy data.

        If the disk gets upgraded, the Server type can not be downgraded any more. If you plan to
        downgrade the Server type, set `upgrade_disk` to `false`.

        **Operation specific errors**

        - `422` - `invalid_server_type` - The server type does not fit for the given server or is
          deprecated
        - `422` - `server_not_stopped` - The action requires a stopped server

        ``POST /servers/{id}/actions/change_type``

        Args:
            server_id: ID of the Server.
            upgrade_disk: If false, do not upgrade the disk (this allows downgrading the Server type
                later).
            server_type: ID or name of Server type the Server should migrate to.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/change_type",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "upgrade_disk": upgrade_disk,
                    "server_type": server_type,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def create_server_image(
        self,
        server_id: int,
        /,
        *,
        description: str | NotGiven = NOT_GIVEN,
        type: CreateImageRequestType | UnknownValue | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CreateServerImageResponse:
        """Create Image from a Server.

        Creates an Image (snapshot) from a Server by copying the contents of its disks. This creates
        a snapshot of the current state of the disk and copies it into an Image. If the Server is
        currently running you must make sure that its disk content is consistent. Otherwise, the
        created Image may not be readable.

        To make sure disk content is consistent, we recommend to shut down the Server prior to
        creating an Image.

        You can either create a `backup` Image that is bound to the Server and therefore will be
        deleted when the Server is deleted, or you can create a `snapshot` Image which is completely
        independent of the Server it was created from and will survive Server deletion. Backup
        Images are only available when the backup option is enabled for the Server. Snapshot Images
        are billed on a per GB basis.

        ``POST /servers/{id}/actions/create_image``

        Args:
            server_id: ID of the Server.
            description: Description of the Image, will be auto-generated if not set. Omitted if not
                given.
            type: Type of Image to create. Omitted if not given. The API default is ``"snapshot"``.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, server_id=server_id, labels=labels)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/create_image",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "description": description,
                    "type": type,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(CreateServerImageResponse, response)

    def detach_server_from_network(self, server_id: int, /, *, network: int) -> ActionResponse:
        """Detach a Server from a Network.

        Detaches a Server from a network. The interface for this network will vanish.

        ``POST /servers/{id}/actions/detach_from_network``

        Args:
            server_id: ID of the Server.
            network: ID of an existing network to detach the Server from.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/detach_from_network",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "network": network,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    def detach_server_iso(self, server_id: int, /) -> ActionResponse:
        """Detach an ISO from a Server.

        Detaches an ISO from a Server. In case no ISO Image is attached to the Server, the status of
        the returned Action is immediately set to `success`.

        ``POST /servers/{id}/actions/detach_iso``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/detach_iso",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def disable_server_backup(self, server_id: int, /) -> ActionResponse:
        """Disable Backups for a Server.

        Disables the automatic backup option and deletes all existing Backups for a Server. No more
        additional charges for backups will be made.

        Caution: This immediately removes all existing backups for the Server!

        ``POST /servers/{id}/actions/disable_backup``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/disable_backup",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def disable_server_rescue(self, server_id: int, /) -> ActionResponse:
        """Disable Rescue Mode for a Server.

        Disables the Hetzner Rescue System for a Server. This makes a Server start from its disks on
        next reboot.

        Rescue Mode is automatically disabled when you first boot into it or if you do not use it
        for 60 minutes.

        Disabling rescue mode will not reboot your Server - you will have to do this yourself.

        ``POST /servers/{id}/actions/disable_rescue``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/disable_rescue",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def enable_server_backup(self, server_id: int, /) -> ActionResponse:
        """Enable and Configure Backups for a Server.

        Enables and configures the automatic daily backup option for the Server. Enabling automatic
        backups will increase the price of the Server by 20%. In return, you will get seven slots
        where Images of type backup can be stored.

        Backups are automatically created daily.

        ``POST /servers/{id}/actions/enable_backup``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/enable_backup",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def enable_server_rescue(
        self,
        server_id: int,
        /,
        *,
        type: Literal["linux64"] | NotGiven = NOT_GIVEN,
        ssh_keys: Sequence[int] | NotGiven = NOT_GIVEN,
    ) -> RootPasswordResponse:
        """Enable Rescue Mode for a Server.

        Enable the Hetzner Rescue System for this Server. The next time a Server with enabled rescue
        mode boots it will start a special minimal Linux distribution designed for repair and
        reinstall.

        In case a Server cannot boot on its own you can use this to access a Server's disks.

        Rescue Mode is automatically disabled when you first boot into it or if you do not use it
        for 60 minutes.

        Enabling rescue mode will not reboot
        (https://docs.hetzner.cloud/#server-actions-soft-reboot-a-server) your Server - you will
        have to do this yourself.

        ``POST /servers/{id}/actions/enable_rescue``

        Args:
            server_id: ID of the Server.
            type: Type of rescue system to boot. Omitted if not given. The API default is
                ``"linux64"``.
            ssh_keys: Array of SSH key IDs which should be injected into the rescue system. Omitted
                if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/enable_rescue",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "type": type,
                    "ssh_keys": ssh_keys,
                },
            ),
        )
        return self._transport.parse(RootPasswordResponse, response)

    def poweroff_server(self, server_id: int, /) -> ActionResponse:
        """Power off a Server.

        Cuts power to the Server. This forcefully stops it without giving the Server operating
        system time to gracefully stop. May lead to data loss, equivalent to pulling the power cord.
        Power off should only be used when shutdown does not work.

        ``POST /servers/{id}/actions/poweroff``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/poweroff",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def poweron_server(self, server_id: int, /) -> ActionResponse:
        """Power on a Server.

        Starts a Server by turning its power on.

        ``POST /servers/{id}/actions/poweron``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/poweron",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def reboot_server(self, server_id: int, /) -> ActionResponse:
        """Soft-reboot a Server.

        Reboots a Server gracefully by sending an ACPI request. The Server operating system must
        support ACPI and react to the request, otherwise the Server will not reboot.

        ``POST /servers/{id}/actions/reboot``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/reboot",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def rebuild_server(
        self,
        server_id: int,
        /,
        *,
        image: str | int,
        user_data: str | NotGiven = NOT_GIVEN,
    ) -> RebuildServerResponse:
        """Rebuild a Server from an Image.

        Rebuilds a Server overwriting its disk with the content of an Image, thereby **destroying
        all data** on the target Server

        The Image can either be one you have created earlier (`backup` or `snapshot` Image) or it
        can be a completely fresh `system` Image provided by us. You can get a list of all available
        Images with `GET /images`.

        Your Server will automatically be powered off before the rebuild command executes.

        ``POST /servers/{id}/actions/rebuild``

        Args:
            server_id: ID of the Server.
            image: ID or name of Image to rebuilt from.
            user_data: Cloud-Init user data to use during Server rebuild. This field is limited to
                32KiB. If not specified, the Server's previous user_data value will be re-used (if
                any was set). Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/rebuild",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "image": image,
                    "user_data": user_data,
                },
            ),
        )
        return self._transport.parse(RebuildServerResponse, response)

    def remove_server_from_placement_group(self, server_id: int, /) -> ActionResponse:
        """Remove from Placement Group.

        Removes a Server from a Placement Group.

        ``POST /servers/{id}/actions/remove_from_placement_group``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/remove_from_placement_group",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def request_server_console(self, server_id: int, /) -> RequestServerConsoleResponse:
        """Request Console for a Server.

        Requests credentials for remote access via VNC over websocket to keyboard, monitor, and
        mouse for a Server. The provided URL is valid for 1 minute, after this period a new url
        needs to be created to connect to the Server. How long the connection is open after the
        initial connect is not subject to this timeout.

        ``POST /servers/{id}/actions/request_console``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/request_console",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(RequestServerConsoleResponse, response)

    def reset_server(self, server_id: int, /) -> ActionResponse:
        """Reset a Server.

        Cuts power to a Server and starts it again. This forcefully stops it without giving the
        Server operating system time to gracefully stop. This may lead to data loss, it's equivalent
        to pulling the power cord and plugging it in again. Reset should only be used when reboot
        does not work.

        ``POST /servers/{id}/actions/reset``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/reset",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    def reset_server_password(self, server_id: int, /) -> RootPasswordResponse:
        """Reset root Password of a Server.

        Resets the root password. Only works for Linux systems that are running the qemu guest
        agent. Server must be powered on (status `running`) in order for this operation to succeed.

        This will generate a new password for this Server and return it.

        If this does not succeed you can use the rescue system to netboot the Server and manually
        change your Server password by hand.

        ``POST /servers/{id}/actions/reset_password``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/reset_password",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(RootPasswordResponse, response)

    def shutdown_server(self, server_id: int, /) -> ActionResponse:
        """Shutdown a Server.

        Shuts down a Server gracefully by sending an ACPI shutdown request. The Server operating
        system must support ACPI and react to the request, otherwise the Server will not shut down.
        Please note that the `action` status in this case only reflects whether the action was sent
        to the server. It does not mean that the server actually shut down successfully. If you need
        to ensure that the server is off, use the `poweroff` action.

        ``POST /servers/{id}/actions/shutdown``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/shutdown",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    @deprecated("GET /servers/{id}/actions/{action_id} is deprecated by the API")
    def get_server_action(self, server_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Server.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action object for a Server.

        ``GET /servers/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            server_id: ID of the Server.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, server_id=server_id, action_id=action_id)
        response = self._transport.request(
            "GET",
            f"/servers/{encode_path(server_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)


class AsyncServerActionsResource:
    """Operations on ``server_actions`` (asynchronous)."""

    __slots__ = ("_transport",)

    def __init__(self, transport: AsyncTransport) -> None:
        self._transport: Final = transport

    async def list_servers_actions(
        self,
        *,
        id: Sequence[int] | None = None,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions.

        Returns all Action objects. You can `sort` the results by using the sort URI parameter, and
        filter them with the `status` and `id` parameter.

        ``GET /servers/actions``

        Args:
            id: Filter the actions by ID. May be used multiple times. The response will only contain
                actions matching the specified IDs.
            sort: Sort actions by field and direction. May be used multiple times. For more
                information, see "Sorting".
            status: Filter the actions by status. May be used multiple times. The response will only
                contain actions matching the specified statuses.
            page: Page number to return. For more information, see "Pagination". The API default is
                ``1``.
            per_page: Maximum number of entries returned per page. For more information, see
                "Pagination". The API default is ``25``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_1, id=id, page=page, per_page=per_page)
        response = await self._transport.request(
            "GET",
            "/servers/actions",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "id": id,
                    "sort": sort,
                    "status": status,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ActionListResponseWithMeta, response)

    async def get_servers_action(self, action_id: int, /) -> ActionResponse:
        """Get an Action.

        Returns a specific Action object.

        ``GET /servers/actions/{id}``

        Args:
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_2, action_id=action_id)
        response = await self._transport.request(
            "GET",
            f"/servers/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def list_server_actions(
        self,
        server_id: int,
        /,
        *,
        sort: Sequence[ActionSort | UnknownValue] | None = None,
        status: Sequence[ActionStatus | UnknownValue] | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> ActionListResponseWithMeta:
        """List Actions for a Server.

        Returns all Action objects for a Server. You can `sort` the results by using the sort URI
        parameter, and filter them with the `status` parameter.

        ``GET /servers/{id}/actions``

        Args:
            server_id: ID of the Server.
            sort: Sort actions by field and direction. May be used multiple times. For more
                information, see "Sorting".
            status: Filter the actions by status. May be used multiple times. The response will only
                contain actions matching the specified statuses.
            page: Page number to return. For more information, see "Pagination". The API default is
                ``1``.
            per_page: Maximum number of entries returned per page. For more information, see
                "Pagination". The API default is ``25``.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_3, server_id=server_id, page=page, per_page=per_page)
        response = await self._transport.request(
            "GET",
            f"/servers/{encode_path(server_id)}/actions",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            params=encode_query(
                {
                    "sort": sort,
                    "status": status,
                    "page": page,
                    "per_page": per_page,
                },
            ),
        )
        return self._transport.parse(ActionListResponseWithMeta, response)

    async def add_server_to_placement_group(
        self,
        server_id: int,
        /,
        *,
        placement_group: int,
    ) -> ActionResponse:
        """Add a Server to a Placement Group.

        Adds a Server to a Placement Group.

        Server must be powered off for this command to succeed.

        **Operation specific errors**

        - `422` - `server_not_stopped` - The action requires a stopped server
        - `422` - `already_in_placement_group` - The server is already part of a placement group

        ``POST /servers/{id}/actions/add_to_placement_group``

        Args:
            server_id: ID of the Server.
            placement_group: ID of Placement Group the Server should be added to.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/add_to_placement_group",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "placement_group": placement_group,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def attach_server_iso(self, server_id: int, /, *, iso: str | int) -> ActionResponse:
        """Attach an ISO to a Server.

        Attaches an ISO to a Server. The Server will immediately see it as a new disk. An already
        attached ISO will automatically be detached before the new ISO is attached.

        Servers with attached ISOs have a modified boot order: They will try to boot from the ISO
        first before falling back to hard disk.

        ``POST /servers/{id}/actions/attach_iso``

        Args:
            server_id: ID of the Server.
            iso: ID or name of ISO to attach to the Server as listed in GET `/isos`.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/attach_iso",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "iso": iso,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def attach_server_to_network(
        self,
        server_id: int,
        /,
        *,
        network: int,
        ip: str | NotGiven = NOT_GIVEN,
        alias_ips: StrSequence | NotGiven = NOT_GIVEN,
        ip_range: str | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Attach a Server to a Network.

        Attaches a Server to a network. This will complement the fixed public Server interface by
        adding an additional ethernet interface to the Server which is connected to the specified
        network.

        The Server will get an IP auto assigned from a subnet of type `server` in the same
        `network_zone`.

        Using the `alias_ips` attribute you can also define one or more additional IPs to the
        Servers. Please note that you will have to configure these IPs by hand on your Server since
        only the primary IP will be given out by DHCP.

        **Operation specific errors**

        - `422` - `server_already_attached` - The server is already attached to the network
        - `422` - `ip_not_available` - The provided Network IP is not available
        - `422` - `no_subnet_available` - No Subnet or IP is available for the Server within the
          network
        - `422` - `networks_overlap` - The network IP range overlaps with one of the server networks

        ``POST /servers/{id}/actions/attach_to_network``

        Args:
            server_id: ID of the Server.
            network: ID of an existing network to attach the Server to.
            ip: IP to request to be assigned to this Server; if you do not provide this then you
                will be auto assigned an IP address. Omitted if not given.
            alias_ips: Additional IPs to be assigned to this Server. Omitted if not given.
            ip_range: IP range in CIDR block notation of the subnet to attach to. This allows for
                auto assigning an IP address for a specific subnet. Providing `ip` that is not part
                of `ip_range` will result in an error. Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/attach_to_network",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "network": network,
                    "ip": ip,
                    "alias_ips": alias_ips,
                    "ip_range": ip_range,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_server_alias_ips(
        self,
        server_id: int,
        /,
        *,
        network: int,
        alias_ips: StrSequence,
    ) -> ActionResponse:
        """Change alias IPs of a Network.

        Changes the alias IPs of an already attached Network. Note that the existing aliases for the
        specified Network will be replaced with these provided in the request body. So if you want
        to add an alias IP, you have to provide the existing ones from the Network plus the new
        alias IP in the request body.

        ``POST /servers/{id}/actions/change_alias_ips``

        Args:
            server_id: ID of the Server.
            network: ID of an existing Network already attached to the Server.
            alias_ips: New alias IPs to set for this Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/change_alias_ips",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "network": network,
                    "alias_ips": alias_ips,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_server_dns_ptr(
        self,
        server_id: int,
        /,
        *,
        ip: str,
        dns_ptr: str | None,
    ) -> ActionResponse:
        """Change reverse DNS entry for this Server.

        Changes the hostname that will appear when getting the hostname belonging to the primary IPs
        (IPv4 and IPv6) of this Server.

        Floating IPs assigned to the Server are not affected by this.

        ``POST /servers/{id}/actions/change_dns_ptr``

        Args:
            server_id: ID of the Server.
            ip: Single IPv4 or IPv6 address to create pointer for.
            dns_ptr: Domain Name to point to. PTR record content used for reverse DNS. Set to null
                to reset (IPv4) to the default value or remove (IPv6) the record.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/change_dns_ptr",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "ip": ip,
                    "dns_ptr": dns_ptr,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_server_protection(
        self,
        server_id: int,
        /,
        *,
        delete: bool | NotGiven = NOT_GIVEN,
        rebuild: bool | NotGiven = NOT_GIVEN,
    ) -> ActionResponse:
        """Change Server Protection.

        Changes the protection configuration of the Server.

        ``POST /servers/{id}/actions/change_protection``

        Args:
            server_id: ID of the Server.
            delete: If true, prevents the Server from being deleted (currently delete and rebuild
                attribute needs to have the same value). Omitted if not given.
            rebuild: If true, prevents the Server from being rebuilt (currently delete and rebuild
                attribute needs to have the same value). Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/change_protection",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "delete": delete,
                    "rebuild": rebuild,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def change_server_type(
        self,
        server_id: int,
        /,
        *,
        upgrade_disk: bool,
        server_type: str | int,
    ) -> ActionResponse:
        """Change the Type of a Server.

        Changes the type (Cores, RAM and disk sizes) of a Server.

        Server must be powered off for this command to succeed.

        This copies the content of its disk, and starts it again.

        You can only migrate to Server types with the same `storage_type` and equal or bigger disks.
        Shrinking disks is not possible as it might destroy data.

        If the disk gets upgraded, the Server type can not be downgraded any more. If you plan to
        downgrade the Server type, set `upgrade_disk` to `false`.

        **Operation specific errors**

        - `422` - `invalid_server_type` - The server type does not fit for the given server or is
          deprecated
        - `422` - `server_not_stopped` - The action requires a stopped server

        ``POST /servers/{id}/actions/change_type``

        Args:
            server_id: ID of the Server.
            upgrade_disk: If false, do not upgrade the disk (this allows downgrading the Server type
                later).
            server_type: ID or name of Server type the Server should migrate to.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/change_type",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "upgrade_disk": upgrade_disk,
                    "server_type": server_type,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def create_server_image(
        self,
        server_id: int,
        /,
        *,
        description: str | NotGiven = NOT_GIVEN,
        type: CreateImageRequestType | UnknownValue | NotGiven = NOT_GIVEN,
        labels: Mapping[str, str] | NotGiven = NOT_GIVEN,
    ) -> CreateServerImageResponse:
        """Create Image from a Server.

        Creates an Image (snapshot) from a Server by copying the contents of its disks. This creates
        a snapshot of the current state of the disk and copies it into an Image. If the Server is
        currently running you must make sure that its disk content is consistent. Otherwise, the
        created Image may not be readable.

        To make sure disk content is consistent, we recommend to shut down the Server prior to
        creating an Image.

        You can either create a `backup` Image that is bound to the Server and therefore will be
        deleted when the Server is deleted, or you can create a `snapshot` Image which is completely
        independent of the Server it was created from and will survive Server deletion. Backup
        Images are only available when the backup option is enabled for the Server. Snapshot Images
        are billed on a per GB basis.

        ``POST /servers/{id}/actions/create_image``

        Args:
            server_id: ID of the Server.
            description: Description of the Image, will be auto-generated if not set. Omitted if not
                given.
            type: Type of Image to create. Omitted if not given. The API default is ``"snapshot"``.
            labels: User-defined labels (`key/value` pairs) for the Resource. For more information,
                see "Labels". Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_5, server_id=server_id, labels=labels)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/create_image",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "description": description,
                    "type": type,
                    "labels": labels,
                },
            ),
        )
        return self._transport.parse(CreateServerImageResponse, response)

    async def detach_server_from_network(
        self,
        server_id: int,
        /,
        *,
        network: int,
    ) -> ActionResponse:
        """Detach a Server from a Network.

        Detaches a Server from a network. The interface for this network will vanish.

        ``POST /servers/{id}/actions/detach_from_network``

        Args:
            server_id: ID of the Server.
            network: ID of an existing network to detach the Server from.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/detach_from_network",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "network": network,
                },
            ),
        )
        return self._transport.parse(ActionResponse, response)

    async def detach_server_iso(self, server_id: int, /) -> ActionResponse:
        """Detach an ISO from a Server.

        Detaches an ISO from a Server. In case no ISO Image is attached to the Server, the status of
        the returned Action is immediately set to `success`.

        ``POST /servers/{id}/actions/detach_iso``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/detach_iso",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def disable_server_backup(self, server_id: int, /) -> ActionResponse:
        """Disable Backups for a Server.

        Disables the automatic backup option and deletes all existing Backups for a Server. No more
        additional charges for backups will be made.

        Caution: This immediately removes all existing backups for the Server!

        ``POST /servers/{id}/actions/disable_backup``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/disable_backup",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def disable_server_rescue(self, server_id: int, /) -> ActionResponse:
        """Disable Rescue Mode for a Server.

        Disables the Hetzner Rescue System for a Server. This makes a Server start from its disks on
        next reboot.

        Rescue Mode is automatically disabled when you first boot into it or if you do not use it
        for 60 minutes.

        Disabling rescue mode will not reboot your Server - you will have to do this yourself.

        ``POST /servers/{id}/actions/disable_rescue``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/disable_rescue",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def enable_server_backup(self, server_id: int, /) -> ActionResponse:
        """Enable and Configure Backups for a Server.

        Enables and configures the automatic daily backup option for the Server. Enabling automatic
        backups will increase the price of the Server by 20%. In return, you will get seven slots
        where Images of type backup can be stored.

        Backups are automatically created daily.

        ``POST /servers/{id}/actions/enable_backup``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/enable_backup",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def enable_server_rescue(
        self,
        server_id: int,
        /,
        *,
        type: Literal["linux64"] | NotGiven = NOT_GIVEN,
        ssh_keys: Sequence[int] | NotGiven = NOT_GIVEN,
    ) -> RootPasswordResponse:
        """Enable Rescue Mode for a Server.

        Enable the Hetzner Rescue System for this Server. The next time a Server with enabled rescue
        mode boots it will start a special minimal Linux distribution designed for repair and
        reinstall.

        In case a Server cannot boot on its own you can use this to access a Server's disks.

        Rescue Mode is automatically disabled when you first boot into it or if you do not use it
        for 60 minutes.

        Enabling rescue mode will not reboot
        (https://docs.hetzner.cloud/#server-actions-soft-reboot-a-server) your Server - you will
        have to do this yourself.

        ``POST /servers/{id}/actions/enable_rescue``

        Args:
            server_id: ID of the Server.
            type: Type of rescue system to boot. Omitted if not given. The API default is
                ``"linux64"``.
            ssh_keys: Array of SSH key IDs which should be injected into the rescue system. Omitted
                if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/enable_rescue",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "type": type,
                    "ssh_keys": ssh_keys,
                },
            ),
        )
        return self._transport.parse(RootPasswordResponse, response)

    async def poweroff_server(self, server_id: int, /) -> ActionResponse:
        """Power off a Server.

        Cuts power to the Server. This forcefully stops it without giving the Server operating
        system time to gracefully stop. May lead to data loss, equivalent to pulling the power cord.
        Power off should only be used when shutdown does not work.

        ``POST /servers/{id}/actions/poweroff``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/poweroff",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def poweron_server(self, server_id: int, /) -> ActionResponse:
        """Power on a Server.

        Starts a Server by turning its power on.

        ``POST /servers/{id}/actions/poweron``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/poweron",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def reboot_server(self, server_id: int, /) -> ActionResponse:
        """Soft-reboot a Server.

        Reboots a Server gracefully by sending an ACPI request. The Server operating system must
        support ACPI and react to the request, otherwise the Server will not reboot.

        ``POST /servers/{id}/actions/reboot``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/reboot",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def rebuild_server(
        self,
        server_id: int,
        /,
        *,
        image: str | int,
        user_data: str | NotGiven = NOT_GIVEN,
    ) -> RebuildServerResponse:
        """Rebuild a Server from an Image.

        Rebuilds a Server overwriting its disk with the content of an Image, thereby **destroying
        all data** on the target Server

        The Image can either be one you have created earlier (`backup` or `snapshot` Image) or it
        can be a completely fresh `system` Image provided by us. You can get a list of all available
        Images with `GET /images`.

        Your Server will automatically be powered off before the rebuild command executes.

        ``POST /servers/{id}/actions/rebuild``

        Args:
            server_id: ID of the Server.
            image: ID or name of Image to rebuilt from.
            user_data: Cloud-Init user data to use during Server rebuild. This field is limited to
                32KiB. If not specified, the Server's previous user_data value will be re-used (if
                any was set). Omitted if not given.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/rebuild",
            security=_SECURITY_1,
            errors=_ERRORS_1,
            json_body=encode_body(
                {
                    "image": image,
                    "user_data": user_data,
                },
            ),
        )
        return self._transport.parse(RebuildServerResponse, response)

    async def remove_server_from_placement_group(self, server_id: int, /) -> ActionResponse:
        """Remove from Placement Group.

        Removes a Server from a Placement Group.

        ``POST /servers/{id}/actions/remove_from_placement_group``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/remove_from_placement_group",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def request_server_console(self, server_id: int, /) -> RequestServerConsoleResponse:
        """Request Console for a Server.

        Requests credentials for remote access via VNC over websocket to keyboard, monitor, and
        mouse for a Server. The provided URL is valid for 1 minute, after this period a new url
        needs to be created to connect to the Server. How long the connection is open after the
        initial connect is not subject to this timeout.

        ``POST /servers/{id}/actions/request_console``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/request_console",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(RequestServerConsoleResponse, response)

    async def reset_server(self, server_id: int, /) -> ActionResponse:
        """Reset a Server.

        Cuts power to a Server and starts it again. This forcefully stops it without giving the
        Server operating system time to gracefully stop. This may lead to data loss, it's equivalent
        to pulling the power cord and plugging it in again. Reset should only be used when reboot
        does not work.

        ``POST /servers/{id}/actions/reset``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/reset",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    async def reset_server_password(self, server_id: int, /) -> RootPasswordResponse:
        """Reset root Password of a Server.

        Resets the root password. Only works for Linux systems that are running the qemu guest
        agent. Server must be powered on (status `running`) in order for this operation to succeed.

        This will generate a new password for this Server and return it.

        If this does not succeed you can use the rescue system to netboot the Server and manually
        change your Server password by hand.

        ``POST /servers/{id}/actions/reset_password``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/reset_password",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(RootPasswordResponse, response)

    async def shutdown_server(self, server_id: int, /) -> ActionResponse:
        """Shutdown a Server.

        Shuts down a Server gracefully by sending an ACPI shutdown request. The Server operating
        system must support ACPI and react to the request, otherwise the Server will not shut down.
        Please note that the `action` status in this case only reflects whether the action was sent
        to the server. It does not mean that the server actually shut down successfully. If you need
        to ensure that the server is off, use the `poweroff` action.

        ``POST /servers/{id}/actions/shutdown``

        Args:
            server_id: ID of the Server.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_4, server_id=server_id)
        response = await self._transport.request(
            "POST",
            f"/servers/{encode_path(server_id)}/actions/shutdown",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)

    @deprecated("GET /servers/{id}/actions/{action_id} is deprecated by the API")
    async def get_server_action(self, server_id: int, action_id: int, /) -> ActionResponse:
        """Get an Action for a Server.

        **Deprecated**: This operation is deprecated, see our changelog
        (https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
        for more details.

        Returns a specific Action object for a Server.

        ``GET /servers/{id}/actions/{action_id}``

        Deprecated by the API.

        Args:
            server_id: ID of the Server.
            action_id: ID of the Action.

        Raises:
            APIStatusError: The API reported an error (one subclass per HTTP status).
            APIConnectionError: The API is not reachable.
            ResponseValidationError: The response does not match the spec.
        """
        self._transport.validate(_CHECKS_6, server_id=server_id, action_id=action_id)
        response = await self._transport.request(
            "GET",
            f"/servers/{encode_path(server_id)}/actions/{encode_path(action_id)}",
            security=_SECURITY_1,
            errors=_ERRORS_1,
        )
        return self._transport.parse(ActionResponse, response)
