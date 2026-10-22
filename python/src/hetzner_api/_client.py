"""Entry points: ``Hetzner`` (sync) and ``AsyncHetzner``."""

from collections.abc import Mapping
from os import environ
from typing import Final, Self, override

import httpx2

from hetzner_api._auth import BearerToken, Credential
from hetzner_api._base_client import AsyncTransport, RetryPolicy, SyncTransport
from hetzner_api._types import NOT_GIVEN, NotGiven
from hetzner_api._validation import Validation
from hetzner_api.errors import HetznerError
from hetzner_api.resources.actions import ActionsResource, AsyncActionsResource
from hetzner_api.resources.certificate_actions import (
    AsyncCertificateActionsResource,
    CertificateActionsResource,
)
from hetzner_api.resources.certificates import AsyncCertificatesResource, CertificatesResource
from hetzner_api.resources.data_centers import AsyncDataCentersResource, DataCentersResource
from hetzner_api.resources.firewall_actions import (
    AsyncFirewallActionsResource,
    FirewallActionsResource,
)
from hetzner_api.resources.firewalls import AsyncFirewallsResource, FirewallsResource
from hetzner_api.resources.floating_ip_actions import (
    AsyncFloatingIpActionsResource,
    FloatingIpActionsResource,
)
from hetzner_api.resources.floating_ips import AsyncFloatingIpsResource, FloatingIpsResource
from hetzner_api.resources.image_actions import AsyncImageActionsResource, ImageActionsResource
from hetzner_api.resources.images import AsyncImagesResource, ImagesResource
from hetzner_api.resources.isos import AsyncIsosResource, IsosResource
from hetzner_api.resources.load_balancer_actions import (
    AsyncLoadBalancerActionsResource,
    LoadBalancerActionsResource,
)
from hetzner_api.resources.load_balancer_types import (
    AsyncLoadBalancerTypesResource,
    LoadBalancerTypesResource,
)
from hetzner_api.resources.load_balancers import AsyncLoadBalancersResource, LoadBalancersResource
from hetzner_api.resources.locations import AsyncLocationsResource, LocationsResource
from hetzner_api.resources.network_actions import (
    AsyncNetworkActionsResource,
    NetworkActionsResource,
)
from hetzner_api.resources.networks import AsyncNetworksResource, NetworksResource
from hetzner_api.resources.placement_groups import (
    AsyncPlacementGroupsResource,
    PlacementGroupsResource,
)
from hetzner_api.resources.pricing import AsyncPricingResource, PricingResource
from hetzner_api.resources.primary_ip_actions import (
    AsyncPrimaryIpActionsResource,
    PrimaryIpActionsResource,
)
from hetzner_api.resources.primary_ips import AsyncPrimaryIpsResource, PrimaryIpsResource
from hetzner_api.resources.server_actions import AsyncServerActionsResource, ServerActionsResource
from hetzner_api.resources.server_types import AsyncServerTypesResource, ServerTypesResource
from hetzner_api.resources.servers import AsyncServersResource, ServersResource
from hetzner_api.resources.ssh_keys import AsyncSshKeysResource, SshKeysResource
from hetzner_api.resources.storage_box_actions import (
    AsyncStorageBoxActionsResource,
    StorageBoxActionsResource,
)
from hetzner_api.resources.storage_box_snapshots import (
    AsyncStorageBoxSnapshotsResource,
    StorageBoxSnapshotsResource,
)
from hetzner_api.resources.storage_box_subaccount_actions import (
    AsyncStorageBoxSubaccountActionsResource,
    StorageBoxSubaccountActionsResource,
)
from hetzner_api.resources.storage_box_subaccounts import (
    AsyncStorageBoxSubaccountsResource,
    StorageBoxSubaccountsResource,
)
from hetzner_api.resources.storage_box_types import (
    AsyncStorageBoxTypesResource,
    StorageBoxTypesResource,
)
from hetzner_api.resources.storage_boxes import AsyncStorageBoxesResource, StorageBoxesResource
from hetzner_api.resources.volume_actions import AsyncVolumeActionsResource, VolumeActionsResource
from hetzner_api.resources.volumes import AsyncVolumesResource, VolumesResource
from hetzner_api.resources.zone_actions import AsyncZoneActionsResource, ZoneActionsResource
from hetzner_api.resources.zone_rrset_actions import (
    AsyncZoneRrsetActionsResource,
    ZoneRrsetActionsResource,
)
from hetzner_api.resources.zone_rrsets import AsyncZoneRrsetsResource, ZoneRrsetsResource
from hetzner_api.resources.zones import AsyncZonesResource, ZonesResource

