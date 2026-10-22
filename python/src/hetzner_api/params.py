"""Request types of the Hetzner API (generated - do not edit by hand).

Nested objects in requests are ``TypedDict``s: just pass a ``dict``, type checkers
verify keys and values. Optional keys that are left out are not sent.
"""

from collections.abc import Mapping, Sequence
from typing import Literal, NotRequired, TypedDict

from hetzner_api._types import StrSequence, UnknownValue
from hetzner_api.models import (
    FirewallResourceType,
    FirewallRuleDirection,
    FirewallRuleProtocol,
    HealthCheckProtocol,
    LoadBalancerAlgorithmType,
    LoadBalancerTargetType,
    RRSetType,
    SubnetType,
    ZonePrimaryNameserverTsigAlgorithm,
)

__all__ = [
    "CreateLoadBalancerRequestServiceParam",
    "CreateLoadBalancerRequestTargetParam",
    "CreateServerRequestFirewallParam",
    "CreateServerRequestPublicNetParam",
    "CreateStorageBoxAccessSettingsParam",
    "CreateStorageBoxSubaccountAccessSettingsParam",
    "FirewallResourceParam",
    "FirewallResourceServerParam",
    "HealthCheckHttpParam",
    "LabelSelectorParam",
    "LoadBalancerAlgorithmParam",
    "LoadBalancerCreatePublicNetParam",
    "LoadBalancerServiceHTTPConfigParam",
    "LoadBalancerServiceHTTPParam",
    "LoadBalancerServiceHTTPSConfigParam",
    "LoadBalancerServiceHealthCheck2Param",
    "LoadBalancerServiceHealthCheckHttpParam",
    "LoadBalancerServiceHealthCheckParam",
    "LoadBalancerTargetIPParam",
    "LoadBalancerTargetLabelSelectorParam",
    "LoadBalancerTargetServerRequestParam",
    "NetworkCreateRequestSubnetParam",
    "RRSetRequestParam",
    "RecordParam",
    "RouteParam",
    "RuleParam",
    "ServiceHTTPProtocolParam",
    "ServiceHTTPSProtocolParam",
    "ServiceTCPParam",
    "UpdateLoadBalancerServiceHealthCheckParam",
    "UpdateLoadBalancerServiceHttpParam",
    "UpdateZoneRrsetRecordsRecordParam",
    "ZonePrimaryNameserverParam",
]


class LoadBalancerServiceHealthCheckHttpParam(TypedDict):
    """Additional configuration for protocol http."""

    domain: str | None
    """Host header to send in the HTTP request. May not contain spaces, percent or backslash
    symbols. Can be null, in that case no host header is sent.
    """

    path: str
    """HTTP path to use for health checks. May not contain literal spaces, use percent-encoding
    instead.
    """

    response: NotRequired[str]
    """String that must be contained in HTTP response in order to pass the health check."""

    status_codes: NotRequired[StrSequence]
    """List of returned HTTP status codes in order to pass the health check. Supports the
    wildcards `?` for exactly one character and `*` for multiple ones.

    The API default is ``["2??", "3??"]``.
    """

    tls: NotRequired[bool]
    """Use HTTPS for health check."""


class LoadBalancerServiceHealthCheckParam(TypedDict):
    """Service health check."""

    protocol: HealthCheckProtocol | UnknownValue
    """Type of the health check."""

    port: int
    """Port the health check will be performed on."""

    interval: int
    """Time interval in seconds health checks are performed."""

    timeout: int
    """Time in seconds after an attempt is considered a timeout."""

    retries: int
    """Unsuccessful retries needed until a target is considered unhealthy; an unhealthy target
    needs the same number of successful retries to become healthy again.
    """

    http: NotRequired[LoadBalancerServiceHealthCheckHttpParam]
    """Additional configuration for protocol http."""


class ServiceTCPParam(TypedDict):
    """``ServiceTCP``."""

    protocol: Literal["tcp"]

    listen_port: int
    """Port the Load Balancer listens on."""

    destination_port: int
    """Port the Load Balancer will balance to."""

    proxyprotocol: bool
    """Is Proxyprotocol enabled or not."""

    health_check: LoadBalancerServiceHealthCheckParam
    """Service health check."""


