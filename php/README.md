# Hetzner API

## API Information

- **Title:** Hetzner API
- **Version:** 1.0.0
- **Source Spec SHA-256:** 1e7eccc0dd638bfa6ba2cde9fecda8b083c45b32829b74b31a4620f03e7794fa

## API description

Quoted in part from the API description, without its formatting. The text is its author's and is
not covered by this package's licence — see [License](#license).

> Overview
>
> This is the official documentation for the Hetzner Cloud API.
>
> Introduction
>
> The Hetzner Cloud API operates over HTTPS and uses JSON as its data format. The API
> is a RESTful API and utilizes HTTP methods and HTTP status codes to specify requests
> and responses.
>
> As an alternative to working directly with our API you may also consider to use:
>
> \- Our CLI program hcloud\
> \- Our library for Go\
> \- Our library for Python
>
> You can find even more libraries, tools and integrations on our Awesome List on
> GitHub.
>
> Getting Started
>
> \[…\]

## Installation

```bash
composer require prefabcortex/hetzner
```

### HTTP client

This package talks to the API over PSR-18 and does not ship an HTTP client of its
own, so it never forces a second one on a project that already has one. If yours has
none yet, the command above stops before installing anything and lists the packages
that qualify — pick one:

```bash
composer require guzzlehttp/guzzle
```

`symfony/http-client` works just as well, and either is picked up automatically. To
use a client you configured yourself, hand it to `ClientConfig::withHttpClient()`
before building the client.

A client picked up automatically gets a timeout — ten seconds to connect, sixty for the
whole request — which `ClientConfig::withTimeout(Timeout::seconds(…))` changes. A client
you hand over keeps the timeouts you gave it.

## Choosing a server

`ClientConfig::forServer()` takes the server the API description names.

| Server | URL |
|---|---|
| `Server::ApiHetznerCloud` | `https://api.hetzner.cloud/v1` |

```php
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Server;

$config = ClientConfig::forServer(Server::ApiHetznerCloud);
```

### Operations with servers of their own

The description sends these operations elsewhere:

- `ListStorageBoxes`, `CreateStorageBox` and 30 more operations: always `https://api.hetzner.com/v1`, the one server the description names for them.

For a mock server or a proxy, `ClientConfig::forBaseUrl('https://mock.example.com')` sends
every request to one address.

## Quickstart

Every link below points at a file under `examples/` to read and copy from.

### Authentication

- **APIToken** (HTTP Bearer token): `Client::withAPIToken($token, $config)` — see [`examples/Auth/APIToken.php`](examples/Auth/APIToken.php)

For a scheme this package generates no authenticator for, or a signature the description cannot express, implement `Authentication\Authenticator` and pass it to `Client::withAuthenticators($config, ...$authenticators)`.

### Operations

#### Actions

- [`getAction`](examples/Operations/Actions/GetActionExample.php)
- [`getActions`](examples/Operations/Actions/GetActionsExample.php)

#### CertificateActions

- [`getCertificateAction`](examples/Operations/CertificateActions/GetCertificateActionExample.php)
- [`getCertificatesAction`](examples/Operations/CertificateActions/GetCertificatesActionExample.php)
- [`listCertificateActions`](examples/Operations/CertificateActions/ListCertificateActionsExample.php)
- [`listCertificatesActions`](examples/Operations/CertificateActions/ListCertificatesActionsExample.php)
- [`retryCertificate`](examples/Operations/CertificateActions/RetryCertificateExample.php)

#### Certificates

- [`createCertificate`](examples/Operations/Certificates/CreateCertificateExample.php)
- [`deleteCertificate`](examples/Operations/Certificates/DeleteCertificateExample.php)
- [`getCertificate`](examples/Operations/Certificates/GetCertificateExample.php)
- [`listCertificates`](examples/Operations/Certificates/ListCertificatesExample.php)
- [`updateCertificate`](examples/Operations/Certificates/UpdateCertificateExample.php)

#### DataCenters

- [`getDatacenter`](examples/Operations/DataCenters/GetDatacenterExample.php)
- [`listDatacenters`](examples/Operations/DataCenters/ListDatacentersExample.php)

#### FirewallActions