__all__ = ["AsyncHetzner", "Hetzner"]

_NEEDED: Final = ("token=... (or $HCLOUD_TOKEN)",)
"""What the client needs (for the error message without credentials)."""


class Hetzner:
    """Synchronous client for the Hetzner API.

    All resources are attributes, for example ``client.actions``.

    The client keeps connections open - use it with ``with`` or call
    ``close()`` at the end.

    Example::

        with Hetzner() as client:
            ...

    Args:
        token: API token, sent as ``Authorization: Bearer``. Default: ``$HCLOUD_TOKEN``.
        cloud_base_url: Base URL for operations on ``https://api.hetzner.cloud/v1``.
        hetzner_base_url: Base URL for operations on ``https://api.hetzner.com/v1``.
        timeout: Timeout per request in seconds (or an ``httpx2.Timeout``); ``None`` disables it.
            Default: 30 s, or the timeout configured on ``http_client``.
        retry: Retry behaviour for rate limits and transient errors.
        validation: How strictly the API is held to its spec. ``"lax"`` (default): rules such as
            ``maxLength`` are not checked, and a response that does not match the spec is still
            returned (with a warning in the log). ``"strict"``: arguments and responses must keep
            every rule - for testing an API against its spec.
        http_client: Your own ``httpx2.Client`` (e.g. for proxies or tests).
        headers: Additional HTTP headers for every request.

    Raises:
        HetznerError: No credentials were passed (and none were found in the environment).
    """

    __slots__ = (
        "_transport",
        "actions",
        "certificate_actions",
        "certificates",
        "data_centers",
        "firewall_actions",
        "firewalls",
        "floating_ip_actions",
        "floating_ips",
        "image_actions",
        "images",
        "isos",
        "load_balancer_actions",
        "load_balancer_types",
        "load_balancers",
        "locations",
        "network_actions",
        "networks",
        "placement_groups",
        "pricing",
        "primary_ip_actions",
        "primary_ips",
        "server_actions",
        "server_types",
        "servers",
        "ssh_keys",
        "storage_box_actions",
        "storage_box_snapshots",
        "storage_box_subaccount_actions",
        "storage_box_subaccounts",
        "storage_box_types",
        "storage_boxes",
        "volume_actions",
        "volumes",
        "zone_actions",
        "zone_rrset_actions",
        "zone_rrsets",
        "zones",
    )

    def __init__(  # noqa: PLR0915 - all settings and one attribute per resource
        self,
        token: str | None = None,
        *,
        cloud_base_url: str = "https://api.hetzner.cloud/v1",
        hetzner_base_url: str = "https://api.hetzner.com/v1",
        timeout: float | httpx2.Timeout | NotGiven | None = NOT_GIVEN,
        retry: RetryPolicy | None = None,
        validation: Validation = "lax",
        http_client: httpx2.Client | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        if token is None:
            token = environ.get("HCLOUD_TOKEN")
        credentials: dict[str, Credential] = {}
        if token:
            credentials["APIToken"] = BearerToken(token)
        if not credentials:
            msg = f"no credentials passed: {' or '.join(_NEEDED)}"
            raise HetznerError(msg)
        self._transport: Final = SyncTransport(
            credentials=credentials,
            base_urls={
                "cloud": cloud_base_url,
                "hetzner": hetzner_base_url,
            },
            default_server="cloud",
            retry=retry or RetryPolicy(),
            timeout=timeout,
            http_client=http_client,
            headers=headers,
            validation=validation,
        )
        self.actions: Final = ActionsResource(self._transport)
        """Resource ``actions``."""
        self.certificate_actions: Final = CertificateActionsResource(self._transport)
        """Resource ``certificate_actions``."""
        self.certificates: Final = CertificatesResource(self._transport)
        """Resource ``certificates``."""
        self.data_centers: Final = DataCentersResource(self._transport)
        """Resource ``data_centers``."""
        self.firewall_actions: Final = FirewallActionsResource(self._transport)
        """Resource ``firewall_actions``."""
        self.firewalls: Final = FirewallsResource(self._transport)
        """Resource ``firewalls``."""
        self.floating_ip_actions: Final = FloatingIpActionsResource(self._transport)
        """Resource ``floating_ip_actions``."""
        self.floating_ips: Final = FloatingIpsResource(self._transport)
        """Resource ``floating_ips``."""
        self.image_actions: Final = ImageActionsResource(self._transport)
        """Resource ``image_actions``."""
        self.images: Final = ImagesResource(self._transport)
        """Resource ``images``."""
        self.isos: Final = IsosResource(self._transport)
        """Resource ``isos``."""
        self.load_balancer_actions: Final = LoadBalancerActionsResource(self._transport)
        """Resource ``load_balancer_actions``."""
        self.load_balancer_types: Final = LoadBalancerTypesResource(self._transport)
        """Resource ``load_balancer_types``."""
        self.load_balancers: Final = LoadBalancersResource(self._transport)
        """Resource ``load_balancers``."""
        self.locations: Final = LocationsResource(self._transport)
        """Resource ``locations``."""
        self.network_actions: Final = NetworkActionsResource(self._transport)
        """Resource ``network_actions``."""
        self.networks: Final = NetworksResource(self._transport)
        """Resource ``networks``."""
        self.placement_groups: Final = PlacementGroupsResource(self._transport)
        """Resource ``placement_groups``."""
        self.pricing: Final = PricingResource(self._transport)
        """Resource ``pricing``."""
        self.primary_ip_actions: Final = PrimaryIpActionsResource(self._transport)
        """Resource ``primary_ip_actions``."""
        self.primary_ips: Final = PrimaryIpsResource(self._transport)
        """Resource ``primary_ips``."""
        self.server_actions: Final = ServerActionsResource(self._transport)
        """Resource ``server_actions``."""
        self.server_types: Final = ServerTypesResource(self._transport)
        """Resource ``server_types``."""
        self.servers: Final = ServersResource(self._transport)
        """Resource ``servers``."""
        self.ssh_keys: Final = SshKeysResource(self._transport)
        """Resource ``ssh_keys``."""
        self.storage_box_actions: Final = StorageBoxActionsResource(self._transport)
        """Resource ``storage_box_actions``."""
        self.storage_box_snapshots: Final = StorageBoxSnapshotsResource(self._transport)
        """Resource ``storage_box_snapshots``."""
        self.storage_box_subaccount_actions: Final = StorageBoxSubaccountActionsResource(
            self._transport
        )
        """Resource ``storage_box_subaccount_actions``."""
        self.storage_box_subaccounts: Final = StorageBoxSubaccountsResource(self._transport)
        """Resource ``storage_box_subaccounts``."""
        self.storage_box_types: Final = StorageBoxTypesResource(self._transport)
        """Resource ``storage_box_types``."""
        self.storage_boxes: Final = StorageBoxesResource(self._transport)
        """Resource ``storage_boxes``."""
        self.volume_actions: Final = VolumeActionsResource(self._transport)
        """Resource ``volume_actions``."""
        self.volumes: Final = VolumesResource(self._transport)
        """Resource ``volumes``."""
        self.zone_actions: Final = ZoneActionsResource(self._transport)
        """Resource ``zone_actions``."""
        self.zone_rrset_actions: Final = ZoneRrsetActionsResource(self._transport)
        """Resource ``zone_rrset_actions``."""
        self.zone_rrsets: Final = ZoneRrsetsResource(self._transport)
        """Resource ``zone_rrsets``."""
        self.zones: Final = ZonesResource(self._transport)
        """Resource ``zones``."""

    @override
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._transport!r})"

    def close(self) -> None:
        """Closes the connections (only an HTTP client the client created itself)."""
        self._transport.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()