class LoadBalancerServiceHTTPConfigParam(TypedDict):
    """Configuration option for protocol http."""

    cookie_name: str
    """Name of the cookie used for sticky sessions."""

    cookie_lifetime: int
    """Lifetime of the cookie used for sticky sessions (in seconds)."""

    timeout_idle: int
    """Idle timeout in seconds for the client and server side."""

    sticky_sessions: bool
    """Use sticky sessions."""


class ServiceHTTPProtocolParam(TypedDict):
    """``ServiceHTTPProtocol``."""

    protocol: Literal["http"]

    listen_port: int
    """Port the Load Balancer listens on."""

    destination_port: int
    """Port the Load Balancer will balance to."""

    proxyprotocol: bool
    """Is Proxyprotocol enabled or not."""

    health_check: LoadBalancerServiceHealthCheckParam
    """Service health check."""

    http: LoadBalancerServiceHTTPConfigParam
    """Configuration option for protocol http."""


class LoadBalancerServiceHTTPSConfigParam(TypedDict):
    """Configuration option for protocol https."""

    cookie_name: str
    """Name of the cookie used for sticky sessions."""

    cookie_lifetime: int
    """Lifetime of the cookie used for sticky sessions (in seconds)."""

    timeout_idle: int
    """Idle timeout in seconds for the client and server side."""

    certificates: Sequence[int]
    """IDs of the Certificates to use for TLS/SSL termination by the Load Balancer; empty for
    TLS/SSL passthrough.
    """

    redirect_http: bool
    """Redirect HTTP requests to HTTPS."""

    sticky_sessions: bool
    """Use sticky sessions."""


class ServiceHTTPSProtocolParam(TypedDict):
    """``ServiceHTTPSProtocol``."""

    protocol: Literal["https"]

    listen_port: int
    """Port the Load Balancer listens on."""

    destination_port: int
    """Port the Load Balancer will balance to."""

    proxyprotocol: bool
    """Is Proxyprotocol enabled or not."""

    health_check: LoadBalancerServiceHealthCheckParam
    """Service health check."""

    http: LoadBalancerServiceHTTPSConfigParam
    """Configuration option for protocol https."""


type CreateLoadBalancerRequestServiceParam = (
    ServiceTCPParam | ServiceHTTPProtocolParam | ServiceHTTPSProtocolParam
)


class LoadBalancerTargetServerRequestParam(TypedDict):
    """Configuration for type Server, only valid and required if type is `server`."""

    id: int
    """ID of the Server."""

    ip: NotRequired[str]
    """Optional public IP of the Server to use as target. Must be the Primary IPv4 of the Server,
    or an IPv6 host address within IPv6 /64 subnet of the Server. If omitted, the Primary IPv4
    of the Server is used. Must not be a private IP and is only valid for public targets.
    """


class LoadBalancerTargetLabelSelectorParam(TypedDict):
    """Configuration for label selector targets, only valid and required if type is...

    Configuration for label selector targets, only valid and required if type is `label_selector`.
    """

    selector: str
    """Label selector."""


class LoadBalancerTargetIPParam(TypedDict):
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


class CreateLoadBalancerRequestTargetParam(TypedDict):
    """Configuration of a Load Balancer target."""

    type: LoadBalancerTargetType | UnknownValue
    """Type of the resource."""

    server: NotRequired[LoadBalancerTargetServerRequestParam]
    """Configuration for type Server, only valid and required if type is `server`."""

    label_selector: NotRequired[LoadBalancerTargetLabelSelectorParam]
    """Configuration for label selector targets, only valid and required if type is
    `label_selector`.
    """

    ip: NotRequired[LoadBalancerTargetIPParam]
    """Configuration for an IP target. It is only possible to use the (Public or vSwitch) IPs of
    Hetzner Online Root Servers belonging to the project owner. IPs belonging to other users
    are blocked. Additionally IPs belonging to services provided by Hetzner Cloud (Servers,
    Load Balancers, ...) are blocked as well. Only valid and required if type is `ip`.
    """

    use_private_ip: NotRequired[bool]
    """Use the private network IP instead of the public IP of the Server, requires the Server and
    Load Balancer to be in the same network. Only valid for target types `server` and
    `label_selector`.

    The API default is ``False``.
    """