- [`applyFirewallToResources`](examples/Operations/FirewallActions/ApplyFirewallToResourcesExample.php)
- [`getFirewallAction`](examples/Operations/FirewallActions/GetFirewallActionExample.php)
- [`getFirewallsAction`](examples/Operations/FirewallActions/GetFirewallsActionExample.php)
- [`listFirewallActions`](examples/Operations/FirewallActions/ListFirewallActionsExample.php)
- [`listFirewallsActions`](examples/Operations/FirewallActions/ListFirewallsActionsExample.php)
- [`removeFirewallFromResources`](examples/Operations/FirewallActions/RemoveFirewallFromResourcesExample.php)
- [`setFirewallRules`](examples/Operations/FirewallActions/SetFirewallRulesExample.php)

#### Firewalls

- [`createFirewall`](examples/Operations/Firewalls/CreateFirewallExample.php)
- [`deleteFirewall`](examples/Operations/Firewalls/DeleteFirewallExample.php)
- [`getFirewall`](examples/Operations/Firewalls/GetFirewallExample.php)
- [`listFirewalls`](examples/Operations/Firewalls/ListFirewallsExample.php)
- [`updateFirewall`](examples/Operations/Firewalls/UpdateFirewallExample.php)

#### FloatingIpActions

- [`assignFloatingIp`](examples/Operations/FloatingIpActions/AssignFloatingIpExample.php)
- [`changeFloatingIpDnsPtr`](examples/Operations/FloatingIpActions/ChangeFloatingIpDnsPtrExample.php)
- [`changeFloatingIpProtection`](examples/Operations/FloatingIpActions/ChangeFloatingIpProtectionExample.php)
- [`getFloatingIpAction`](examples/Operations/FloatingIpActions/GetFloatingIpActionExample.php)
- [`getFloatingIpsAction`](examples/Operations/FloatingIpActions/GetFloatingIpsActionExample.php)
- [`listFloatingIpActions`](examples/Operations/FloatingIpActions/ListFloatingIpActionsExample.php)
- [`listFloatingIpsActions`](examples/Operations/FloatingIpActions/ListFloatingIpsActionsExample.php)
- [`unassignFloatingIp`](examples/Operations/FloatingIpActions/UnassignFloatingIpExample.php)

#### FloatingIps

- [`createFloatingIp`](examples/Operations/FloatingIps/CreateFloatingIpExample.php)
- [`deleteFloatingIp`](examples/Operations/FloatingIps/DeleteFloatingIpExample.php)
- [`getFloatingIp`](examples/Operations/FloatingIps/GetFloatingIpExample.php)
- [`listFloatingIps`](examples/Operations/FloatingIps/ListFloatingIpsExample.php)
- [`updateFloatingIp`](examples/Operations/FloatingIps/UpdateFloatingIpExample.php)

#### ImageActions

- [`changeImageProtection`](examples/Operations/ImageActions/ChangeImageProtectionExample.php)
- [`getImageAction`](examples/Operations/ImageActions/GetImageActionExample.php)
- [`getImagesAction`](examples/Operations/ImageActions/GetImagesActionExample.php)
- [`listImageActions`](examples/Operations/ImageActions/ListImageActionsExample.php)
- [`listImagesActions`](examples/Operations/ImageActions/ListImagesActionsExample.php)

#### Images

- [`deleteImage`](examples/Operations/Images/DeleteImageExample.php)
- [`getImage`](examples/Operations/Images/GetImageExample.php)
- [`listImages`](examples/Operations/Images/ListImagesExample.php)
- [`updateImage`](examples/Operations/Images/UpdateImageExample.php)

#### Isos

- [`getIso`](examples/Operations/Isos/GetIsoExample.php)
- [`listIsos`](examples/Operations/Isos/ListIsosExample.php)

#### LoadBalancerActions