class AsyncHetzner:
    """Asynchronous client for the Hetzner API.

    All resources are attributes, for example ``client.actions``.

    The client keeps connections open - use it with ``async with`` or call
    ``aclose()`` at the end.

    Example::

        async with AsyncHetzner() as client:
            ...

    Args:
        token: API token, sent as ``Authorization: Bearer``. Default: ``$HCLOUD_TOKEN``.
        cloud_base_url: Base URL for operations on ``https://api.hetzner.cloud/v1``.
        hetzner_base_url: Base URL for operations on ``https://api.hetzner.com/v1``.
        timeout: Timeout per request in seconds (or an ``httpx2.Timeout``); ``None`` disables it.
            Default: 30 s, or the timeout configured on ``http_client``.
        retry: Retry behaviour for rate limits and transient errors.
        validation: How strictly the API is held to its spec. ``"lax"`` (default): rules such as
            ``maxLength`` are not checked, and a response that does not match the spec is still
            returned (with a warning in the log). ``"strict"``: arguments and responses must keep
            every rule - for testing an API against its spec.
        http_client: Your own ``httpx2.AsyncClient`` (e.g. for proxies or tests).
        headers: Additional HTTP headers for every request.

    Raises:
        HetznerError: No credentials were passed (and none were found in the environment).
    """

    __slots__ = (
        "_transport",
        "actions",
        "certificate_actions",
        "certificates",
        "data_centers",
        "firewall_actions",
        "firewalls",
        "floating_ip_actions",
        "floating_ips",
        "image_actions",
        "images",
        "isos",
        "load_balancer_actions",
        "load_balancer_types",
        "load_balancers",
        "locations",
        "network_actions",
        "networks",
        "placement_groups",
        "pricing",
        "primary_ip_actions",
        "primary_ips",
        "server_actions",
        "server_types",
        "servers",
        "ssh_keys",
        "storage_box_actions",
        "storage_box_snapshots",
        "storage_box_subaccount_actions",
        "storage_box_subaccounts",
        "storage_box_types",
        "storage_boxes",
        "volume_actions",
        "volumes",
        "zone_actions",
        "zone_rrset_actions",
        "zone_rrsets",
        "zones",
    )

    def __init__(  # noqa: PLR0915 - all settings and one attribute per resource
        self,
        token: str | None = None,
        *,
        cloud_base_url: str = "https://api.hetzner.cloud/v1",
        hetzner_base_url: str = "https://api.hetzner.com/v1",
        timeout: float | httpx2.Timeout | NotGiven | None = NOT_GIVEN,
        retry: RetryPolicy | None = None,
        validation: Validation = "lax",
        http_client: httpx2.AsyncClient | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        if token is None:
            token = environ.get("HCLOUD_TOKEN")
        credentials: dict[str, Credential] = {}
        if token:
            credentials["APIToken"] = BearerToken(token)
        if not credentials:
            msg = f"no credentials passed: {' or '.join(_NEEDED)}"
            raise HetznerError(msg)
        self._transport: Final = AsyncTransport(
            credentials=credentials,
            base_urls={
                "cloud": cloud_base_url,
                "hetzner": hetzner_base_url,
            },
            default_server="cloud",
            retry=retry or RetryPolicy(),
            timeout=timeout,
            http_client=http_client,
            headers=headers,
            validation=validation,
        )
        self.actions: Final = AsyncActionsResource(self._transport)
        """Resource ``actions``."""
        self.certificate_actions: Final = AsyncCertificateActionsResource(self._transport)
        """Resource ``certificate_actions``."""
        self.certificates: Final = AsyncCertificatesResource(self._transport)
        """Resource ``certificates``."""
        self.data_centers: Final = AsyncDataCentersResource(self._transport)
        """Resource ``data_centers``."""
        self.firewall_actions: Final = AsyncFirewallActionsResource(self._transport)
        """Resource ``firewall_actions``."""
        self.firewalls: Final = AsyncFirewallsResource(self._transport)
        """Resource ``firewalls``."""
        self.floating_ip_actions: Final = AsyncFloatingIpActionsResource(self._transport)
        """Resource ``floating_ip_actions``."""
        self.floating_ips: Final = AsyncFloatingIpsResource(self._transport)
        """Resource ``floating_ips``."""
        self.image_actions: Final = AsyncImageActionsResource(self._transport)
        """Resource ``image_actions``."""
        self.images: Final = AsyncImagesResource(self._transport)
        """Resource ``images``."""
        self.isos: Final = AsyncIsosResource(self._transport)
        """Resource ``isos``."""
        self.load_balancer_actions: Final = AsyncLoadBalancerActionsResource(self._transport)
        """Resource ``load_balancer_actions``."""
        self.load_balancer_types: Final = AsyncLoadBalancerTypesResource(self._transport)
        """Resource ``load_balancer_types``."""
        self.load_balancers: Final = AsyncLoadBalancersResource(self._transport)
        """Resource ``load_balancers``."""
        self.locations: Final = AsyncLocationsResource(self._transport)
        """Resource ``locations``."""
        self.network_actions: Final = AsyncNetworkActionsResource(self._transport)
        """Resource ``network_actions``."""
        self.networks: Final = AsyncNetworksResource(self._transport)
        """Resource ``networks``."""
        self.placement_groups: Final = AsyncPlacementGroupsResource(self._transport)
        """Resource ``placement_groups``."""
        self.pricing: Final = AsyncPricingResource(self._transport)
        """Resource ``pricing``."""
        self.primary_ip_actions: Final = AsyncPrimaryIpActionsResource(self._transport)
        """Resource ``primary_ip_actions``."""
        self.primary_ips: Final = AsyncPrimaryIpsResource(self._transport)
        """Resource ``primary_ips``."""
        self.server_actions: Final = AsyncServerActionsResource(self._transport)
        """Resource ``server_actions``."""
        self.server_types: Final = AsyncServerTypesResource(self._transport)
        """Resource ``server_types``."""
        self.servers: Final = AsyncServersResource(self._transport)
        """Resource ``servers``."""
        self.ssh_keys: Final = AsyncSshKeysResource(self._transport)
        """Resource ``ssh_keys``."""
        self.storage_box_actions: Final = AsyncStorageBoxActionsResource(self._transport)
        """Resource ``storage_box_actions``."""
        self.storage_box_snapshots: Final = AsyncStorageBoxSnapshotsResource(self._transport)
        """Resource ``storage_box_snapshots``."""
        self.storage_box_subaccount_actions: Final = AsyncStorageBoxSubaccountActionsResource(
            self._transport
        )
        """Resource ``storage_box_subaccount_actions``."""
        self.storage_box_subaccounts: Final = AsyncStorageBoxSubaccountsResource(self._transport)
        """Resource ``storage_box_subaccounts``."""
        self.storage_box_types: Final = AsyncStorageBoxTypesResource(self._transport)
        """Resource ``storage_box_types``."""
        self.storage_boxes: Final = AsyncStorageBoxesResource(self._transport)
        """Resource ``storage_boxes``."""
        self.volume_actions: Final = AsyncVolumeActionsResource(self._transport)
        """Resource ``volume_actions``."""
        self.volumes: Final = AsyncVolumesResource(self._transport)
        """Resource ``volumes``."""
        self.zone_actions: Final = AsyncZoneActionsResource(self._transport)
        """Resource ``zone_actions``."""
        self.zone_rrset_actions: Final = AsyncZoneRrsetActionsResource(self._transport)
        """Resource ``zone_rrset_actions``."""
        self.zone_rrsets: Final = AsyncZoneRrsetsResource(self._transport)
        """Resource ``zone_rrsets``."""
        self.zones: Final = AsyncZonesResource(self._transport)
        """Resource ``zones``."""

    @override
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._transport!r})"

    async def aclose(self) -> None:
        """Closes the connections (only an HTTP client the client created itself)."""
        await self._transport.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.aclose()