class CreateServerRequestFirewallParam(TypedDict):
    """``CreateServerRequestFirewall``."""

    firewall: int
    """ID of the Firewall."""


class CreateServerRequestPublicNetParam(TypedDict):
    """Public Network options."""

    enable_ipv4: NotRequired[bool]
    """Attach an IPv4 on the public NIC. If false, no IPv4 address will be attached.

    The API default is ``True``.
    """

    enable_ipv6: NotRequired[bool]
    """Attach an IPv6 on the public NIC. If false, no IPv6 address will be attached.

    The API default is ``True``.
    """

    ipv4: NotRequired[int | None]
    """ID of the ipv4 Primary IP to use. If omitted and enable_ipv4 is true, a new ipv4 Primary
    IP will automatically be created.
    """

    ipv6: NotRequired[int | None]
    """ID of the ipv6 Primary IP to use. If omitted and enable_ipv6 is true, a new ipv6 Primary
    IP will automatically be created.
    """


class CreateStorageBoxAccessSettingsParam(TypedDict):
    """Access settings of the Storage Box."""

    reachable_externally: NotRequired[bool]
    """Whether access from outside the Hetzner network is allowed."""

    samba_enabled: NotRequired[bool]
    """Whether the Samba subsystem is enabled."""

    ssh_enabled: NotRequired[bool]
    """Whether the SSH subsystem is enabled."""

    webdav_enabled: NotRequired[bool]
    """Whether the WebDAV subsystem is enabled."""

    zfs_enabled: NotRequired[bool]
    """Whether the ZFS snapshot folder is visible."""


class CreateStorageBoxSubaccountAccessSettingsParam(TypedDict):
    """``CreateStorageBoxSubaccountAccessSettings``."""

    reachable_externally: NotRequired[bool]
    """Whether access from outside the Hetzner network is allowed."""

    samba_enabled: NotRequired[bool]
    """Whether the Samba subsystem is enabled."""

    ssh_enabled: NotRequired[bool]
    """Whether the SSH subsystem is enabled."""

    webdav_enabled: NotRequired[bool]
    """Whether the WebDAV subsystem is enabled."""

    readonly: NotRequired[bool]
    """Whether the Subaccount is read-only."""


class FirewallResourceServerParam(TypedDict):
    """Server the Firewall is applied to.

    Only set for `type` `server`, otherwise `null`.
    """

    id: int
    """ID of the Server."""


class LabelSelectorParam(TypedDict):
    """Label Selector the Firewall is applied to.

    Only set for `type` `label_selector`, otherwise `null`.
    """

    selector: str
    """The selector."""


class FirewallResourceParam(TypedDict):
    """``FirewallResource``."""

    type: FirewallResourceType | UnknownValue
    """Type of the resource."""

    server: NotRequired[FirewallResourceServerParam]
    """Server the Firewall is applied to.

    Only set for `type` `server`, otherwise `null`.
    """

    label_selector: NotRequired[LabelSelectorParam]
    """Label Selector the Firewall is applied to.

    Only set for `type` `label_selector`, otherwise `null`.
    """


class HealthCheckHttpParam(TypedDict):
    """Additional configuration for protocol http."""

    domain: NotRequired[str | None]
    """Host header to send in the HTTP request. May not contain spaces, percent or backslash
    symbols. Can be null, in that case no host header is sent.
    """

    path: NotRequired[str]
    """HTTP path to use for health checks. May not contain literal spaces, use percent-encoding
    instead.
    """

    response: NotRequired[str]
    """String that must be contained in HTTP response in order to pass the health check."""

    status_codes: NotRequired[StrSequence]
    """List of returned HTTP status codes in order to pass the health check. Supports the
    wildcards `?` for exactly one character and `*` for multiple ones.

    The API default is ``["2??", "3??"]``.
    """

    tls: NotRequired[bool]
    """Use HTTPS for health check."""


class LoadBalancerAlgorithmParam(TypedDict):
    """Algorithm of the Load Balancer."""

    type: LoadBalancerAlgorithmType | UnknownValue
    """Type of the algorithm."""


