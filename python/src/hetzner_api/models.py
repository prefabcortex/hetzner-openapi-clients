"""Response models of the Hetzner API (generated - do not edit by hand)."""

from collections.abc import Mapping
from decimal import Decimal
from typing import Annotated, Literal, override

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, JsonValue

from hetzner_api._types import UnknownValue
from hetzner_api._validation import Check
from hetzner_api.rules import LABELS_RULES

__all__ = [
    "Action",
    "ActionError",
    "ActionListResponse",
    "ActionListResponseWithMeta",
    "ActionNullable",
    "ActionResource",
    "ActionResponse",
    "ActionSort",
    "ActionStatus",
    "Architecture",
    "ArchitectureNullable",
    "AssigneeType",
    "Certificate",
    "CertificateResponse",
    "CertificateStatus",
    "CertificateStatusError",
    "CertificateStatusIssuance",
    "CertificateStatusRenewal",
    "CertificateType",
    "CertificateUsedBy",
    "CertificatesResponse",
    "CreateCertificateResponse",
    "CreateFirewallResponse",
    "CreateFloatingIpResponse",
    "CreateImageRequestType",
    "CreateLoadBalancerResponse",
    "CreatePlacementGroupResponse",
    "CreatePrimaryIPResponse",
    "CreateServerImageResponse",
    "CreateServerResponse",
    "CreateStorageBoxResponse",
    "CreateStorageBoxSnapshotResponse",
    "CreateStorageBoxSnapshotResponseSnapshot",
    "CreateStorageBoxSubaccountResponse",
    "CreateStorageBoxSubaccountResponseSubaccount",
    "CreateVolumeResponse",
    "CreateZoneResponse",
    "CreateZoneRrsetResponse",
    "CreatedFrom",
    "Datacenter",
    "DatacenterServerTypes",
    "DeprecationInfo",
    "DnsPtr",
    "ErrorResponse",
    "ErrorResponseError",
    "Firewall",
    "FirewallAppliedTo",
    "FirewallAppliedToAppliedToResource",
    "FirewallAppliedToServer",
    "FirewallResourceType",
    "FirewallResponse",
    "FirewallRuleDirection",
    "FirewallRuleProtocol",
    "FirewallsResponse",
    "FloatingIp",
    "FloatingIpResponse",
    "GetDatacenterResponse",
    "GetIsoResponse",
    "GetLoadBalancerMetricsType",
    "GetLoadBalancerTypeResponse",
    "GetLocationResponse",
    "GetPricingResponse",
    "GetServerMetricsType",
    "GetServerTypeResponse",
    "GetStorageBoxTypeResponse",
    "HealthCheckProtocol",
    "HealthStatus",
    "HealthStatusDetail",
    "HealthStatusStatus",
    "Image",
    "ImageResponse",
    "ImageStatus",
    "ImageType",
    "IpType",
    "Iso",
    "IsoType",
    "LabelSelector",
    "ListDatacentersResponse",
    "ListFloatingIpsResponse",
    "ListImagesResponse",
    "ListIsosResponse",
    "ListLoadBalancerTypesResponse",
    "ListLoadBalancersResponse",
    "ListLocationsResponse",
    "ListMeta",
    "ListMeta100",
    "ListMeta100Pagination",
    "ListMetaPagination",
    "ListNetworkMembersResponse",
    "ListNetworkMembersSort",
    "ListNetworksResponse",
    "ListServerTypesResponse",
    "ListServersResponse",
    "ListSshKeysResponse",
    "ListStorageBoxFoldersResponse",
    "ListStorageBoxSnapshotsResponse",
    "ListStorageBoxSubaccountsResponse",
    "ListStorageBoxTypesResponse",
    "ListStorageBoxesResponse",
    "ListStorageBoxesSort",
    "ListVolumesResponse",
    "ListZoneRrsetsResponse",
    "ListZonesResponse",
    "LoadBalancer",
    "LoadBalancerAlgorithm",
    "LoadBalancerAlgorithmType",
    "LoadBalancerPrivateNet",
    "LoadBalancerPublicIp",
    "LoadBalancerPublicNet",
    "LoadBalancerResponse",
    "LoadBalancerService",
    "LoadBalancerServiceHTTPConfig",
    "LoadBalancerServiceHTTPSConfig",
    "LoadBalancerServiceHealthCheck",
    "LoadBalancerServiceHealthCheckHttp",
    "LoadBalancerServiceProtocol",
    "LoadBalancerTarget",
    "LoadBalancerTargetIP",
    "LoadBalancerTargetLabelSelector",
    "LoadBalancerTargetServer",
    "LoadBalancerTargetTarget",
    "LoadBalancerTargetType",
    "LoadBalancerType",
    "Location",
    "LocationPrice",
    "Member",
    "MetricsResponse",
    "MetricsResponseMetrics",
    "MetricsResponseMetricsTimeSeriesValue",
    "Network",
    "NetworkMemberStatus",
    "NetworkMemberType",
    "NetworkResponse",
    "NetworkSubnet",
    "OsFlavor",
    "PlacementGroup",
    "PlacementGroupResponse",
    "PlacementGroupsResponse",
    "Price",
    "PricePerGbMonth",
    "Pricing",
    "PricingFloatingIp",
    "PricingFloatingIp2",
    "PricingFloatingIpPrice",
    "PricingPrimaryIp",
    "PricingPrimaryIpPrice",
    "PricingServerBackup",
    "PrimaryIP",
    "PrimaryIPResponse",
    "PrimaryIPsResponse",
    "Protection",
    "RRSet",
    "RRSetProtection",
    "RRSetType",
    "RebuildServerResponse",
    "Record",
    "RequestServerConsoleResponse",
    "RootPasswordResponse",
    "Route",
    "RrsetResponse",
    "RuleResponse",
    "Server",
    "ServerPrivateNet",
    "ServerProtection",
    "ServerPublicNet",
    "ServerPublicNetFirewall",
    "ServerPublicNetFirewallStatus",
    "ServerPublicNetIpv4",
    "ServerPublicNetIpv6",
    "ServerResponse",
    "ServerStatus",
    "ServerType",
    "ServerTypeCpuType",
    "ServerTypeLocation",
    "ServerTypeStorageType",
    "ServiceHTTPProtocol",
    "ServiceHTTPSProtocol",
    "ServiceTCP",
    "Snapshot",
    "SnapshotResponse",
    "SnapshotStats",
    "SortByIdCreated",
    "SortByIdName",
    "SortByIdNameCreated",
    "SshKey",
    "SshKeyResponse",
    "StorageBox",
    "StorageBoxAccessSettings",
    "StorageBoxResponse",
    "StorageBoxSnapshotPlan",
    "StorageBoxStats",
    "StorageBoxStatus",
    "StorageBoxType",
    "StorageBoxTypePrice",
    "Subaccount",
    "SubaccountAccessSettings",
    "SubaccountResponse",
    "SubnetType",
    "TargetTypeIP",
    "TargetTypeLabelSelector",
    "TargetTypeServer",
    "TypePricing",
    "Volume",
    "VolumeResponse",
    "VolumeStatus",
    "Zone",
    "ZoneBaseAuthoritativeNameservers",
    "ZoneBaseAuthoritativeNameserversDelegationStatus",
    "ZoneBaseRegistrar",
    "ZoneBaseStatus",
    "ZoneMode",
    "ZonePrimary",
    "ZonePrimaryNameserver",
    "ZonePrimaryNameserverTsigAlgorithm",
    "ZoneResponse",
    "ZoneSecondary",
    "Zonefile",
]


class _Model(BaseModel):
    """Base of all response models.

    Immutable and validated - how strictly depends on ``validation`` of the client.
    Fields the spec does not know (yet) are ignored, so new API fields do not break the
    client.
    """

    model_config = ConfigDict(frozen=True, strict=True, extra="ignore", defer_build=True)

    @override
    def __hash__(self) -> int:
        """Hashable although fields may be dicts (labels): consistent with ``==``."""
        return hash((type(self), self.model_dump_json(warnings=False)))


type ActionSort = Literal[
    "id",
    "id:asc",
    "id:desc",
    "command",
    "command:asc",
    "command:desc",
    "status",
    "status:asc",
    "status:desc",
    "started",
    "started:asc",
    "started:desc",
    "finished",
    "finished:asc",
    "finished:desc",
]
"""Allowed values of ``ActionSort``."""


type ActionStatus = Literal["running", "success", "error"]
"""Status of the Action."""


type Architecture = Literal["x86", "arm"]
"""CPU architecture of the Resource."""


type AssigneeType = Literal["server", "unassigned"]
"""Type of resource to assign the Primary IP to.

Omitted if the Primary IP should not get assigned.
"""


type CertificateStatusIssuance = Literal["pending", "completed", "failed"]
"""Status of the issuance process of the Certificate."""


type CertificateStatusRenewal = Literal["scheduled", "pending", "failed", "unavailable"]
"""Status of the renewal process of the Certificate."""


type CertificateType = Literal["uploaded", "managed"]
"""Type of the Certificate."""


type CreateImageRequestType = Literal["snapshot", "backup"]
"""Type of Image to create."""


type FirewallResourceType = Literal["server", "label_selector"]
"""Type of the resource."""


type FirewallRuleDirection = Literal["in", "out"]
"""Traffic direction in which the rule should be applied to.

Use `source_ips` for direction `in` and `destination_ips` for direction `out` to specify IPs.
"""


type FirewallRuleProtocol = Literal["tcp", "udp", "icmp", "esp", "gre"]
"""Network protocol to apply the rule for."""


type GetLoadBalancerMetricsType = Literal[
    "open_connections", "connections_per_second", "requests_per_second", "bandwidth"
]
"""Allowed values of ``GetLoadBalancerMetricsType``."""


type GetServerMetricsType = Literal["cpu", "disk", "network"]
"""Allowed values of ``GetServerMetricsType``."""


type HealthCheckProtocol = Literal["tcp", "http"]
"""Type of the health check."""


type HealthStatusDetail = Literal[
    "unspecified",
    "layer4_no_connection",
    "layer4_timeout",
    "layer7_timeout",
    "unexpected_http_status",
    "unexpected_http_content",
]
"""Additional details about why the health check failed. Only present when `status` is
`unhealthy`.
"""