- [`addLoadBalancerService`](examples/Operations/LoadBalancerActions/AddLoadBalancerServiceExample.php)
- [`addLoadBalancerTarget`](examples/Operations/LoadBalancerActions/AddLoadBalancerTargetExample.php)
- [`attachLoadBalancerToNetwork`](examples/Operations/LoadBalancerActions/AttachLoadBalancerToNetworkExample.php)
- [`changeLoadBalancerAlgorithm`](examples/Operations/LoadBalancerActions/ChangeLoadBalancerAlgorithmExample.php)
- [`changeLoadBalancerDnsPtr`](examples/Operations/LoadBalancerActions/ChangeLoadBalancerDnsPtrExample.php)
- [`changeLoadBalancerProtection`](examples/Operations/LoadBalancerActions/ChangeLoadBalancerProtectionExample.php)
- [`changeLoadBalancerType`](examples/Operations/LoadBalancerActions/ChangeLoadBalancerTypeExample.php)
- [`deleteLoadBalancerService`](examples/Operations/LoadBalancerActions/DeleteLoadBalancerServiceExample.php)
- [`detachLoadBalancerFromNetwork`](examples/Operations/LoadBalancerActions/DetachLoadBalancerFromNetworkExample.php)
- [`disableLoadBalancerPublicInterface`](examples/Operations/LoadBalancerActions/DisableLoadBalancerPublicInterfaceExample.php)
- [`enableLoadBalancerPublicInterface`](examples/Operations/LoadBalancerActions/EnableLoadBalancerPublicInterfaceExample.php)
- [`getLoadBalancerAction`](examples/Operations/LoadBalancerActions/GetLoadBalancerActionExample.php)
- [`getLoadBalancersAction`](examples/Operations/LoadBalancerActions/GetLoadBalancersActionExample.php)
- [`listLoadBalancerActions`](examples/Operations/LoadBalancerActions/ListLoadBalancerActionsExample.php)
- [`listLoadBalancersActions`](examples/Operations/LoadBalancerActions/ListLoadBalancersActionsExample.php)
- [`removeLoadBalancerTarget`](examples/Operations/LoadBalancerActions/RemoveLoadBalancerTargetExample.php)
- [`updateLoadBalancerService`](examples/Operations/LoadBalancerActions/UpdateLoadBalancerServiceExample.php)

#### LoadBalancerTypes

- [`getLoadBalancerType`](examples/Operations/LoadBalancerTypes/GetLoadBalancerTypeExample.php)
- [`listLoadBalancerTypes`](examples/Operations/LoadBalancerTypes/ListLoadBalancerTypesExample.php)

#### LoadBalancers

- [`createLoadBalancer`](examples/Operations/LoadBalancers/CreateLoadBalancerExample.php)
- [`deleteLoadBalancer`](examples/Operations/LoadBalancers/DeleteLoadBalancerExample.php)
- [`getLoadBalancer`](examples/Operations/LoadBalancers/GetLoadBalancerExample.php)
- [`getLoadBalancerMetrics`](examples/Operations/LoadBalancers/GetLoadBalancerMetricsExample.php)
- [`listLoadBalancers`](examples/Operations/LoadBalancers/ListLoadBalancersExample.php)
- [`updateLoadBalancer`](examples/Operations/LoadBalancers/UpdateLoadBalancerExample.php)

#### Locations

- [`getLocation`](examples/Operations/Locations/GetLocationExample.php)
- [`listLocations`](examples/Operations/Locations/ListLocationsExample.php)

#### NetworkActions

- [`addNetworkRoute`](examples/Operations/NetworkActions/AddNetworkRouteExample.php)
- [`addNetworkSubnet`](examples/Operations/NetworkActions/AddNetworkSubnetExample.php)
- [`changeNetworkIpRange`](examples/Operations/NetworkActions/ChangeNetworkIpRangeExample.php)
- [`changeNetworkProtection`](examples/Operations/NetworkActions/ChangeNetworkProtectionExample.php)
- [`deleteNetworkRoute`](examples/Operations/NetworkActions/DeleteNetworkRouteExample.php)
- [`deleteNetworkSubnet`](examples/Operations/NetworkActions/DeleteNetworkSubnetExample.php)
- [`getNetworkAction`](examples/Operations/NetworkActions/GetNetworkActionExample.php)
- [`getNetworksAction`](examples/Operations/NetworkActions/GetNetworksActionExample.php)
- [`listNetworkActions`](examples/Operations/NetworkActions/ListNetworkActionsExample.php)
- [`listNetworksActions`](examples/Operations/NetworkActions/ListNetworksActionsExample.php)

#### Networks

- [`createNetwork`](examples/Operations/Networks/CreateNetworkExample.php)
- [`deleteNetwork`](examples/Operations/Networks/DeleteNetworkExample.php)
- [`getNetwork`](examples/Operations/Networks/GetNetworkExample.php)
- [`listNetworkMembers`](examples/Operations/Networks/ListNetworkMembersExample.php)
- [`listNetworks`](examples/Operations/Networks/ListNetworksExample.php)
- [`updateNetwork`](examples/Operations/Networks/UpdateNetworkExample.php)

#### PlacementGroups

- [`createPlacementGroup`](examples/Operations/PlacementGroups/CreatePlacementGroupExample.php)
- [`deletePlacementGroup`](examples/Operations/PlacementGroups/DeletePlacementGroupExample.php)
- [`getPlacementGroup`](examples/Operations/PlacementGroups/GetPlacementGroupExample.php)
- [`listPlacementGroups`](examples/Operations/PlacementGroups/ListPlacementGroupsExample.php)
- [`updatePlacementGroup`](examples/Operations/PlacementGroups/UpdatePlacementGroupExample.php)