class LoadBalancerCreatePublicNetParam(TypedDict):
    """Public network options of the Load Balancer.

    Only allowed if the public interface is enabled.
    """

    ipv4: NotRequired[int | None]
    """ID of an existing Primary IP of type `ipv4` to assign to the Load Balancer.

    The Primary IP must be unassigned, must not be blocked and must be bound to the same
    Location as the Load Balancer.

    Omit or set to `null` to get a system managed IP address instead. System managed IP
    addresses are not Primary IPs and are created and deleted together with the Load Balancer.
    """

    ipv6: NotRequired[int | None]
    """ID of an existing Primary IP of type `ipv6` to assign to the Load Balancer.

    The Primary IP must be unassigned, must not be blocked and must be bound to the same
    Location as the Load Balancer.

    Omit or set to `null` to get a system managed IP address instead. System managed IP
    addresses are not Primary IPs and are created and deleted together with the Load Balancer.
    """


class LoadBalancerServiceHTTPParam(TypedDict):
    """Configuration option for protocols http and https."""

    cookie_name: NotRequired[str]
    """Name of the cookie used for sticky sessions.

    The API default is ``"HCLBSTICKY"``.
    """

    cookie_lifetime: NotRequired[int]
    """Lifetime of the cookie used for sticky sessions (in seconds).

    The API default is ``300``.
    """

    timeout_idle: NotRequired[int]
    """Idle timeout in seconds for the client and server side."""

    certificates: NotRequired[Sequence[int]]
    """IDs of the Certificates to use for TLS/SSL termination by the Load Balancer; empty for
    TLS/SSL passthrough or if `protocol` is `http`.
    """

    redirect_http: NotRequired[bool]
    """Redirect HTTP requests to HTTPS. Only available if `protocol` is `https`.

    The API default is ``False``.
    """

    sticky_sessions: NotRequired[bool]
    """Use sticky sessions. Only available if `protocol` is `http` or `https`.

    The API default is ``False``.
    """


class LoadBalancerServiceHealthCheck2Param(TypedDict):
    """Service health check."""

    protocol: HealthCheckProtocol | UnknownValue
    """Type of the health check."""

    port: int
    """Port the health check will be performed on."""

    interval: int
    """Time interval in seconds health checks are performed."""

    timeout: int
    """Time in seconds after an attempt is considered a timeout."""

    retries: int
    """Unsuccessful retries needed until a target is considered unhealthy; an unhealthy target
    needs the same number of successful retries to become healthy again.
    """

    http: NotRequired[HealthCheckHttpParam]
    """Additional configuration for protocol http."""


class NetworkCreateRequestSubnetParam(TypedDict):
    """``NetworkCreateRequestSubnet``."""

    type: SubnetType | UnknownValue
    """Type of subnet."""

    ip_range: NotRequired[str]
    """IP range of the subnet.

    Uses CIDR notation.

    Must be a subnet of the parent Networks `ip_range`.

    Must not overlap with any other subnets or with any destinations in routes.

    Minimum network size is /30. We highly recommend that you pick a larger subnet with a /24
    netmask.
    """

    network_zone: str
    """Name of the Network Zone.

    The Location contains the `network_zone` property it belongs to.
    """

    vswitch_id: NotRequired[int]
    """ID of the robot vSwitch.

    Must only be supplied for subnets of type `vswitch`.
    """


class RecordParam(TypedDict):
    """Record of a RRSet.

    The `value` is used to identify the record in an RRSet.
    """

    value: str
    """Value of the record.

    For details about accepted values, see the DNS record types documentation
    (https://docs.hetzner.com/networking/dns/record-types/overview/).
    """

    comment: NotRequired[str]
    """Comment of the record."""


class RRSetRequestParam(TypedDict):
    """``RRSetRequest``."""

    name: str
    """Name of the RRSet.

    The name must be in lower case, and must not end with a dot or the Zone name. Names
    containing non-ASCII characters must be transcribed to Punycode
    (https://wikipedia.org/wiki/Punycode) representation with ACE prefix, e.g. `xn--4bi` (️).

    For the Zone apex, use `@`.
    """

    type: RRSetType | UnknownValue
    """Type of the RRSet."""

    ttl: NotRequired[int | None]
    """Time To Live (TTL) of the RRSet.

    Must be in between 60s and 2147483647s.

    If not set, the Zone's Default TTL is used.
    """

    records: Sequence[RecordParam]
    """Records of the RRSet.

    Must not be empty and must only contain distinct record values. The order of records
    returned in responses is not guaranteed to be consistent.
    """

    labels: NotRequired[Mapping[str, str]]
    """User-defined labels (`key/value` pairs) for the Resource. For more information, see
    "Labels".
    """