type HealthStatusStatus = Literal["healthy", "unhealthy", "unknown"]
"""Allowed values of ``HealthStatusStatus``."""


type ImageStatus = Literal["available", "creating", "unavailable"]
"""Status of the Image."""


type ImageType = Literal["system", "app", "snapshot", "backup"]
"""Type of the Image."""


type IpType = Literal["ipv4", "ipv6"]
"""The Floating IP type."""


type IsoType = Literal["public", "private"]
"""Type of the ISO."""


type ListNetworkMembersSort = Literal[
    "id",
    "id:asc",
    "id:desc",
    "type",
    "type:asc",
    "type:desc",
    "status",
    "status:asc",
    "status:desc",
    "ip",
    "ip:asc",
    "ip:desc",
]
"""Allowed values of ``ListNetworkMembersSort``."""


type ListStorageBoxesSort = Literal[
    "id",
    "id:asc",
    "id:desc",
    "name",
    "name:asc",
    "name:desc",
    "created",
    "created:asc",
    "created:desc",
    "stats.size",
    "stats.size:asc",
    "stats.size:desc",
    "stats.size_filesystem",
    "stats.size_filesystem:asc",
    "stats.size_filesystem:desc",
]
"""Allowed values of ``ListStorageBoxesSort``."""


type LoadBalancerAlgorithmType = Literal["round_robin", "least_connections"]
"""Type of the algorithm."""


type LoadBalancerServiceProtocol = Literal["tcp", "http", "https"]
"""Protocol of the Load Balancer."""


type LoadBalancerTargetType = Literal["server", "label_selector", "ip"]
"""Type of the resource."""


type NetworkMemberStatus = Literal["ok", "attaching", "detaching", "updating", "error"]
"""Status of the resource within the Network.

- ``ok``: The resource is attached and its network configuration is up to date.
- ``attaching``: The resource is being attached to the Network.
- ``detaching``: The resource is being detached from the Network.
- ``updating``: The resource network configuration is being updated.
- ``error``: The last operation on this member failed. Its network configuration might be out
  of date, and the resource might not be reachable within the Network as expected.
"""


type NetworkMemberType = Literal["server", "load_balancer"]
"""Type of the resource attached to the Network.

- ``server``: The member is a Server.
- ``load_balancer``: The member is a Load Balancer.
"""


type OsFlavor = Literal[
    "ubuntu", "centos", "debian", "fedora", "rocky", "alma", "opensuse", "unknown"
]
"""Flavor of operating system contained in the Image."""


type RRSetType = Literal[
    "A",
    "AAAA",
    "CAA",
    "CNAME",
    "DS",
    "HINFO",
    "HTTPS",
    "MX",
    "NS",
    "PTR",
    "RP",
    "SOA",
    "SRV",
    "SVCB",
    "TLSA",
    "TXT",
]
"""Type of the RRSet."""


type ServerPublicNetFirewallStatus = Literal["applied", "pending"]
"""Status of the Firewall on the Server."""


type ServerStatus = Literal[
    "running",
    "initializing",
    "starting",
    "stopping",
    "off",
    "deleting",
    "migrating",
    "rebuilding",
    "unknown",
]
"""Status of the Server."""


type ServerTypeCpuType = Literal["shared", "dedicated"]
"""Type of cpu."""


type ServerTypeStorageType = Literal["local", "network"]
"""Type of Server boot drive. Local has higher speed. Network has better availability."""


type SortByIdCreated = Literal["id", "id:asc", "id:desc", "created", "created:asc", "created:desc"]
"""Allowed values of ``SortByIdCreated``."""


type SortByIdName = Literal["id", "id:asc", "id:desc", "name", "name:asc", "name:desc"]
"""Allowed values of ``SortByIdName``."""


type SortByIdNameCreated = Literal[
    "id",
    "id:asc",
    "id:desc",
    "name",
    "name:asc",
    "name:desc",
    "created",
    "created:asc",
    "created:desc",
]
"""Allowed values of ``SortByIdNameCreated``."""


type StorageBoxStatus = Literal["active", "initializing", "locked"]
"""Status of the Storage Box."""


type SubnetType = Literal["cloud", "server", "vswitch"]
"""Type of subnet.

- ``cloud``: Used to connect cloud Servers and Load Balancers.
- ``server``: Same as the `cloud` type. **Deprecated**, use the `cloud` type instead.
- ``vswitch``: Used to connect cloud Servers and Load Balancers with dedicated Servers
  (https://docs.hetzner.com/cloud/networks/connect-dedi-vswitch).
"""


type VolumeStatus = Literal["available", "creating"]
"""Status of the Volume."""


type ZoneBaseAuthoritativeNameserversDelegationStatus = Literal[
    "valid", "partially-valid", "invalid", "lame", "unregistered", "unknown"
]
"""Status of the delegation.

- ``valid``: Parent zone correctly delegates to assigned nameservers.
- ``partially-valid``: Parent zone delegates to additional Hetzner nameservers not assigned to
  this zone.
- ``invalid``: Parent zone does not delegate to the assigned nameservers.
- ``lame``: Parent zone delegates to nameservers that don't know the zone.
- ``unregistered``: Domain is not registered.
- ``unknown``: Not yet known.
"""


type ZoneBaseRegistrar = Literal["hetzner", "other", "unknown"]
"""Registrar of the domain."""


type ZoneBaseStatus = Literal["ok", "updating", "error"]
"""Status of the Zone.

- ``ok``: The Zone is pushed to the authoritative nameservers.
- ``updating``: The Zone is currently being published to the authoritative nameservers.
- ``error``: The Zone could not be published to the authoritative nameservers.
"""


type ZoneMode = Literal["primary", "secondary"]
"""Mode of the Zone.

For more information, see Zone Modes.
"""


type ZonePrimaryNameserverTsigAlgorithm = Literal["hmac-md5", "hmac-sha1", "hmac-sha256"]
"""Transaction signature (TSIG) (https://en.wikipedia.org/wiki/TSIG) algorithm used to generate
the TSIG key.
"""


class ActionResource(_Model):
    """``ActionResource``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Resource."""

    type: str
    """Type of the Resource."""


class ActionError(_Model):
    """Error message for the Action if an error occurred, otherwise null."""

    code: str
    """Fixed error code for machines."""

    message: str
    """Error message for humans."""


class Action(_Model):
    """``Action``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Action."""

    command: str
    """Command executed in the Action."""

    status: ActionStatus | UnknownValue
    """Status of the Action."""

    started: AwareDatetime
    """Point in time when the Action was started (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    finished: AwareDatetime | None
    """Point in time when the Action was finished (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format). Only set if the
    Action is finished otherwise null.
    """

    progress: int
    """Progress of the Action in percent."""

    resources: tuple[ActionResource, ...]
    """Resources the Action relates to."""

    error: ActionError | None
    """Error message for the Action if an error occurred, otherwise null."""


class ActionListResponse(_Model):
    """``ActionListResponse``."""

    actions: tuple[Action, ...]


class ListMetaPagination(_Model):
    """See "Pagination" for more information."""

    page: Annotated[int, Check(minimum=1)]
    """Current page number."""

    per_page: Annotated[int, Check(minimum=1, maximum=50)]
    """Maximum number of entries returned per page."""

    previous_page: int | None
    """Page number of the previous page. Can be null if the current page is the first one."""

    next_page: int | None
    """Page number of the next page. Can be null if the current page is the last one."""

    last_page: int | None
    """Page number of the last page available. Can be null if the current page is the last one."""

    total_entries: int | None
    """Total number of entries that exist for this query. Can be null if unknown."""


class ListMeta(_Model):
    """``ListMeta``."""

    pagination: ListMetaPagination
    """See "Pagination" for more information."""


class ActionListResponseWithMeta(_Model):
    """``ActionListResponseWithMeta``."""

    actions: tuple[Action, ...]
    meta: ListMeta


type ActionNullable = Action
"""One of the variants of ``ActionNullable``."""


class ActionResponse(_Model):
    """``ActionResponse``."""

    action: Action


type ArchitectureNullable = Architecture | UnknownValue
"""CPU architecture compatible with the ISO.