#### Pricing

- [`getPricing`](examples/Operations/Pricing/GetPricingExample.php)

#### PrimaryIpActions

- [`assignPrimaryIp`](examples/Operations/PrimaryIpActions/AssignPrimaryIpExample.php)
- [`changePrimaryIpDnsPtr`](examples/Operations/PrimaryIpActions/ChangePrimaryIpDnsPtrExample.php)
- [`changePrimaryIpProtection`](examples/Operations/PrimaryIpActions/ChangePrimaryIpProtectionExample.php)
- [`getPrimaryIpAction`](examples/Operations/PrimaryIpActions/GetPrimaryIpActionExample.php)
- [`getPrimaryIpsAction`](examples/Operations/PrimaryIpActions/GetPrimaryIpsActionExample.php)
- [`listPrimaryIpActions`](examples/Operations/PrimaryIpActions/ListPrimaryIpActionsExample.php)
- [`listPrimaryIpsActions`](examples/Operations/PrimaryIpActions/ListPrimaryIpsActionsExample.php)
- [`unassignPrimaryIp`](examples/Operations/PrimaryIpActions/UnassignPrimaryIpExample.php)

#### PrimaryIps

- [`createPrimaryIp`](examples/Operations/PrimaryIps/CreatePrimaryIpExample.php)
- [`deletePrimaryIp`](examples/Operations/PrimaryIps/DeletePrimaryIpExample.php)
- [`getPrimaryIp`](examples/Operations/PrimaryIps/GetPrimaryIpExample.php)
- [`listPrimaryIps`](examples/Operations/PrimaryIps/ListPrimaryIpsExample.php)
- [`updatePrimaryIp`](examples/Operations/PrimaryIps/UpdatePrimaryIpExample.php)

#### ServerActions

- [`addServerToPlacementGroup`](examples/Operations/ServerActions/AddServerToPlacementGroupExample.php)
- [`attachServerIso`](examples/Operations/ServerActions/AttachServerIsoExample.php)
- [`attachServerToNetwork`](examples/Operations/ServerActions/AttachServerToNetworkExample.php)
- [`changeServerAliasIps`](examples/Operations/ServerActions/ChangeServerAliasIpsExample.php)
- [`changeServerDnsPtr`](examples/Operations/ServerActions/ChangeServerDnsPtrExample.php)
- [`changeServerProtection`](examples/Operations/ServerActions/ChangeServerProtectionExample.php)
- [`changeServerType`](examples/Operations/ServerActions/ChangeServerTypeExample.php)
- [`createServerImage`](examples/Operations/ServerActions/CreateServerImageExample.php)
- [`detachServerFromNetwork`](examples/Operations/ServerActions/DetachServerFromNetworkExample.php)
- [`detachServerIso`](examples/Operations/ServerActions/DetachServerIsoExample.php)
- [`disableServerBackup`](examples/Operations/ServerActions/DisableServerBackupExample.php)
- [`disableServerRescue`](examples/Operations/ServerActions/DisableServerRescueExample.php)
- [`enableServerBackup`](examples/Operations/ServerActions/EnableServerBackupExample.php)
- [`enableServerRescue`](examples/Operations/ServerActions/EnableServerRescueExample.php)
- [`getServerAction`](examples/Operations/ServerActions/GetServerActionExample.php)
- [`getServersAction`](examples/Operations/ServerActions/GetServersActionExample.php)
- [`listServerActions`](examples/Operations/ServerActions/ListServerActionsExample.php)
- [`listServersActions`](examples/Operations/ServerActions/ListServersActionsExample.php)
- [`poweroffServer`](examples/Operations/ServerActions/PoweroffServerExample.php)
- [`poweronServer`](examples/Operations/ServerActions/PoweronServerExample.php)
- [`rebootServer`](examples/Operations/ServerActions/RebootServerExample.php)
- [`rebuildServer`](examples/Operations/ServerActions/RebuildServerExample.php)
- [`removeServerFromPlacementGroup`](examples/Operations/ServerActions/RemoveServerFromPlacementGroupExample.php)
- [`requestServerConsole`](examples/Operations/ServerActions/RequestServerConsoleExample.php)
- [`resetServer`](examples/Operations/ServerActions/ResetServerExample.php)
- [`resetServerPassword`](examples/Operations/ServerActions/ResetServerPasswordExample.php)
- [`shutdownServer`](examples/Operations/ServerActions/ShutdownServerExample.php)