class RouteParam(TypedDict):
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


class RuleParam(TypedDict):
    """``Rule``."""

    description: NotRequired[str | None]
    """Description of the rule."""

    direction: FirewallRuleDirection | UnknownValue
    """Traffic direction in which the rule should be applied to.

    Use `source_ips` for direction `in` and `destination_ips` for direction `out` to specify
    IPs.
    """

    source_ips: NotRequired[StrSequence]
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

    destination_ips: NotRequired[StrSequence]
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

    port: NotRequired[str]
    """Port or port range to apply the rule for.

    Only applicable for protocols `tcp` and `udp`.

    A port range can be specified by separating lower and upper bounds with a dash.
    `1024-5000` will include all ports starting from 1024 up to port 5000.
    """


class UpdateLoadBalancerServiceHealthCheckParam(TypedDict):
    """Service health check."""

    protocol: NotRequired[HealthCheckProtocol | UnknownValue]
    """Type of the health check."""

    port: NotRequired[int]
    """Port the health check will be performed on."""

    interval: NotRequired[int]
    """Time interval in seconds health checks are performed."""

    timeout: NotRequired[int]
    """Time in seconds after an attempt is considered a timeout."""

    retries: NotRequired[int]
    """Unsuccessful retries needed until a target is considered unhealthy; an unhealthy target
    needs the same number of successful retries to become healthy again.
    """

    http: NotRequired[HealthCheckHttpParam]
    """Additional configuration for protocol http."""


class UpdateLoadBalancerServiceHttpParam(TypedDict):
    """Configuration option for protocols http and https."""

    cookie_name: NotRequired[str]
    """Name of the cookie used for sticky sessions."""

    cookie_lifetime: NotRequired[int]
    """Lifetime of the cookie used for sticky sessions (in seconds)."""

    timeout_idle: NotRequired[int]
    """Idle timeout in seconds for the client and server side."""

    certificates: NotRequired[Sequence[int]]
    """IDs of the Certificates to use for TLS/SSL termination by the Load Balancer; empty for
    TLS/SSL passthrough or if `protocol` is `http`.
    """

    redirect_http: NotRequired[bool]
    """Redirect HTTP requests to HTTPS. Only available if `protocol` is `https`.

    The API default is ``False``.
    """

    sticky_sessions: NotRequired[bool]
    """Use sticky sessions. Only available if `protocol` is `http` or `https`.

    The API default is ``False``.
    """


class UpdateZoneRrsetRecordsRecordParam(TypedDict):
    """Record of a RRSet.

    The `value` is used to identify the record in an RRSet.
    """

    value: str
    """Value of the record to update."""

    comment: str
    """New comment for the record."""


class ZonePrimaryNameserverParam(TypedDict):
    """Primary nameserver that returns Zones via `AXFR`.

    Must allow queries from and may send `NOTIFY` queries to Hetzner's secondary nameservers
    (https://docs.hetzner.com/dns-console/dns/general/authoritative-name-servers#secondary-dns-servers-old-name-servers-for-robot-customers).
    """

    address: str
    """Public IPv4 or IPv6 address of the primary nameserver.

    Must be unique across all primary nameservers of this zone.
    """

    port: NotRequired[int]
    """Port of the primary nameserver.

    The API default is ``53``.
    """

    tsig_key: NotRequired[str]
    """Transaction signature (TSIG) (https://en.wikipedia.org/wiki/TSIG) key to use for the zone
    transfer. Must be base64 encoded.
    """

    tsig_algorithm: NotRequired[ZonePrimaryNameserverTsigAlgorithm | UnknownValue]
    """Transaction signature (TSIG) (https://en.wikipedia.org/wiki/TSIG) algorithm used to
    generate the TSIG key.
    """