Null indicates no restriction on the architecture (wildcard).
"""


class CertificateStatusError(_Model):
    """If issuance or renewal reports `failed`, this property contains information about what...

    If issuance or renewal reports `failed`, this property contains information about what happened.
    """

    code: str | None = None
    message: str | None = None


class CertificateStatus(_Model):
    """Current status of a type `managed` Certificate, always *null* for type `uploaded`...

    Current status of a type `managed` Certificate, always *null* for type `uploaded` Certificates.
    """

    issuance: CertificateStatusIssuance | UnknownValue | None = None
    """Status of the issuance process of the Certificate."""

    renewal: CertificateStatusRenewal | UnknownValue | None = None
    """Status of the renewal process of the Certificate."""

    error: CertificateStatusError | None = None
    """If issuance or renewal reports `failed`, this property contains information about what
    happened.
    """


class CertificateUsedBy(_Model):
    """``CertificateUsedBy``."""

    id: int
    """ID of resource referenced."""

    type: str
    """Type of resource referenced."""


class Certificate(_Model):
    """``Certificate``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Certificate."""

    name: str
    """Name of the Resource. Must be unique per Project."""

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    type: CertificateType | UnknownValue | None = None
    """Type of the Certificate."""

    certificate: str | None
    """Certificate and chain in PEM format, in order so that each record directly certifies the
    one preceding.
    """

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    not_valid_before: AwareDatetime | None
    """Point in time when the Certificate becomes valid (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    not_valid_after: AwareDatetime | None
    """Point in time when the Certificate stops being valid (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    domain_names: tuple[str, ...]
    """Domains and subdomains covered by the Certificate."""

    fingerprint: str | None
    """SHA256 fingerprint of the Certificate."""

    status: CertificateStatus | None = None
    """Current status of a type `managed` Certificate, always *null* for type `uploaded`
    Certificates.
    """

    used_by: tuple[CertificateUsedBy, ...]
    """Resources currently using the Certificate."""


class CertificateResponse(_Model):
    """``CertificateResponse``."""

    certificate: Certificate


class CertificatesResponse(_Model):
    """``CertificatesResponse``."""

    certificates: tuple[Certificate, ...]
    meta: ListMeta


class CreateCertificateResponse(_Model):
    """``CreateCertificateResponse``."""

    certificate: Certificate
    action: ActionNullable | None = None


class RuleResponse(_Model):
    """``RuleResponse``."""

    description: Annotated[str | None, Check(max_length=255)] = None
    """Description of the rule."""

    direction: FirewallRuleDirection | UnknownValue
    """Traffic direction in which the rule should be applied to.

    Use `source_ips` for direction `in` and `destination_ips` for direction `out` to specify
    IPs.
    """

    source_ips: tuple[str, ...]
    """List of permitted IPv4/IPv6 addresses for incoming traffic.

    The `direction` must be set to `in`.

    IPs must be provided in CIDR block notation (https://wikipedia.org/wiki/CIDR). You can
    specify 100 CIDR blocks at most.

    The CIDR blocks may refer to networks (with empty host bits) or single hosts. For example,
    a network could be defined with `10.0.1.0/24` or `2001:db8:ff00:42::/64`, and a single
    host with `10.0.1.1/32` or `2001:db8:ff00:42::8329/128`.

    Use `0.0.0.0/0` to allow any IPv4 addresses and `::/0` to allow any IPv6 addresses.

    IPv6 CIDRs will be transformed to their canonical form according to RFC5952
    (https://datatracker.ietf.org/doc/html/rfc5952#section-4).
    """

    destination_ips: tuple[str, ...]
    """List of permitted IPv4/IPv6 addresses for outgoing traffic.

    The `direction` must be set to `out`.

    IPs must be in CIDR block notation (https://wikipedia.org/wiki/CIDR). You can specify 100
    CIDR blocks at most.

    The CIDR blocks may refer to networks (with empty host bits) or single hosts. For example,
    a network could be defined with `10.0.1.0/24` or `2001:db8:ff00:42::/64`, and a single
    host with `10.0.1.1/32` or `2001:db8:ff00:42::8329/128`.

    Use `0.0.0.0/0` to allow any IPv4 addresses and `::/0` to allow any IPv6 addresses.

    IPv6 CIDRs will be transformed to their canonical form according to RFC5952
    (https://datatracker.ietf.org/doc/html/rfc5952#section-4).
    """

    protocol: FirewallRuleProtocol | UnknownValue
    """Network protocol to apply the rule for."""

    port: str | None
    """Port or port range to apply the rule for.

    Only applicable for protocols `tcp` and `udp`.

    A port range can be specified by separating lower and upper bounds with a dash.
    `1024-5000` will include all ports starting from 1024 up to port 5000.
    """


class FirewallAppliedToServer(_Model):
    """Server the Firewall is applied to.

    Only set for `type` `server`, otherwise `null`.
    """

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Server."""


class LabelSelector(_Model):
    """Label Selector the Firewall is applied to.

    Only set for `type` `label_selector`, otherwise `null`.
    """

    selector: str
    """The selector."""


class FirewallAppliedToAppliedToResource(_Model):
    """``FirewallAppliedToAppliedToResource``."""

    type: Literal["server"] | None = None
    """Type of resource."""

    server: FirewallAppliedToServer | None = None
    """Server the Firewall is applied to.

    Only set for `type` `server`, otherwise `null`.
    """


class FirewallAppliedTo(_Model):
    """``FirewallAppliedTo``."""

    type: FirewallResourceType | UnknownValue
    """The type of resource to apply."""

    server: FirewallAppliedToServer | None = None
    """Server the Firewall is applied to.

    Only set for `type` `server`, otherwise `null`.
    """

    label_selector: LabelSelector | None = None
    """Label Selector the Firewall is applied to.

    Only set for `type` `label_selector`, otherwise `null`.
    """

    applied_to_resources: tuple[FirewallAppliedToAppliedToResource, ...] | None = None
    """Resources applied to via this Label Selector."""


class Firewall(_Model):
    """``Firewall``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Firewall."""

    name: Annotated[str, Check(min_length=1, max_length=128)]
    """Name of the Firewall.

    Must be unique per Project.
    """

    labels: Annotated[Mapping[str, str] | None, LABELS_RULES] = None
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    rules: tuple[RuleResponse, ...]
    applied_to: tuple[FirewallAppliedTo, ...]


class CreateFirewallResponse(_Model):
    """``CreateFirewallResponse``."""

    firewall: Firewall
    actions: tuple[Action, ...] | None = None


class DnsPtr(_Model):
    """``DnsPtr``."""

    ip: str
    """Single IPv4 or IPv6 address of the record."""

    dns_ptr: str
    """Domain Name to point to.

    PTR record content used for reverse DNS.
    """


class Location(_Model):
    """``Location``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Location."""

    name: Annotated[str, Check(pattern="^[a-z0-9]+(-?[a-z0-9]*)*$")]
    """Unique identifier of the Location."""

    description: str
    """Human readable description of the Location."""

    country: str
    """Country the Location resides in.

    ISO 3166-1 alpha-2 code of the country.
    """

    city: str
    """Name of the closest city to the Location.

    City name or city name and state in short form. E.g. `Falkenstein` or `Ashburn, VA`.
    """

    latitude: float
    """Latitude of the city closest to the Location."""

    longitude: float
    """Longitude of the city closest to the Location."""

    network_zone: Annotated[str, Check(pattern="^[a-z0-9]+(-?[a-z0-9]*)*$")]
    """Name of the Network Zone this Location resides in."""


class Protection(_Model):
    """Protection configuration for the Resource."""

    delete: bool
    """Prevent the Resource from being deleted."""


class FloatingIp(_Model):
    """``FloatingIp``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Floating IP."""

    name: Annotated[str, Check(min_length=1, max_length=255)]
    """Name of the Resource. Must be unique per Project."""

    description: str | None
    """Description of the Resource."""

    ip: str
    """IP address."""

    type: IpType | UnknownValue
    """The Floating IP type."""

    server: int | None
    """Server the Floating IP is assigned to.

    `null` if not assigned.
    """

    dns_ptr: tuple[DnsPtr, ...]
    """List of reverse DNS entries for the Floating IP."""

    home_location: Location
    """Location the for the Floating IP is located at.

    Routing is optimized for this Location.
    """

    blocked: bool
    """Indicates whether the Floating IP is blocked."""

    protection: Protection
    """Protection configuration for the Resource."""

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """


class CreateFloatingIpResponse(_Model):
    """``CreateFloatingIpResponse``."""

    floating_ip: FloatingIp

    action: ActionNullable | None = None
    """Action will only be returned if the Floating IP is getting assigned."""


class LoadBalancerPublicIp(_Model):
    """IP address (v4)."""

    id: Annotated[int | None, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Primary IP assigned to this Load Balancer.

    `null` if the IP address is still managed by the system and is not a Primary IP yet.
    """

    ip: str | None
    """IP address (v4) of this Load Balancer."""

    blocked: bool
    """Whether the IP is blocked by our abuse department."""

    dns_ptr: str | None
    """Reverse DNS PTR entry for the IPv4 address of this Load Balancer."""


class LoadBalancerPublicNet(_Model):
    """Public network information."""

    enabled: bool
    """Public Interface enabled or not."""

    ipv4: LoadBalancerPublicIp
    """IP address (v4)."""

    ipv6: LoadBalancerPublicIp
    """IP address (v6)."""


class LoadBalancerPrivateNet(_Model):
    """``LoadBalancerPrivateNet``."""

    network: int
    """ID of the Network."""

    ip: str
    """IP address (v4) of this Load Balancer in this Network."""


class DeprecationInfo(_Model):
    """Describes if, when and how the resource is deprecated.

    If this field is set to `null` the resource is not deprecated. If a value is set, it is
    considered deprecated.
    """

    unavailable_after: AwareDatetime
    """Date of the deprecated resource removal.

    Once this date is reached, the resource will not be returned by resource type "list"
    endpoint, and the resource can not be used to create new resources. For example, if this
    is an image, you can not create new servers with this image after the mentioned date.
    """

    announced: AwareDatetime
    """Date of the deprecation announcement."""


class Price(_Model):
    """Hourly price in this Location."""

    net: Decimal
    """Price without VAT."""

    gross: Decimal
    """Price with VAT added."""


class LocationPrice(_Model):
    """``LocationPrice``."""

    location: str
    """Name of the Location the price is for."""

    price_hourly: Price
    """Hourly price in this Location."""

    price_monthly: Price
    """Monthly price in this Location."""

    included_traffic: int
    """Free traffic per month in bytes in this Location."""

    price_per_tb_traffic: Price
    """Additional traffic price per TB in this Location."""


class LoadBalancerType(_Model):
    """``LoadBalancerType``."""

    id: int
    """ID of the Load Balancer type."""

    name: str
    """Unique identifier of the Load Balancer type."""

    description: str
    """Description of the Load Balancer type."""

    max_connections: int
    """Number of maximum simultaneous open connections."""

    max_services: int
    """Number of services a Load Balancer of this type can have."""

    max_targets: int
    """Number of targets a single Load Balancer can have."""

    max_assigned_certificates: int
    """Number of SSL Certificates that can be assigned to a single Load Balancer."""

    deprecated: AwareDatetime | None = None
    """**Deprecated:** This field is deprecated. Use the `deprecation` object instead.

    Point in time when the Load Balancer type is deprecated (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).

    Deprecated by the API.
    """

    deprecation: DeprecationInfo | None
    """Describes if, when and how the resource is deprecated. If this field is set to `null` the
    resource is not deprecated. If a value is set, it is considered deprecated.
    """

    prices: tuple[LocationPrice, ...]
    """Price per Location."""


class LoadBalancerServiceHealthCheckHttp(_Model):
    """Additional configuration for protocol http."""

    domain: Annotated[str | None, Check(max_length=128)]
    """Host header to send in the HTTP request. May not contain spaces, percent or backslash
    symbols. Can be null, in that case no host header is sent.
    """

    path: Annotated[str, Check(min_length=1, max_length=256)]
    """HTTP path to use for health checks. May not contain literal spaces, use percent-encoding
    instead.
    """

    response: Annotated[str | None, Check(max_length=256)] = None
    """String that must be contained in HTTP response in order to pass the health check."""

    status_codes: Annotated[tuple[str, ...] | None, Check(max_items=20)] = None
    """List of returned HTTP status codes in order to pass the health check. Supports the
    wildcards `?` for exactly one character and `*` for multiple ones.
    """

    tls: bool | None = None
    """Use HTTPS for health check."""


class LoadBalancerServiceHealthCheck(_Model):
    """Service health check."""

    protocol: HealthCheckProtocol | UnknownValue
    """Type of the health check."""

    port: int
    """Port the health check will be performed on."""

    interval: Annotated[int, Check(minimum=3, maximum=60)]
    """Time interval in seconds health checks are performed."""

    timeout: Annotated[int, Check(minimum=1, maximum=60)]
    """Time in seconds after an attempt is considered a timeout."""

    retries: Annotated[int, Check(minimum=1, maximum=5)]
    """Unsuccessful retries needed until a target is considered unhealthy; an unhealthy target
    needs the same number of successful retries to become healthy again.
    """

    http: LoadBalancerServiceHealthCheckHttp | None = None
    """Additional configuration for protocol http."""


class ServiceTCP(_Model):
    """``ServiceTCP``."""

    protocol: Literal["tcp"]

    listen_port: int
    """Port the Load Balancer listens on."""

    destination_port: int
    """Port the Load Balancer will balance to."""

    proxyprotocol: bool
    """Is Proxyprotocol enabled or not."""

    health_check: LoadBalancerServiceHealthCheck
    """Service health check."""


class LoadBalancerServiceHTTPConfig(_Model):
    """Configuration option for protocol http."""

    cookie_name: Annotated[str, Check(min_length=1, max_length=100)]
    """Name of the cookie used for sticky sessions."""

    cookie_lifetime: Annotated[int, Check(minimum=30, maximum=86400)]
    """Lifetime of the cookie used for sticky sessions (in seconds)."""

    timeout_idle: Annotated[int, Check(minimum=30, maximum=300)]
    """Idle timeout in seconds for the client and server side."""

    sticky_sessions: bool
    """Use sticky sessions."""


class ServiceHTTPProtocol(_Model):
    """``ServiceHTTPProtocol``."""

    protocol: Literal["http"]

    listen_port: int
    """Port the Load Balancer listens on."""

    destination_port: int
    """Port the Load Balancer will balance to."""

    proxyprotocol: bool
    """Is Proxyprotocol enabled or not."""

    health_check: LoadBalancerServiceHealthCheck
    """Service health check."""

    http: LoadBalancerServiceHTTPConfig
    """Configuration option for protocol http."""


class LoadBalancerServiceHTTPSConfig(_Model):
    """Configuration option for protocol https."""

    cookie_name: Annotated[str, Check(min_length=1, max_length=100)]
    """Name of the cookie used for sticky sessions."""

    cookie_lifetime: Annotated[int, Check(minimum=30, maximum=86400)]
    """Lifetime of the cookie used for sticky sessions (in seconds)."""

    timeout_idle: Annotated[int, Check(minimum=30, maximum=300)]
    """Idle timeout in seconds for the client and server side."""

    certificates: tuple[int, ...]
    """IDs of the Certificates to use for TLS/SSL termination by the Load Balancer; empty for
    TLS/SSL passthrough.
    """

    redirect_http: bool
    """Redirect HTTP requests to HTTPS."""

    sticky_sessions: bool
    """Use sticky sessions."""


class ServiceHTTPSProtocol(_Model):
    """``ServiceHTTPSProtocol``."""

    protocol: Literal["https"]

    listen_port: int
    """Port the Load Balancer listens on."""

    destination_port: int
    """Port the Load Balancer will balance to."""

    proxyprotocol: bool
    """Is Proxyprotocol enabled or not."""

    health_check: LoadBalancerServiceHealthCheck
    """Service health check."""

    http: LoadBalancerServiceHTTPSConfig
    """Configuration option for protocol https."""


type LoadBalancerService = Annotated[
    ServiceTCP | ServiceHTTPProtocol | ServiceHTTPSProtocol, Field(discriminator="protocol")
]
"""One of the variants of ``LoadBalancerService``."""


class LoadBalancerTargetServer(_Model):
    """Server where the traffic should be routed to.

    Only present for target type "server".
    """

    id: int
    """ID of the Server."""

    ip: str
    """IP of the Server that the traffic is routed to. Either the Server's primary IPv4 or, if an
    IPv6 was specified when adding the target, an IPv6 within the Server's /64 subnet.
    """


class HealthStatus(_Model):
    """``HealthStatus``."""

    listen_port: int
    status: HealthStatusStatus | UnknownValue

    detail: HealthStatusDetail | UnknownValue | None = None
    """Additional details about why the health check failed. Only present when `status` is
    `unhealthy`.
    """

    http_status_code: int | None = None
    """HTTP status code returned by the target during the last health check. Only present when
    `status` is `unhealthy` and `detail` is `unexpected_http_status`.
    """


class TargetTypeServer(_Model):
    """``TargetTypeServer``."""

    type: Literal["server"]

    server: LoadBalancerTargetServer
    """Server where the traffic should be routed to. Only present for target type "server"."""

    health_status: tuple[HealthStatus, ...]
    """List of health statuses of the services on this target. Only present for target types
    "server" and "ip".
    """

    use_private_ip: bool
    """Use the private network IP instead of the public IP. Only present for target types
    "server" and "label_selector".
    """


class LoadBalancerTargetLabelSelector(_Model):
    """Configuration for label selector targets, only valid and required if type is...

    Configuration for label selector targets, only valid and required if type is `label_selector`.
    """

    selector: Annotated[str, Check(min_length=1, max_length=1000)]
    """Label selector."""


class LoadBalancerTargetTarget(_Model):
    """``LoadBalancerTargetTarget``."""

    type: str
    """Type of the resource. Here always "server"."""

    server: LoadBalancerTargetServer
    """Server where the traffic should be routed to. Only present for target type "server"."""

    health_status: tuple[HealthStatus, ...]
    """List of health statuses of the services on this target. Only present for target types
    "server" and "ip".
    """

    use_private_ip: bool
    """Use the private network IP instead of the public IP. Only present for target types
    "server" and "label_selector".
    """


class TargetTypeLabelSelector(_Model):
    """``TargetTypeLabelSelector``."""

    type: Literal["label_selector"]

    label_selector: LoadBalancerTargetLabelSelector
    """Label selector used to determine targets. Only present for target type "label_selector"."""

    targets: tuple[LoadBalancerTargetTarget, ...]
    """List of resolved label selector target Servers."""

    use_private_ip: bool
    """Use the private network IP instead of the public IP. Only present for target types
    "server" and "label_selector".
    """


class LoadBalancerTargetIP(_Model):
    """Configuration for an IP target.

    It is only possible to use the (Public or vSwitch) IPs of Hetzner Online Root Servers belonging
    to the project owner. IPs belonging to other users are blocked. Additionally IPs belonging to
    services provided by Hetzner Cloud (Servers, Load Balancers, ...) are blocked as well. Only
    valid and required if type is `ip`.
    """

    ip: str
    """IP of a server that belongs to the same customer (public IPv4/IPv6) or private IP in a
    subnet type vswitch.
    """


class TargetTypeIP(_Model):
    """``TargetTypeIP``."""

    type: Literal["ip"]

    ip: LoadBalancerTargetIP
    """IP target where the traffic should be routed to. It is only possible to use the (Public or
    vSwitch) IPs of Hetzner Online Root Servers belonging to the project owner. IPs belonging
    to other users are blocked. Additionally IPs belonging to services provided by Hetzner
    Cloud (Servers, Load Balancers, ...) are blocked as well. Only present for target type
    `ip`.
    """

    health_status: tuple[HealthStatus, ...]
    """List of health statuses of the services on this target. Only present for target types
    "server" and "ip".
    """


type LoadBalancerTarget = Annotated[
    TargetTypeServer | TargetTypeLabelSelector | TargetTypeIP, Field(discriminator="type")
]
"""One of the variants of ``LoadBalancerTarget``."""


class LoadBalancerAlgorithm(_Model):
    """Algorithm of the Load Balancer."""

    type: LoadBalancerAlgorithmType | UnknownValue
    """Type of the algorithm."""


class LoadBalancer(_Model):
    """``LoadBalancer``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Load Balancer."""

    name: str
    """Name of the Resource. Must be unique per Project."""

    public_net: LoadBalancerPublicNet
    """Public network information."""

    private_net: tuple[LoadBalancerPrivateNet, ...]
    """Private networks information."""

    location: Location
    load_balancer_type: LoadBalancerType

    protection: Protection
    """Protection configuration for the Resource."""

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    services: tuple[LoadBalancerService, ...]
    """List of services that belong to this Load Balancer."""

    targets: tuple[LoadBalancerTarget, ...]
    """List of targets that belong to this Load Balancer."""

    algorithm: LoadBalancerAlgorithm
    """Algorithm of the Load Balancer."""

    outgoing_traffic: int | None
    """Outbound Traffic for the current billing period in bytes."""

    ingoing_traffic: int | None
    """Inbound Traffic for the current billing period in bytes."""

    included_traffic: int
    """Free Traffic for the current billing period in bytes."""


class CreateLoadBalancerResponse(_Model):
    """``CreateLoadBalancerResponse``."""

    load_balancer: LoadBalancer
    action: Action


class PlacementGroup(_Model):
    """``PlacementGroup``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Placement Group."""

    name: str
    """Name of the Resource. Must be unique per Project."""

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    type: Literal["spread"]
    """Type of Placement Group."""

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    servers: tuple[int, ...]
    """Array of IDs of Servers that are part of this Placement Group."""


class CreatePlacementGroupResponse(_Model):
    """``CreatePlacementGroupResponse``."""

    placement_group: PlacementGroup
    action: ActionNullable | None = None


class PrimaryIP(_Model):
    """``PrimaryIP``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Primary IP."""

    name: Annotated[str, Check(min_length=1, max_length=255)]
    """Name of the Resource. Must be unique per Project."""

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    blocked: bool
    """Blocked state of the Primary IP."""

    location: Location
    """Location of the Primary IP."""

    ip: str
    """IP address."""

    dns_ptr: tuple[DnsPtr, ...]
    """List of reverse DNS records."""

    protection: Protection
    """Protection configuration for the Resource."""

    type: IpType | UnknownValue
    """Primary IP type."""

    auto_delete: bool
    """Auto deletion state.

    If enabled the Primary IP will be deleted once the assigned resource gets deleted.
    """

    assignee_type: AssigneeType | UnknownValue
    """Type of resource the Primary IP is assigned to.

    As of 23 September 2026 `unassigned` is returned if the Primary IP is not assigned.
    """

    assignee_id: int | None
    """ID of resource the Primary IP is assigned to.

    `null` if the Primary IP is not assigned.
    """


class CreatePrimaryIPResponse(_Model):
    """``CreatePrimaryIPResponse``."""

    primary_ip: PrimaryIP

    action: ActionNullable | None = None
    """Action will only be returned if the Primary IP is getting assigned."""


class CreatedFrom(_Model):
    """Information about the Server the Image was created from."""

    id: int
    """ID of the Server the Image was created from."""

    name: str
    """Server name at the time the Image was created."""


class Image(_Model):
    """``Image``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Image."""

    type: ImageType | UnknownValue
    """Type of the Image."""

    status: ImageStatus | UnknownValue
    """Status of the Image."""

    name: str | None
    """Unique identifier of the Image. This value is only set for system Images."""

    description: str
    """Description of the Image."""

    image_size: float | None
    """Size of the Image file in our storage in GB. For snapshot Images this is the value
    relevant for calculating costs for the Image.
    """

    disk_size: float
    """Size of the disk contained in the Image in GB."""

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    created_from: CreatedFrom | None
    """Information about the Server the Image was created from."""

    bound_to: int | None
    """ID of Server the Image is bound to. Only set for Images of type `backup`."""

    os_flavor: OsFlavor | UnknownValue
    """Flavor of operating system contained in the Image."""

    os_version: str | None
    """Operating system version."""

    rapid_deploy: bool | None = None
    """Indicates that rapid deploy of the Image is available."""

    protection: Protection
    """Protection configuration for the Resource."""

    deprecated: AwareDatetime | None = None
    """**Deprecated:** This field is deprecated, use the deprecation object instead.

    Point in time when the Image is considered to be deprecated (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).

    Deprecated by the API.
    """

    deprecation: DeprecationInfo | None
    """Describes if, when and how the resource is deprecated. If this field is set to `null` the
    resource is not deprecated. If a value is set, it is considered deprecated.
    """

    deleted: str | None
    """Point in time where the Image was deleted (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    architecture: Architecture | UnknownValue
    """CPU architecture compatible with the Image."""


class CreateServerImageResponse(_Model):
    """``CreateServerImageResponse``."""

    image: Image
    action: Action


class ServerPublicNetIpv4(_Model):
    """IP address (v4) and its reverse DNS entry of this Server."""

    id: Annotated[int | None, Check(minimum=1, maximum=9007199254740991)] = None
    """ID of the Primary IP."""

    ip: str
    """IP address (v4) of this Server."""

    blocked: bool
    """Whether the IP is blocked by our abuse department."""

    dns_ptr: str
    """Reverse DNS PTR entry for the IPv4 addresses of this Server."""


class ServerPublicNetIpv6(_Model):
    """IPv6 network assigned to this Server and its reverse DNS entry."""

    id: Annotated[int | None, Check(minimum=1, maximum=9007199254740991)] = None
    """ID of the Primary IP."""

    ip: str
    """IP address (v6) of this Server."""

    blocked: bool
    """Whether the IP is blocked by our abuse department."""

    dns_ptr: tuple[DnsPtr, ...] | None
    """Reverse DNS PTR entries for the IPv6 addresses of this Server."""


class ServerPublicNetFirewall(_Model):
    """``ServerPublicNetFirewall``."""

    id: Annotated[int | None, Check(minimum=1, maximum=9007199254740991)] = None
    """ID of the Firewall."""

    status: ServerPublicNetFirewallStatus | UnknownValue | None = None
    """Status of the Firewall on the Server."""


class ServerPublicNet(_Model):
    """Public network information.

    The Server's IPv4 address can be found in `public_net->ipv4->ip`.
    """

    ipv4: ServerPublicNetIpv4 | None
    """IP address (v4) and its reverse DNS entry of this Server."""

    ipv6: ServerPublicNetIpv6 | None
    """IPv6 network assigned to this Server and its reverse DNS entry."""

    floating_ips: tuple[int, ...]
    """IDs of Floating IPs assigned to this Server."""

    firewalls: tuple[ServerPublicNetFirewall, ...] | None = None
    """Firewalls applied to the public network interface of this Server."""


class ServerPrivateNet(_Model):
    """``ServerPrivateNet``."""

    network: int | None = None
    """The Network ID the server is attached to."""

    ip: str | None = None
    """The server IP address on the network."""

    alias_ips: tuple[str, ...] | None = None
    """Additional IP addresses of the server on the network."""

    mac_address: str | None = None
    """The server MAC address on the network."""


class ServerTypeLocation(_Model):
    """A Location (containing only id and name) and Server Type specific metadata."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Location."""

    name: str
    """Name of the Location."""

    deprecation: DeprecationInfo | None
    """Describes if, when and how the resource is deprecated. If this field is set to `null` the
    resource is not deprecated. If a value is set, it is considered deprecated.
    """

    recommended: bool
    """Whether the Server Type is recommended in this Location."""

    available: bool
    """Whether the Server Type is temporarily unavailable in this Location."""


class ServerType(_Model):
    """``ServerType``."""

    id: int
    """ID of the Server type."""

    name: str
    """Unique identifier of the Server type."""

    description: str
    """Description of the Server type."""

    cores: int
    """Number of cpu cores a Server of this type will have."""

    memory: float
    """Memory a Server of this type will have in GB."""

    disk: float
    """Disk size a Server of this type will have in GB."""

    deprecated: bool
    """This field is deprecated. Use the deprecation object instead."""

    prices: tuple[LocationPrice, ...]
    """Price per Location."""

    storage_type: ServerTypeStorageType | UnknownValue
    """Type of Server boot drive. Local has higher speed. Network has better availability."""

    cpu_type: ServerTypeCpuType | UnknownValue
    """Type of cpu."""

    category: str | None = None
    """Category of Server Type."""

    architecture: Architecture | UnknownValue
    """CPU architecture of the Server Type."""

    deprecation: DeprecationInfo | None = None
    """This field is deprecated.

    Use the `deprecation` object in the `locations` field instead
    (`.locations[].deprecation`).

    Deprecated by the API.
    """

    locations: tuple[ServerTypeLocation, ...]
    """Supported Location and per Location details for the Server Type.

    A Server Type is:
     - only supported in the Location that are listed.
     - deprecated in the Location when the `deprecation` property is set.
     - permanently unavailable in the Location when the `deprecation.unavailable_after` date
       is in the past.
     - temporarily unavailable in the Location when the `deprecation.available` is false.
    """


class Iso(_Model):
    """``Iso``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the ISO."""

    name: str | None
    """Unique identifier of the ISO. Only set for public ISOs."""

    description: str
    """Description of the ISO."""

    type: IsoType | UnknownValue | None
    """Type of the ISO."""

    deprecation: DeprecationInfo | None
    """Describes if, when and how the resource is deprecated. If this field is set to `null` the
    resource is not deprecated. If a value is set, it is considered deprecated.
    """

    architecture: ArchitectureNullable | None
    """CPU architecture compatible with the ISO.

    Null indicates no restriction on the architecture (wildcard).
    """


class ServerProtection(_Model):
    """Protection configuration for the Server."""

    delete: bool
    """If true, prevents the Server from being deleted."""

    rebuild: bool
    """If true, prevents the Server from being rebuilt."""


class Server(_Model):
    """``Server``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Server."""

    name: str
    """Name of the Server (must be unique per Project and a valid hostname as per RFC 1123)."""

    status: ServerStatus | UnknownValue
    """Status of the Server."""

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    public_net: ServerPublicNet
    """Public network information. The Server's IPv4 address can be found in
    `public_net->ipv4->ip`.
    """

    private_net: tuple[ServerPrivateNet, ...]
    """Private networks information."""

    server_type: ServerType

    location: Location
    """Location this Resource is located at."""

    image: Image | None
    """Image the server is based on."""

    iso: Iso | None
    """ISO Image that is attached to this Server. Null if no ISO is attached."""

    rescue_enabled: bool
    """True if rescue mode is enabled. Server will then boot into rescue system on next reboot."""

    locked: bool
    """True if Server has been locked and is not available to user."""

    backup_window: str | None
    """Time window (UTC) in which the backup will run, or null if the backups are not enabled."""

    outgoing_traffic: int | None
    """Outbound Traffic for the current billing period in bytes."""

    ingoing_traffic: int | None
    """Inbound Traffic for the current billing period in bytes."""

    included_traffic: int | None
    """Free Traffic for the current billing period in bytes."""

    protection: ServerProtection
    """Protection configuration for the Server."""

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    volumes: tuple[int, ...] | None = None
    """IDs of Volumes assigned to this Server."""

    load_balancers: tuple[int, ...] | None = None
    """Load Balancer IDs assigned to the server."""

    primary_disk_size: float
    """Size of the primary Disk."""

    placement_group: PlacementGroup | None = None
    """The placement group the server is assigned to."""


class CreateServerResponse(_Model):
    """``CreateServerResponse``."""

    server: Server
    action: Action
    next_actions: tuple[Action, ...]

    root_password: str | None = Field(repr=False)
    """Root password when no SSH keys have been specified."""


class StorageBoxTypePrice(_Model):
    """``StorageBoxTypePrice``."""

    location: str
    """Name of the Location the price is for."""

    price_hourly: Price
    """Hourly price in this Location."""

    price_monthly: Price
    """Monthly price in this Location."""

    setup_fee: Price
    """Setup fee in this Location."""


class StorageBoxType(_Model):
    """``StorageBoxType``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Storage Box Type."""

    name: str
    """Name of the Storage Box Type."""

    description: str
    """Description of the Storage Box Type."""

    snapshot_limit: int | None
    """Maximum number of allowed manual snapshots."""

    automatic_snapshot_limit: int | None
    """Maximum number of snapshots created automatically by a snapshot plan."""

    subaccounts_limit: int
    """Maximum number of subaccounts."""

    size: int
    """Available storage in bytes."""

    prices: tuple[StorageBoxTypePrice, ...]
    """Price per Location."""

    deprecation: DeprecationInfo | None
    """Describes if, when and how the resource is deprecated. If this field is set to `null` the
    resource is not deprecated. If a value is set, it is considered deprecated.
    """


class StorageBoxAccessSettings(_Model):
    """Access settings of the Storage Box."""

    reachable_externally: bool
    """Whether access from outside the Hetzner network is allowed."""

    samba_enabled: bool
    """Whether the Samba subsystem is enabled."""

    ssh_enabled: bool
    """Whether the SSH subsystem is enabled."""

    webdav_enabled: bool
    """Whether the WebDAV subsystem is enabled."""

    zfs_enabled: bool
    """Whether the ZFS snapshot folder is visible."""


class StorageBoxSnapshotPlan(_Model):
    """Details of the active snapshot plan.

    Not available if the `status` is `initializing`.
    """

    max_snapshots: Annotated[int, Check(minimum=1)]
    """Maximum amount of Snapshots that will be created by this Snapshot Plan.

    Older Snapshots will be deleted.
    """

    minute: Annotated[int, Check(minimum=0, maximum=59)]
    """Minute when the Snapshot Plan is executed (UTC)."""

    hour: Annotated[int, Check(minimum=0, maximum=23)]
    """Hour when the Snapshot Plan is executed (UTC)."""

    day_of_week: Annotated[int | None, Check(minimum=1, maximum=7)]
    """Day of the week when the Snapshot Plan is executed.

    Starts at 1 for Monday til 7 for Sunday. Null means every day.
    """

    day_of_month: Annotated[int | None, Check(minimum=1, maximum=31)]
    """Day of the month when the Snapshot Plan is executed.

    Null means every day.
    """


class StorageBoxStats(_Model):
    """Statistics of the Storage Box."""

    size: int
    """Current disk usage in bytes."""

    size_data: int
    """Current disk usage for data in bytes."""

    size_snapshots: int
    """Current disk usage for snapshots in bytes."""


class StorageBox(_Model):
    """``StorageBox``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Storage Box."""

    name: str
    """Name of the Storage Box."""

    storage_box_type: StorageBoxType
    """Type of the Storage Box."""

    location: Location

    access_settings: StorageBoxAccessSettings
    """Access settings of the Storage Box."""

    snapshot_plan: StorageBoxSnapshotPlan | None
    """Details of the active snapshot plan.

    Not available if the `status` is `initializing`.
    """

    protection: Protection
    """Protection configuration for the Resource."""

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    status: StorageBoxStatus | UnknownValue
    """Status of the Storage Box."""

    username: str | None
    """Primary username of the Storage Box.

    Not available if the `status` is `initializing`.
    """

    server: str | None
    """FQDN of the Storage Box.

    Not available if the `status` is `initializing`.
    """

    system: str | None
    """Host system of the Storage Box.

    Not available if the `status` is `initializing`.
    """

    stats: StorageBoxStats
    """Statistics of the Storage Box."""

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """


class CreateStorageBoxResponse(_Model):
    """``CreateStorageBoxResponse``."""

    storage_box: StorageBox
    action: Action


class CreateStorageBoxSnapshotResponseSnapshot(_Model):
    """``CreateStorageBoxSnapshotResponseSnapshot``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Storage Box Snapshot."""

    storage_box: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Storage Box."""


class CreateStorageBoxSnapshotResponse(_Model):
    """``CreateStorageBoxSnapshotResponse``."""

    snapshot: CreateStorageBoxSnapshotResponseSnapshot
    action: Action


class CreateStorageBoxSubaccountResponseSubaccount(_Model):
    """``CreateStorageBoxSubaccountResponseSubaccount``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Storage Box Subaccount."""

    storage_box: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Storage Box."""


class CreateStorageBoxSubaccountResponse(_Model):
    """``CreateStorageBoxSubaccountResponse``."""

    subaccount: CreateStorageBoxSubaccountResponseSubaccount
    action: Action


class Volume(_Model):
    """``Volume``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Volume."""

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    name: str
    """Name of the Resource. Must be unique per Project."""

    server: int | None
    """ID of the Server the Volume is attached to, null if it is not attached at all."""

    location: Location
    """Location of the Volume. Volume can only be attached to Servers in the same Location."""

    size: float
    """Size in GB of the Volume."""

    linux_device: str
    """Device path on the file system for the Volume."""

    protection: Protection
    """Protection configuration for the Resource."""

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    status: VolumeStatus | UnknownValue
    """Status of the Volume."""

    format: str | None
    """Filesystem of the Volume if formatted on creation, null if not formatted on creation."""


class CreateVolumeResponse(_Model):
    """``CreateVolumeResponse``."""

    volume: Volume
    action: Action
    next_actions: tuple[Action, ...]


class ZonePrimaryNameserver(_Model):
    """Primary nameserver that returns Zones via `AXFR`.

    Must allow queries from and may send `NOTIFY` queries to Hetzner's secondary nameservers
    (https://docs.hetzner.com/dns-console/dns/general/authoritative-name-servers#secondary-dns-servers-old-name-servers-for-robot-customers).
    """

    address: str
    """Public IPv4 or IPv6 address of the primary nameserver.

    Must be unique across all primary nameservers of this zone.
    """

    port: int | None = None
    """Port of the primary nameserver."""

    tsig_key: str | None = None
    """Transaction signature (TSIG) (https://en.wikipedia.org/wiki/TSIG) key to use for the zone
    transfer. Must be base64 encoded.
    """

    tsig_algorithm: ZonePrimaryNameserverTsigAlgorithm | UnknownValue | None = None
    """Transaction signature (TSIG) (https://en.wikipedia.org/wiki/TSIG) algorithm used to
    generate the TSIG key.
    """


class ZoneBaseAuthoritativeNameservers(_Model):
    """``ZoneBaseAuthoritativeNameservers``."""

    assigned: tuple[str, ...]
    """Authoritative Hetzner nameservers assigned to this Zone."""

    delegated: tuple[str, ...]
    """Authoritative nameservers currently delegated to by the parent DNS zone.

    If these don't match the assigned authoritative nameservers, the DNS zone is currently not
    being served by Hetzner.
    """

    delegation_last_check: AwareDatetime | None
    """Point in time (in RFC3339 (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6)
    format) when the DNS zone delegation was last checked.
    """

    delegation_status: ZoneBaseAuthoritativeNameserversDelegationStatus | UnknownValue | None = None
    """Status of the delegation."""


class ZonePrimary(_Model):
    """``ZonePrimary``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Zone."""

    name: Annotated[str, Check(max_length=255)]
    """Name of the Zone.

    All names with well-known public suffixes (https://publicsuffix.org/) (e.g. `.de`, `.com`,
    `.co.uk`) are supported. Subdomains are not supported.

    The name must be in lower case and must not end with a dot. Internationalized domain names
    (https://en.wikipedia.org/wiki/Internationalized_domain_name) must be transcribed to
    Punycode (https://wikipedia.org/wiki/Punycode) representation with ACE prefix, e.g.
    `xn--mnchen-3ya.de` (`münchen.de`).
    """

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    primary_nameservers: tuple[ZonePrimaryNameserver, ...] | None = None
    """Primary nameservers of the Zone.

    Only set if Zone is in secondary mode, otherwise empty.
    """

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    protection: Protection
    """Protection configuration for the Resource."""

    ttl: Annotated[int, Check(minimum=60, maximum=2147483647)]
    """Default Time To Live (TTL) of the Zone.

    Must be in between 60s and 2147483647s.

    This TTL is used for RRSets that do not explicitly define a TTL.
    """

    status: ZoneBaseStatus | UnknownValue
    """Status of the Zone."""

    record_count: int
    """Number of resource records (RR) within the Zone."""

    authoritative_nameservers: ZoneBaseAuthoritativeNameservers

    registrar: ZoneBaseRegistrar | UnknownValue
    """Registrar of the domain."""

    mode: Literal["primary"]
    """Mode of the Zone.

    For more information, see Zone Modes.
    """


class ZoneSecondary(_Model):
    """``ZoneSecondary``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Zone."""

    name: Annotated[str, Check(max_length=255)]
    """Name of the Zone.

    All names with well-known public suffixes (https://publicsuffix.org/) (e.g. `.de`, `.com`,
    `.co.uk`) are supported. Subdomains are not supported.

    The name must be in lower case and must not end with a dot. Internationalized domain names
    (https://en.wikipedia.org/wiki/Internationalized_domain_name) must be transcribed to
    Punycode (https://wikipedia.org/wiki/Punycode) representation with ACE prefix, e.g.
    `xn--mnchen-3ya.de` (`münchen.de`).
    """

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    primary_nameservers: tuple[ZonePrimaryNameserver, ...] | None = None
    """Primary nameservers of the Zone.

    Only set if Zone is in secondary mode, otherwise empty.
    """

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    protection: Protection
    """Protection configuration for the Resource."""

    ttl: Annotated[int, Check(minimum=60, maximum=2147483647)]
    """Default Time To Live (TTL) of the Zone.

    Must be in between 60s and 2147483647s.

    This TTL is used for RRSets that do not explicitly define a TTL.
    """

    status: ZoneBaseStatus | UnknownValue
    """Status of the Zone."""

    record_count: int
    """Number of resource records (RR) within the Zone."""

    authoritative_nameservers: ZoneBaseAuthoritativeNameservers

    registrar: ZoneBaseRegistrar | UnknownValue
    """Registrar of the domain."""

    mode: Literal["secondary"]
    """Mode of the Zone.

    For more information, see Zone Modes.
    """


type Zone = Annotated[ZonePrimary | ZoneSecondary, Field(discriminator="mode")]
"""One of the variants of ``Zone``."""


class CreateZoneResponse(_Model):
    """``CreateZoneResponse``."""

    zone: Zone
    action: Action


class RRSetProtection(_Model):
    """Protection of the RRSet."""

    change: bool
    """Prevent the Resource from being changed."""


class Record(_Model):
    """Record of a RRSet.

    The `value` is used to identify the record in an RRSet.
    """

    value: str
    """Value of the record.

    For details about accepted values, see the DNS record types documentation
    (https://docs.hetzner.com/networking/dns/record-types/overview/).
    """

    comment: str | None = None
    """Comment of the record."""


class RRSet(_Model):
    """``RRSet``."""

    id: str
    """ID of the RRSet.

    The ID is composed of the name and type, joined with a slash (e.g. `www/AAAA`).
    """

    name: str
    """Name of the RRSet.

    The name must be in lower case, and must not end with a dot or the Zone name. Names
    containing non-ASCII characters must be transcribed to Punycode
    (https://wikipedia.org/wiki/Punycode) representation with ACE prefix, e.g. `xn--4bi` (️).

    For the Zone apex, use `@`.
    """

    type: RRSetType | UnknownValue
    """Type of the RRSet."""

    ttl: Annotated[int | None, Check(minimum=60, maximum=2147483647)]
    """Time To Live (TTL) of the RRSet.

    Must be in between 60s and 2147483647s.

    If not set, the Zone's Default TTL is used.
    """

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    protection: RRSetProtection
    """Protection of the RRSet."""

    records: tuple[Record, ...]
    """Records of the RRSet.

    Must not be empty and must only contain distinct record values. The order of records
    returned in responses is not guaranteed to be consistent.
    """

    zone: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Zone."""


class CreateZoneRrsetResponse(_Model):
    """``CreateZoneRrsetResponse``."""

    rrset: RRSet
    action: Action


class DatacenterServerTypes(_Model):
    """This field is deprecated, as all of it's properties are deprecated.

    Server Types supported and available in this Data Center.

    Deprecated by the API.
    """

    supported: tuple[int, ...] | None = None
    """This field is deprecated. Use the Server Type `locations` field instead.

    List of Server Types supported in this Data Center.

    These Server Types are generally available in this Data Center, but may be temporarily out
    of stock.

    Deprecated by the API.
    """

    available: tuple[int, ...] | None = None
    """This field is deprecated. Use the `available` flag in the Server Type `locations` field
    instead (`server_type.locations[].available`).

    Server Types currently available in this Data Center.

    These Server Types can currently be purchased. Types that are temporarily unavailable but
    are supported in this Data Center are listed as `supported`.

    Deprecated by the API.
    """

    available_for_migration: tuple[int, ...] | None = None
    """This field is deprecated. Use the `available` flag in the Server Type `locations` field
    instead (`server_type.locations[].available`).

    Server Types available to migrate to in this Data Center.

    Existing Servers can be migrated to these Server Types.

    Deprecated by the API.
    """


class Datacenter(_Model):
    """``Datacenter``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Data Center."""

    name: Annotated[str, Check(pattern="^[a-z0-9]+(-?[a-z0-9]*)*$")]
    """Unique name for the Data Center.

    May be used as a more descriptive identifier.
    """

    description: str
    """Descriptive name for the Data Center.

    Desired to be easy to understand for humans. May change for cosmetic reasons. Must not be
    used as an identifier.
    """

    location: Location
    """Location the Data Center is located at."""

    server_types: DatacenterServerTypes | None = None
    """This field is deprecated, as all of it's properties are deprecated.

    Server Types supported and available in this Data Center.

    Deprecated by the API.
    """


class ErrorResponseError(_Model):
    """``ErrorResponseError``."""

    code: str
    """Error code for machines."""

    message: str
    """Error message for humans."""

    details: Mapping[str, JsonValue] | None = None
    """Details about the error."""


class ErrorResponse(_Model):
    """``ErrorResponse``."""

    error: ErrorResponseError


class FirewallResponse(_Model):
    """``FirewallResponse``."""

    firewall: Firewall


class FirewallsResponse(_Model):
    """``FirewallsResponse``."""

    firewalls: tuple[Firewall, ...]
    meta: ListMeta


class FloatingIpResponse(_Model):
    """``FloatingIpResponse``."""

    floating_ip: FloatingIp


class GetDatacenterResponse(_Model):
    """``GetDatacenterResponse``."""

    datacenter: Datacenter


class GetIsoResponse(_Model):
    """``GetIsoResponse``."""

    iso: Iso


class GetLoadBalancerTypeResponse(_Model):
    """``GetLoadBalancerTypeResponse``."""

    load_balancer_type: LoadBalancerType


class GetLocationResponse(_Model):
    """``GetLocationResponse``."""

    location: Location


class PricingPrimaryIpPrice(_Model):
    """``PricingPrimaryIpPrice``."""

    location: str
    """Name of the Location the price is for."""

    price_hourly: Price
    """Hourly price in this Location."""

    price_monthly: Price
    """Monthly price in this Location."""


class PricingPrimaryIp(_Model):
    """``PricingPrimaryIp``."""

    type: IpType | UnknownValue
    """Type of Primary IP the price is for."""

    prices: tuple[PricingPrimaryIpPrice, ...]
    """Price of the Primary IP type per Location."""


class PricingFloatingIpPrice(_Model):
    """``PricingFloatingIpPrice``."""

    location: str
    """Name of the Location the price is for."""

    price_monthly: Price
    """Monthly price in this Location."""


class PricingFloatingIp(_Model):
    """``PricingFloatingIp``."""

    type: IpType | UnknownValue
    """Type of Floating IP the price is for."""

    prices: tuple[PricingFloatingIpPrice, ...]
    """Price of the Floating IP type per Location."""


class PricePerGbMonth(_Model):
    """Price of Images."""

    price_per_gb_month: Price
    """Price of Images per GB/month."""


class PricingServerBackup(_Model):
    """Price of Server backups."""

    percentage: Decimal
    """Price increase of the Server base price in percentage."""


class TypePricing(_Model):
    """``TypePricing``."""

    id: int
    """ID of the Server Types the price is for."""

    name: str
    """Name of the Server Types the price is for."""

    prices: tuple[LocationPrice, ...]
    """Price of the Server Types per Location."""


class PricingFloatingIp2(_Model):
    """Price of Floating IPs.

    **Deprecated**: This field is deprecated, please refer to the `floating_ips` field instead.

    See the Changelog
    (https://docs.hetzner.cloud/changelog#2024-08-29-field-floating_ip-in-pricing-response-is-now-deprecated)
    for more details.

    Deprecated by the API.
    """

    price_monthly: Price
    """Price of one Floating IP per month."""


class Pricing(_Model):
    """``Pricing``."""

    currency: str
    """Currency the returned prices are expressed in, coded according to ISO 4217
    (https://wikipedia.org/wiki/ISO_4217).
    """

    vat_rate: Decimal
    """VAT rate used for calculating prices with VAT."""

    primary_ips: tuple[PricingPrimaryIp, ...]
    """Price of Primary IPs per type and per Location."""

    floating_ips: tuple[PricingFloatingIp, ...]
    """Price of Floating IPs per type and per Location."""

    image: PricePerGbMonth
    """Price of Images."""

    volume: PricePerGbMonth
    """Price of Volumes."""

    server_backup: PricingServerBackup
    """Price of Server backups."""

    server_types: tuple[TypePricing, ...]
    """Price of Server per type and per Location."""

    load_balancer_types: tuple[TypePricing, ...]
    """Price of Load Balancer per type and per Location."""

    floating_ip: PricingFloatingIp2 | None = None
    """Price of Floating IPs.

    **Deprecated**: This field is deprecated, please refer to the `floating_ips` field
    instead.

    See the Changelog
    (https://docs.hetzner.cloud/changelog#2024-08-29-field-floating_ip-in-pricing-response-is-now-deprecated)
    for more details.

    Deprecated by the API.
    """


class GetPricingResponse(_Model):
    """``GetPricingResponse``."""

    pricing: Pricing


class GetServerTypeResponse(_Model):
    """``GetServerTypeResponse``."""

    server_type: ServerType


class GetStorageBoxTypeResponse(_Model):
    """``GetStorageBoxTypeResponse``."""

    storage_box_type: StorageBoxType


class ImageResponse(_Model):
    """``ImageResponse``."""

    image: Image


class ListDatacentersResponse(_Model):
    """``ListDatacentersResponse``."""

    datacenters: tuple[Datacenter, ...]
    """List of Data Centers."""

    recommendation: int | None = None
    """This field is deprecated. Use the `recommended` flag in the Server Type `locations` field
    instead (`server_type.locations[].recommended`).

    Recommended Data Center for creating new resources.

    Deprecated by the API.
    """

    meta: ListMeta


class ListFloatingIpsResponse(_Model):
    """``ListFloatingIpsResponse``."""

    floating_ips: tuple[FloatingIp, ...]
    meta: ListMeta


class ListImagesResponse(_Model):
    """``ListImagesResponse``."""

    images: tuple[Image, ...]
    meta: ListMeta


class ListIsosResponse(_Model):
    """``ListIsosResponse``."""

    isos: tuple[Iso, ...]
    meta: ListMeta


class ListLoadBalancerTypesResponse(_Model):
    """``ListLoadBalancerTypesResponse``."""

    load_balancer_types: tuple[LoadBalancerType, ...]
    meta: ListMeta


class ListLoadBalancersResponse(_Model):
    """``ListLoadBalancersResponse``."""

    load_balancers: tuple[LoadBalancer, ...]
    meta: ListMeta


class ListLocationsResponse(_Model):
    """``ListLocationsResponse``."""

    locations: tuple[Location, ...]
    """List of Locations."""

    meta: ListMeta


class ListMeta100Pagination(_Model):
    """See "Pagination" for more information."""

    page: Annotated[int, Check(minimum=1)]
    """Current page number."""

    per_page: Annotated[int, Check(minimum=1, maximum=100)]
    """Maximum number of entries returned per page."""

    previous_page: int | None
    """Page number of the previous page. Can be null if the current page is the first one."""

    next_page: int | None
    """Page number of the next page. Can be null if the current page is the last one."""

    last_page: int | None
    """Page number of the last page available. Can be null if the current page is the last one."""

    total_entries: int | None
    """Total number of entries that exist for this query. Can be null if unknown."""


class ListMeta100(_Model):
    """``ListMeta100``."""

    pagination: ListMeta100Pagination
    """See "Pagination" for more information."""


class Member(_Model):
    """``Member``."""

    type: NetworkMemberType | UnknownValue
    """Type of the resource attached to the Network."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the attached resource."""

    ip: str
    """IP address of the resource within the Network."""

    status: NetworkMemberStatus | UnknownValue
    """Status of the resource within the Network."""

    alias_ips: tuple[str, ...]
    """Additional IP addresses of the resource within the Network."""

    subnet: str
    """IP range of the subnet the resource is attached to.

    Uses CIDR notation.
    """


class ListNetworkMembersResponse(_Model):
    """``ListNetworkMembersResponse``."""

    members: tuple[Member, ...]
    meta: ListMeta


class NetworkSubnet(_Model):
    """``NetworkSubnet``."""

    type: SubnetType | UnknownValue
    """Type of subnet."""

    ip_range: str | None = None
    """IP range of the subnet.

    Uses CIDR notation.
    """

    network_zone: str
    """Name of the Network Zone.

    The Location contains the `network_zone` property it belongs to.
    """

    gateway: str
    """Gateway for Servers attached to this subnet.

    For subnets of type `server` this is always the first IP of the subnets IP range.
    """

    vswitch_id: int | None = None
    """ID of the robot vSwitch if the subnet is of type `vswitch`."""


class Route(_Model):
    """``Route``."""

    destination: str
    """Destination network or host of the route.

    Packages addressed for IPs matching the destination IP prefix will be send to the
    specified gateway.

    Must be one of
    * private IPv4 ranges of RFC1918
    * or `0.0.0.0/0`.

    Must not overlap with
    * an existing ip_range in any subnets
    * or with any destinations in other routes
    * or with `172.31.1.1`.

    `172.31.1.1` is being used as a gateway for the public network interface of Servers.
    """

    gateway: str
    """Gateway of the route.

    Packages addressed for the specified destination will be send to this IP address.

    Cannot be
    * the first IP of the networks ip_range,
    * an IP behind a vSwitch or
    * `172.31.1.1`.

    `172.31.1.1` is being used as a gateway for the public network interface of Servers.
    """


class Network(_Model):
    """``Network``."""

    id: int
    """ID of the Network."""

    name: Annotated[str, Check(min_length=1, max_length=128)]
    """Name of the Network."""

    ip_range: str
    """IP range of the Network.

    Uses CIDR notation.
    """

    subnets: tuple[NetworkSubnet, ...]
    """List of subnets allocated in this Network."""

    routes: tuple[Route, ...]
    """Array of routes set in this Network."""

    servers: tuple[int, ...]
    """Array of IDs of Servers attached to this Network."""

    load_balancers: tuple[int, ...] | None = None
    """Array of IDs of Load Balancers attached to this Network."""

    protection: Protection
    """Protection configuration for the Resource."""

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    expose_routes_to_vswitch: bool
    """Indicates if the routes from this Network should be exposed to the vSwitch connection."""


class ListNetworksResponse(_Model):
    """``ListNetworksResponse``."""

    networks: tuple[Network, ...]
    meta: ListMeta


class ListServerTypesResponse(_Model):
    """``ListServerTypesResponse``."""

    server_types: tuple[ServerType, ...]
    meta: ListMeta


class ListServersResponse(_Model):
    """``ListServersResponse``."""

    servers: tuple[Server, ...]
    meta: ListMeta


class SshKey(_Model):
    """``SshKey``."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the SSH Key."""

    name: str
    """Name of the Resource. Must be unique per Project."""

    fingerprint: str
    """MD5 fingerprint of the SSH public key."""

    public_key: str
    """Public key."""

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """


class ListSshKeysResponse(_Model):
    """``ListSshKeysResponse``."""

    ssh_keys: tuple[SshKey, ...]
    meta: ListMeta


class ListStorageBoxFoldersResponse(_Model):
    """``ListStorageBoxFoldersResponse``."""

    folders: tuple[str, ...]


class SnapshotStats(_Model):
    """Statistics of the Storage Box Snapshot."""

    size: int
    """Current storage requirements of the Snapshot in bytes."""

    size_filesystem: int
    """Size of the compressed file system contained in the Snapshot in bytes."""


class Snapshot(_Model):
    """``Snapshot``."""

    storage_box: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Storage Box."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Storage Box Snapshot."""

    name: str
    """Name of the Storage Box Snapshot."""

    description: Annotated[
        str, Check(max_length=1000, pattern="[a-zA-Z0-9-_,:<>+#!\\(\\)\\[\\]\\{\\}\x20]*")
    ]
    """Description of the Storage Box Snapshot."""

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    stats: SnapshotStats
    """Statistics of the Storage Box Snapshot."""

    is_automatic: bool
    """Whether the Storage Box Snapshot was created automatically."""

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """


class ListStorageBoxSnapshotsResponse(_Model):
    """``ListStorageBoxSnapshotsResponse``."""

    snapshots: tuple[Snapshot, ...]


class SubaccountAccessSettings(_Model):
    """Access settings for the Subaccount."""

    reachable_externally: bool
    """Whether access from outside the Hetzner network is allowed."""

    samba_enabled: bool
    """Whether the Samba subsystem is enabled."""

    ssh_enabled: bool
    """Whether the SSH subsystem is enabled."""

    webdav_enabled: bool
    """Whether the WebDAV subsystem is enabled."""

    readonly: bool
    """Whether the Subaccount is read-only."""


class Subaccount(_Model):
    """``Subaccount``."""

    storage_box: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Storage Box."""

    id: Annotated[int, Check(minimum=1, maximum=9007199254740991)]
    """ID of the Storage Box Subaccount."""

    name: Annotated[str, Check(min_length=1, max_length=50)]
    """Name of the Storage Box Subaccount."""

    home_directory: Annotated[
        str, Check(min_length=1, max_length=999, pattern="^[a-zA-Z0-9\x20./_-]+$")
    ]
    """Home directory of the Storage Box Subaccount."""

    access_settings: SubaccountAccessSettings
    """Access settings for the Subaccount."""

    description: Annotated[str, Check(max_length=1000)]
    """A description of Storage Box Subaccount."""

    labels: Annotated[Mapping[str, str], LABELS_RULES]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """

    username: str
    """Username of the Storage Box Subaccount."""

    server: str
    """FQDN of the Storage Box Subaccount."""

    created: AwareDatetime
    """Point in time when the Resource was created (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """


class ListStorageBoxSubaccountsResponse(_Model):
    """``ListStorageBoxSubaccountsResponse``."""

    subaccounts: tuple[Subaccount, ...]


class ListStorageBoxTypesResponse(_Model):
    """``ListStorageBoxTypesResponse``."""

    storage_box_types: tuple[StorageBoxType, ...]
    meta: ListMeta


class ListStorageBoxesResponse(_Model):
    """``ListStorageBoxesResponse``."""

    storage_boxes: tuple[StorageBox, ...]
    meta: ListMeta


class ListVolumesResponse(_Model):
    """``ListVolumesResponse``."""

    volumes: tuple[Volume, ...]
    meta: ListMeta


class ListZoneRrsetsResponse(_Model):
    """``ListZoneRrsetsResponse``."""

    rrsets: tuple[RRSet, ...]
    meta: ListMeta100


class ListZonesResponse(_Model):
    """``ListZonesResponse``."""

    zones: tuple[Zone, ...]
    meta: ListMeta


class LoadBalancerResponse(_Model):
    """``LoadBalancerResponse``."""

    load_balancer: LoadBalancer


class MetricsResponseMetricsTimeSeriesValue(_Model):
    """``MetricsResponseMetricsTimeSeriesValue``."""

    values: tuple[tuple[float, str], ...]
    """Metrics timestamps with values."""


class MetricsResponseMetrics(_Model):
    """``MetricsResponseMetrics``."""

    start: AwareDatetime
    """Start of period of metrics reported (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    end: AwareDatetime
    """End of period of metrics reported (in RFC3339
    (https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format).
    """

    step: float
    """Resolution of results in seconds."""

    time_series: Mapping[str, MetricsResponseMetricsTimeSeriesValue]
    """Hash with timeseries information, containing the name of timeseries as key."""


class MetricsResponse(_Model):
    """``MetricsResponse``."""

    metrics: MetricsResponseMetrics


class NetworkResponse(_Model):
    """``NetworkResponse``."""

    network: Network


class PlacementGroupResponse(_Model):
    """``PlacementGroupResponse``."""

    placement_group: PlacementGroup


class PlacementGroupsResponse(_Model):
    """``PlacementGroupsResponse``."""

    placement_groups: tuple[PlacementGroup, ...]
    meta: ListMeta


class PrimaryIPResponse(_Model):
    """``PrimaryIPResponse``."""

    primary_ip: PrimaryIP


class PrimaryIPsResponse(_Model):
    """``PrimaryIPsResponse``."""

    primary_ips: tuple[PrimaryIP, ...]
    meta: ListMeta


class RebuildServerResponse(_Model):
    """``RebuildServerResponse``."""

    root_password: str | None = Field(default=None, repr=False)
    """New root password when not using SSH keys."""

    action: Action


class RequestServerConsoleResponse(_Model):
    """``RequestServerConsoleResponse``."""

    wss_url: str
    """URL of websocket proxy to use; this includes a token which is valid for a limited time
    only.
    """

    password: str = Field(repr=False)
    """VNC password to use for this connection (this password only works in combination with a
    wss_url with valid token).
    """

    action: Action


class RootPasswordResponse(_Model):
    """The `root_password` key in the reply contains the root password that can be used to...

    The `root_password` key in the reply contains the root password that can be used to access the
    booted rescue system.
    """

    root_password: str = Field(repr=False)
    """Password that will be set for this Server once the Action succeeds."""

    action: Action


class RrsetResponse(_Model):
    """``RrsetResponse``."""

    rrset: RRSet


class ServerResponse(_Model):
    """``ServerResponse``."""

    server: Server


class SnapshotResponse(_Model):
    """``SnapshotResponse``."""

    snapshot: Snapshot


class SshKeyResponse(_Model):
    """``SshKeyResponse``."""

    ssh_key: SshKey


class StorageBoxResponse(_Model):
    """``StorageBoxResponse``."""

    storage_box: StorageBox


class SubaccountResponse(_Model):
    """``SubaccountResponse``."""

    subaccount: Subaccount


class VolumeResponse(_Model):
    """``VolumeResponse``."""

    volume: Volume


class ZoneResponse(_Model):
    """``ZoneResponse``."""

    zone: Zone


class Zonefile(_Model):
    """``Zonefile``."""

    zonefile: str
    """Generated zone file.

    Example:

    ```dns
    $ORIGIN example.com.
    $TTL    3600

    @   IN  SOA hydrogen.ns.hetzner.com. dns.hetzner.com. 2024010100 86400 10800 3600000 3600

    @   IN  10800   NS  hydrogen.ns.hetzner.com. ; Some comment.
    @   IN  10800   NS  oxygen.ns.hetzner.com.
    @   IN  10800   NS  helium.ns.hetzner.de.
    ```
    """