#### ServerTypes

- [`getServerType`](examples/Operations/ServerTypes/GetServerTypeExample.php)
- [`listServerTypes`](examples/Operations/ServerTypes/ListServerTypesExample.php)

#### Servers

- [`createServer`](examples/Operations/Servers/CreateServerExample.php)
- [`deleteServer`](examples/Operations/Servers/DeleteServerExample.php)
- [`getServer`](examples/Operations/Servers/GetServerExample.php)
- [`getServerMetrics`](examples/Operations/Servers/GetServerMetricsExample.php)
- [`listServers`](examples/Operations/Servers/ListServersExample.php)
- [`updateServer`](examples/Operations/Servers/UpdateServerExample.php)

#### SshKeys

- [`createSshKey`](examples/Operations/SshKeys/CreateSshKeyExample.php)
- [`deleteSshKey`](examples/Operations/SshKeys/DeleteSshKeyExample.php)
- [`getSshKey`](examples/Operations/SshKeys/GetSshKeyExample.php)
- [`listSshKeys`](examples/Operations/SshKeys/ListSshKeysExample.php)
- [`updateSshKey`](examples/Operations/SshKeys/UpdateSshKeyExample.php)

#### StorageBoxActions

- [`changeStorageBoxProtection`](examples/Operations/StorageBoxActions/ChangeStorageBoxProtectionExample.php)
- [`changeStorageBoxType`](examples/Operations/StorageBoxActions/ChangeStorageBoxTypeExample.php)
- [`disableStorageBoxSnapshotPlan`](examples/Operations/StorageBoxActions/DisableStorageBoxSnapshotPlanExample.php)
- [`enableStorageBoxSnapshotPlan`](examples/Operations/StorageBoxActions/EnableStorageBoxSnapshotPlanExample.php)
- [`getStorageBoxAction`](examples/Operations/StorageBoxActions/GetStorageBoxActionExample.php)
- [`getStorageBoxesAction`](examples/Operations/StorageBoxActions/GetStorageBoxesActionExample.php)
- [`listStorageBoxActions`](examples/Operations/StorageBoxActions/ListStorageBoxActionsExample.php)
- [`listStorageBoxesActions`](examples/Operations/StorageBoxActions/ListStorageBoxesActionsExample.php)
- [`resetStorageBoxPassword`](examples/Operations/StorageBoxActions/ResetStorageBoxPasswordExample.php)
- [`rollbackStorageBoxSnapshot`](examples/Operations/StorageBoxActions/RollbackStorageBoxSnapshotExample.php)
- [`updateStorageBoxAccessSettings`](examples/Operations/StorageBoxActions/UpdateStorageBoxAccessSettingsExample.php)

#### StorageBoxSnapshots

- [`createStorageBoxSnapshot`](examples/Operations/StorageBoxSnapshots/CreateStorageBoxSnapshotExample.php)
- [`deleteStorageBoxSnapshot`](examples/Operations/StorageBoxSnapshots/DeleteStorageBoxSnapshotExample.php)
- [`getStorageBoxSnapshot`](examples/Operations/StorageBoxSnapshots/GetStorageBoxSnapshotExample.php)
- [`listStorageBoxSnapshots`](examples/Operations/StorageBoxSnapshots/ListStorageBoxSnapshotsExample.php)
- [`updateStorageBoxSnapshot`](examples/Operations/StorageBoxSnapshots/UpdateStorageBoxSnapshotExample.php)

#### StorageBoxSubaccountActions

- [`changeStorageBoxSubaccountHomeDirectory`](examples/Operations/StorageBoxSubaccountActions/ChangeStorageBoxSubaccountHomeDirectoryExample.php)
- [`resetStorageBoxSubaccountPassword`](examples/Operations/StorageBoxSubaccountActions/ResetStorageBoxSubaccountPasswordExample.php)
- [`updateStorageBoxSubaccountAccessSettings`](examples/Operations/StorageBoxSubaccountActions/UpdateStorageBoxSubaccountAccessSettingsExample.php)

#### StorageBoxSubaccounts

- [`createStorageBoxSubaccount`](examples/Operations/StorageBoxSubaccounts/CreateStorageBoxSubaccountExample.php)
- [`deleteStorageBoxSubaccount`](examples/Operations/StorageBoxSubaccounts/DeleteStorageBoxSubaccountExample.php)
- [`getStorageBoxSubaccount`](examples/Operations/StorageBoxSubaccounts/GetStorageBoxSubaccountExample.php)
- [`listStorageBoxSubaccounts`](examples/Operations/StorageBoxSubaccounts/ListStorageBoxSubaccountsExample.php)
- [`updateStorageBoxSubaccount`](examples/Operations/StorageBoxSubaccounts/UpdateStorageBoxSubaccountExample.php)

#### StorageBoxTypes

- [`getStorageBoxType`](examples/Operations/StorageBoxTypes/GetStorageBoxTypeExample.php)
- [`listStorageBoxTypes`](examples/Operations/StorageBoxTypes/ListStorageBoxTypesExample.php)

#### StorageBoxes

- [`createStorageBox`](examples/Operations/StorageBoxes/CreateStorageBoxExample.php)
- [`deleteStorageBox`](examples/Operations/StorageBoxes/DeleteStorageBoxExample.php)
- [`getStorageBox`](examples/Operations/StorageBoxes/GetStorageBoxExample.php)
- [`listStorageBoxFolders`](examples/Operations/StorageBoxes/ListStorageBoxFoldersExample.php)
- [`listStorageBoxes`](examples/Operations/StorageBoxes/ListStorageBoxesExample.php)
- [`updateStorageBox`](examples/Operations/StorageBoxes/UpdateStorageBoxExample.php)

#### VolumeActions

- [`attachVolume`](examples/Operations/VolumeActions/AttachVolumeExample.php)
- [`changeVolumeProtection`](examples/Operations/VolumeActions/ChangeVolumeProtectionExample.php)
- [`detachVolume`](examples/Operations/VolumeActions/DetachVolumeExample.php)
- [`getVolumeAction`](examples/Operations/VolumeActions/GetVolumeActionExample.php)
- [`getVolumesAction`](examples/Operations/VolumeActions/GetVolumesActionExample.php)
- [`listVolumeActions`](examples/Operations/VolumeActions/ListVolumeActionsExample.php)
- [`listVolumesActions`](examples/Operations/VolumeActions/ListVolumesActionsExample.php)
- [`resizeVolume`](examples/Operations/VolumeActions/ResizeVolumeExample.php)

#### Volumes

- [`createVolume`](examples/Operations/Volumes/CreateVolumeExample.php)
- [`deleteVolume`](examples/Operations/Volumes/DeleteVolumeExample.php)
- [`getVolume`](examples/Operations/Volumes/GetVolumeExample.php)
- [`listVolumes`](examples/Operations/Volumes/ListVolumesExample.php)
- [`updateVolume`](examples/Operations/Volumes/UpdateVolumeExample.php)

#### ZoneActions

- [`changeZonePrimaryNameservers`](examples/Operations/ZoneActions/ChangeZonePrimaryNameserversExample.php)
- [`changeZoneProtection`](examples/Operations/ZoneActions/ChangeZoneProtectionExample.php)
- [`changeZoneTtl`](examples/Operations/ZoneActions/ChangeZoneTtlExample.php)
- [`getZoneAction`](examples/Operations/ZoneActions/GetZoneActionExample.php)
- [`getZonesAction`](examples/Operations/ZoneActions/GetZonesActionExample.php)
- [`importZoneZonefile`](examples/Operations/ZoneActions/ImportZoneZonefileExample.php)
- [`listZoneActions`](examples/Operations/ZoneActions/ListZoneActionsExample.php)
- [`listZonesActions`](examples/Operations/ZoneActions/ListZonesActionsExample.php)

#### ZoneRrsetActions

- [`addZoneRrsetRecords`](examples/Operations/ZoneRrsetActions/AddZoneRrsetRecordsExample.php)
- [`changeZoneRrsetProtection`](examples/Operations/ZoneRrsetActions/ChangeZoneRrsetProtectionExample.php)
- [`changeZoneRrsetTtl`](examples/Operations/ZoneRrsetActions/ChangeZoneRrsetTtlExample.php)
- [`removeZoneRrsetRecords`](examples/Operations/ZoneRrsetActions/RemoveZoneRrsetRecordsExample.php)
- [`setZoneRrsetRecords`](examples/Operations/ZoneRrsetActions/SetZoneRrsetRecordsExample.php)
- [`updateZoneRrsetRecords`](examples/Operations/ZoneRrsetActions/UpdateZoneRrsetRecordsExample.php)

#### ZoneRrsets

- [`createZoneRrset`](examples/Operations/ZoneRrsets/CreateZoneRrsetExample.php)
- [`deleteZoneRrset`](examples/Operations/ZoneRrsets/DeleteZoneRrsetExample.php)
- [`getZoneRrset`](examples/Operations/ZoneRrsets/GetZoneRrsetExample.php)
- [`listZoneRrsets`](examples/Operations/ZoneRrsets/ListZoneRrsetsExample.php)
- [`updateZoneRrset`](examples/Operations/ZoneRrsets/UpdateZoneRrsetExample.php)

#### Zones

- [`createZone`](examples/Operations/Zones/CreateZoneExample.php)
- [`deleteZone`](examples/Operations/Zones/DeleteZoneExample.php)
- [`getZone`](examples/Operations/Zones/GetZoneExample.php)
- [`getZoneZonefile`](examples/Operations/Zones/GetZoneZonefileExample.php)
- [`listZones`](examples/Operations/Zones/ListZonesExample.php)
- [`updateZone`](examples/Operations/Zones/UpdateZoneExample.php)

## Validation is lax by default

**An API description is a claim about an API, and it is wrong more often than you would
expect.** A code is declared three characters long while every documented value has two.
A weight carries a maximum of `1` that was never meant as a limit. A response field runs
one character past its declared length, or arrives as `null` where a value was promised.
None of this is rare, and none of it is yours to fix.

So this package does **not** hold what it sends or what it reads to the constraints of
the description — maximum and minimum lengths, patterns, ranges, formats, item counts.
A request is sent as you built it; a response is read as far as its model can hold it.
This is `ValidationMode::Lax`, and it is what you get without asking.

What the PHP types say holds either way: a property has its declared type, a required
property is there, and a request names only the cases an enum has.

### If the API keeps to its description

Then have every constraint checked, in both directions:

```php
use Prefabcortex\Hetzner\Http\ValidationMode;

$config = $config->withValidation(ValidationMode::Strict);
```

A request that breaks a constraint then raises `ValidationException` and is never sent,
so a mistake in your data surfaces before the API sees it. A response that breaks one
raises `ResponseValidationException`, so a difference between the API and its description
shows up the first time it happens, not somewhere further down your code. If either one
turns out to be the description's mistake rather than yours, go back to `Lax`.

|                                              | `Lax` (default)              | `Strict`                      |
|----------------------------------------------|------------------------------|-------------------------------|
| **A request carries**                        |                              |                               |
| a text too long, a pattern or range not met  | sent as it is                | `ValidationException`         |
| **A response carries**                       |                              |                               |
| a text too long, a pattern or range not met  | read as it is                | `ResponseValidationException` |
| `null` in an optional property               | read as absent               | `ResponseValidationException` |
| an enum value no case of its enum names      | read as `UnknownEnumValue`   | `ResponseValidationException` |
| a value its model cannot hold                | `MalformedResponseException` | `ResponseValidationException` |

An API adds a value to an enum — a new status, a new service — before this package is
regenerated. That is why every enum property of a model is typed `SomeEnum|UnknownEnumValue`:
the value is kept, and `->value` reads it on either. A `match` over the enum
then needs a `default` arm, which is the point — it is where your code decides what a
value it has never seen means.

A case is named after the value it stands for, with `_` in place of any character a
PHP name cannot hold: `partially-valid` is
`ZoneBaseAuthoritativeNameserversDelegationStatus::partially_valid`.

A value its model cannot hold — a wrong type, a missing required property — stays an
error either way, because a typed model has nowhere to put it.

`ValidationException` means nothing was sent. The two response exceptions are
`ResponseException`s, so `getResponse()` and `getRawResponse()` hand back what arrived.
Mind what that means: **the request reached the API**, and whatever it asked for may have
happened — an order placed, a payment taken. Do not simply send it again; read the raw
response first.

## Optional values

A property the description marks required is a plain type on the model. A property it
leaves optional is an `Option`, because there are three states to tell apart and not
two: the field was absent, the field was `null`, or the field had a value. A `?string`
can hold the last two and loses the first, and losing it matters — `toArray()` sends
back only what was actually set, so a field the server never mentioned stays unmentioned
rather than being echoed as `null`.

Three methods, and no others:

```php
$value->isDefined();        // was it there at all?
$value->get();              // the value — RuntimeException on an absent one
$value->getOrElse($other);  // the value, or $other when it is absent
```

On `AddLoadBalancerServiceBody`, for instance, `getListenPort()` is required and
reads as itself, while `getHttp()` is optional:

```php
$model->getListenPort();           // the value
$model->getHttp()->getOrElse('');  // the value, or a default
```

Writing one is the other way round, and needs none of this. `builder()` takes the required
properties and starts every optional one absent; each `set…()` takes the bare value and
wraps it for you, and `build()` hands back the model. `toBuilder()` starts from a model you
already have, which itself never changes. Query and header parameter objects take bare
values in their `with…()` the same way. There is no reason to write `Some::create()` or
`None::create()` yourself.

## Error handling

Every exception a call can end in implements `ApiException`, so one catch covers
everything the API can report:

```php
try {
    // … any operation
} catch (ApiException $e) {
    // …
}
```

That includes the call never completing. A failure your HTTP client reports — a
timeout, a refused connection, a request it would not send — is caught and re-thrown as
`TransportException`, so it lands in the same catch as everything else rather than
beside it.

Two things follow, and both are deliberate. The PSR interfaces still match, so
`catch (Psr\Http\Client\NetworkExceptionInterface $e)` before the block above still
picks out the failures worth retrying, and `getRequest()` tells you what was being
sent. But a catch written against your client's *own* class — Guzzle's
`ConnectException`, say — does not match, because the exception you receive is not that
class. The original is there as `getPrevious()`.

One exception stays outside the catch on purpose, because it is a mistake in the
calling code rather than a way the call can fail: `get()` on an `Option` that holds no
value throws `RuntimeException`. Ask `isDefined()` first, or use `getOrElse()`.

Below it the hierarchy narrows:

- `ResponseException` — raised by a response that arrived, and where
  `getResponse()` and `getRawResponse()` are declared. `MalformedDataException`,
  `NoHttpClientException`, `UnsupportedValueException` and `ValidationException` have
  none to hand back and stop at `ApiException`.
- `ClientException` (4xx) and `ServerException` (5xx) — which side the failure came from.
- One class per status: `ServerErrorException`.
- One class per operation and status — these are the ones actually thrown. Each adds the
  typed error body:
  `AddLoadBalancerServiceClientErrorException::getErrorResponse(): ErrorResponse`.

A response that fits no declared branch is one of two `ResponseException`s with nothing
beyond the two accessors, named after what did not fit:

- `UnexpectedStatusCodeException` — no response declares the status, or a declared error
  response's body does not read as declared (the reason is `getPrevious()`). Its status
  still says which side failed: a 4xx is a `ClientException`, a 5xx a `ServerException`.
- `UnexpectedContentTypeException` — the status is declared, but not under the content
  type the response arrived with. A 404 served as `text/html` by a proxy in front of the
  API is this, not a `NotFoundException`: its body is not the one the description
  promises, so there is nothing to read it into.

Two things an error response carries are read from any `ResponseException`, whether or
not the description declares its status. A 429 or a 503 often says how long to wait in
a `Retry-After` header, as a number of seconds or as a date; `RetryAfter` reads either.
A body served as `application/problem+json` (RFC 9457) reads as `ProblemDetails`:

```php
use Prefabcortex\Hetzner\Exception\ClientException;
use Prefabcortex\Hetzner\Http\ProblemDetails;
use Prefabcortex\Hetzner\Http\RetryAfter;

try {
    // … any operation
} catch (ClientException $e) {
    $problem = ProblemDetails::of($e);
    if ($problem->isDefined()) {
        error_log($problem->get()->detail->getOrElse($e->getMessage()));
    }

    $retryAfter = RetryAfter::of($e);
    if ($retryAfter->isDefined()) {
        sleep($retryAfter->get()->secondsFrom(new DateTimeImmutable()));
    }
}
```

## Trademarks

Trademarks mentioned here — including in the name of this package — are the
property of their respective owners. They appear to identify the API this client
addresses, and for no other purpose: nothing here is a claim about who made this
package or who stands behind it.

This is an unofficial client, generated from the published API description. It IS
NOT affiliated with, endorsed by, or connected to the operator of that API.

## License

The generated code is 0BSD — see [LICENSE](LICENSE). Documentation text carried over
from the API description is quoted from that description and remains its author's;
it is reproduced here to document the interface, not relicensed. Holding the rights to
that description is the responsibility of this package's publisher, the copyright
holder named in [LICENSE](LICENSE).

## About This Package

This package was generated from an OpenAPI specification. It is yours to take
further — bear in mind only that regenerating it replaces every file in the
package, so anything changed by hand is worth keeping somewhere that survives
that: a patch, a subclass, or a fork you maintain yourself.

Generated by [PrefabCortex](https://www.prefabcortex.com), which turns an OpenAPI
specification into a ready-to-use PHP Composer package. PrefabCortex
generated it on behalf of the publisher named in [LICENSE](LICENSE) and
neither publishes, reviews nor maintains it.
