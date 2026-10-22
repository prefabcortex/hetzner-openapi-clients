<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\SelfNormalizingModel;
use Symfony\Component\Validator\Constraint;

/**
 * The data providers over the fixture classes beside them: one schema-conformant instance of every
 * model in this package, and what each is checked against.
 *
 * Values are the ones the API description states — `example` or `default` where it gives one, a
 * typed placeholder where it does not. They are shaped like real data, not equal to it: nothing
 * here has been sent to the service, so a value being accepted by the schema says nothing about it
 * being accepted by the server.
 *
 * Built, but not checked against their constraints: at least one value could not be chosen so that
 * it passes — a pattern too intricate to sample, a range with no room, a list that must hold
 * distinct items. Their fixtures carry a placeholder there:
 *   - MetricsResponseMetricsTimeSeriesItem
 */
final class ModelFixtureProviders
{
    /**
     * Every model that could be built and reads back what it writes, keyed by class name so a
     * failure names the model.
     *
     * @return iterable<string, array{SelfNormalizingModel, callable(array<int|string, mixed>): SelfNormalizingModel}>
     */
    public static function roundTrips(): iterable
    {
        yield 'ServiceTCP' => [ServiceTCPFixture::build(), ServiceTCPFixture::reader()];
        yield 'ServiceHTTPProtocol' => [ServiceHTTPProtocolFixture::build(), ServiceHTTPProtocolFixture::reader()];
        yield 'ServiceHTTPSProtocol' => [ServiceHTTPSProtocolFixture::build(), ServiceHTTPSProtocolFixture::reader()];
        yield 'TargetTypeServer' => [TargetTypeServerFixture::build(), TargetTypeServerFixture::reader()];
        yield 'TargetTypeLabelSelector' => [
            TargetTypeLabelSelectorFixture::build(),
            TargetTypeLabelSelectorFixture::reader(),
        ];
        yield 'TargetTypeIP' => [TargetTypeIPFixture::build(), TargetTypeIPFixture::reader()];
        yield 'ZonePrimary' => [ZonePrimaryFixture::build(), ZonePrimaryFixture::reader()];
        yield 'ZoneSecondary' => [ZoneSecondaryFixture::build(), ZoneSecondaryFixture::reader()];
        yield 'Action' => [ActionFixture::build(), ActionFixture::reader()];
        yield 'ActionError' => [ActionErrorFixture::build(), ActionErrorFixture::reader()];
        yield 'ActionListResponse' => [ActionListResponseFixture::build(), ActionListResponseFixture::reader()];
        yield 'ActionListResponseWithMeta' => [
            ActionListResponseWithMetaFixture::build(),
            ActionListResponseWithMetaFixture::reader(),
        ];
        yield 'ActionResource' => [ActionResourceFixture::build(), ActionResourceFixture::reader()];
        yield 'ActionResponse' => [ActionResponseFixture::build(), ActionResponseFixture::reader()];
        yield 'Certificate' => [CertificateFixture::build(), CertificateFixture::reader()];
        yield 'CertificateStatus' => [CertificateStatusFixture::build(), CertificateStatusFixture::reader()];
        yield 'CertificateStatusError' => [
            CertificateStatusErrorFixture::build(),
            CertificateStatusErrorFixture::reader(),
        ];
        yield 'CertificateUsedByItem' => [
            CertificateUsedByItemFixture::build(),
            CertificateUsedByItemFixture::reader(),
        ];
        yield 'CertificateResponse' => [CertificateResponseFixture::build(), CertificateResponseFixture::reader()];
        yield 'ChangeDeleteProtectionRequest' => [
            ChangeDeleteProtectionRequestFixture::build(),
            ChangeDeleteProtectionRequestFixture::reader(),
        ];
        yield 'CreatedFrom' => [CreatedFromFixture::build(), CreatedFromFixture::reader()];
        yield 'Datacenter' => [DatacenterFixture::build(), DatacenterFixture::reader()];
        yield 'DatacenterServerTypes' => [
            DatacenterServerTypesFixture::build(),
            DatacenterServerTypesFixture::reader(),
        ];
        yield 'DeprecationInfo' => [DeprecationInfoFixture::build(), DeprecationInfoFixture::reader()];
        yield 'DnsPtr' => [DnsPtrFixture::build(), DnsPtrFixture::reader()];
        yield 'ErrorResponse' => [ErrorResponseFixture::build(), ErrorResponseFixture::reader()];
        yield 'ErrorResponseError' => [ErrorResponseErrorFixture::build(), ErrorResponseErrorFixture::reader()];
        yield 'Firewall' => [FirewallFixture::build(), FirewallFixture::reader()];
        yield 'FirewallRulesItem' => [FirewallRulesItemFixture::build(), FirewallRulesItemFixture::reader()];
        yield 'FirewallAppliedToItem' => [
            FirewallAppliedToItemFixture::build(),
            FirewallAppliedToItemFixture::reader(),
        ];
        yield 'FirewallAppliedToItemAppliedToResourcesItem' => [
            FirewallAppliedToItemAppliedToResourcesItemFixture::build(),
            FirewallAppliedToItemAppliedToResourcesItemFixture::reader(),
        ];
        yield 'FirewallAppliedToServer' => [
            FirewallAppliedToServerFixture::build(),
            FirewallAppliedToServerFixture::reader(),
        ];
        yield 'FirewallResource' => [FirewallResourceFixture::build(), FirewallResourceFixture::reader()];
        yield 'FirewallResourceServer' => [
            FirewallResourceServerFixture::build(),
            FirewallResourceServerFixture::reader(),
        ];
        yield 'FirewallResponse' => [FirewallResponseFixture::build(), FirewallResponseFixture::reader()];
        yield 'FloatingIp' => [FloatingIpFixture::build(), FloatingIpFixture::reader()];
        yield 'FloatingIpResponse' => [FloatingIpResponseFixture::build(), FloatingIpResponseFixture::reader()];
        yield 'HealthCheckHttp' => [HealthCheckHttpFixture::build(), HealthCheckHttpFixture::reader()];
        yield 'HealthStatus' => [HealthStatusFixture::build(), HealthStatusFixture::reader()];
        yield 'Image' => [ImageFixture::build(), ImageFixture::reader()];
        yield 'ImageResponse' => [ImageResponseFixture::build(), ImageResponseFixture::reader()];
        yield 'Iso' => [IsoFixture::build(), IsoFixture::reader()];
        yield 'LabelSelector' => [LabelSelectorFixture::build(), LabelSelectorFixture::reader()];
        yield 'ListMeta' => [ListMetaFixture::build(), ListMetaFixture::reader()];
        yield 'ListMetaPagination' => [ListMetaPaginationFixture::build(), ListMetaPaginationFixture::reader()];
        yield 'LoadBalancer' => [LoadBalancerFixture::build(), LoadBalancerFixture::reader()];
        yield 'LoadBalancerPublicNet' => [
            LoadBalancerPublicNetFixture::build(),
            LoadBalancerPublicNetFixture::reader(),
        ];
        yield 'LoadBalancerPrivateNetItem' => [
            LoadBalancerPrivateNetItemFixture::build(),
            LoadBalancerPrivateNetItemFixture::reader(),
        ];
        yield 'LoadBalancerAlgorithm2' => [
            LoadBalancerAlgorithm2Fixture::build(),
            LoadBalancerAlgorithm2Fixture::reader(),
        ];
        yield 'LoadBalancerAlgorithm' => [
            LoadBalancerAlgorithmFixture::build(),
            LoadBalancerAlgorithmFixture::reader(),
        ];
        yield 'LoadBalancerPublicIp' => [LoadBalancerPublicIpFixture::build(), LoadBalancerPublicIpFixture::reader()];
        yield 'LoadBalancerResponse' => [LoadBalancerResponseFixture::build(), LoadBalancerResponseFixture::reader()];
        yield 'LoadBalancerService' => [LoadBalancerServiceFixture::build(), LoadBalancerServiceFixture::reader()];
        yield 'LoadBalancerServiceHealthCheck' => [
            LoadBalancerServiceHealthCheckFixture::build(),
            LoadBalancerServiceHealthCheckFixture::reader(),
        ];
        yield 'LoadBalancerServiceBase' => [
            LoadBalancerServiceBaseFixture::build(),
            LoadBalancerServiceBaseFixture::reader(),
        ];
        yield 'LoadBalancerServiceBaseHealthCheck' => [
            LoadBalancerServiceBaseHealthCheckFixture::build(),
            LoadBalancerServiceBaseHealthCheckFixture::reader(),
        ];
        yield 'LoadBalancerServiceBaseHealthCheckHttp' => [
            LoadBalancerServiceBaseHealthCheckHttpFixture::build(),
            LoadBalancerServiceBaseHealthCheckHttpFixture::reader(),
        ];
        yield 'LoadBalancerServiceHTTPProtocolProperties' => [
            LoadBalancerServiceHTTPProtocolPropertiesFixture::build(),
            LoadBalancerServiceHTTPProtocolPropertiesFixture::reader(),
        ];
        yield 'LoadBalancerServiceHTTPProtocolPropertiesHttp' => [
            LoadBalancerServiceHTTPProtocolPropertiesHttpFixture::build(),
            LoadBalancerServiceHTTPProtocolPropertiesHttpFixture::reader(),
        ];
        yield 'LoadBalancerServiceHTTPSProtocolProperties' => [
            LoadBalancerServiceHTTPSProtocolPropertiesFixture::build(),
            LoadBalancerServiceHTTPSProtocolPropertiesFixture::reader(),
        ];
        yield 'LoadBalancerServiceHTTPSProtocolPropertiesHttp' => [
            LoadBalancerServiceHTTPSProtocolPropertiesHttpFixture::build(),
            LoadBalancerServiceHTTPSProtocolPropertiesHttpFixture::reader(),
        ];
        yield 'LoadBalancerServiceTCPProperties' => [
            LoadBalancerServiceTCPPropertiesFixture::build(),
            LoadBalancerServiceTCPPropertiesFixture::reader(),
        ];
        yield 'LoadBalancerTarget' => [LoadBalancerTargetFixture::build(), LoadBalancerTargetFixture::reader()];
        yield 'LoadBalancerTargetIP' => [LoadBalancerTargetIPFixture::build(), LoadBalancerTargetIPFixture::reader()];
        yield 'LoadBalancerTargetLabelSelector' => [
            LoadBalancerTargetLabelSelectorFixture::build(),
            LoadBalancerTargetLabelSelectorFixture::reader(),
        ];
        yield 'LoadBalancerTargetRequestProperties' => [
            LoadBalancerTargetRequestPropertiesFixture::build(),
            LoadBalancerTargetRequestPropertiesFixture::reader(),
        ];
        yield 'LoadBalancerTargetServer' => [
            LoadBalancerTargetServerFixture::build(),
            LoadBalancerTargetServerFixture::reader(),
        ];
        yield 'LoadBalancerTargetServerRequest' => [
            LoadBalancerTargetServerRequestFixture::build(),
            LoadBalancerTargetServerRequestFixture::reader(),
        ];
        yield 'LoadBalancerTargetTypeBase' => [
            LoadBalancerTargetTypeBaseFixture::build(),
            LoadBalancerTargetTypeBaseFixture::reader(),
        ];
        yield 'LoadBalancerTargetTypeIPProperties' => [
            LoadBalancerTargetTypeIPPropertiesFixture::build(),
            LoadBalancerTargetTypeIPPropertiesFixture::reader(),
        ];
        yield 'LoadBalancerTargetTypeLabelSelectorProperties' => [
            LoadBalancerTargetTypeLabelSelectorPropertiesFixture::build(),
            LoadBalancerTargetTypeLabelSelectorPropertiesFixture::reader(),
        ];
        yield 'LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItem' => [
            LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItemFixture::build(),
            LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItemFixture::reader(),
        ];
        yield 'LoadBalancerTargetTypeServerProperties' => [
            LoadBalancerTargetTypeServerPropertiesFixture::build(),
            LoadBalancerTargetTypeServerPropertiesFixture::reader(),
        ];
        yield 'LoadBalancerType' => [LoadBalancerTypeFixture::build(), LoadBalancerTypeFixture::reader()];
        yield 'Location' => [LocationFixture::build(), LocationFixture::reader()];
        yield 'LocationPrice' => [LocationPriceFixture::build(), LocationPriceFixture::reader()];
        yield 'MetricsResponse' => [MetricsResponseFixture::build(), MetricsResponseFixture::reader()];
        yield 'MetricsResponseMetrics' => [
            MetricsResponseMetricsFixture::build(),
            MetricsResponseMetricsFixture::reader(),
        ];
        yield 'MetricsResponseMetricsTimeSeriesItem' => [
            MetricsResponseMetricsTimeSeriesItemFixture::build(),
            MetricsResponseMetricsTimeSeriesItemFixture::reader(),
        ];
        yield 'Network' => [NetworkFixture::build(), NetworkFixture::reader()];
        yield 'NetworkSubnetsItem' => [NetworkSubnetsItemFixture::build(), NetworkSubnetsItemFixture::reader()];
        yield 'NetworkResponse' => [NetworkResponseFixture::build(), NetworkResponseFixture::reader()];
        yield 'PlacementGroup' => [PlacementGroupFixture::build(), PlacementGroupFixture::reader()];
        yield 'PlacementGroupResponse' => [
            PlacementGroupResponseFixture::build(),
            PlacementGroupResponseFixture::reader(),
        ];
        yield 'Price' => [PriceFixture::build(), PriceFixture::reader()];
        yield 'PricePerGbMonth' => [PricePerGbMonthFixture::build(), PricePerGbMonthFixture::reader()];
        yield 'PrimaryIP' => [PrimaryIPFixture::build(), PrimaryIPFixture::reader()];
        yield 'PrimaryIPResponse' => [PrimaryIPResponseFixture::build(), PrimaryIPResponseFixture::reader()];
        yield 'PrimaryZoneProperties' => [
            PrimaryZonePropertiesFixture::build(),
            PrimaryZonePropertiesFixture::reader(),
        ];
        yield 'Protection' => [ProtectionFixture::build(), ProtectionFixture::reader()];
        yield 'RRSet' => [RRSetFixture::build(), RRSetFixture::reader()];
        yield 'RRSetProtection' => [RRSetProtectionFixture::build(), RRSetProtectionFixture::reader()];
        yield 'RRSetRecordsRequest' => [RRSetRecordsRequestFixture::build(), RRSetRecordsRequestFixture::reader()];
        yield 'RRSetRequest' => [RRSetRequestFixture::build(), RRSetRequestFixture::reader()];
        yield 'Record' => [RecordFixture::build(), RecordFixture::reader()];
        yield 'RootPasswordResponse' => [RootPasswordResponseFixture::build(), RootPasswordResponseFixture::reader()];
        yield 'Route' => [RouteFixture::build(), RouteFixture::reader()];
        yield 'RrsetResponse' => [RrsetResponseFixture::build(), RrsetResponseFixture::reader()];
        yield 'Rule' => [RuleFixture::build(), RuleFixture::reader()];
        yield 'SecondaryZoneProperties' => [
            SecondaryZonePropertiesFixture::build(),
            SecondaryZonePropertiesFixture::reader(),
        ];
        yield 'Server' => [ServerFixture::build(), ServerFixture::reader()];
        yield 'ServerPublicNet' => [ServerPublicNetFixture::build(), ServerPublicNetFixture::reader()];
        yield 'ServerPublicNetIpv4' => [ServerPublicNetIpv4Fixture::build(), ServerPublicNetIpv4Fixture::reader()];
        yield 'ServerPublicNetIpv6' => [ServerPublicNetIpv6Fixture::build(), ServerPublicNetIpv6Fixture::reader()];
        yield 'ServerPublicNetFirewallsItem' => [
            ServerPublicNetFirewallsItemFixture::build(),
            ServerPublicNetFirewallsItemFixture::reader(),
        ];
        yield 'ServerPrivateNetItem' => [ServerPrivateNetItemFixture::build(), ServerPrivateNetItemFixture::reader()];
        yield 'ServerProtection' => [ServerProtectionFixture::build(), ServerProtectionFixture::reader()];
        yield 'ServerResponse' => [ServerResponseFixture::build(), ServerResponseFixture::reader()];
        yield 'ServerType' => [ServerTypeFixture::build(), ServerTypeFixture::reader()];
        yield 'ServerTypeLocationsItem' => [
            ServerTypeLocationsItemFixture::build(),
            ServerTypeLocationsItemFixture::reader(),
        ];
        yield 'SshKey' => [SshKeyFixture::build(), SshKeyFixture::reader()];
        yield 'SshKeyResponse' => [SshKeyResponseFixture::build(), SshKeyResponseFixture::reader()];
        yield 'TypePricing' => [TypePricingFixture::build(), TypePricingFixture::reader()];
        yield 'Volume' => [VolumeFixture::build(), VolumeFixture::reader()];
        yield 'VolumeResponse' => [VolumeResponseFixture::build(), VolumeResponseFixture::reader()];
        yield 'ZoneBase' => [ZoneBaseFixture::build(), ZoneBaseFixture::reader()];
        yield 'ZoneBaseAuthoritativeNameservers' => [
            ZoneBaseAuthoritativeNameserversFixture::build(),
            ZoneBaseAuthoritativeNameserversFixture::reader(),
        ];
        yield 'ZonePrimaryNameserver' => [
            ZonePrimaryNameserverFixture::build(),
            ZonePrimaryNameserverFixture::reader(),
        ];
        yield 'ZoneResponse' => [ZoneResponseFixture::build(), ZoneResponseFixture::reader()];
        yield 'Zonefile' => [ZonefileFixture::build(), ZonefileFixture::reader()];
        yield 'ResetPasswordRequest' => [ResetPasswordRequestFixture::build(), ResetPasswordRequestFixture::reader()];
        yield 'Snapshot' => [SnapshotFixture::build(), SnapshotFixture::reader()];
        yield 'SnapshotStats' => [SnapshotStatsFixture::build(), SnapshotStatsFixture::reader()];
        yield 'SnapshotResponse' => [SnapshotResponseFixture::build(), SnapshotResponseFixture::reader()];
        yield 'StorageBox' => [StorageBoxFixture::build(), StorageBoxFixture::reader()];
        yield 'StorageBoxAccessSettings' => [
            StorageBoxAccessSettingsFixture::build(),
            StorageBoxAccessSettingsFixture::reader(),
        ];
        yield 'StorageBoxSnapshotPlan' => [
            StorageBoxSnapshotPlanFixture::build(),
            StorageBoxSnapshotPlanFixture::reader(),
        ];
        yield 'StorageBoxStats' => [StorageBoxStatsFixture::build(), StorageBoxStatsFixture::reader()];
        yield 'StorageBoxResponse' => [StorageBoxResponseFixture::build(), StorageBoxResponseFixture::reader()];
        yield 'StorageBoxType' => [StorageBoxTypeFixture::build(), StorageBoxTypeFixture::reader()];
        yield 'StorageBoxTypePricesItem' => [
            StorageBoxTypePricesItemFixture::build(),
            StorageBoxTypePricesItemFixture::reader(),
        ];
        yield 'Subaccount' => [SubaccountFixture::build(), SubaccountFixture::reader()];
        yield 'SubaccountAccessSettings' => [
            SubaccountAccessSettingsFixture::build(),
            SubaccountAccessSettingsFixture::reader(),
        ];
        yield 'SubaccountResponse' => [SubaccountResponseFixture::build(), SubaccountResponseFixture::reader()];
        yield 'ListCertificatesResponse200' => [
            ListCertificatesResponse200Fixture::build(),
            ListCertificatesResponse200Fixture::reader(),
        ];
        yield 'CreateCertificateBody' => [
            CreateCertificateBodyFixture::build(),
            CreateCertificateBodyFixture::reader(),
        ];
        yield 'CreateCertificateResponse201' => [
            CreateCertificateResponse201Fixture::build(),
            CreateCertificateResponse201Fixture::reader(),
        ];
        yield 'UpdateCertificateBody' => [
            UpdateCertificateBodyFixture::build(),
            UpdateCertificateBodyFixture::reader(),
        ];
        yield 'ListDatacentersResponse200' => [
            ListDatacentersResponse200Fixture::build(),
            ListDatacentersResponse200Fixture::reader(),
        ];
        yield 'GetDatacenterResponse200' => [
            GetDatacenterResponse200Fixture::build(),
            GetDatacenterResponse200Fixture::reader(),
        ];
        yield 'ListFirewallsResponse200' => [
            ListFirewallsResponse200Fixture::build(),
            ListFirewallsResponse200Fixture::reader(),
        ];
        yield 'CreateFirewallBody' => [CreateFirewallBodyFixture::build(), CreateFirewallBodyFixture::reader()];
        yield 'CreateFirewallResponse201' => [
            CreateFirewallResponse201Fixture::build(),
            CreateFirewallResponse201Fixture::reader(),
        ];
        yield 'UpdateFirewallBody' => [UpdateFirewallBodyFixture::build(), UpdateFirewallBodyFixture::reader()];
        yield 'ApplyFirewallToResourcesBody' => [
            ApplyFirewallToResourcesBodyFixture::build(),
            ApplyFirewallToResourcesBodyFixture::reader(),
        ];
        yield 'RemoveFirewallFromResourcesBody' => [
            RemoveFirewallFromResourcesBodyFixture::build(),
            RemoveFirewallFromResourcesBodyFixture::reader(),
        ];
        yield 'SetFirewallRulesBody' => [SetFirewallRulesBodyFixture::build(), SetFirewallRulesBodyFixture::reader()];
        yield 'ListFloatingIpsResponse200' => [
            ListFloatingIpsResponse200Fixture::build(),
            ListFloatingIpsResponse200Fixture::reader(),
        ];
        yield 'CreateFloatingIpBody' => [CreateFloatingIpBodyFixture::build(), CreateFloatingIpBodyFixture::reader()];
        yield 'CreateFloatingIpResponse201' => [
            CreateFloatingIpResponse201Fixture::build(),
            CreateFloatingIpResponse201Fixture::reader(),
        ];
        yield 'UpdateFloatingIpBody' => [UpdateFloatingIpBodyFixture::build(), UpdateFloatingIpBodyFixture::reader()];
        yield 'AssignFloatingIpBody' => [AssignFloatingIpBodyFixture::build(), AssignFloatingIpBodyFixture::reader()];
        yield 'ChangeFloatingIpDnsPtrBody' => [
            ChangeFloatingIpDnsPtrBodyFixture::build(),
            ChangeFloatingIpDnsPtrBodyFixture::reader(),
        ];
        yield 'ChangeFloatingIpProtectionBody' => [
            ChangeFloatingIpProtectionBodyFixture::build(),
            ChangeFloatingIpProtectionBodyFixture::reader(),
        ];
        yield 'ListImagesResponse200' => [
            ListImagesResponse200Fixture::build(),
            ListImagesResponse200Fixture::reader(),
        ];
        yield 'UpdateImageBody' => [UpdateImageBodyFixture::build(), UpdateImageBodyFixture::reader()];
        yield 'ListIsosResponse200' => [ListIsosResponse200Fixture::build(), ListIsosResponse200Fixture::reader()];
        yield 'GetIsoResponse200' => [GetIsoResponse200Fixture::build(), GetIsoResponse200Fixture::reader()];
        yield 'ListLoadBalancerTypesResponse200' => [
            ListLoadBalancerTypesResponse200Fixture::build(),
            ListLoadBalancerTypesResponse200Fixture::reader(),
        ];
        yield 'GetLoadBalancerTypeResponse200' => [
            GetLoadBalancerTypeResponse200Fixture::build(),
            GetLoadBalancerTypeResponse200Fixture::reader(),
        ];
        yield 'ListLoadBalancersResponse200' => [
            ListLoadBalancersResponse200Fixture::build(),
            ListLoadBalancersResponse200Fixture::reader(),
        ];
        yield 'CreateLoadBalancerBody' => [
            CreateLoadBalancerBodyFixture::build(),
            CreateLoadBalancerBodyFixture::reader(),
        ];
        yield 'CreateLoadBalancerBodyTargetsItem' => [
            CreateLoadBalancerBodyTargetsItemFixture::build(),
            CreateLoadBalancerBodyTargetsItemFixture::reader(),
        ];
        yield 'CreateLoadBalancerBodyPublicNet' => [
            CreateLoadBalancerBodyPublicNetFixture::build(),
            CreateLoadBalancerBodyPublicNetFixture::reader(),
        ];
        yield 'CreateLoadBalancerResponse201' => [
            CreateLoadBalancerResponse201Fixture::build(),
            CreateLoadBalancerResponse201Fixture::reader(),
        ];
        yield 'UpdateLoadBalancerBody' => [
            UpdateLoadBalancerBodyFixture::build(),
            UpdateLoadBalancerBodyFixture::reader(),
        ];
        yield 'AddLoadBalancerServiceBody' => [
            AddLoadBalancerServiceBodyFixture::build(),
            AddLoadBalancerServiceBodyFixture::reader(),
        ];
        yield 'AddLoadBalancerServiceBodyHttp' => [
            AddLoadBalancerServiceBodyHttpFixture::build(),
            AddLoadBalancerServiceBodyHttpFixture::reader(),
        ];
        yield 'AddLoadBalancerTargetBody' => [
            AddLoadBalancerTargetBodyFixture::build(),
            AddLoadBalancerTargetBodyFixture::reader(),
        ];
        yield 'AttachLoadBalancerToNetworkBody' => [
            AttachLoadBalancerToNetworkBodyFixture::build(),
            AttachLoadBalancerToNetworkBodyFixture::reader(),
        ];
        yield 'ChangeLoadBalancerDnsPtrBody' => [
            ChangeLoadBalancerDnsPtrBodyFixture::build(),
            ChangeLoadBalancerDnsPtrBodyFixture::reader(),
        ];
        yield 'ChangeLoadBalancerTypeBody' => [
            ChangeLoadBalancerTypeBodyFixture::build(),
            ChangeLoadBalancerTypeBodyFixture::reader(),
        ];
        yield 'DeleteLoadBalancerServiceBody' => [
            DeleteLoadBalancerServiceBodyFixture::build(),
            DeleteLoadBalancerServiceBodyFixture::reader(),
        ];
        yield 'DetachLoadBalancerFromNetworkBody' => [
            DetachLoadBalancerFromNetworkBodyFixture::build(),
            DetachLoadBalancerFromNetworkBodyFixture::reader(),
        ];
        yield 'UpdateLoadBalancerServiceBody' => [
            UpdateLoadBalancerServiceBodyFixture::build(),
            UpdateLoadBalancerServiceBodyFixture::reader(),
        ];
        yield 'UpdateLoadBalancerServiceBodyHealthCheck' => [
            UpdateLoadBalancerServiceBodyHealthCheckFixture::build(),
            UpdateLoadBalancerServiceBodyHealthCheckFixture::reader(),
        ];
        yield 'UpdateLoadBalancerServiceBodyHttp' => [
            UpdateLoadBalancerServiceBodyHttpFixture::build(),
            UpdateLoadBalancerServiceBodyHttpFixture::reader(),
        ];
        yield 'ListLocationsResponse200' => [
            ListLocationsResponse200Fixture::build(),
            ListLocationsResponse200Fixture::reader(),
        ];
        yield 'GetLocationResponse200' => [
            GetLocationResponse200Fixture::build(),
            GetLocationResponse200Fixture::reader(),
        ];
        yield 'ListNetworksResponse200' => [
            ListNetworksResponse200Fixture::build(),
            ListNetworksResponse200Fixture::reader(),
        ];
        yield 'CreateNetworkBody' => [CreateNetworkBodyFixture::build(), CreateNetworkBodyFixture::reader()];
        yield 'CreateNetworkBodySubnetsItem' => [
            CreateNetworkBodySubnetsItemFixture::build(),
            CreateNetworkBodySubnetsItemFixture::reader(),
        ];
        yield 'UpdateNetworkBody' => [UpdateNetworkBodyFixture::build(), UpdateNetworkBodyFixture::reader()];
        yield 'AddNetworkSubnetBody' => [AddNetworkSubnetBodyFixture::build(), AddNetworkSubnetBodyFixture::reader()];
        yield 'ChangeNetworkIpRangeBody' => [
            ChangeNetworkIpRangeBodyFixture::build(),
            ChangeNetworkIpRangeBodyFixture::reader(),
        ];
        yield 'DeleteNetworkSubnetBody' => [
            DeleteNetworkSubnetBodyFixture::build(),
            DeleteNetworkSubnetBodyFixture::reader(),
        ];
        yield 'ListNetworkMembersResponse200' => [
            ListNetworkMembersResponse200Fixture::build(),
            ListNetworkMembersResponse200Fixture::reader(),
        ];
        yield 'ListNetworkMembersResponse200MembersItem' => [
            ListNetworkMembersResponse200MembersItemFixture::build(),
            ListNetworkMembersResponse200MembersItemFixture::reader(),
        ];
        yield 'ListPlacementGroupsResponse200' => [
            ListPlacementGroupsResponse200Fixture::build(),
            ListPlacementGroupsResponse200Fixture::reader(),
        ];
        yield 'CreatePlacementGroupBody' => [
            CreatePlacementGroupBodyFixture::build(),
            CreatePlacementGroupBodyFixture::reader(),
        ];
        yield 'CreatePlacementGroupResponse201' => [
            CreatePlacementGroupResponse201Fixture::build(),
            CreatePlacementGroupResponse201Fixture::reader(),
        ];
        yield 'UpdatePlacementGroupBody' => [
            UpdatePlacementGroupBodyFixture::build(),
            UpdatePlacementGroupBodyFixture::reader(),
        ];
        yield 'GetPricingResponse200' => [
            GetPricingResponse200Fixture::build(),
            GetPricingResponse200Fixture::reader(),
        ];
        yield 'GetPricingResponse200Pricing' => [
            GetPricingResponse200PricingFixture::build(),
            GetPricingResponse200PricingFixture::reader(),
        ];
        yield 'GetPricingResponse200PricingPrimaryIpsItem' => [
            GetPricingResponse200PricingPrimaryIpsItemFixture::build(),
            GetPricingResponse200PricingPrimaryIpsItemFixture::reader(),
        ];
        yield 'GetPricingResponse200PricingPrimaryIpsItemPricesItem' => [
            GetPricingResponse200PricingPrimaryIpsItemPricesItemFixture::build(),
            GetPricingResponse200PricingPrimaryIpsItemPricesItemFixture::reader(),
        ];
        yield 'GetPricingResponse200PricingFloatingIpsItem' => [
            GetPricingResponse200PricingFloatingIpsItemFixture::build(),
            GetPricingResponse200PricingFloatingIpsItemFixture::reader(),
        ];
        yield 'GetPricingResponse200PricingFloatingIpsItemPricesItem' => [
            GetPricingResponse200PricingFloatingIpsItemPricesItemFixture::build(),
            GetPricingResponse200PricingFloatingIpsItemPricesItemFixture::reader(),
        ];
        yield 'GetPricingResponse200PricingServerBackup' => [
            GetPricingResponse200PricingServerBackupFixture::build(),
            GetPricingResponse200PricingServerBackupFixture::reader(),
        ];
        yield 'GetPricingResponse200PricingFloatingIp' => [
            GetPricingResponse200PricingFloatingIpFixture::build(),
            GetPricingResponse200PricingFloatingIpFixture::reader(),
        ];
        yield 'ListPrimaryIpsResponse200' => [
            ListPrimaryIpsResponse200Fixture::build(),
            ListPrimaryIpsResponse200Fixture::reader(),
        ];
        yield 'CreatePrimaryIpBody' => [CreatePrimaryIpBodyFixture::build(), CreatePrimaryIpBodyFixture::reader()];
        yield 'CreatePrimaryIpResponse201' => [
            CreatePrimaryIpResponse201Fixture::build(),
            CreatePrimaryIpResponse201Fixture::reader(),
        ];
        yield 'UpdatePrimaryIpBody' => [UpdatePrimaryIpBodyFixture::build(), UpdatePrimaryIpBodyFixture::reader()];
        yield 'AssignPrimaryIpBody' => [AssignPrimaryIpBodyFixture::build(), AssignPrimaryIpBodyFixture::reader()];
        yield 'ChangePrimaryIpDnsPtrBody' => [
            ChangePrimaryIpDnsPtrBodyFixture::build(),
            ChangePrimaryIpDnsPtrBodyFixture::reader(),
        ];
        yield 'ChangePrimaryIpProtectionBody' => [
            ChangePrimaryIpProtectionBodyFixture::build(),
            ChangePrimaryIpProtectionBodyFixture::reader(),
        ];
        yield 'ListServerTypesResponse200' => [
            ListServerTypesResponse200Fixture::build(),
            ListServerTypesResponse200Fixture::reader(),
        ];
        yield 'GetServerTypeResponse200' => [
            GetServerTypeResponse200Fixture::build(),
            GetServerTypeResponse200Fixture::reader(),
        ];
        yield 'ListServersResponse200' => [
            ListServersResponse200Fixture::build(),
            ListServersResponse200Fixture::reader(),
        ];
        yield 'CreateServerBody' => [CreateServerBodyFixture::build(), CreateServerBodyFixture::reader()];
        yield 'CreateServerBodyFirewallsItem' => [
            CreateServerBodyFirewallsItemFixture::build(),
            CreateServerBodyFirewallsItemFixture::reader(),
        ];
        yield 'CreateServerBodyPublicNet' => [
            CreateServerBodyPublicNetFixture::build(),
            CreateServerBodyPublicNetFixture::reader(),
        ];
        yield 'CreateServerResponse201' => [
            CreateServerResponse201Fixture::build(),
            CreateServerResponse201Fixture::reader(),
        ];
        yield 'UpdateServerBody' => [UpdateServerBodyFixture::build(), UpdateServerBodyFixture::reader()];
        yield 'AddServerToPlacementGroupBody' => [
            AddServerToPlacementGroupBodyFixture::build(),
            AddServerToPlacementGroupBodyFixture::reader(),
        ];
        yield 'AttachServerIsoBody' => [AttachServerIsoBodyFixture::build(), AttachServerIsoBodyFixture::reader()];
        yield 'AttachServerToNetworkBody' => [
            AttachServerToNetworkBodyFixture::build(),
            AttachServerToNetworkBodyFixture::reader(),
        ];
        yield 'ChangeServerAliasIpsBody' => [
            ChangeServerAliasIpsBodyFixture::build(),
            ChangeServerAliasIpsBodyFixture::reader(),
        ];
        yield 'ChangeServerDnsPtrBody' => [
            ChangeServerDnsPtrBodyFixture::build(),
            ChangeServerDnsPtrBodyFixture::reader(),
        ];
        yield 'ChangeServerProtectionBody' => [
            ChangeServerProtectionBodyFixture::build(),
            ChangeServerProtectionBodyFixture::reader(),
        ];
        yield 'ChangeServerTypeBody' => [ChangeServerTypeBodyFixture::build(), ChangeServerTypeBodyFixture::reader()];
        yield 'CreateServerImageBody' => [
            CreateServerImageBodyFixture::build(),
            CreateServerImageBodyFixture::reader(),
        ];
        yield 'CreateServerImageResponse201' => [
            CreateServerImageResponse201Fixture::build(),
            CreateServerImageResponse201Fixture::reader(),
        ];
        yield 'DetachServerFromNetworkBody' => [
            DetachServerFromNetworkBodyFixture::build(),
            DetachServerFromNetworkBodyFixture::reader(),
        ];
        yield 'EnableServerRescueBody' => [
            EnableServerRescueBodyFixture::build(),
            EnableServerRescueBodyFixture::reader(),
        ];
        yield 'RebuildServerBody' => [RebuildServerBodyFixture::build(), RebuildServerBodyFixture::reader()];
        yield 'RebuildServerResponse201' => [
            RebuildServerResponse201Fixture::build(),
            RebuildServerResponse201Fixture::reader(),
        ];
        yield 'RequestServerConsoleResponse201' => [
            RequestServerConsoleResponse201Fixture::build(),
            RequestServerConsoleResponse201Fixture::reader(),
        ];
        yield 'ListSshKeysResponse200' => [
            ListSshKeysResponse200Fixture::build(),
            ListSshKeysResponse200Fixture::reader(),
        ];
        yield 'CreateSshKeyBody' => [CreateSshKeyBodyFixture::build(), CreateSshKeyBodyFixture::reader()];
        yield 'UpdateSshKeyBody' => [UpdateSshKeyBodyFixture::build(), UpdateSshKeyBodyFixture::reader()];
        yield 'ListVolumesResponse200' => [
            ListVolumesResponse200Fixture::build(),
            ListVolumesResponse200Fixture::reader(),
        ];
        yield 'CreateVolumeBody' => [CreateVolumeBodyFixture::build(), CreateVolumeBodyFixture::reader()];
        yield 'CreateVolumeResponse201' => [
            CreateVolumeResponse201Fixture::build(),
            CreateVolumeResponse201Fixture::reader(),
        ];
        yield 'UpdateVolumeBody' => [UpdateVolumeBodyFixture::build(), UpdateVolumeBodyFixture::reader()];
        yield 'AttachVolumeBody' => [AttachVolumeBodyFixture::build(), AttachVolumeBodyFixture::reader()];
        yield 'ResizeVolumeBody' => [ResizeVolumeBodyFixture::build(), ResizeVolumeBodyFixture::reader()];
        yield 'ListZonesResponse200' => [ListZonesResponse200Fixture::build(), ListZonesResponse200Fixture::reader()];
        yield 'CreateZoneBody' => [CreateZoneBodyFixture::build(), CreateZoneBodyFixture::reader()];
        yield 'CreateZoneResponse201' => [
            CreateZoneResponse201Fixture::build(),
            CreateZoneResponse201Fixture::reader(),
        ];
        yield 'UpdateZoneBody' => [UpdateZoneBodyFixture::build(), UpdateZoneBodyFixture::reader()];
        yield 'ChangeZonePrimaryNameserversBody' => [
            ChangeZonePrimaryNameserversBodyFixture::build(),
            ChangeZonePrimaryNameserversBodyFixture::reader(),
        ];
        yield 'ChangeZoneTtlBody' => [ChangeZoneTtlBodyFixture::build(), ChangeZoneTtlBodyFixture::reader()];
        yield 'ListZoneRrsetsResponse200' => [
            ListZoneRrsetsResponse200Fixture::build(),
            ListZoneRrsetsResponse200Fixture::reader(),
        ];
        yield 'ListZoneRrsetsResponse200Meta' => [
            ListZoneRrsetsResponse200MetaFixture::build(),
            ListZoneRrsetsResponse200MetaFixture::reader(),
        ];
        yield 'ListZoneRrsetsResponse200MetaPagination' => [
            ListZoneRrsetsResponse200MetaPaginationFixture::build(),
            ListZoneRrsetsResponse200MetaPaginationFixture::reader(),
        ];
        yield 'CreateZoneRrsetResponse201' => [
            CreateZoneRrsetResponse201Fixture::build(),
            CreateZoneRrsetResponse201Fixture::reader(),
        ];
        yield 'UpdateZoneRrsetBody' => [UpdateZoneRrsetBodyFixture::build(), UpdateZoneRrsetBodyFixture::reader()];
        yield 'ChangeZoneRrsetTtlBody' => [
            ChangeZoneRrsetTtlBodyFixture::build(),
            ChangeZoneRrsetTtlBodyFixture::reader(),
        ];
        yield 'AddZoneRrsetRecordsBody' => [
            AddZoneRrsetRecordsBodyFixture::build(),
            AddZoneRrsetRecordsBodyFixture::reader(),
        ];
        yield 'UpdateZoneRrsetRecordsBody' => [
            UpdateZoneRrsetRecordsBodyFixture::build(),
            UpdateZoneRrsetRecordsBodyFixture::reader(),
        ];
        yield 'UpdateZoneRrsetRecordsBodyRecordsItem' => [
            UpdateZoneRrsetRecordsBodyRecordsItemFixture::build(),
            UpdateZoneRrsetRecordsBodyRecordsItemFixture::reader(),
        ];
        yield 'ListStorageBoxesResponse200' => [
            ListStorageBoxesResponse200Fixture::build(),
            ListStorageBoxesResponse200Fixture::reader(),
        ];
        yield 'CreateStorageBoxBody' => [CreateStorageBoxBodyFixture::build(), CreateStorageBoxBodyFixture::reader()];
        yield 'CreateStorageBoxBodyAccessSettings' => [
            CreateStorageBoxBodyAccessSettingsFixture::build(),
            CreateStorageBoxBodyAccessSettingsFixture::reader(),
        ];
        yield 'CreateStorageBoxResponse201' => [
            CreateStorageBoxResponse201Fixture::build(),
            CreateStorageBoxResponse201Fixture::reader(),
        ];
        yield 'UpdateStorageBoxBody' => [UpdateStorageBoxBodyFixture::build(), UpdateStorageBoxBodyFixture::reader()];
        yield 'ListStorageBoxFoldersResponse200' => [
            ListStorageBoxFoldersResponse200Fixture::build(),
            ListStorageBoxFoldersResponse200Fixture::reader(),
        ];
        yield 'ChangeStorageBoxTypeBody' => [
            ChangeStorageBoxTypeBodyFixture::build(),
            ChangeStorageBoxTypeBodyFixture::reader(),
        ];
        yield 'UpdateStorageBoxAccessSettingsBody' => [
            UpdateStorageBoxAccessSettingsBodyFixture::build(),
            UpdateStorageBoxAccessSettingsBodyFixture::reader(),
        ];
        yield 'RollbackStorageBoxSnapshotBody' => [
            RollbackStorageBoxSnapshotBodyFixture::build(),
            RollbackStorageBoxSnapshotBodyFixture::reader(),
        ];
        yield 'EnableStorageBoxSnapshotPlanBody' => [
            EnableStorageBoxSnapshotPlanBodyFixture::build(),
            EnableStorageBoxSnapshotPlanBodyFixture::reader(),
        ];
        yield 'ListStorageBoxSubaccountsResponse200' => [
            ListStorageBoxSubaccountsResponse200Fixture::build(),
            ListStorageBoxSubaccountsResponse200Fixture::reader(),
        ];
        yield 'CreateStorageBoxSubaccountBody' => [
            CreateStorageBoxSubaccountBodyFixture::build(),
            CreateStorageBoxSubaccountBodyFixture::reader(),
        ];
        yield 'CreateStorageBoxSubaccountBodyAccessSettings' => [
            CreateStorageBoxSubaccountBodyAccessSettingsFixture::build(),
            CreateStorageBoxSubaccountBodyAccessSettingsFixture::reader(),
        ];
        yield 'CreateStorageBoxSubaccountResponse201' => [
            CreateStorageBoxSubaccountResponse201Fixture::build(),
            CreateStorageBoxSubaccountResponse201Fixture::reader(),
        ];
        yield 'CreateStorageBoxSubaccountResponse201Subaccount' => [
            CreateStorageBoxSubaccountResponse201SubaccountFixture::build(),
            CreateStorageBoxSubaccountResponse201SubaccountFixture::reader(),
        ];
        yield 'UpdateStorageBoxSubaccountBody' => [
            UpdateStorageBoxSubaccountBodyFixture::build(),
            UpdateStorageBoxSubaccountBodyFixture::reader(),
        ];
        yield 'ChangeStorageBoxSubaccountHomeDirectoryBody' => [
            ChangeStorageBoxSubaccountHomeDirectoryBodyFixture::build(),
            ChangeStorageBoxSubaccountHomeDirectoryBodyFixture::reader(),
        ];
        yield 'UpdateStorageBoxSubaccountAccessSettingsBody' => [
            UpdateStorageBoxSubaccountAccessSettingsBodyFixture::build(),
            UpdateStorageBoxSubaccountAccessSettingsBodyFixture::reader(),
        ];
        yield 'ListStorageBoxSnapshotsResponse200' => [
            ListStorageBoxSnapshotsResponse200Fixture::build(),
            ListStorageBoxSnapshotsResponse200Fixture::reader(),
        ];
        yield 'CreateStorageBoxSnapshotBody' => [
            CreateStorageBoxSnapshotBodyFixture::build(),
            CreateStorageBoxSnapshotBodyFixture::reader(),
        ];
        yield 'CreateStorageBoxSnapshotResponse201' => [
            CreateStorageBoxSnapshotResponse201Fixture::build(),
            CreateStorageBoxSnapshotResponse201Fixture::reader(),
        ];
        yield 'CreateStorageBoxSnapshotResponse201Snapshot' => [
            CreateStorageBoxSnapshotResponse201SnapshotFixture::build(),
            CreateStorageBoxSnapshotResponse201SnapshotFixture::reader(),
        ];
        yield 'UpdateStorageBoxSnapshotBody' => [
            UpdateStorageBoxSnapshotBodyFixture::build(),
            UpdateStorageBoxSnapshotBodyFixture::reader(),
        ];
        yield 'ListStorageBoxTypesResponse200' => [
            ListStorageBoxTypesResponse200Fixture::build(),
            ListStorageBoxTypesResponse200Fixture::reader(),
        ];
        yield 'GetStorageBoxTypeResponse200' => [
            GetStorageBoxTypeResponse200Fixture::build(),
            GetStorageBoxTypeResponse200Fixture::reader(),
        ];
    }

    /**
     * Each model with the wire names its document must carry.
     *
     * @return iterable<string, array{SelfNormalizingModel, callable(array<int|string, mixed>): SelfNormalizingModel, list<string>}>
     */
    public static function documentsMissingARequiredProperty(): iterable
    {
        yield 'ServiceTCP' => [
            ServiceTCPFixture::build(),
            ServiceTCPFixture::reader(),
            ['protocol', 'listen_port', 'destination_port', 'proxyprotocol', 'health_check'],
        ];
        yield 'ServiceHTTPProtocol' => [
            ServiceHTTPProtocolFixture::build(),
            ServiceHTTPProtocolFixture::reader(),
            ['protocol', 'listen_port', 'destination_port', 'proxyprotocol', 'health_check', 'http'],
        ];
        yield 'ServiceHTTPSProtocol' => [
            ServiceHTTPSProtocolFixture::build(),
            ServiceHTTPSProtocolFixture::reader(),
            ['protocol', 'listen_port', 'destination_port', 'proxyprotocol', 'health_check', 'http'],
        ];
        yield 'TargetTypeServer' => [
            TargetTypeServerFixture::build(),
            TargetTypeServerFixture::reader(),
            ['type', 'server', 'health_status', 'use_private_ip'],
        ];
        yield 'TargetTypeLabelSelector' => [
            TargetTypeLabelSelectorFixture::build(),
            TargetTypeLabelSelectorFixture::reader(),
            ['type', 'label_selector', 'targets', 'use_private_ip'],
        ];
        yield 'TargetTypeIP' => [
            TargetTypeIPFixture::build(),
            TargetTypeIPFixture::reader(),
            ['type', 'ip', 'health_status'],
        ];
        yield 'ZonePrimary' => [
            ZonePrimaryFixture::build(),
            ZonePrimaryFixture::reader(),
            [
                'id',
                'name',
                'created',
                'labels',
                'protection',
                'ttl',
                'status',
                'record_count',
                'authoritative_nameservers',
                'registrar',
                'mode',
            ],
        ];
        yield 'ZoneSecondary' => [
            ZoneSecondaryFixture::build(),
            ZoneSecondaryFixture::reader(),
            [
                'id',
                'name',
                'created',
                'labels',
                'protection',
                'ttl',
                'status',
                'record_count',
                'authoritative_nameservers',
                'registrar',
                'mode',
            ],
        ];
        yield 'Action' => [
            ActionFixture::build(),
            ActionFixture::reader(),
            ['id', 'command', 'status', 'started', 'finished', 'progress', 'resources', 'error'],
        ];
        yield 'ActionError' => [ActionErrorFixture::build(), ActionErrorFixture::reader(), ['code', 'message']];
        yield 'ActionListResponse' => [
            ActionListResponseFixture::build(),
            ActionListResponseFixture::reader(),
            ['actions'],
        ];
        yield 'ActionListResponseWithMeta' => [
            ActionListResponseWithMetaFixture::build(),
            ActionListResponseWithMetaFixture::reader(),
            ['actions', 'meta'],
        ];
        yield 'ActionResource' => [ActionResourceFixture::build(), ActionResourceFixture::reader(), ['id', 'type']];
        yield 'ActionResponse' => [ActionResponseFixture::build(), ActionResponseFixture::reader(), ['action']];
        yield 'Certificate' => [
            CertificateFixture::build(),
            CertificateFixture::reader(),
            [
                'id',
                'name',
                'labels',
                'certificate',
                'created',
                'not_valid_before',
                'not_valid_after',
                'domain_names',
                'fingerprint',
                'used_by',
            ],
        ];
        yield 'CertificateUsedByItem' => [
            CertificateUsedByItemFixture::build(),
            CertificateUsedByItemFixture::reader(),
            ['id', 'type'],
        ];
        yield 'CertificateResponse' => [
            CertificateResponseFixture::build(),
            CertificateResponseFixture::reader(),
            ['certificate'],
        ];
        yield 'CreatedFrom' => [CreatedFromFixture::build(), CreatedFromFixture::reader(), ['id', 'name']];
        yield 'Datacenter' => [
            DatacenterFixture::build(),
            DatacenterFixture::reader(),
            ['id', 'name', 'description', 'location', 'server_types'],
        ];
        yield 'DatacenterServerTypes' => [
            DatacenterServerTypesFixture::build(),
            DatacenterServerTypesFixture::reader(),
            ['supported', 'available', 'available_for_migration'],
        ];
        yield 'DeprecationInfo' => [
            DeprecationInfoFixture::build(),
            DeprecationInfoFixture::reader(),
            ['unavailable_after', 'announced'],
        ];
        yield 'DnsPtr' => [DnsPtrFixture::build(), DnsPtrFixture::reader(), ['ip', 'dns_ptr']];
        yield 'ErrorResponse' => [ErrorResponseFixture::build(), ErrorResponseFixture::reader(), ['error']];
        yield 'ErrorResponseError' => [
            ErrorResponseErrorFixture::build(),
            ErrorResponseErrorFixture::reader(),
            ['code', 'message'],
        ];
        yield 'Firewall' => [
            FirewallFixture::build(),
            FirewallFixture::reader(),
            ['id', 'name', 'created', 'rules', 'applied_to'],
        ];
        yield 'FirewallRulesItem' => [
            FirewallRulesItemFixture::build(),
            FirewallRulesItemFixture::reader(),
            ['direction', 'source_ips', 'destination_ips', 'protocol', 'port'],
        ];
        yield 'FirewallAppliedToItem' => [
            FirewallAppliedToItemFixture::build(),
            FirewallAppliedToItemFixture::reader(),
            ['type'],
        ];
        yield 'FirewallAppliedToServer' => [
            FirewallAppliedToServerFixture::build(),
            FirewallAppliedToServerFixture::reader(),
            ['id'],
        ];
        yield 'FirewallResource' => [FirewallResourceFixture::build(), FirewallResourceFixture::reader(), ['type']];
        yield 'FirewallResourceServer' => [
            FirewallResourceServerFixture::build(),
            FirewallResourceServerFixture::reader(),
            ['id'],
        ];
        yield 'FirewallResponse' => [FirewallResponseFixture::build(), FirewallResponseFixture::reader(), ['firewall']];
        yield 'FloatingIp' => [
            FloatingIpFixture::build(),
            FloatingIpFixture::reader(),
            [
                'id',
                'name',
                'description',
                'ip',
                'type',
                'server',
                'dns_ptr',
                'home_location',
                'blocked',
                'protection',
                'labels',
                'created',
            ],
        ];
        yield 'FloatingIpResponse' => [
            FloatingIpResponseFixture::build(),
            FloatingIpResponseFixture::reader(),
            ['floating_ip'],
        ];
        yield 'HealthStatus' => [
            HealthStatusFixture::build(),
            HealthStatusFixture::reader(),
            ['listen_port', 'status'],
        ];
        yield 'Image' => [
            ImageFixture::build(),
            ImageFixture::reader(),
            [
                'id',
                'type',
                'status',
                'name',
                'description',
                'image_size',
                'disk_size',
                'created',
                'created_from',
                'bound_to',
                'os_flavor',
                'os_version',
                'protection',
                'deprecated',
                'deprecation',
                'deleted',
                'labels',
                'architecture',
            ],
        ];
        yield 'ImageResponse' => [ImageResponseFixture::build(), ImageResponseFixture::reader(), ['image']];
        yield 'Iso' => [
            IsoFixture::build(),
            IsoFixture::reader(),
            ['id', 'name', 'description', 'type', 'deprecation', 'architecture'],
        ];
        yield 'LabelSelector' => [LabelSelectorFixture::build(), LabelSelectorFixture::reader(), ['selector']];
        yield 'ListMeta' => [ListMetaFixture::build(), ListMetaFixture::reader(), ['pagination']];
        yield 'ListMetaPagination' => [
            ListMetaPaginationFixture::build(),
            ListMetaPaginationFixture::reader(),
            ['page', 'per_page', 'previous_page', 'next_page', 'last_page', 'total_entries'],
        ];
        yield 'LoadBalancer' => [
            LoadBalancerFixture::build(),
            LoadBalancerFixture::reader(),
            [
                'id',
                'name',
                'public_net',
                'private_net',
                'location',
                'load_balancer_type',
                'protection',
                'labels',
                'created',
                'services',
                'targets',
                'algorithm',
                'outgoing_traffic',
                'ingoing_traffic',
                'included_traffic',
            ],
        ];
        yield 'LoadBalancerPublicNet' => [
            LoadBalancerPublicNetFixture::build(),
            LoadBalancerPublicNetFixture::reader(),
            ['enabled', 'ipv4', 'ipv6'],
        ];
        yield 'LoadBalancerPrivateNetItem' => [
            LoadBalancerPrivateNetItemFixture::build(),
            LoadBalancerPrivateNetItemFixture::reader(),
            ['network', 'ip'],
        ];
        yield 'LoadBalancerAlgorithm2' => [
            LoadBalancerAlgorithm2Fixture::build(),
            LoadBalancerAlgorithm2Fixture::reader(),
            ['type'],
        ];
        yield 'LoadBalancerAlgorithm' => [
            LoadBalancerAlgorithmFixture::build(),
            LoadBalancerAlgorithmFixture::reader(),
            ['type'],
        ];
        yield 'LoadBalancerPublicIp' => [
            LoadBalancerPublicIpFixture::build(),
            LoadBalancerPublicIpFixture::reader(),
            ['id', 'ip', 'blocked', 'dns_ptr'],
        ];
        yield 'LoadBalancerResponse' => [
            LoadBalancerResponseFixture::build(),
            LoadBalancerResponseFixture::reader(),
            ['load_balancer'],
        ];
        yield 'LoadBalancerServiceHealthCheck' => [
            LoadBalancerServiceHealthCheckFixture::build(),
            LoadBalancerServiceHealthCheckFixture::reader(),
            ['protocol', 'port', 'interval', 'timeout', 'retries'],
        ];
        yield 'LoadBalancerServiceBase' => [
            LoadBalancerServiceBaseFixture::build(),
            LoadBalancerServiceBaseFixture::reader(),
            ['protocol', 'listen_port', 'destination_port', 'proxyprotocol', 'health_check'],
        ];
        yield 'LoadBalancerServiceBaseHealthCheck' => [
            LoadBalancerServiceBaseHealthCheckFixture::build(),
            LoadBalancerServiceBaseHealthCheckFixture::reader(),
            ['protocol', 'port', 'interval', 'timeout', 'retries'],
        ];
        yield 'LoadBalancerServiceBaseHealthCheckHttp' => [
            LoadBalancerServiceBaseHealthCheckHttpFixture::build(),
            LoadBalancerServiceBaseHealthCheckHttpFixture::reader(),
            ['domain', 'path'],
        ];
        yield 'LoadBalancerServiceHTTPProtocolProperties' => [
            LoadBalancerServiceHTTPProtocolPropertiesFixture::build(),
            LoadBalancerServiceHTTPProtocolPropertiesFixture::reader(),
            ['http'],
        ];
        yield 'LoadBalancerServiceHTTPProtocolPropertiesHttp' => [
            LoadBalancerServiceHTTPProtocolPropertiesHttpFixture::build(),
            LoadBalancerServiceHTTPProtocolPropertiesHttpFixture::reader(),
            ['cookie_name', 'cookie_lifetime', 'timeout_idle', 'sticky_sessions'],
        ];
        yield 'LoadBalancerServiceHTTPSProtocolProperties' => [
            LoadBalancerServiceHTTPSProtocolPropertiesFixture::build(),
            LoadBalancerServiceHTTPSProtocolPropertiesFixture::reader(),
            ['http'],
        ];
        yield 'LoadBalancerServiceHTTPSProtocolPropertiesHttp' => [
            LoadBalancerServiceHTTPSProtocolPropertiesHttpFixture::build(),
            LoadBalancerServiceHTTPSProtocolPropertiesHttpFixture::reader(),
            ['cookie_name', 'cookie_lifetime', 'timeout_idle', 'certificates', 'redirect_http', 'sticky_sessions'],
        ];
        yield 'LoadBalancerTarget' => [
            LoadBalancerTargetFixture::build(),
            LoadBalancerTargetFixture::reader(),
            ['type'],
        ];
        yield 'LoadBalancerTargetIP' => [
            LoadBalancerTargetIPFixture::build(),
            LoadBalancerTargetIPFixture::reader(),
            ['ip'],
        ];
        yield 'LoadBalancerTargetLabelSelector' => [
            LoadBalancerTargetLabelSelectorFixture::build(),
            LoadBalancerTargetLabelSelectorFixture::reader(),
            ['selector'],
        ];
        yield 'LoadBalancerTargetServer' => [
            LoadBalancerTargetServerFixture::build(),
            LoadBalancerTargetServerFixture::reader(),
            ['id', 'ip'],
        ];
        yield 'LoadBalancerTargetServerRequest' => [
            LoadBalancerTargetServerRequestFixture::build(),
            LoadBalancerTargetServerRequestFixture::reader(),
            ['id'],
        ];
        yield 'LoadBalancerTargetTypeBase' => [
            LoadBalancerTargetTypeBaseFixture::build(),
            LoadBalancerTargetTypeBaseFixture::reader(),
            ['type'],
        ];
        yield 'LoadBalancerTargetTypeIPProperties' => [
            LoadBalancerTargetTypeIPPropertiesFixture::build(),
            LoadBalancerTargetTypeIPPropertiesFixture::reader(),
            ['ip', 'health_status'],
        ];
        yield 'LoadBalancerTargetTypeLabelSelectorProperties' => [
            LoadBalancerTargetTypeLabelSelectorPropertiesFixture::build(),
            LoadBalancerTargetTypeLabelSelectorPropertiesFixture::reader(),
            ['label_selector', 'targets', 'use_private_ip'],
        ];
        yield 'LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItem' => [
            LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItemFixture::build(),
            LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItemFixture::reader(),
            ['type', 'server', 'health_status', 'use_private_ip'],
        ];
        yield 'LoadBalancerTargetTypeServerProperties' => [
            LoadBalancerTargetTypeServerPropertiesFixture::build(),
            LoadBalancerTargetTypeServerPropertiesFixture::reader(),
            ['server', 'health_status', 'use_private_ip'],
        ];
        yield 'LoadBalancerType' => [
            LoadBalancerTypeFixture::build(),
            LoadBalancerTypeFixture::reader(),
            [
                'id',
                'name',
                'description',
                'max_connections',
                'max_services',
                'max_targets',
                'max_assigned_certificates',
                'deprecated',
                'deprecation',
                'prices',
            ],
        ];
        yield 'Location' => [
            LocationFixture::build(),
            LocationFixture::reader(),
            ['id', 'name', 'description', 'country', 'city', 'latitude', 'longitude', 'network_zone'],
        ];
        yield 'LocationPrice' => [
            LocationPriceFixture::build(),
            LocationPriceFixture::reader(),
            ['location', 'price_hourly', 'price_monthly', 'included_traffic', 'price_per_tb_traffic'],
        ];
        yield 'MetricsResponse' => [MetricsResponseFixture::build(), MetricsResponseFixture::reader(), ['metrics']];
        yield 'MetricsResponseMetrics' => [
            MetricsResponseMetricsFixture::build(),
            MetricsResponseMetricsFixture::reader(),
            ['start', 'end', 'step', 'time_series'],
        ];
        yield 'MetricsResponseMetricsTimeSeriesItem' => [
            MetricsResponseMetricsTimeSeriesItemFixture::build(),
            MetricsResponseMetricsTimeSeriesItemFixture::reader(),
            ['values'],
        ];
        yield 'Network' => [
            NetworkFixture::build(),
            NetworkFixture::reader(),
            [
                'id',
                'name',
                'ip_range',
                'subnets',
                'routes',
                'servers',
                'protection',
                'labels',
                'created',
                'expose_routes_to_vswitch',
            ],
        ];
        yield 'NetworkSubnetsItem' => [
            NetworkSubnetsItemFixture::build(),
            NetworkSubnetsItemFixture::reader(),
            ['type', 'network_zone', 'gateway'],
        ];
        yield 'NetworkResponse' => [NetworkResponseFixture::build(), NetworkResponseFixture::reader(), ['network']];
        yield 'PlacementGroup' => [
            PlacementGroupFixture::build(),
            PlacementGroupFixture::reader(),
            ['id', 'name', 'labels', 'type', 'created', 'servers'],
        ];
        yield 'PlacementGroupResponse' => [
            PlacementGroupResponseFixture::build(),
            PlacementGroupResponseFixture::reader(),
            ['placement_group'],
        ];
        yield 'Price' => [PriceFixture::build(), PriceFixture::reader(), ['net', 'gross']];
        yield 'PricePerGbMonth' => [
            PricePerGbMonthFixture::build(),
            PricePerGbMonthFixture::reader(),
            ['price_per_gb_month'],
        ];
        yield 'PrimaryIP' => [
            PrimaryIPFixture::build(),
            PrimaryIPFixture::reader(),
            [
                'id',
                'name',
                'labels',
                'created',
                'blocked',
                'location',
                'ip',
                'dns_ptr',
                'protection',
                'type',
                'auto_delete',
                'assignee_type',
                'assignee_id',
            ],
        ];
        yield 'PrimaryIPResponse' => [
            PrimaryIPResponseFixture::build(),
            PrimaryIPResponseFixture::reader(),
            ['primary_ip'],
        ];
        yield 'PrimaryZoneProperties' => [
            PrimaryZonePropertiesFixture::build(),
            PrimaryZonePropertiesFixture::reader(),
            ['mode'],
        ];
        yield 'Protection' => [ProtectionFixture::build(), ProtectionFixture::reader(), ['delete']];
        yield 'RRSet' => [
            RRSetFixture::build(),
            RRSetFixture::reader(),
            ['id', 'name', 'type', 'ttl', 'labels', 'protection', 'records', 'zone'],
        ];
        yield 'RRSetProtection' => [RRSetProtectionFixture::build(), RRSetProtectionFixture::reader(), ['change']];
        yield 'RRSetRecordsRequest' => [
            RRSetRecordsRequestFixture::build(),
            RRSetRecordsRequestFixture::reader(),
            ['records'],
        ];
        yield 'RRSetRequest' => [
            RRSetRequestFixture::build(),
            RRSetRequestFixture::reader(),
            ['name', 'type', 'records'],
        ];
        yield 'Record' => [RecordFixture::build(), RecordFixture::reader(), ['value']];
        yield 'RootPasswordResponse' => [
            RootPasswordResponseFixture::build(),
            RootPasswordResponseFixture::reader(),
            ['root_password', 'action'],
        ];
        yield 'Route' => [RouteFixture::build(), RouteFixture::reader(), ['destination', 'gateway']];
        yield 'RrsetResponse' => [RrsetResponseFixture::build(), RrsetResponseFixture::reader(), ['rrset']];
        yield 'Rule' => [RuleFixture::build(), RuleFixture::reader(), ['direction', 'protocol']];
        yield 'SecondaryZoneProperties' => [
            SecondaryZonePropertiesFixture::build(),
            SecondaryZonePropertiesFixture::reader(),
            ['mode'],
        ];
        yield 'Server' => [
            ServerFixture::build(),
            ServerFixture::reader(),
            [
                'id',
                'name',
                'status',
                'created',
                'public_net',
                'private_net',
                'server_type',
                'location',
                'image',
                'iso',
                'rescue_enabled',
                'locked',
                'backup_window',
                'outgoing_traffic',
                'ingoing_traffic',
                'included_traffic',
                'protection',
                'labels',
                'primary_disk_size',
            ],
        ];
        yield 'ServerPublicNet' => [
            ServerPublicNetFixture::build(),
            ServerPublicNetFixture::reader(),
            ['ipv4', 'ipv6', 'floating_ips'],
        ];
        yield 'ServerPublicNetIpv4' => [
            ServerPublicNetIpv4Fixture::build(),
            ServerPublicNetIpv4Fixture::reader(),
            ['ip', 'blocked', 'dns_ptr'],
        ];
        yield 'ServerPublicNetIpv6' => [
            ServerPublicNetIpv6Fixture::build(),
            ServerPublicNetIpv6Fixture::reader(),
            ['ip', 'blocked', 'dns_ptr'],
        ];
        yield 'ServerProtection' => [
            ServerProtectionFixture::build(),
            ServerProtectionFixture::reader(),
            ['delete', 'rebuild'],
        ];
        yield 'ServerResponse' => [ServerResponseFixture::build(), ServerResponseFixture::reader(), ['server']];
        yield 'ServerType' => [
            ServerTypeFixture::build(),
            ServerTypeFixture::reader(),
            [
                'id',
                'name',
                'description',
                'cores',
                'memory',
                'disk',
                'deprecated',
                'prices',
                'storage_type',
                'cpu_type',
                'architecture',
                'locations',
            ],
        ];
        yield 'ServerTypeLocationsItem' => [
            ServerTypeLocationsItemFixture::build(),
            ServerTypeLocationsItemFixture::reader(),
            ['id', 'name', 'deprecation', 'recommended', 'available'],
        ];
        yield 'SshKey' => [
            SshKeyFixture::build(),
            SshKeyFixture::reader(),
            ['id', 'name', 'fingerprint', 'public_key', 'labels', 'created'],
        ];
        yield 'SshKeyResponse' => [SshKeyResponseFixture::build(), SshKeyResponseFixture::reader(), ['ssh_key']];
        yield 'TypePricing' => [TypePricingFixture::build(), TypePricingFixture::reader(), ['id', 'name', 'prices']];
        yield 'Volume' => [
            VolumeFixture::build(),
            VolumeFixture::reader(),
            [
                'id',
                'created',
                'name',
                'server',
                'location',
                'size',
                'linux_device',
                'protection',
                'labels',
                'status',
                'format',
            ],
        ];
        yield 'VolumeResponse' => [VolumeResponseFixture::build(), VolumeResponseFixture::reader(), ['volume']];
        yield 'ZoneBase' => [
            ZoneBaseFixture::build(),
            ZoneBaseFixture::reader(),
            [
                'id',
                'name',
                'created',
                'labels',
                'protection',
                'ttl',
                'status',
                'record_count',
                'authoritative_nameservers',
                'registrar',
            ],
        ];
        yield 'ZoneBaseAuthoritativeNameservers' => [
            ZoneBaseAuthoritativeNameserversFixture::build(),
            ZoneBaseAuthoritativeNameserversFixture::reader(),
            ['assigned', 'delegated', 'delegation_last_check'],
        ];
        yield 'ZonePrimaryNameserver' => [
            ZonePrimaryNameserverFixture::build(),
            ZonePrimaryNameserverFixture::reader(),
            ['address'],
        ];
        yield 'ZoneResponse' => [ZoneResponseFixture::build(), ZoneResponseFixture::reader(), ['zone']];
        yield 'Zonefile' => [ZonefileFixture::build(), ZonefileFixture::reader(), ['zonefile']];
        yield 'ResetPasswordRequest' => [
            ResetPasswordRequestFixture::build(),
            ResetPasswordRequestFixture::reader(),
            ['password'],
        ];
        yield 'Snapshot' => [
            SnapshotFixture::build(),
            SnapshotFixture::reader(),
            ['storage_box', 'id', 'name', 'description', 'labels', 'stats', 'is_automatic', 'created'],
        ];
        yield 'SnapshotStats' => [
            SnapshotStatsFixture::build(),
            SnapshotStatsFixture::reader(),
            ['size', 'size_filesystem'],
        ];
        yield 'SnapshotResponse' => [SnapshotResponseFixture::build(), SnapshotResponseFixture::reader(), ['snapshot']];
        yield 'StorageBox' => [
            StorageBoxFixture::build(),
            StorageBoxFixture::reader(),
            [
                'id',
                'name',
                'storage_box_type',
                'location',
                'access_settings',
                'snapshot_plan',
                'protection',
                'labels',
                'status',
                'username',
                'server',
                'system',
                'stats',
                'created',
            ],
        ];
        yield 'StorageBoxAccessSettings' => [
            StorageBoxAccessSettingsFixture::build(),
            StorageBoxAccessSettingsFixture::reader(),
            ['reachable_externally', 'samba_enabled', 'ssh_enabled', 'webdav_enabled', 'zfs_enabled'],
        ];
        yield 'StorageBoxSnapshotPlan' => [
            StorageBoxSnapshotPlanFixture::build(),
            StorageBoxSnapshotPlanFixture::reader(),
            ['max_snapshots', 'minute', 'hour', 'day_of_week', 'day_of_month'],
        ];
        yield 'StorageBoxStats' => [
            StorageBoxStatsFixture::build(),
            StorageBoxStatsFixture::reader(),
            ['size', 'size_data', 'size_snapshots'],
        ];
        yield 'StorageBoxResponse' => [
            StorageBoxResponseFixture::build(),
            StorageBoxResponseFixture::reader(),
            ['storage_box'],
        ];
        yield 'StorageBoxType' => [
            StorageBoxTypeFixture::build(),
            StorageBoxTypeFixture::reader(),
            [
                'id',
                'name',
                'description',
                'snapshot_limit',
                'automatic_snapshot_limit',
                'subaccounts_limit',
                'size',
                'prices',
                'deprecation',
            ],
        ];
        yield 'StorageBoxTypePricesItem' => [
            StorageBoxTypePricesItemFixture::build(),
            StorageBoxTypePricesItemFixture::reader(),
            ['location', 'price_hourly', 'price_monthly', 'setup_fee'],
        ];
        yield 'Subaccount' => [
            SubaccountFixture::build(),
            SubaccountFixture::reader(),
            [
                'storage_box',
                'id',
                'name',
                'home_directory',
                'access_settings',
                'description',
                'labels',
                'username',
                'server',
                'created',
            ],
        ];
        yield 'SubaccountAccessSettings' => [
            SubaccountAccessSettingsFixture::build(),
            SubaccountAccessSettingsFixture::reader(),
            ['reachable_externally', 'samba_enabled', 'ssh_enabled', 'webdav_enabled', 'readonly'],
        ];
        yield 'SubaccountResponse' => [
            SubaccountResponseFixture::build(),
            SubaccountResponseFixture::reader(),
            ['subaccount'],
        ];
        yield 'ListCertificatesResponse200' => [
            ListCertificatesResponse200Fixture::build(),
            ListCertificatesResponse200Fixture::reader(),
            ['certificates', 'meta'],
        ];
        yield 'CreateCertificateBody' => [
            CreateCertificateBodyFixture::build(),
            CreateCertificateBodyFixture::reader(),
            ['name'],
        ];
        yield 'CreateCertificateResponse201' => [
            CreateCertificateResponse201Fixture::build(),
            CreateCertificateResponse201Fixture::reader(),
            ['certificate'],
        ];
        yield 'ListDatacentersResponse200' => [
            ListDatacentersResponse200Fixture::build(),
            ListDatacentersResponse200Fixture::reader(),
            ['datacenters', 'recommendation', 'meta'],
        ];
        yield 'GetDatacenterResponse200' => [
            GetDatacenterResponse200Fixture::build(),
            GetDatacenterResponse200Fixture::reader(),
            ['datacenter'],
        ];
        yield 'ListFirewallsResponse200' => [
            ListFirewallsResponse200Fixture::build(),
            ListFirewallsResponse200Fixture::reader(),
            ['firewalls', 'meta'],
        ];
        yield 'CreateFirewallBody' => [
            CreateFirewallBodyFixture::build(),
            CreateFirewallBodyFixture::reader(),
            ['name'],
        ];
        yield 'CreateFirewallResponse201' => [
            CreateFirewallResponse201Fixture::build(),
            CreateFirewallResponse201Fixture::reader(),
            ['firewall'],
        ];
        yield 'ApplyFirewallToResourcesBody' => [
            ApplyFirewallToResourcesBodyFixture::build(),
            ApplyFirewallToResourcesBodyFixture::reader(),
            ['apply_to'],
        ];
        yield 'RemoveFirewallFromResourcesBody' => [
            RemoveFirewallFromResourcesBodyFixture::build(),
            RemoveFirewallFromResourcesBodyFixture::reader(),
            ['remove_from'],
        ];
        yield 'SetFirewallRulesBody' => [
            SetFirewallRulesBodyFixture::build(),
            SetFirewallRulesBodyFixture::reader(),
            ['rules'],
        ];
        yield 'ListFloatingIpsResponse200' => [
            ListFloatingIpsResponse200Fixture::build(),
            ListFloatingIpsResponse200Fixture::reader(),
            ['floating_ips', 'meta'],
        ];
        yield 'CreateFloatingIpBody' => [
            CreateFloatingIpBodyFixture::build(),
            CreateFloatingIpBodyFixture::reader(),
            ['type'],
        ];
        yield 'CreateFloatingIpResponse201' => [
            CreateFloatingIpResponse201Fixture::build(),
            CreateFloatingIpResponse201Fixture::reader(),
            ['floating_ip'],
        ];
        yield 'AssignFloatingIpBody' => [
            AssignFloatingIpBodyFixture::build(),
            AssignFloatingIpBodyFixture::reader(),
            ['server'],
        ];
        yield 'ChangeFloatingIpDnsPtrBody' => [
            ChangeFloatingIpDnsPtrBodyFixture::build(),
            ChangeFloatingIpDnsPtrBodyFixture::reader(),
            ['ip', 'dns_ptr'],
        ];
        yield 'ChangeFloatingIpProtectionBody' => [
            ChangeFloatingIpProtectionBodyFixture::build(),
            ChangeFloatingIpProtectionBodyFixture::reader(),
            ['delete'],
        ];
        yield 'ListImagesResponse200' => [
            ListImagesResponse200Fixture::build(),
            ListImagesResponse200Fixture::reader(),
            ['images', 'meta'],
        ];
        yield 'ListIsosResponse200' => [
            ListIsosResponse200Fixture::build(),
            ListIsosResponse200Fixture::reader(),
            ['isos', 'meta'],
        ];
        yield 'GetIsoResponse200' => [GetIsoResponse200Fixture::build(), GetIsoResponse200Fixture::reader(), ['iso']];
        yield 'ListLoadBalancerTypesResponse200' => [
            ListLoadBalancerTypesResponse200Fixture::build(),
            ListLoadBalancerTypesResponse200Fixture::reader(),
            ['load_balancer_types', 'meta'],
        ];
        yield 'GetLoadBalancerTypeResponse200' => [
            GetLoadBalancerTypeResponse200Fixture::build(),
            GetLoadBalancerTypeResponse200Fixture::reader(),
            ['load_balancer_type'],
        ];
        yield 'ListLoadBalancersResponse200' => [
            ListLoadBalancersResponse200Fixture::build(),
            ListLoadBalancersResponse200Fixture::reader(),
            ['load_balancers', 'meta'],
        ];
        yield 'CreateLoadBalancerBody' => [
            CreateLoadBalancerBodyFixture::build(),
            CreateLoadBalancerBodyFixture::reader(),
            ['name', 'load_balancer_type'],
        ];
        yield 'CreateLoadBalancerBodyTargetsItem' => [
            CreateLoadBalancerBodyTargetsItemFixture::build(),
            CreateLoadBalancerBodyTargetsItemFixture::reader(),
            ['type'],
        ];
        yield 'CreateLoadBalancerResponse201' => [
            CreateLoadBalancerResponse201Fixture::build(),
            CreateLoadBalancerResponse201Fixture::reader(),
            ['load_balancer', 'action'],
        ];
        yield 'AddLoadBalancerServiceBody' => [
            AddLoadBalancerServiceBodyFixture::build(),
            AddLoadBalancerServiceBodyFixture::reader(),
            ['protocol', 'listen_port', 'destination_port', 'proxyprotocol', 'health_check'],
        ];
        yield 'AddLoadBalancerTargetBody' => [
            AddLoadBalancerTargetBodyFixture::build(),
            AddLoadBalancerTargetBodyFixture::reader(),
            ['type'],
        ];
        yield 'AttachLoadBalancerToNetworkBody' => [
            AttachLoadBalancerToNetworkBodyFixture::build(),
            AttachLoadBalancerToNetworkBodyFixture::reader(),
            ['network'],
        ];
        yield 'ChangeLoadBalancerDnsPtrBody' => [
            ChangeLoadBalancerDnsPtrBodyFixture::build(),
            ChangeLoadBalancerDnsPtrBodyFixture::reader(),
            ['ip', 'dns_ptr'],
        ];
        yield 'ChangeLoadBalancerTypeBody' => [
            ChangeLoadBalancerTypeBodyFixture::build(),
            ChangeLoadBalancerTypeBodyFixture::reader(),
            ['load_balancer_type'],
        ];
        yield 'DeleteLoadBalancerServiceBody' => [
            DeleteLoadBalancerServiceBodyFixture::build(),
            DeleteLoadBalancerServiceBodyFixture::reader(),
            ['listen_port'],
        ];
        yield 'DetachLoadBalancerFromNetworkBody' => [
            DetachLoadBalancerFromNetworkBodyFixture::build(),
            DetachLoadBalancerFromNetworkBodyFixture::reader(),
            ['network'],
        ];
        yield 'UpdateLoadBalancerServiceBody' => [
            UpdateLoadBalancerServiceBodyFixture::build(),
            UpdateLoadBalancerServiceBodyFixture::reader(),
            ['listen_port'],
        ];
        yield 'ListLocationsResponse200' => [
            ListLocationsResponse200Fixture::build(),
            ListLocationsResponse200Fixture::reader(),
            ['locations', 'meta'],
        ];
        yield 'GetLocationResponse200' => [
            GetLocationResponse200Fixture::build(),
            GetLocationResponse200Fixture::reader(),
            ['location'],
        ];
        yield 'ListNetworksResponse200' => [
            ListNetworksResponse200Fixture::build(),
            ListNetworksResponse200Fixture::reader(),
            ['networks', 'meta'],
        ];
        yield 'CreateNetworkBody' => [
            CreateNetworkBodyFixture::build(),
            CreateNetworkBodyFixture::reader(),
            ['name', 'ip_range'],
        ];
        yield 'CreateNetworkBodySubnetsItem' => [
            CreateNetworkBodySubnetsItemFixture::build(),
            CreateNetworkBodySubnetsItemFixture::reader(),
            ['type', 'network_zone'],
        ];
        yield 'AddNetworkSubnetBody' => [
            AddNetworkSubnetBodyFixture::build(),
            AddNetworkSubnetBodyFixture::reader(),
            ['type', 'network_zone'],
        ];
        yield 'ChangeNetworkIpRangeBody' => [
            ChangeNetworkIpRangeBodyFixture::build(),
            ChangeNetworkIpRangeBodyFixture::reader(),
            ['ip_range'],
        ];
        yield 'DeleteNetworkSubnetBody' => [
            DeleteNetworkSubnetBodyFixture::build(),
            DeleteNetworkSubnetBodyFixture::reader(),
            ['ip_range'],
        ];
        yield 'ListNetworkMembersResponse200' => [
            ListNetworkMembersResponse200Fixture::build(),
            ListNetworkMembersResponse200Fixture::reader(),
            ['members', 'meta'],
        ];
        yield 'ListNetworkMembersResponse200MembersItem' => [
            ListNetworkMembersResponse200MembersItemFixture::build(),
            ListNetworkMembersResponse200MembersItemFixture::reader(),
            ['type', 'id', 'ip', 'status', 'alias_ips', 'subnet'],
        ];
        yield 'ListPlacementGroupsResponse200' => [
            ListPlacementGroupsResponse200Fixture::build(),
            ListPlacementGroupsResponse200Fixture::reader(),
            ['placement_groups', 'meta'],
        ];
        yield 'CreatePlacementGroupBody' => [
            CreatePlacementGroupBodyFixture::build(),
            CreatePlacementGroupBodyFixture::reader(),
            ['name', 'type'],
        ];
        yield 'CreatePlacementGroupResponse201' => [
            CreatePlacementGroupResponse201Fixture::build(),
            CreatePlacementGroupResponse201Fixture::reader(),
            ['placement_group'],
        ];
        yield 'GetPricingResponse200' => [
            GetPricingResponse200Fixture::build(),
            GetPricingResponse200Fixture::reader(),
            ['pricing'],
        ];
        yield 'GetPricingResponse200Pricing' => [
            GetPricingResponse200PricingFixture::build(),
            GetPricingResponse200PricingFixture::reader(),
            [
                'currency',
                'vat_rate',
                'primary_ips',
                'floating_ips',
                'image',
                'volume',
                'server_backup',
                'server_types',
                'load_balancer_types',
                'floating_ip',
            ],
        ];
        yield 'GetPricingResponse200PricingPrimaryIpsItem' => [
            GetPricingResponse200PricingPrimaryIpsItemFixture::build(),
            GetPricingResponse200PricingPrimaryIpsItemFixture::reader(),
            ['type', 'prices'],
        ];
        yield 'GetPricingResponse200PricingPrimaryIpsItemPricesItem' => [
            GetPricingResponse200PricingPrimaryIpsItemPricesItemFixture::build(),
            GetPricingResponse200PricingPrimaryIpsItemPricesItemFixture::reader(),
            ['location', 'price_hourly', 'price_monthly'],
        ];
        yield 'GetPricingResponse200PricingFloatingIpsItem' => [
            GetPricingResponse200PricingFloatingIpsItemFixture::build(),
            GetPricingResponse200PricingFloatingIpsItemFixture::reader(),
            ['type', 'prices'],
        ];
        yield 'GetPricingResponse200PricingFloatingIpsItemPricesItem' => [
            GetPricingResponse200PricingFloatingIpsItemPricesItemFixture::build(),
            GetPricingResponse200PricingFloatingIpsItemPricesItemFixture::reader(),
            ['location', 'price_monthly'],
        ];
        yield 'GetPricingResponse200PricingServerBackup' => [
            GetPricingResponse200PricingServerBackupFixture::build(),
            GetPricingResponse200PricingServerBackupFixture::reader(),
            ['percentage'],
        ];
        yield 'GetPricingResponse200PricingFloatingIp' => [
            GetPricingResponse200PricingFloatingIpFixture::build(),
            GetPricingResponse200PricingFloatingIpFixture::reader(),
            ['price_monthly'],
        ];
        yield 'ListPrimaryIpsResponse200' => [
            ListPrimaryIpsResponse200Fixture::build(),
            ListPrimaryIpsResponse200Fixture::reader(),
            ['primary_ips', 'meta'],
        ];
        yield 'CreatePrimaryIpBody' => [
            CreatePrimaryIpBodyFixture::build(),
            CreatePrimaryIpBodyFixture::reader(),
            ['name', 'type'],
        ];
        yield 'CreatePrimaryIpResponse201' => [
            CreatePrimaryIpResponse201Fixture::build(),
            CreatePrimaryIpResponse201Fixture::reader(),
            ['primary_ip'],
        ];
        yield 'AssignPrimaryIpBody' => [
            AssignPrimaryIpBodyFixture::build(),
            AssignPrimaryIpBodyFixture::reader(),
            ['assignee_type', 'assignee_id'],
        ];
        yield 'ChangePrimaryIpDnsPtrBody' => [
            ChangePrimaryIpDnsPtrBodyFixture::build(),
            ChangePrimaryIpDnsPtrBodyFixture::reader(),
            ['ip', 'dns_ptr'],
        ];
        yield 'ChangePrimaryIpProtectionBody' => [
            ChangePrimaryIpProtectionBodyFixture::build(),
            ChangePrimaryIpProtectionBodyFixture::reader(),
            ['delete'],
        ];
        yield 'ListServerTypesResponse200' => [
            ListServerTypesResponse200Fixture::build(),
            ListServerTypesResponse200Fixture::reader(),
            ['server_types', 'meta'],
        ];
        yield 'GetServerTypeResponse200' => [
            GetServerTypeResponse200Fixture::build(),
            GetServerTypeResponse200Fixture::reader(),
            ['server_type'],
        ];
        yield 'ListServersResponse200' => [
            ListServersResponse200Fixture::build(),
            ListServersResponse200Fixture::reader(),
            ['servers', 'meta'],
        ];
        yield 'CreateServerBody' => [
            CreateServerBodyFixture::build(),
            CreateServerBodyFixture::reader(),
            ['name', 'server_type', 'image'],
        ];
        yield 'CreateServerBodyFirewallsItem' => [
            CreateServerBodyFirewallsItemFixture::build(),
            CreateServerBodyFirewallsItemFixture::reader(),
            ['firewall'],
        ];
        yield 'CreateServerResponse201' => [
            CreateServerResponse201Fixture::build(),
            CreateServerResponse201Fixture::reader(),
            ['server', 'action', 'next_actions', 'root_password'],
        ];
        yield 'AddServerToPlacementGroupBody' => [
            AddServerToPlacementGroupBodyFixture::build(),
            AddServerToPlacementGroupBodyFixture::reader(),
            ['placement_group'],
        ];
        yield 'AttachServerIsoBody' => [
            AttachServerIsoBodyFixture::build(),
            AttachServerIsoBodyFixture::reader(),
            ['iso'],
        ];
        yield 'AttachServerToNetworkBody' => [
            AttachServerToNetworkBodyFixture::build(),
            AttachServerToNetworkBodyFixture::reader(),
            ['network'],
        ];
        yield 'ChangeServerAliasIpsBody' => [
            ChangeServerAliasIpsBodyFixture::build(),
            ChangeServerAliasIpsBodyFixture::reader(),
            ['network', 'alias_ips'],
        ];
        yield 'ChangeServerDnsPtrBody' => [
            ChangeServerDnsPtrBodyFixture::build(),
            ChangeServerDnsPtrBodyFixture::reader(),
            ['ip', 'dns_ptr'],
        ];
        yield 'ChangeServerTypeBody' => [
            ChangeServerTypeBodyFixture::build(),
            ChangeServerTypeBodyFixture::reader(),
            ['upgrade_disk', 'server_type'],
        ];
        yield 'CreateServerImageResponse201' => [
            CreateServerImageResponse201Fixture::build(),
            CreateServerImageResponse201Fixture::reader(),
            ['image', 'action'],
        ];
        yield 'DetachServerFromNetworkBody' => [
            DetachServerFromNetworkBodyFixture::build(),
            DetachServerFromNetworkBodyFixture::reader(),
            ['network'],
        ];
        yield 'RebuildServerBody' => [RebuildServerBodyFixture::build(), RebuildServerBodyFixture::reader(), ['image']];
        yield 'RebuildServerResponse201' => [
            RebuildServerResponse201Fixture::build(),
            RebuildServerResponse201Fixture::reader(),
            ['action'],
        ];
        yield 'RequestServerConsoleResponse201' => [
            RequestServerConsoleResponse201Fixture::build(),
            RequestServerConsoleResponse201Fixture::reader(),
            ['wss_url', 'password', 'action'],
        ];
        yield 'ListSshKeysResponse200' => [
            ListSshKeysResponse200Fixture::build(),
            ListSshKeysResponse200Fixture::reader(),
            ['ssh_keys', 'meta'],
        ];
        yield 'CreateSshKeyBody' => [
            CreateSshKeyBodyFixture::build(),
            CreateSshKeyBodyFixture::reader(),
            ['name', 'public_key'],
        ];
        yield 'ListVolumesResponse200' => [
            ListVolumesResponse200Fixture::build(),
            ListVolumesResponse200Fixture::reader(),
            ['volumes', 'meta'],
        ];
        yield 'CreateVolumeBody' => [
            CreateVolumeBodyFixture::build(),
            CreateVolumeBodyFixture::reader(),
            ['size', 'name'],
        ];
        yield 'CreateVolumeResponse201' => [
            CreateVolumeResponse201Fixture::build(),
            CreateVolumeResponse201Fixture::reader(),
            ['volume', 'action', 'next_actions'],
        ];
        yield 'AttachVolumeBody' => [AttachVolumeBodyFixture::build(), AttachVolumeBodyFixture::reader(), ['server']];
        yield 'ResizeVolumeBody' => [ResizeVolumeBodyFixture::build(), ResizeVolumeBodyFixture::reader(), ['size']];
        yield 'ListZonesResponse200' => [
            ListZonesResponse200Fixture::build(),
            ListZonesResponse200Fixture::reader(),
            ['zones', 'meta'],
        ];
        yield 'CreateZoneBody' => [CreateZoneBodyFixture::build(), CreateZoneBodyFixture::reader(), ['name', 'mode']];
        yield 'CreateZoneResponse201' => [
            CreateZoneResponse201Fixture::build(),
            CreateZoneResponse201Fixture::reader(),
            ['zone', 'action'],
        ];
        yield 'ChangeZonePrimaryNameserversBody' => [
            ChangeZonePrimaryNameserversBodyFixture::build(),
            ChangeZonePrimaryNameserversBodyFixture::reader(),
            ['primary_nameservers'],
        ];
        yield 'ChangeZoneTtlBody' => [ChangeZoneTtlBodyFixture::build(), ChangeZoneTtlBodyFixture::reader(), ['ttl']];
        yield 'ListZoneRrsetsResponse200' => [
            ListZoneRrsetsResponse200Fixture::build(),
            ListZoneRrsetsResponse200Fixture::reader(),
            ['rrsets', 'meta'],
        ];
        yield 'ListZoneRrsetsResponse200Meta' => [
            ListZoneRrsetsResponse200MetaFixture::build(),
            ListZoneRrsetsResponse200MetaFixture::reader(),
            ['pagination'],
        ];
        yield 'ListZoneRrsetsResponse200MetaPagination' => [
            ListZoneRrsetsResponse200MetaPaginationFixture::build(),
            ListZoneRrsetsResponse200MetaPaginationFixture::reader(),
            ['page', 'per_page', 'previous_page', 'next_page', 'last_page', 'total_entries'],
        ];
        yield 'CreateZoneRrsetResponse201' => [
            CreateZoneRrsetResponse201Fixture::build(),
            CreateZoneRrsetResponse201Fixture::reader(),
            ['rrset', 'action'],
        ];
        yield 'ChangeZoneRrsetTtlBody' => [
            ChangeZoneRrsetTtlBodyFixture::build(),
            ChangeZoneRrsetTtlBodyFixture::reader(),
            ['ttl'],
        ];
        yield 'AddZoneRrsetRecordsBody' => [
            AddZoneRrsetRecordsBodyFixture::build(),
            AddZoneRrsetRecordsBodyFixture::reader(),
            ['records'],
        ];
        yield 'UpdateZoneRrsetRecordsBody' => [
            UpdateZoneRrsetRecordsBodyFixture::build(),
            UpdateZoneRrsetRecordsBodyFixture::reader(),
            ['records'],
        ];
        yield 'UpdateZoneRrsetRecordsBodyRecordsItem' => [
            UpdateZoneRrsetRecordsBodyRecordsItemFixture::build(),
            UpdateZoneRrsetRecordsBodyRecordsItemFixture::reader(),
            ['value', 'comment'],
        ];
        yield 'ListStorageBoxesResponse200' => [
            ListStorageBoxesResponse200Fixture::build(),
            ListStorageBoxesResponse200Fixture::reader(),
            ['storage_boxes', 'meta'],
        ];
        yield 'CreateStorageBoxBody' => [
            CreateStorageBoxBodyFixture::build(),
            CreateStorageBoxBodyFixture::reader(),
            ['name', 'location', 'storage_box_type', 'password'],
        ];
        yield 'CreateStorageBoxResponse201' => [
            CreateStorageBoxResponse201Fixture::build(),
            CreateStorageBoxResponse201Fixture::reader(),
            ['storage_box', 'action'],
        ];
        yield 'ListStorageBoxFoldersResponse200' => [
            ListStorageBoxFoldersResponse200Fixture::build(),
            ListStorageBoxFoldersResponse200Fixture::reader(),
            ['folders'],
        ];
        yield 'ChangeStorageBoxTypeBody' => [
            ChangeStorageBoxTypeBodyFixture::build(),
            ChangeStorageBoxTypeBodyFixture::reader(),
            ['storage_box_type'],
        ];
        yield 'RollbackStorageBoxSnapshotBody' => [
            RollbackStorageBoxSnapshotBodyFixture::build(),
            RollbackStorageBoxSnapshotBodyFixture::reader(),
            ['snapshot'],
        ];
        yield 'EnableStorageBoxSnapshotPlanBody' => [
            EnableStorageBoxSnapshotPlanBodyFixture::build(),
            EnableStorageBoxSnapshotPlanBodyFixture::reader(),
            ['max_snapshots', 'minute', 'hour'],
        ];
        yield 'ListStorageBoxSubaccountsResponse200' => [
            ListStorageBoxSubaccountsResponse200Fixture::build(),
            ListStorageBoxSubaccountsResponse200Fixture::reader(),
            ['subaccounts'],
        ];
        yield 'CreateStorageBoxSubaccountBody' => [
            CreateStorageBoxSubaccountBodyFixture::build(),
            CreateStorageBoxSubaccountBodyFixture::reader(),
            ['home_directory', 'password'],
        ];
        yield 'CreateStorageBoxSubaccountResponse201' => [
            CreateStorageBoxSubaccountResponse201Fixture::build(),
            CreateStorageBoxSubaccountResponse201Fixture::reader(),
            ['subaccount', 'action'],
        ];
        yield 'CreateStorageBoxSubaccountResponse201Subaccount' => [
            CreateStorageBoxSubaccountResponse201SubaccountFixture::build(),
            CreateStorageBoxSubaccountResponse201SubaccountFixture::reader(),
            ['id', 'storage_box'],
        ];
        yield 'ChangeStorageBoxSubaccountHomeDirectoryBody' => [
            ChangeStorageBoxSubaccountHomeDirectoryBodyFixture::build(),
            ChangeStorageBoxSubaccountHomeDirectoryBodyFixture::reader(),
            ['home_directory'],
        ];
        yield 'ListStorageBoxSnapshotsResponse200' => [
            ListStorageBoxSnapshotsResponse200Fixture::build(),
            ListStorageBoxSnapshotsResponse200Fixture::reader(),
            ['snapshots'],
        ];
        yield 'CreateStorageBoxSnapshotResponse201' => [
            CreateStorageBoxSnapshotResponse201Fixture::build(),
            CreateStorageBoxSnapshotResponse201Fixture::reader(),
            ['snapshot', 'action'],
        ];
        yield 'CreateStorageBoxSnapshotResponse201Snapshot' => [
            CreateStorageBoxSnapshotResponse201SnapshotFixture::build(),
            CreateStorageBoxSnapshotResponse201SnapshotFixture::reader(),
            ['id', 'storage_box'],
        ];
        yield 'ListStorageBoxTypesResponse200' => [
            ListStorageBoxTypesResponse200Fixture::build(),
            ListStorageBoxTypesResponse200Fixture::reader(),
            ['storage_box_types', 'meta'],
        ];
        yield 'GetStorageBoxTypeResponse200' => [
            GetStorageBoxTypeResponse200Fixture::build(),
            GetStorageBoxTypeResponse200Fixture::reader(),
            ['storage_box_type'],
        ];
    }

    /**
     * Each model with, per wire name, a value of a type that property cannot hold.
     *
     * Only properties whose type is a single closed shape appear. A union may legitimately accept
     * what looks like the wrong type, and a schema stating no type accepts anything.
     *
     * @return iterable<string, array{SelfNormalizingModel, callable(array<int|string, mixed>): SelfNormalizingModel, array<array-key, int|string>}>
     */
    public static function documentsWithAMistypedProperty(): iterable
    {
        yield 'ServiceTCP' => [
            ServiceTCPFixture::build(),
            ServiceTCPFixture::reader(),
            [
                'protocol' => 42,
                'listen_port' => 'not-a-number',
                'destination_port' => 'not-a-number',
                'proxyprotocol' => 0,
                'health_check' => 'not-an-object',
            ],
        ];
        yield 'ServiceHTTPProtocol' => [
            ServiceHTTPProtocolFixture::build(),
            ServiceHTTPProtocolFixture::reader(),
            [
                'protocol' => 42,
                'listen_port' => 'not-a-number',
                'destination_port' => 'not-a-number',
                'proxyprotocol' => 0,
                'health_check' => 'not-an-object',
                'http' => 'not-an-object',
            ],
        ];
        yield 'ServiceHTTPSProtocol' => [
            ServiceHTTPSProtocolFixture::build(),
            ServiceHTTPSProtocolFixture::reader(),
            [
                'protocol' => 42,
                'listen_port' => 'not-a-number',
                'destination_port' => 'not-a-number',
                'proxyprotocol' => 0,
                'health_check' => 'not-an-object',
                'http' => 'not-an-object',
            ],
        ];
        yield 'TargetTypeServer' => [
            TargetTypeServerFixture::build(),
            TargetTypeServerFixture::reader(),
            ['type' => 42, 'server' => 'not-an-object', 'health_status' => 'not-an-object', 'use_private_ip' => 0],
        ];
        yield 'TargetTypeLabelSelector' => [
            TargetTypeLabelSelectorFixture::build(),
            TargetTypeLabelSelectorFixture::reader(),
            ['type' => 42, 'label_selector' => 'not-an-object', 'targets' => 'not-an-object', 'use_private_ip' => 0],
        ];
        yield 'TargetTypeIP' => [
            TargetTypeIPFixture::build(),
            TargetTypeIPFixture::reader(),
            ['type' => 42, 'ip' => 'not-an-object', 'health_status' => 'not-an-object'],
        ];
        yield 'ZonePrimary' => [
            ZonePrimaryFixture::build(),
            ZonePrimaryFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'created' => 'not-an-object',
                'labels' => 'not-an-object',
                'protection' => 'not-an-object',
                'ttl' => 'not-a-number',
                'status' => 42,
                'record_count' => 'not-a-number',
                'authoritative_nameservers' => 'not-an-object',
                'registrar' => 42,
                'mode' => 42,
            ],
        ];
        yield 'ZoneSecondary' => [
            ZoneSecondaryFixture::build(),
            ZoneSecondaryFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'created' => 'not-an-object',
                'labels' => 'not-an-object',
                'protection' => 'not-an-object',
                'ttl' => 'not-a-number',
                'status' => 42,
                'record_count' => 'not-a-number',
                'authoritative_nameservers' => 'not-an-object',
                'registrar' => 42,
                'mode' => 42,
            ],
        ];
        yield 'Action' => [
            ActionFixture::build(),
            ActionFixture::reader(),
            [
                'id' => 'not-a-number',
                'command' => 42,
                'status' => 42,
                'started' => 'not-an-object',
                'progress' => 'not-a-number',
                'resources' => 'not-an-object',
            ],
        ];
        yield 'ActionError' => [
            ActionErrorFixture::build(),
            ActionErrorFixture::reader(),
            ['code' => 42, 'message' => 42],
        ];
        yield 'ActionListResponse' => [
            ActionListResponseFixture::build(),
            ActionListResponseFixture::reader(),
            ['actions' => 'not-an-object'],
        ];
        yield 'ActionListResponseWithMeta' => [
            ActionListResponseWithMetaFixture::build(),
            ActionListResponseWithMetaFixture::reader(),
            ['actions' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'ActionResource' => [
            ActionResourceFixture::build(),
            ActionResourceFixture::reader(),
            ['id' => 'not-a-number', 'type' => 42],
        ];
        yield 'ActionResponse' => [
            ActionResponseFixture::build(),
            ActionResponseFixture::reader(),
            ['action' => 'not-an-object'],
        ];
        yield 'Certificate' => [
            CertificateFixture::build(),
            CertificateFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'labels' => 'not-an-object',
                'created' => 'not-an-object',
                'domain_names' => 'not-an-object',
                'used_by' => 'not-an-object',
            ],
        ];
        yield 'CertificateUsedByItem' => [
            CertificateUsedByItemFixture::build(),
            CertificateUsedByItemFixture::reader(),
            ['id' => 'not-a-number', 'type' => 42],
        ];
        yield 'CertificateResponse' => [
            CertificateResponseFixture::build(),
            CertificateResponseFixture::reader(),
            ['certificate' => 'not-an-object'],
        ];
        yield 'CreatedFrom' => [
            CreatedFromFixture::build(),
            CreatedFromFixture::reader(),
            ['id' => 'not-a-number', 'name' => 42],
        ];
        yield 'Datacenter' => [
            DatacenterFixture::build(),
            DatacenterFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'description' => 42,
                'location' => 'not-an-object',
                'server_types' => 'not-an-object',
            ],
        ];
        yield 'DatacenterServerTypes' => [
            DatacenterServerTypesFixture::build(),
            DatacenterServerTypesFixture::reader(),
            [
                'supported' => 'not-an-object',
                'available' => 'not-an-object',
                'available_for_migration' => 'not-an-object',
            ],
        ];
        yield 'DeprecationInfo' => [
            DeprecationInfoFixture::build(),
            DeprecationInfoFixture::reader(),
            ['unavailable_after' => 'not-an-object', 'announced' => 'not-an-object'],
        ];
        yield 'DnsPtr' => [DnsPtrFixture::build(), DnsPtrFixture::reader(), ['ip' => 42, 'dns_ptr' => 42]];
        yield 'ErrorResponse' => [
            ErrorResponseFixture::build(),
            ErrorResponseFixture::reader(),
            ['error' => 'not-an-object'],
        ];
        yield 'ErrorResponseError' => [
            ErrorResponseErrorFixture::build(),
            ErrorResponseErrorFixture::reader(),
            ['code' => 42, 'message' => 42],
        ];
        yield 'Firewall' => [
            FirewallFixture::build(),
            FirewallFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'created' => 'not-an-object',
                'rules' => 'not-an-object',
                'applied_to' => 'not-an-object',
            ],
        ];
        yield 'FirewallRulesItem' => [
            FirewallRulesItemFixture::build(),
            FirewallRulesItemFixture::reader(),
            [
                'direction' => 42,
                'source_ips' => 'not-an-object',
                'destination_ips' => 'not-an-object',
                'protocol' => 42,
            ],
        ];
        yield 'FirewallAppliedToItem' => [
            FirewallAppliedToItemFixture::build(),
            FirewallAppliedToItemFixture::reader(),
            ['type' => 42],
        ];
        yield 'FirewallAppliedToServer' => [
            FirewallAppliedToServerFixture::build(),
            FirewallAppliedToServerFixture::reader(),
            ['id' => 'not-a-number'],
        ];
        yield 'FirewallResource' => [
            FirewallResourceFixture::build(),
            FirewallResourceFixture::reader(),
            ['type' => 42],
        ];
        yield 'FirewallResourceServer' => [
            FirewallResourceServerFixture::build(),
            FirewallResourceServerFixture::reader(),
            ['id' => 'not-a-number'],
        ];
        yield 'FirewallResponse' => [
            FirewallResponseFixture::build(),
            FirewallResponseFixture::reader(),
            ['firewall' => 'not-an-object'],
        ];
        yield 'FloatingIp' => [
            FloatingIpFixture::build(),
            FloatingIpFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'ip' => 42,
                'type' => 42,
                'dns_ptr' => 'not-an-object',
                'home_location' => 'not-an-object',
                'blocked' => 0,
                'protection' => 'not-an-object',
                'labels' => 'not-an-object',
                'created' => 'not-an-object',
            ],
        ];
        yield 'FloatingIpResponse' => [
            FloatingIpResponseFixture::build(),
            FloatingIpResponseFixture::reader(),
            ['floating_ip' => 'not-an-object'],
        ];
        yield 'HealthStatus' => [
            HealthStatusFixture::build(),
            HealthStatusFixture::reader(),
            ['listen_port' => 'not-a-number', 'status' => 42],
        ];
        yield 'Image' => [
            ImageFixture::build(),
            ImageFixture::reader(),
            [
                'id' => 'not-a-number',
                'type' => 42,
                'status' => 42,
                'description' => 42,
                'disk_size' => 'not-a-number',
                'created' => 'not-an-object',
                'os_flavor' => 42,
                'protection' => 'not-an-object',
                'labels' => 'not-an-object',
                'architecture' => 42,
            ],
        ];
        yield 'ImageResponse' => [
            ImageResponseFixture::build(),
            ImageResponseFixture::reader(),
            ['image' => 'not-an-object'],
        ];
        yield 'Iso' => [IsoFixture::build(), IsoFixture::reader(), ['id' => 'not-a-number', 'description' => 42]];
        yield 'LabelSelector' => [LabelSelectorFixture::build(), LabelSelectorFixture::reader(), ['selector' => 42]];
        yield 'ListMeta' => [ListMetaFixture::build(), ListMetaFixture::reader(), ['pagination' => 'not-an-object']];
        yield 'ListMetaPagination' => [
            ListMetaPaginationFixture::build(),
            ListMetaPaginationFixture::reader(),
            ['page' => 'not-a-number', 'per_page' => 'not-a-number'],
        ];
        yield 'LoadBalancer' => [
            LoadBalancerFixture::build(),
            LoadBalancerFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'public_net' => 'not-an-object',
                'private_net' => 'not-an-object',
                'location' => 'not-an-object',
                'load_balancer_type' => 'not-an-object',
                'protection' => 'not-an-object',
                'labels' => 'not-an-object',
                'created' => 'not-an-object',
                'services' => 'not-an-object',
                'targets' => 'not-an-object',
                'algorithm' => 'not-an-object',
                'included_traffic' => 'not-a-number',
            ],
        ];
        yield 'LoadBalancerPublicNet' => [
            LoadBalancerPublicNetFixture::build(),
            LoadBalancerPublicNetFixture::reader(),
            ['enabled' => 0, 'ipv4' => 'not-an-object', 'ipv6' => 'not-an-object'],
        ];
        yield 'LoadBalancerPrivateNetItem' => [
            LoadBalancerPrivateNetItemFixture::build(),
            LoadBalancerPrivateNetItemFixture::reader(),
            ['network' => 'not-a-number', 'ip' => 42],
        ];
        yield 'LoadBalancerAlgorithm2' => [
            LoadBalancerAlgorithm2Fixture::build(),
            LoadBalancerAlgorithm2Fixture::reader(),
            ['type' => 42],
        ];
        yield 'LoadBalancerAlgorithm' => [
            LoadBalancerAlgorithmFixture::build(),
            LoadBalancerAlgorithmFixture::reader(),
            ['type' => 42],
        ];
        yield 'LoadBalancerPublicIp' => [
            LoadBalancerPublicIpFixture::build(),
            LoadBalancerPublicIpFixture::reader(),
            ['blocked' => 0],
        ];
        yield 'LoadBalancerResponse' => [
            LoadBalancerResponseFixture::build(),
            LoadBalancerResponseFixture::reader(),
            ['load_balancer' => 'not-an-object'],
        ];
        yield 'LoadBalancerServiceHealthCheck' => [
            LoadBalancerServiceHealthCheckFixture::build(),
            LoadBalancerServiceHealthCheckFixture::reader(),
            [
                'protocol' => 42,
                'port' => 'not-a-number',
                'interval' => 'not-a-number',
                'timeout' => 'not-a-number',
                'retries' => 'not-a-number',
            ],
        ];
        yield 'LoadBalancerServiceBase' => [
            LoadBalancerServiceBaseFixture::build(),
            LoadBalancerServiceBaseFixture::reader(),
            [
                'protocol' => 42,
                'listen_port' => 'not-a-number',
                'destination_port' => 'not-a-number',
                'proxyprotocol' => 0,
                'health_check' => 'not-an-object',
            ],
        ];
        yield 'LoadBalancerServiceBaseHealthCheck' => [
            LoadBalancerServiceBaseHealthCheckFixture::build(),
            LoadBalancerServiceBaseHealthCheckFixture::reader(),
            [
                'protocol' => 42,
                'port' => 'not-a-number',
                'interval' => 'not-a-number',
                'timeout' => 'not-a-number',
                'retries' => 'not-a-number',
            ],
        ];
        yield 'LoadBalancerServiceBaseHealthCheckHttp' => [
            LoadBalancerServiceBaseHealthCheckHttpFixture::build(),
            LoadBalancerServiceBaseHealthCheckHttpFixture::reader(),
            ['path' => 42],
        ];
        yield 'LoadBalancerServiceHTTPProtocolProperties' => [
            LoadBalancerServiceHTTPProtocolPropertiesFixture::build(),
            LoadBalancerServiceHTTPProtocolPropertiesFixture::reader(),
            ['http' => 'not-an-object'],
        ];
        yield 'LoadBalancerServiceHTTPProtocolPropertiesHttp' => [
            LoadBalancerServiceHTTPProtocolPropertiesHttpFixture::build(),
            LoadBalancerServiceHTTPProtocolPropertiesHttpFixture::reader(),
            [
                'cookie_name' => 42,
                'cookie_lifetime' => 'not-a-number',
                'timeout_idle' => 'not-a-number',
                'sticky_sessions' => 0,
            ],
        ];
        yield 'LoadBalancerServiceHTTPSProtocolProperties' => [
            LoadBalancerServiceHTTPSProtocolPropertiesFixture::build(),
            LoadBalancerServiceHTTPSProtocolPropertiesFixture::reader(),
            ['http' => 'not-an-object'],
        ];
        yield 'LoadBalancerServiceHTTPSProtocolPropertiesHttp' => [
            LoadBalancerServiceHTTPSProtocolPropertiesHttpFixture::build(),
            LoadBalancerServiceHTTPSProtocolPropertiesHttpFixture::reader(),
            [
                'cookie_name' => 42,
                'cookie_lifetime' => 'not-a-number',
                'timeout_idle' => 'not-a-number',
                'certificates' => 'not-an-object',
                'redirect_http' => 0,
                'sticky_sessions' => 0,
            ],
        ];
        yield 'LoadBalancerTarget' => [
            LoadBalancerTargetFixture::build(),
            LoadBalancerTargetFixture::reader(),
            ['type' => 42],
        ];
        yield 'LoadBalancerTargetIP' => [
            LoadBalancerTargetIPFixture::build(),
            LoadBalancerTargetIPFixture::reader(),
            ['ip' => 42],
        ];
        yield 'LoadBalancerTargetLabelSelector' => [
            LoadBalancerTargetLabelSelectorFixture::build(),
            LoadBalancerTargetLabelSelectorFixture::reader(),
            ['selector' => 42],
        ];
        yield 'LoadBalancerTargetServer' => [
            LoadBalancerTargetServerFixture::build(),
            LoadBalancerTargetServerFixture::reader(),
            ['id' => 'not-a-number', 'ip' => 42],
        ];
        yield 'LoadBalancerTargetServerRequest' => [
            LoadBalancerTargetServerRequestFixture::build(),
            LoadBalancerTargetServerRequestFixture::reader(),
            ['id' => 'not-a-number'],
        ];
        yield 'LoadBalancerTargetTypeBase' => [
            LoadBalancerTargetTypeBaseFixture::build(),
            LoadBalancerTargetTypeBaseFixture::reader(),
            ['type' => 42],
        ];
        yield 'LoadBalancerTargetTypeIPProperties' => [
            LoadBalancerTargetTypeIPPropertiesFixture::build(),
            LoadBalancerTargetTypeIPPropertiesFixture::reader(),
            ['ip' => 'not-an-object', 'health_status' => 'not-an-object'],
        ];
        yield 'LoadBalancerTargetTypeLabelSelectorProperties' => [
            LoadBalancerTargetTypeLabelSelectorPropertiesFixture::build(),
            LoadBalancerTargetTypeLabelSelectorPropertiesFixture::reader(),
            ['label_selector' => 'not-an-object', 'targets' => 'not-an-object', 'use_private_ip' => 0],
        ];
        yield 'LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItem' => [
            LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItemFixture::build(),
            LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItemFixture::reader(),
            ['type' => 42, 'server' => 'not-an-object', 'health_status' => 'not-an-object', 'use_private_ip' => 0],
        ];
        yield 'LoadBalancerTargetTypeServerProperties' => [
            LoadBalancerTargetTypeServerPropertiesFixture::build(),
            LoadBalancerTargetTypeServerPropertiesFixture::reader(),
            ['server' => 'not-an-object', 'health_status' => 'not-an-object', 'use_private_ip' => 0],
        ];
        yield 'LoadBalancerType' => [
            LoadBalancerTypeFixture::build(),
            LoadBalancerTypeFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'description' => 42,
                'max_connections' => 'not-a-number',
                'max_services' => 'not-a-number',
                'max_targets' => 'not-a-number',
                'max_assigned_certificates' => 'not-a-number',
                'prices' => 'not-an-object',
            ],
        ];
        yield 'Location' => [
            LocationFixture::build(),
            LocationFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'description' => 42,
                'country' => 42,
                'city' => 42,
                'latitude' => 'not-a-number',
                'longitude' => 'not-a-number',
                'network_zone' => 42,
            ],
        ];
        yield 'LocationPrice' => [
            LocationPriceFixture::build(),
            LocationPriceFixture::reader(),
            [
                'location' => 42,
                'price_hourly' => 'not-an-object',
                'price_monthly' => 'not-an-object',
                'included_traffic' => 'not-a-number',
                'price_per_tb_traffic' => 'not-an-object',
            ],
        ];
        yield 'MetricsResponse' => [
            MetricsResponseFixture::build(),
            MetricsResponseFixture::reader(),
            ['metrics' => 'not-an-object'],
        ];
        yield 'MetricsResponseMetrics' => [
            MetricsResponseMetricsFixture::build(),
            MetricsResponseMetricsFixture::reader(),
            [
                'start' => 'not-an-object',
                'end' => 'not-an-object',
                'step' => 'not-a-number',
                'time_series' => 'not-an-object',
            ],
        ];
        yield 'MetricsResponseMetricsTimeSeriesItem' => [
            MetricsResponseMetricsTimeSeriesItemFixture::build(),
            MetricsResponseMetricsTimeSeriesItemFixture::reader(),
            ['values' => 'not-an-object'],
        ];
        yield 'Network' => [
            NetworkFixture::build(),
            NetworkFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'ip_range' => 42,
                'subnets' => 'not-an-object',
                'routes' => 'not-an-object',
                'servers' => 'not-an-object',
                'protection' => 'not-an-object',
                'labels' => 'not-an-object',
                'created' => 'not-an-object',
                'expose_routes_to_vswitch' => 0,
            ],
        ];
        yield 'NetworkSubnetsItem' => [
            NetworkSubnetsItemFixture::build(),
            NetworkSubnetsItemFixture::reader(),
            ['type' => 42, 'network_zone' => 42, 'gateway' => 42],
        ];
        yield 'NetworkResponse' => [
            NetworkResponseFixture::build(),
            NetworkResponseFixture::reader(),
            ['network' => 'not-an-object'],
        ];
        yield 'PlacementGroup' => [
            PlacementGroupFixture::build(),
            PlacementGroupFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'labels' => 'not-an-object',
                'type' => 42,
                'created' => 'not-an-object',
                'servers' => 'not-an-object',
            ],
        ];
        yield 'PlacementGroupResponse' => [
            PlacementGroupResponseFixture::build(),
            PlacementGroupResponseFixture::reader(),
            ['placement_group' => 'not-an-object'],
        ];
        yield 'Price' => [PriceFixture::build(), PriceFixture::reader(), ['net' => 42, 'gross' => 42]];
        yield 'PricePerGbMonth' => [
            PricePerGbMonthFixture::build(),
            PricePerGbMonthFixture::reader(),
            ['price_per_gb_month' => 'not-an-object'],
        ];
        yield 'PrimaryIP' => [
            PrimaryIPFixture::build(),
            PrimaryIPFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'labels' => 'not-an-object',
                'created' => 'not-an-object',
                'blocked' => 0,
                'location' => 'not-an-object',
                'ip' => 42,
                'dns_ptr' => 'not-an-object',
                'protection' => 'not-an-object',
                'type' => 42,
                'auto_delete' => 0,
                'assignee_type' => 42,
            ],
        ];
        yield 'PrimaryIPResponse' => [
            PrimaryIPResponseFixture::build(),
            PrimaryIPResponseFixture::reader(),
            ['primary_ip' => 'not-an-object'],
        ];
        yield 'PrimaryZoneProperties' => [
            PrimaryZonePropertiesFixture::build(),
            PrimaryZonePropertiesFixture::reader(),
            ['mode' => 42],
        ];
        yield 'Protection' => [ProtectionFixture::build(), ProtectionFixture::reader(), ['delete' => 0]];
        yield 'RRSet' => [
            RRSetFixture::build(),
            RRSetFixture::reader(),
            [
                'id' => 42,
                'name' => 42,
                'type' => 42,
                'labels' => 'not-an-object',
                'protection' => 'not-an-object',
                'records' => 'not-an-object',
                'zone' => 'not-a-number',
            ],
        ];
        yield 'RRSetProtection' => [RRSetProtectionFixture::build(), RRSetProtectionFixture::reader(), ['change' => 0]];
        yield 'RRSetRecordsRequest' => [
            RRSetRecordsRequestFixture::build(),
            RRSetRecordsRequestFixture::reader(),
            ['records' => 'not-an-object'],
        ];
        yield 'RRSetRequest' => [
            RRSetRequestFixture::build(),
            RRSetRequestFixture::reader(),
            ['name' => 42, 'type' => 42, 'records' => 'not-an-object'],
        ];
        yield 'Record' => [RecordFixture::build(), RecordFixture::reader(), ['value' => 42]];
        yield 'RootPasswordResponse' => [
            RootPasswordResponseFixture::build(),
            RootPasswordResponseFixture::reader(),
            ['root_password' => 42, 'action' => 'not-an-object'],
        ];
        yield 'Route' => [RouteFixture::build(), RouteFixture::reader(), ['destination' => 42, 'gateway' => 42]];
        yield 'RrsetResponse' => [
            RrsetResponseFixture::build(),
            RrsetResponseFixture::reader(),
            ['rrset' => 'not-an-object'],
        ];
        yield 'Rule' => [RuleFixture::build(), RuleFixture::reader(), ['direction' => 42, 'protocol' => 42]];
        yield 'SecondaryZoneProperties' => [
            SecondaryZonePropertiesFixture::build(),
            SecondaryZonePropertiesFixture::reader(),
            ['mode' => 42],
        ];
        yield 'Server' => [
            ServerFixture::build(),
            ServerFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'status' => 42,
                'created' => 'not-an-object',
                'public_net' => 'not-an-object',
                'private_net' => 'not-an-object',
                'server_type' => 'not-an-object',
                'location' => 'not-an-object',
                'rescue_enabled' => 0,
                'locked' => 0,
                'protection' => 'not-an-object',
                'labels' => 'not-an-object',
                'primary_disk_size' => 'not-a-number',
            ],
        ];
        yield 'ServerPublicNet' => [
            ServerPublicNetFixture::build(),
            ServerPublicNetFixture::reader(),
            ['floating_ips' => 'not-an-object'],
        ];
        yield 'ServerPublicNetIpv4' => [
            ServerPublicNetIpv4Fixture::build(),
            ServerPublicNetIpv4Fixture::reader(),
            ['ip' => 42, 'blocked' => 0, 'dns_ptr' => 42],
        ];
        yield 'ServerPublicNetIpv6' => [
            ServerPublicNetIpv6Fixture::build(),
            ServerPublicNetIpv6Fixture::reader(),
            ['ip' => 42, 'blocked' => 0],
        ];
        yield 'ServerProtection' => [
            ServerProtectionFixture::build(),
            ServerProtectionFixture::reader(),
            ['delete' => 0, 'rebuild' => 0],
        ];
        yield 'ServerResponse' => [
            ServerResponseFixture::build(),
            ServerResponseFixture::reader(),
            ['server' => 'not-an-object'],
        ];
        yield 'ServerType' => [
            ServerTypeFixture::build(),
            ServerTypeFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'description' => 42,
                'cores' => 'not-a-number',
                'memory' => 'not-a-number',
                'disk' => 'not-a-number',
                'deprecated' => 0,
                'prices' => 'not-an-object',
                'storage_type' => 42,
                'cpu_type' => 42,
                'architecture' => 42,
                'locations' => 'not-an-object',
            ],
        ];
        yield 'ServerTypeLocationsItem' => [
            ServerTypeLocationsItemFixture::build(),
            ServerTypeLocationsItemFixture::reader(),
            ['id' => 'not-a-number', 'name' => 42, 'recommended' => 0, 'available' => 0],
        ];
        yield 'SshKey' => [
            SshKeyFixture::build(),
            SshKeyFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'fingerprint' => 42,
                'public_key' => 42,
                'labels' => 'not-an-object',
                'created' => 'not-an-object',
            ],
        ];
        yield 'SshKeyResponse' => [
            SshKeyResponseFixture::build(),
            SshKeyResponseFixture::reader(),
            ['ssh_key' => 'not-an-object'],
        ];
        yield 'TypePricing' => [
            TypePricingFixture::build(),
            TypePricingFixture::reader(),
            ['id' => 'not-a-number', 'name' => 42, 'prices' => 'not-an-object'],
        ];
        yield 'Volume' => [
            VolumeFixture::build(),
            VolumeFixture::reader(),
            [
                'id' => 'not-a-number',
                'created' => 'not-an-object',
                'name' => 42,
                'location' => 'not-an-object',
                'size' => 'not-a-number',
                'linux_device' => 42,
                'protection' => 'not-an-object',
                'labels' => 'not-an-object',
                'status' => 42,
            ],
        ];
        yield 'VolumeResponse' => [
            VolumeResponseFixture::build(),
            VolumeResponseFixture::reader(),
            ['volume' => 'not-an-object'],
        ];
        yield 'ZoneBase' => [
            ZoneBaseFixture::build(),
            ZoneBaseFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'created' => 'not-an-object',
                'labels' => 'not-an-object',
                'protection' => 'not-an-object',
                'ttl' => 'not-a-number',
                'status' => 42,
                'record_count' => 'not-a-number',
                'authoritative_nameservers' => 'not-an-object',
                'registrar' => 42,
            ],
        ];
        yield 'ZoneBaseAuthoritativeNameservers' => [
            ZoneBaseAuthoritativeNameserversFixture::build(),
            ZoneBaseAuthoritativeNameserversFixture::reader(),
            ['assigned' => 'not-an-object', 'delegated' => 'not-an-object'],
        ];
        yield 'ZonePrimaryNameserver' => [
            ZonePrimaryNameserverFixture::build(),
            ZonePrimaryNameserverFixture::reader(),
            ['address' => 42],
        ];
        yield 'Zonefile' => [ZonefileFixture::build(), ZonefileFixture::reader(), ['zonefile' => 42]];
        yield 'ResetPasswordRequest' => [
            ResetPasswordRequestFixture::build(),
            ResetPasswordRequestFixture::reader(),
            ['password' => 42],
        ];
        yield 'Snapshot' => [
            SnapshotFixture::build(),
            SnapshotFixture::reader(),
            [
                'storage_box' => 'not-a-number',
                'id' => 'not-a-number',
                'name' => 42,
                'description' => 42,
                'labels' => 'not-an-object',
                'stats' => 'not-an-object',
                'is_automatic' => 0,
                'created' => 'not-an-object',
            ],
        ];
        yield 'SnapshotStats' => [
            SnapshotStatsFixture::build(),
            SnapshotStatsFixture::reader(),
            ['size' => 'not-a-number', 'size_filesystem' => 'not-a-number'],
        ];
        yield 'SnapshotResponse' => [
            SnapshotResponseFixture::build(),
            SnapshotResponseFixture::reader(),
            ['snapshot' => 'not-an-object'],
        ];
        yield 'StorageBox' => [
            StorageBoxFixture::build(),
            StorageBoxFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'storage_box_type' => 'not-an-object',
                'location' => 'not-an-object',
                'access_settings' => 'not-an-object',
                'protection' => 'not-an-object',
                'labels' => 'not-an-object',
                'status' => 42,
                'stats' => 'not-an-object',
                'created' => 'not-an-object',
            ],
        ];
        yield 'StorageBoxAccessSettings' => [
            StorageBoxAccessSettingsFixture::build(),
            StorageBoxAccessSettingsFixture::reader(),
            [
                'reachable_externally' => 0,
                'samba_enabled' => 0,
                'ssh_enabled' => 0,
                'webdav_enabled' => 0,
                'zfs_enabled' => 0,
            ],
        ];
        yield 'StorageBoxSnapshotPlan' => [
            StorageBoxSnapshotPlanFixture::build(),
            StorageBoxSnapshotPlanFixture::reader(),
            ['max_snapshots' => 'not-a-number', 'minute' => 'not-a-number', 'hour' => 'not-a-number'],
        ];
        yield 'StorageBoxStats' => [
            StorageBoxStatsFixture::build(),
            StorageBoxStatsFixture::reader(),
            ['size' => 'not-a-number', 'size_data' => 'not-a-number', 'size_snapshots' => 'not-a-number'],
        ];
        yield 'StorageBoxResponse' => [
            StorageBoxResponseFixture::build(),
            StorageBoxResponseFixture::reader(),
            ['storage_box' => 'not-an-object'],
        ];
        yield 'StorageBoxType' => [
            StorageBoxTypeFixture::build(),
            StorageBoxTypeFixture::reader(),
            [
                'id' => 'not-a-number',
                'name' => 42,
                'description' => 42,
                'subaccounts_limit' => 'not-a-number',
                'size' => 'not-a-number',
                'prices' => 'not-an-object',
            ],
        ];
        yield 'StorageBoxTypePricesItem' => [
            StorageBoxTypePricesItemFixture::build(),
            StorageBoxTypePricesItemFixture::reader(),
            [
                'location' => 42,
                'price_hourly' => 'not-an-object',
                'price_monthly' => 'not-an-object',
                'setup_fee' => 'not-an-object',
            ],
        ];
        yield 'Subaccount' => [
            SubaccountFixture::build(),
            SubaccountFixture::reader(),
            [
                'storage_box' => 'not-a-number',
                'id' => 'not-a-number',
                'name' => 42,
                'home_directory' => 42,
                'access_settings' => 'not-an-object',
                'description' => 42,
                'labels' => 'not-an-object',
                'username' => 42,
                'server' => 42,
                'created' => 'not-an-object',
            ],
        ];
        yield 'SubaccountAccessSettings' => [
            SubaccountAccessSettingsFixture::build(),
            SubaccountAccessSettingsFixture::reader(),
            [
                'reachable_externally' => 0,
                'samba_enabled' => 0,
                'ssh_enabled' => 0,
                'webdav_enabled' => 0,
                'readonly' => 0,
            ],
        ];
        yield 'SubaccountResponse' => [
            SubaccountResponseFixture::build(),
            SubaccountResponseFixture::reader(),
            ['subaccount' => 'not-an-object'],
        ];
        yield 'ListCertificatesResponse200' => [
            ListCertificatesResponse200Fixture::build(),
            ListCertificatesResponse200Fixture::reader(),
            ['certificates' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'CreateCertificateBody' => [
            CreateCertificateBodyFixture::build(),
            CreateCertificateBodyFixture::reader(),
            ['name' => 42],
        ];
        yield 'CreateCertificateResponse201' => [
            CreateCertificateResponse201Fixture::build(),
            CreateCertificateResponse201Fixture::reader(),
            ['certificate' => 'not-an-object'],
        ];
        yield 'ListDatacentersResponse200' => [
            ListDatacentersResponse200Fixture::build(),
            ListDatacentersResponse200Fixture::reader(),
            ['datacenters' => 'not-an-object', 'recommendation' => 'not-a-number', 'meta' => 'not-an-object'],
        ];
        yield 'GetDatacenterResponse200' => [
            GetDatacenterResponse200Fixture::build(),
            GetDatacenterResponse200Fixture::reader(),
            ['datacenter' => 'not-an-object'],
        ];
        yield 'ListFirewallsResponse200' => [
            ListFirewallsResponse200Fixture::build(),
            ListFirewallsResponse200Fixture::reader(),
            ['firewalls' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'CreateFirewallBody' => [
            CreateFirewallBodyFixture::build(),
            CreateFirewallBodyFixture::reader(),
            ['name' => 42],
        ];
        yield 'CreateFirewallResponse201' => [
            CreateFirewallResponse201Fixture::build(),
            CreateFirewallResponse201Fixture::reader(),
            ['firewall' => 'not-an-object'],
        ];
        yield 'ApplyFirewallToResourcesBody' => [
            ApplyFirewallToResourcesBodyFixture::build(),
            ApplyFirewallToResourcesBodyFixture::reader(),
            ['apply_to' => 'not-an-object'],
        ];
        yield 'RemoveFirewallFromResourcesBody' => [
            RemoveFirewallFromResourcesBodyFixture::build(),
            RemoveFirewallFromResourcesBodyFixture::reader(),
            ['remove_from' => 'not-an-object'],
        ];
        yield 'SetFirewallRulesBody' => [
            SetFirewallRulesBodyFixture::build(),
            SetFirewallRulesBodyFixture::reader(),
            ['rules' => 'not-an-object'],
        ];
        yield 'ListFloatingIpsResponse200' => [
            ListFloatingIpsResponse200Fixture::build(),
            ListFloatingIpsResponse200Fixture::reader(),
            ['floating_ips' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'CreateFloatingIpBody' => [
            CreateFloatingIpBodyFixture::build(),
            CreateFloatingIpBodyFixture::reader(),
            ['type' => 42],
        ];
        yield 'CreateFloatingIpResponse201' => [
            CreateFloatingIpResponse201Fixture::build(),
            CreateFloatingIpResponse201Fixture::reader(),
            ['floating_ip' => 'not-an-object'],
        ];
        yield 'ChangeFloatingIpDnsPtrBody' => [
            ChangeFloatingIpDnsPtrBodyFixture::build(),
            ChangeFloatingIpDnsPtrBodyFixture::reader(),
            ['ip' => 42],
        ];
        yield 'ChangeFloatingIpProtectionBody' => [
            ChangeFloatingIpProtectionBodyFixture::build(),
            ChangeFloatingIpProtectionBodyFixture::reader(),
            ['delete' => 0],
        ];
        yield 'ListImagesResponse200' => [
            ListImagesResponse200Fixture::build(),
            ListImagesResponse200Fixture::reader(),
            ['images' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'ListIsosResponse200' => [
            ListIsosResponse200Fixture::build(),
            ListIsosResponse200Fixture::reader(),
            ['isos' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'GetIsoResponse200' => [
            GetIsoResponse200Fixture::build(),
            GetIsoResponse200Fixture::reader(),
            ['iso' => 'not-an-object'],
        ];
        yield 'ListLoadBalancerTypesResponse200' => [
            ListLoadBalancerTypesResponse200Fixture::build(),
            ListLoadBalancerTypesResponse200Fixture::reader(),
            ['load_balancer_types' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'GetLoadBalancerTypeResponse200' => [
            GetLoadBalancerTypeResponse200Fixture::build(),
            GetLoadBalancerTypeResponse200Fixture::reader(),
            ['load_balancer_type' => 'not-an-object'],
        ];
        yield 'ListLoadBalancersResponse200' => [
            ListLoadBalancersResponse200Fixture::build(),
            ListLoadBalancersResponse200Fixture::reader(),
            ['load_balancers' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'CreateLoadBalancerBody' => [
            CreateLoadBalancerBodyFixture::build(),
            CreateLoadBalancerBodyFixture::reader(),
            ['name' => 42],
        ];
        yield 'CreateLoadBalancerBodyTargetsItem' => [
            CreateLoadBalancerBodyTargetsItemFixture::build(),
            CreateLoadBalancerBodyTargetsItemFixture::reader(),
            ['type' => 42],
        ];
        yield 'CreateLoadBalancerResponse201' => [
            CreateLoadBalancerResponse201Fixture::build(),
            CreateLoadBalancerResponse201Fixture::reader(),
            ['load_balancer' => 'not-an-object', 'action' => 'not-an-object'],
        ];
        yield 'AddLoadBalancerServiceBody' => [
            AddLoadBalancerServiceBodyFixture::build(),
            AddLoadBalancerServiceBodyFixture::reader(),
            [
                'protocol' => 42,
                'listen_port' => 'not-a-number',
                'destination_port' => 'not-a-number',
                'proxyprotocol' => 0,
                'health_check' => 'not-an-object',
            ],
        ];
        yield 'AddLoadBalancerTargetBody' => [
            AddLoadBalancerTargetBodyFixture::build(),
            AddLoadBalancerTargetBodyFixture::reader(),
            ['type' => 42],
        ];
        yield 'AttachLoadBalancerToNetworkBody' => [
            AttachLoadBalancerToNetworkBodyFixture::build(),
            AttachLoadBalancerToNetworkBodyFixture::reader(),
            ['network' => 'not-a-number'],
        ];
        yield 'ChangeLoadBalancerDnsPtrBody' => [
            ChangeLoadBalancerDnsPtrBodyFixture::build(),
            ChangeLoadBalancerDnsPtrBodyFixture::reader(),
            ['ip' => 42],
        ];
        yield 'DeleteLoadBalancerServiceBody' => [
            DeleteLoadBalancerServiceBodyFixture::build(),
            DeleteLoadBalancerServiceBodyFixture::reader(),
            ['listen_port' => 'not-a-number'],
        ];
        yield 'DetachLoadBalancerFromNetworkBody' => [
            DetachLoadBalancerFromNetworkBodyFixture::build(),
            DetachLoadBalancerFromNetworkBodyFixture::reader(),
            ['network' => 'not-a-number'],
        ];
        yield 'UpdateLoadBalancerServiceBody' => [
            UpdateLoadBalancerServiceBodyFixture::build(),
            UpdateLoadBalancerServiceBodyFixture::reader(),
            ['listen_port' => 'not-a-number'],
        ];
        yield 'ListLocationsResponse200' => [
            ListLocationsResponse200Fixture::build(),
            ListLocationsResponse200Fixture::reader(),
            ['locations' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'GetLocationResponse200' => [
            GetLocationResponse200Fixture::build(),
            GetLocationResponse200Fixture::reader(),
            ['location' => 'not-an-object'],
        ];
        yield 'ListNetworksResponse200' => [
            ListNetworksResponse200Fixture::build(),
            ListNetworksResponse200Fixture::reader(),
            ['networks' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'CreateNetworkBody' => [
            CreateNetworkBodyFixture::build(),
            CreateNetworkBodyFixture::reader(),
            ['name' => 42, 'ip_range' => 42],
        ];
        yield 'CreateNetworkBodySubnetsItem' => [
            CreateNetworkBodySubnetsItemFixture::build(),
            CreateNetworkBodySubnetsItemFixture::reader(),
            ['type' => 42, 'network_zone' => 42],
        ];
        yield 'AddNetworkSubnetBody' => [
            AddNetworkSubnetBodyFixture::build(),
            AddNetworkSubnetBodyFixture::reader(),
            ['type' => 42, 'network_zone' => 42],
        ];
        yield 'ChangeNetworkIpRangeBody' => [
            ChangeNetworkIpRangeBodyFixture::build(),
            ChangeNetworkIpRangeBodyFixture::reader(),
            ['ip_range' => 42],
        ];
        yield 'DeleteNetworkSubnetBody' => [
            DeleteNetworkSubnetBodyFixture::build(),
            DeleteNetworkSubnetBodyFixture::reader(),
            ['ip_range' => 42],
        ];
        yield 'ListNetworkMembersResponse200' => [
            ListNetworkMembersResponse200Fixture::build(),
            ListNetworkMembersResponse200Fixture::reader(),
            ['members' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'ListNetworkMembersResponse200MembersItem' => [
            ListNetworkMembersResponse200MembersItemFixture::build(),
            ListNetworkMembersResponse200MembersItemFixture::reader(),
            [
                'type' => 42,
                'id' => 'not-a-number',
                'ip' => 42,
                'status' => 42,
                'alias_ips' => 'not-an-object',
                'subnet' => 42,
            ],
        ];
        yield 'ListPlacementGroupsResponse200' => [
            ListPlacementGroupsResponse200Fixture::build(),
            ListPlacementGroupsResponse200Fixture::reader(),
            ['placement_groups' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'CreatePlacementGroupBody' => [
            CreatePlacementGroupBodyFixture::build(),
            CreatePlacementGroupBodyFixture::reader(),
            ['name' => 42, 'type' => 42],
        ];
        yield 'CreatePlacementGroupResponse201' => [
            CreatePlacementGroupResponse201Fixture::build(),
            CreatePlacementGroupResponse201Fixture::reader(),
            ['placement_group' => 'not-an-object'],
        ];
        yield 'GetPricingResponse200' => [
            GetPricingResponse200Fixture::build(),
            GetPricingResponse200Fixture::reader(),
            ['pricing' => 'not-an-object'],
        ];
        yield 'GetPricingResponse200Pricing' => [
            GetPricingResponse200PricingFixture::build(),
            GetPricingResponse200PricingFixture::reader(),
            [
                'currency' => 42,
                'vat_rate' => 42,
                'primary_ips' => 'not-an-object',
                'floating_ips' => 'not-an-object',
                'image' => 'not-an-object',
                'volume' => 'not-an-object',
                'server_backup' => 'not-an-object',
                'server_types' => 'not-an-object',
                'load_balancer_types' => 'not-an-object',
                'floating_ip' => 'not-an-object',
            ],
        ];
        yield 'GetPricingResponse200PricingPrimaryIpsItem' => [
            GetPricingResponse200PricingPrimaryIpsItemFixture::build(),
            GetPricingResponse200PricingPrimaryIpsItemFixture::reader(),
            ['type' => 42, 'prices' => 'not-an-object'],
        ];
        yield 'GetPricingResponse200PricingPrimaryIpsItemPricesItem' => [
            GetPricingResponse200PricingPrimaryIpsItemPricesItemFixture::build(),
            GetPricingResponse200PricingPrimaryIpsItemPricesItemFixture::reader(),
            ['location' => 42, 'price_hourly' => 'not-an-object', 'price_monthly' => 'not-an-object'],
        ];
        yield 'GetPricingResponse200PricingFloatingIpsItem' => [
            GetPricingResponse200PricingFloatingIpsItemFixture::build(),
            GetPricingResponse200PricingFloatingIpsItemFixture::reader(),
            ['type' => 42, 'prices' => 'not-an-object'],
        ];
        yield 'GetPricingResponse200PricingFloatingIpsItemPricesItem' => [
            GetPricingResponse200PricingFloatingIpsItemPricesItemFixture::build(),
            GetPricingResponse200PricingFloatingIpsItemPricesItemFixture::reader(),
            ['location' => 42, 'price_monthly' => 'not-an-object'],
        ];
        yield 'GetPricingResponse200PricingServerBackup' => [
            GetPricingResponse200PricingServerBackupFixture::build(),
            GetPricingResponse200PricingServerBackupFixture::reader(),
            ['percentage' => 42],
        ];
        yield 'GetPricingResponse200PricingFloatingIp' => [
            GetPricingResponse200PricingFloatingIpFixture::build(),
            GetPricingResponse200PricingFloatingIpFixture::reader(),
            ['price_monthly' => 'not-an-object'],
        ];
        yield 'ListPrimaryIpsResponse200' => [
            ListPrimaryIpsResponse200Fixture::build(),
            ListPrimaryIpsResponse200Fixture::reader(),
            ['primary_ips' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'CreatePrimaryIpBody' => [
            CreatePrimaryIpBodyFixture::build(),
            CreatePrimaryIpBodyFixture::reader(),
            ['name' => 42, 'type' => 42],
        ];
        yield 'CreatePrimaryIpResponse201' => [
            CreatePrimaryIpResponse201Fixture::build(),
            CreatePrimaryIpResponse201Fixture::reader(),
            ['primary_ip' => 'not-an-object'],
        ];
        yield 'AssignPrimaryIpBody' => [
            AssignPrimaryIpBodyFixture::build(),
            AssignPrimaryIpBodyFixture::reader(),
            ['assignee_type' => 42, 'assignee_id' => 'not-a-number'],
        ];
        yield 'ChangePrimaryIpDnsPtrBody' => [
            ChangePrimaryIpDnsPtrBodyFixture::build(),
            ChangePrimaryIpDnsPtrBodyFixture::reader(),
            ['ip' => 42],
        ];
        yield 'ChangePrimaryIpProtectionBody' => [
            ChangePrimaryIpProtectionBodyFixture::build(),
            ChangePrimaryIpProtectionBodyFixture::reader(),
            ['delete' => 0],
        ];
        yield 'ListServerTypesResponse200' => [
            ListServerTypesResponse200Fixture::build(),
            ListServerTypesResponse200Fixture::reader(),
            ['server_types' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'GetServerTypeResponse200' => [
            GetServerTypeResponse200Fixture::build(),
            GetServerTypeResponse200Fixture::reader(),
            ['server_type' => 'not-an-object'],
        ];
        yield 'ListServersResponse200' => [
            ListServersResponse200Fixture::build(),
            ListServersResponse200Fixture::reader(),
            ['servers' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'CreateServerBody' => [
            CreateServerBodyFixture::build(),
            CreateServerBodyFixture::reader(),
            ['name' => 42],
        ];
        yield 'CreateServerBodyFirewallsItem' => [
            CreateServerBodyFirewallsItemFixture::build(),
            CreateServerBodyFirewallsItemFixture::reader(),
            ['firewall' => 'not-a-number'],
        ];
        yield 'CreateServerResponse201' => [
            CreateServerResponse201Fixture::build(),
            CreateServerResponse201Fixture::reader(),
            ['server' => 'not-an-object', 'action' => 'not-an-object', 'next_actions' => 'not-an-object'],
        ];
        yield 'AddServerToPlacementGroupBody' => [
            AddServerToPlacementGroupBodyFixture::build(),
            AddServerToPlacementGroupBodyFixture::reader(),
            ['placement_group' => 'not-a-number'],
        ];
        yield 'AttachServerToNetworkBody' => [
            AttachServerToNetworkBodyFixture::build(),
            AttachServerToNetworkBodyFixture::reader(),
            ['network' => 'not-a-number'],
        ];
        yield 'ChangeServerAliasIpsBody' => [
            ChangeServerAliasIpsBodyFixture::build(),
            ChangeServerAliasIpsBodyFixture::reader(),
            ['network' => 'not-a-number', 'alias_ips' => 'not-an-object'],
        ];
        yield 'ChangeServerDnsPtrBody' => [
            ChangeServerDnsPtrBodyFixture::build(),
            ChangeServerDnsPtrBodyFixture::reader(),
            ['ip' => 42],
        ];
        yield 'ChangeServerTypeBody' => [
            ChangeServerTypeBodyFixture::build(),
            ChangeServerTypeBodyFixture::reader(),
            ['upgrade_disk' => 0],
        ];
        yield 'CreateServerImageResponse201' => [
            CreateServerImageResponse201Fixture::build(),
            CreateServerImageResponse201Fixture::reader(),
            ['image' => 'not-an-object', 'action' => 'not-an-object'],
        ];
        yield 'DetachServerFromNetworkBody' => [
            DetachServerFromNetworkBodyFixture::build(),
            DetachServerFromNetworkBodyFixture::reader(),
            ['network' => 'not-a-number'],
        ];
        yield 'RebuildServerResponse201' => [
            RebuildServerResponse201Fixture::build(),
            RebuildServerResponse201Fixture::reader(),
            ['action' => 'not-an-object'],
        ];
        yield 'RequestServerConsoleResponse201' => [
            RequestServerConsoleResponse201Fixture::build(),
            RequestServerConsoleResponse201Fixture::reader(),
            ['wss_url' => 42, 'password' => 42, 'action' => 'not-an-object'],
        ];
        yield 'ListSshKeysResponse200' => [
            ListSshKeysResponse200Fixture::build(),
            ListSshKeysResponse200Fixture::reader(),
            ['ssh_keys' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'CreateSshKeyBody' => [
            CreateSshKeyBodyFixture::build(),
            CreateSshKeyBodyFixture::reader(),
            ['name' => 42, 'public_key' => 42],
        ];
        yield 'ListVolumesResponse200' => [
            ListVolumesResponse200Fixture::build(),
            ListVolumesResponse200Fixture::reader(),
            ['volumes' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'CreateVolumeBody' => [
            CreateVolumeBodyFixture::build(),
            CreateVolumeBodyFixture::reader(),
            ['size' => 'not-a-number', 'name' => 42],
        ];
        yield 'CreateVolumeResponse201' => [
            CreateVolumeResponse201Fixture::build(),
            CreateVolumeResponse201Fixture::reader(),
            ['volume' => 'not-an-object', 'action' => 'not-an-object', 'next_actions' => 'not-an-object'],
        ];
        yield 'AttachVolumeBody' => [
            AttachVolumeBodyFixture::build(),
            AttachVolumeBodyFixture::reader(),
            ['server' => 'not-a-number'],
        ];
        yield 'ResizeVolumeBody' => [
            ResizeVolumeBodyFixture::build(),
            ResizeVolumeBodyFixture::reader(),
            ['size' => 'not-a-number'],
        ];
        yield 'ListZonesResponse200' => [
            ListZonesResponse200Fixture::build(),
            ListZonesResponse200Fixture::reader(),
            ['zones' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'CreateZoneBody' => [
            CreateZoneBodyFixture::build(),
            CreateZoneBodyFixture::reader(),
            ['name' => 42, 'mode' => 42],
        ];
        yield 'CreateZoneResponse201' => [
            CreateZoneResponse201Fixture::build(),
            CreateZoneResponse201Fixture::reader(),
            ['action' => 'not-an-object'],
        ];
        yield 'ChangeZonePrimaryNameserversBody' => [
            ChangeZonePrimaryNameserversBodyFixture::build(),
            ChangeZonePrimaryNameserversBodyFixture::reader(),
            ['primary_nameservers' => 'not-an-object'],
        ];
        yield 'ChangeZoneTtlBody' => [
            ChangeZoneTtlBodyFixture::build(),
            ChangeZoneTtlBodyFixture::reader(),
            ['ttl' => 'not-a-number'],
        ];
        yield 'ListZoneRrsetsResponse200' => [
            ListZoneRrsetsResponse200Fixture::build(),
            ListZoneRrsetsResponse200Fixture::reader(),
            ['rrsets' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'ListZoneRrsetsResponse200Meta' => [
            ListZoneRrsetsResponse200MetaFixture::build(),
            ListZoneRrsetsResponse200MetaFixture::reader(),
            ['pagination' => 'not-an-object'],
        ];
        yield 'ListZoneRrsetsResponse200MetaPagination' => [
            ListZoneRrsetsResponse200MetaPaginationFixture::build(),
            ListZoneRrsetsResponse200MetaPaginationFixture::reader(),
            ['page' => 'not-a-number', 'per_page' => 'not-a-number'],
        ];
        yield 'CreateZoneRrsetResponse201' => [
            CreateZoneRrsetResponse201Fixture::build(),
            CreateZoneRrsetResponse201Fixture::reader(),
            ['rrset' => 'not-an-object', 'action' => 'not-an-object'],
        ];
        yield 'AddZoneRrsetRecordsBody' => [
            AddZoneRrsetRecordsBodyFixture::build(),
            AddZoneRrsetRecordsBodyFixture::reader(),
            ['records' => 'not-an-object'],
        ];
        yield 'UpdateZoneRrsetRecordsBody' => [
            UpdateZoneRrsetRecordsBodyFixture::build(),
            UpdateZoneRrsetRecordsBodyFixture::reader(),
            ['records' => 'not-an-object'],
        ];
        yield 'UpdateZoneRrsetRecordsBodyRecordsItem' => [
            UpdateZoneRrsetRecordsBodyRecordsItemFixture::build(),
            UpdateZoneRrsetRecordsBodyRecordsItemFixture::reader(),
            ['value' => 42, 'comment' => 42],
        ];
        yield 'ListStorageBoxesResponse200' => [
            ListStorageBoxesResponse200Fixture::build(),
            ListStorageBoxesResponse200Fixture::reader(),
            ['storage_boxes' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'CreateStorageBoxBody' => [
            CreateStorageBoxBodyFixture::build(),
            CreateStorageBoxBodyFixture::reader(),
            ['name' => 42, 'password' => 42],
        ];
        yield 'CreateStorageBoxResponse201' => [
            CreateStorageBoxResponse201Fixture::build(),
            CreateStorageBoxResponse201Fixture::reader(),
            ['storage_box' => 'not-an-object', 'action' => 'not-an-object'],
        ];
        yield 'ListStorageBoxFoldersResponse200' => [
            ListStorageBoxFoldersResponse200Fixture::build(),
            ListStorageBoxFoldersResponse200Fixture::reader(),
            ['folders' => 'not-an-object'],
        ];
        yield 'EnableStorageBoxSnapshotPlanBody' => [
            EnableStorageBoxSnapshotPlanBodyFixture::build(),
            EnableStorageBoxSnapshotPlanBodyFixture::reader(),
            ['max_snapshots' => 'not-a-number', 'minute' => 'not-a-number', 'hour' => 'not-a-number'],
        ];
        yield 'ListStorageBoxSubaccountsResponse200' => [
            ListStorageBoxSubaccountsResponse200Fixture::build(),
            ListStorageBoxSubaccountsResponse200Fixture::reader(),
            ['subaccounts' => 'not-an-object'],
        ];
        yield 'CreateStorageBoxSubaccountBody' => [
            CreateStorageBoxSubaccountBodyFixture::build(),
            CreateStorageBoxSubaccountBodyFixture::reader(),
            ['home_directory' => 42, 'password' => 42],
        ];
        yield 'CreateStorageBoxSubaccountResponse201' => [
            CreateStorageBoxSubaccountResponse201Fixture::build(),
            CreateStorageBoxSubaccountResponse201Fixture::reader(),
            ['subaccount' => 'not-an-object', 'action' => 'not-an-object'],
        ];
        yield 'CreateStorageBoxSubaccountResponse201Subaccount' => [
            CreateStorageBoxSubaccountResponse201SubaccountFixture::build(),
            CreateStorageBoxSubaccountResponse201SubaccountFixture::reader(),
            ['id' => 'not-a-number', 'storage_box' => 'not-a-number'],
        ];
        yield 'ChangeStorageBoxSubaccountHomeDirectoryBody' => [
            ChangeStorageBoxSubaccountHomeDirectoryBodyFixture::build(),
            ChangeStorageBoxSubaccountHomeDirectoryBodyFixture::reader(),
            ['home_directory' => 42],
        ];
        yield 'ListStorageBoxSnapshotsResponse200' => [
            ListStorageBoxSnapshotsResponse200Fixture::build(),
            ListStorageBoxSnapshotsResponse200Fixture::reader(),
            ['snapshots' => 'not-an-object'],
        ];
        yield 'CreateStorageBoxSnapshotResponse201' => [
            CreateStorageBoxSnapshotResponse201Fixture::build(),
            CreateStorageBoxSnapshotResponse201Fixture::reader(),
            ['snapshot' => 'not-an-object', 'action' => 'not-an-object'],
        ];
        yield 'CreateStorageBoxSnapshotResponse201Snapshot' => [
            CreateStorageBoxSnapshotResponse201SnapshotFixture::build(),
            CreateStorageBoxSnapshotResponse201SnapshotFixture::reader(),
            ['id' => 'not-a-number', 'storage_box' => 'not-a-number'],
        ];
        yield 'ListStorageBoxTypesResponse200' => [
            ListStorageBoxTypesResponse200Fixture::build(),
            ListStorageBoxTypesResponse200Fixture::reader(),
            ['storage_box_types' => 'not-an-object', 'meta' => 'not-an-object'],
        ];
        yield 'GetStorageBoxTypeResponse200' => [
            GetStorageBoxTypeResponse200Fixture::build(),
            GetStorageBoxTypeResponse200Fixture::reader(),
            ['storage_box_type' => 'not-an-object'],
        ];
    }

    /**
     * Each model whose values all pass their constraints, with those constraints.
     *
     * @return iterable<string, array{SelfNormalizingModel, list<Constraint>}>
     */
    public static function modelsWithTheirConstraints(): iterable
    {
        yield 'ServiceTCP' => [ServiceTCPFixture::build(), ServiceTCPFixture::constraints()];
        yield 'ServiceHTTPProtocol' => [ServiceHTTPProtocolFixture::build(), ServiceHTTPProtocolFixture::constraints()];
        yield 'ServiceHTTPSProtocol' => [
            ServiceHTTPSProtocolFixture::build(),
            ServiceHTTPSProtocolFixture::constraints(),
        ];
        yield 'TargetTypeServer' => [TargetTypeServerFixture::build(), TargetTypeServerFixture::constraints()];
        yield 'TargetTypeLabelSelector' => [
            TargetTypeLabelSelectorFixture::build(),
            TargetTypeLabelSelectorFixture::constraints(),
        ];
        yield 'TargetTypeIP' => [TargetTypeIPFixture::build(), TargetTypeIPFixture::constraints()];
        yield 'ZonePrimary' => [ZonePrimaryFixture::build(), ZonePrimaryFixture::constraints()];
        yield 'ZoneSecondary' => [ZoneSecondaryFixture::build(), ZoneSecondaryFixture::constraints()];
        yield 'Action' => [ActionFixture::build(), ActionFixture::constraints()];
        yield 'ActionError' => [ActionErrorFixture::build(), ActionErrorFixture::constraints()];
        yield 'ActionListResponse' => [ActionListResponseFixture::build(), ActionListResponseFixture::constraints()];
        yield 'ActionListResponseWithMeta' => [
            ActionListResponseWithMetaFixture::build(),
            ActionListResponseWithMetaFixture::constraints(),
        ];
        yield 'ActionResource' => [ActionResourceFixture::build(), ActionResourceFixture::constraints()];
        yield 'ActionResponse' => [ActionResponseFixture::build(), ActionResponseFixture::constraints()];
        yield 'Certificate' => [CertificateFixture::build(), CertificateFixture::constraints()];
        yield 'CertificateStatus' => [CertificateStatusFixture::build(), CertificateStatusFixture::constraints()];
        yield 'CertificateStatusError' => [
            CertificateStatusErrorFixture::build(),
            CertificateStatusErrorFixture::constraints(),
        ];
        yield 'CertificateUsedByItem' => [
            CertificateUsedByItemFixture::build(),
            CertificateUsedByItemFixture::constraints(),
        ];
        yield 'CertificateResponse' => [CertificateResponseFixture::build(), CertificateResponseFixture::constraints()];
        yield 'ChangeDeleteProtectionRequest' => [
            ChangeDeleteProtectionRequestFixture::build(),
            ChangeDeleteProtectionRequestFixture::constraints(),
        ];
        yield 'CreatedFrom' => [CreatedFromFixture::build(), CreatedFromFixture::constraints()];
        yield 'Datacenter' => [DatacenterFixture::build(), DatacenterFixture::constraints()];
        yield 'DatacenterServerTypes' => [
            DatacenterServerTypesFixture::build(),
            DatacenterServerTypesFixture::constraints(),
        ];
        yield 'DeprecationInfo' => [DeprecationInfoFixture::build(), DeprecationInfoFixture::constraints()];
        yield 'DnsPtr' => [DnsPtrFixture::build(), DnsPtrFixture::constraints()];
        yield 'ErrorResponse' => [ErrorResponseFixture::build(), ErrorResponseFixture::constraints()];
        yield 'ErrorResponseError' => [ErrorResponseErrorFixture::build(), ErrorResponseErrorFixture::constraints()];
        yield 'Firewall' => [FirewallFixture::build(), FirewallFixture::constraints()];
        yield 'FirewallRulesItem' => [FirewallRulesItemFixture::build(), FirewallRulesItemFixture::constraints()];
        yield 'FirewallAppliedToItem' => [
            FirewallAppliedToItemFixture::build(),
            FirewallAppliedToItemFixture::constraints(),
        ];
        yield 'FirewallAppliedToItemAppliedToResourcesItem' => [
            FirewallAppliedToItemAppliedToResourcesItemFixture::build(),
            FirewallAppliedToItemAppliedToResourcesItemFixture::constraints(),
        ];
        yield 'FirewallAppliedToServer' => [
            FirewallAppliedToServerFixture::build(),
            FirewallAppliedToServerFixture::constraints(),
        ];
        yield 'FirewallResource' => [FirewallResourceFixture::build(), FirewallResourceFixture::constraints()];
        yield 'FirewallResourceServer' => [
            FirewallResourceServerFixture::build(),
            FirewallResourceServerFixture::constraints(),
        ];
        yield 'FirewallResponse' => [FirewallResponseFixture::build(), FirewallResponseFixture::constraints()];
        yield 'FloatingIp' => [FloatingIpFixture::build(), FloatingIpFixture::constraints()];
        yield 'FloatingIpResponse' => [FloatingIpResponseFixture::build(), FloatingIpResponseFixture::constraints()];
        yield 'HealthCheckHttp' => [HealthCheckHttpFixture::build(), HealthCheckHttpFixture::constraints()];
        yield 'HealthStatus' => [HealthStatusFixture::build(), HealthStatusFixture::constraints()];
        yield 'Image' => [ImageFixture::build(), ImageFixture::constraints()];
        yield 'ImageResponse' => [ImageResponseFixture::build(), ImageResponseFixture::constraints()];
        yield 'Iso' => [IsoFixture::build(), IsoFixture::constraints()];
        yield 'LabelSelector' => [LabelSelectorFixture::build(), LabelSelectorFixture::constraints()];
        yield 'ListMeta' => [ListMetaFixture::build(), ListMetaFixture::constraints()];
        yield 'ListMetaPagination' => [ListMetaPaginationFixture::build(), ListMetaPaginationFixture::constraints()];
        yield 'LoadBalancer' => [LoadBalancerFixture::build(), LoadBalancerFixture::constraints()];
        yield 'LoadBalancerPublicNet' => [
            LoadBalancerPublicNetFixture::build(),
            LoadBalancerPublicNetFixture::constraints(),
        ];
        yield 'LoadBalancerPrivateNetItem' => [
            LoadBalancerPrivateNetItemFixture::build(),
            LoadBalancerPrivateNetItemFixture::constraints(),
        ];
        yield 'LoadBalancerAlgorithm2' => [
            LoadBalancerAlgorithm2Fixture::build(),
            LoadBalancerAlgorithm2Fixture::constraints(),
        ];
        yield 'LoadBalancerAlgorithm' => [
            LoadBalancerAlgorithmFixture::build(),
            LoadBalancerAlgorithmFixture::constraints(),
        ];
        yield 'LoadBalancerPublicIp' => [
            LoadBalancerPublicIpFixture::build(),
            LoadBalancerPublicIpFixture::constraints(),
        ];
        yield 'LoadBalancerResponse' => [
            LoadBalancerResponseFixture::build(),
            LoadBalancerResponseFixture::constraints(),
        ];
        yield 'LoadBalancerService' => [LoadBalancerServiceFixture::build(), LoadBalancerServiceFixture::constraints()];
        yield 'LoadBalancerServiceHealthCheck' => [
            LoadBalancerServiceHealthCheckFixture::build(),
            LoadBalancerServiceHealthCheckFixture::constraints(),
        ];
        yield 'LoadBalancerServiceBase' => [
            LoadBalancerServiceBaseFixture::build(),
            LoadBalancerServiceBaseFixture::constraints(),
        ];
        yield 'LoadBalancerServiceBaseHealthCheck' => [
            LoadBalancerServiceBaseHealthCheckFixture::build(),
            LoadBalancerServiceBaseHealthCheckFixture::constraints(),
        ];
        yield 'LoadBalancerServiceBaseHealthCheckHttp' => [
            LoadBalancerServiceBaseHealthCheckHttpFixture::build(),
            LoadBalancerServiceBaseHealthCheckHttpFixture::constraints(),
        ];
        yield 'LoadBalancerServiceHTTPProtocolProperties' => [
            LoadBalancerServiceHTTPProtocolPropertiesFixture::build(),
            LoadBalancerServiceHTTPProtocolPropertiesFixture::constraints(),
        ];
        yield 'LoadBalancerServiceHTTPProtocolPropertiesHttp' => [
            LoadBalancerServiceHTTPProtocolPropertiesHttpFixture::build(),
            LoadBalancerServiceHTTPProtocolPropertiesHttpFixture::constraints(),
        ];
        yield 'LoadBalancerServiceHTTPSProtocolProperties' => [
            LoadBalancerServiceHTTPSProtocolPropertiesFixture::build(),
            LoadBalancerServiceHTTPSProtocolPropertiesFixture::constraints(),
        ];
        yield 'LoadBalancerServiceHTTPSProtocolPropertiesHttp' => [
            LoadBalancerServiceHTTPSProtocolPropertiesHttpFixture::build(),
            LoadBalancerServiceHTTPSProtocolPropertiesHttpFixture::constraints(),
        ];
        yield 'LoadBalancerServiceTCPProperties' => [
            LoadBalancerServiceTCPPropertiesFixture::build(),
            LoadBalancerServiceTCPPropertiesFixture::constraints(),
        ];
        yield 'LoadBalancerTarget' => [LoadBalancerTargetFixture::build(), LoadBalancerTargetFixture::constraints()];
        yield 'LoadBalancerTargetIP' => [
            LoadBalancerTargetIPFixture::build(),
            LoadBalancerTargetIPFixture::constraints(),
        ];
        yield 'LoadBalancerTargetLabelSelector' => [
            LoadBalancerTargetLabelSelectorFixture::build(),
            LoadBalancerTargetLabelSelectorFixture::constraints(),
        ];
        yield 'LoadBalancerTargetRequestProperties' => [
            LoadBalancerTargetRequestPropertiesFixture::build(),
            LoadBalancerTargetRequestPropertiesFixture::constraints(),
        ];
        yield 'LoadBalancerTargetServer' => [
            LoadBalancerTargetServerFixture::build(),
            LoadBalancerTargetServerFixture::constraints(),
        ];
        yield 'LoadBalancerTargetServerRequest' => [
            LoadBalancerTargetServerRequestFixture::build(),
            LoadBalancerTargetServerRequestFixture::constraints(),
        ];
        yield 'LoadBalancerTargetTypeBase' => [
            LoadBalancerTargetTypeBaseFixture::build(),
            LoadBalancerTargetTypeBaseFixture::constraints(),
        ];
        yield 'LoadBalancerTargetTypeIPProperties' => [
            LoadBalancerTargetTypeIPPropertiesFixture::build(),
            LoadBalancerTargetTypeIPPropertiesFixture::constraints(),
        ];
        yield 'LoadBalancerTargetTypeLabelSelectorProperties' => [
            LoadBalancerTargetTypeLabelSelectorPropertiesFixture::build(),
            LoadBalancerTargetTypeLabelSelectorPropertiesFixture::constraints(),
        ];
        yield 'LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItem' => [
            LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItemFixture::build(),
            LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItemFixture::constraints(),
        ];
        yield 'LoadBalancerTargetTypeServerProperties' => [
            LoadBalancerTargetTypeServerPropertiesFixture::build(),
            LoadBalancerTargetTypeServerPropertiesFixture::constraints(),
        ];
        yield 'LoadBalancerType' => [LoadBalancerTypeFixture::build(), LoadBalancerTypeFixture::constraints()];
        yield 'Location' => [LocationFixture::build(), LocationFixture::constraints()];
        yield 'LocationPrice' => [LocationPriceFixture::build(), LocationPriceFixture::constraints()];
        yield 'MetricsResponse' => [MetricsResponseFixture::build(), MetricsResponseFixture::constraints()];
        yield 'MetricsResponseMetrics' => [
            MetricsResponseMetricsFixture::build(),
            MetricsResponseMetricsFixture::constraints(),
        ];
        yield 'Network' => [NetworkFixture::build(), NetworkFixture::constraints()];
        yield 'NetworkSubnetsItem' => [NetworkSubnetsItemFixture::build(), NetworkSubnetsItemFixture::constraints()];
        yield 'NetworkResponse' => [NetworkResponseFixture::build(), NetworkResponseFixture::constraints()];
        yield 'PlacementGroup' => [PlacementGroupFixture::build(), PlacementGroupFixture::constraints()];
        yield 'PlacementGroupResponse' => [
            PlacementGroupResponseFixture::build(),
            PlacementGroupResponseFixture::constraints(),
        ];
        yield 'Price' => [PriceFixture::build(), PriceFixture::constraints()];
        yield 'PricePerGbMonth' => [PricePerGbMonthFixture::build(), PricePerGbMonthFixture::constraints()];
        yield 'PrimaryIP' => [PrimaryIPFixture::build(), PrimaryIPFixture::constraints()];
        yield 'PrimaryIPResponse' => [PrimaryIPResponseFixture::build(), PrimaryIPResponseFixture::constraints()];
        yield 'PrimaryZoneProperties' => [
            PrimaryZonePropertiesFixture::build(),
            PrimaryZonePropertiesFixture::constraints(),
        ];
        yield 'Protection' => [ProtectionFixture::build(), ProtectionFixture::constraints()];
        yield 'RRSet' => [RRSetFixture::build(), RRSetFixture::constraints()];
        yield 'RRSetProtection' => [RRSetProtectionFixture::build(), RRSetProtectionFixture::constraints()];
        yield 'RRSetRecordsRequest' => [RRSetRecordsRequestFixture::build(), RRSetRecordsRequestFixture::constraints()];
        yield 'RRSetRequest' => [RRSetRequestFixture::build(), RRSetRequestFixture::constraints()];
        yield 'Record' => [RecordFixture::build(), RecordFixture::constraints()];
        yield 'RootPasswordResponse' => [
            RootPasswordResponseFixture::build(),
            RootPasswordResponseFixture::constraints(),
        ];
        yield 'Route' => [RouteFixture::build(), RouteFixture::constraints()];
        yield 'RrsetResponse' => [RrsetResponseFixture::build(), RrsetResponseFixture::constraints()];
        yield 'Rule' => [RuleFixture::build(), RuleFixture::constraints()];
        yield 'SecondaryZoneProperties' => [
            SecondaryZonePropertiesFixture::build(),
            SecondaryZonePropertiesFixture::constraints(),
        ];
        yield 'Server' => [ServerFixture::build(), ServerFixture::constraints()];
        yield 'ServerPublicNet' => [ServerPublicNetFixture::build(), ServerPublicNetFixture::constraints()];
        yield 'ServerPublicNetIpv4' => [ServerPublicNetIpv4Fixture::build(), ServerPublicNetIpv4Fixture::constraints()];
        yield 'ServerPublicNetIpv6' => [ServerPublicNetIpv6Fixture::build(), ServerPublicNetIpv6Fixture::constraints()];
        yield 'ServerPublicNetFirewallsItem' => [
            ServerPublicNetFirewallsItemFixture::build(),
            ServerPublicNetFirewallsItemFixture::constraints(),
        ];
        yield 'ServerPrivateNetItem' => [
            ServerPrivateNetItemFixture::build(),
            ServerPrivateNetItemFixture::constraints(),
        ];
        yield 'ServerProtection' => [ServerProtectionFixture::build(), ServerProtectionFixture::constraints()];
        yield 'ServerResponse' => [ServerResponseFixture::build(), ServerResponseFixture::constraints()];
        yield 'ServerType' => [ServerTypeFixture::build(), ServerTypeFixture::constraints()];
        yield 'ServerTypeLocationsItem' => [
            ServerTypeLocationsItemFixture::build(),
            ServerTypeLocationsItemFixture::constraints(),
        ];
        yield 'SshKey' => [SshKeyFixture::build(), SshKeyFixture::constraints()];
        yield 'SshKeyResponse' => [SshKeyResponseFixture::build(), SshKeyResponseFixture::constraints()];
        yield 'TypePricing' => [TypePricingFixture::build(), TypePricingFixture::constraints()];
        yield 'Volume' => [VolumeFixture::build(), VolumeFixture::constraints()];
        yield 'VolumeResponse' => [VolumeResponseFixture::build(), VolumeResponseFixture::constraints()];
        yield 'ZoneBase' => [ZoneBaseFixture::build(), ZoneBaseFixture::constraints()];
        yield 'ZoneBaseAuthoritativeNameservers' => [
            ZoneBaseAuthoritativeNameserversFixture::build(),
            ZoneBaseAuthoritativeNameserversFixture::constraints(),
        ];
        yield 'ZonePrimaryNameserver' => [
            ZonePrimaryNameserverFixture::build(),
            ZonePrimaryNameserverFixture::constraints(),
        ];
        yield 'ZoneResponse' => [ZoneResponseFixture::build(), ZoneResponseFixture::constraints()];
        yield 'Zonefile' => [ZonefileFixture::build(), ZonefileFixture::constraints()];
        yield 'ResetPasswordRequest' => [
            ResetPasswordRequestFixture::build(),
            ResetPasswordRequestFixture::constraints(),
        ];
        yield 'Snapshot' => [SnapshotFixture::build(), SnapshotFixture::constraints()];
        yield 'SnapshotStats' => [SnapshotStatsFixture::build(), SnapshotStatsFixture::constraints()];
        yield 'SnapshotResponse' => [SnapshotResponseFixture::build(), SnapshotResponseFixture::constraints()];
        yield 'StorageBox' => [StorageBoxFixture::build(), StorageBoxFixture::constraints()];
        yield 'StorageBoxAccessSettings' => [
            StorageBoxAccessSettingsFixture::build(),
            StorageBoxAccessSettingsFixture::constraints(),
        ];
        yield 'StorageBoxSnapshotPlan' => [
            StorageBoxSnapshotPlanFixture::build(),
            StorageBoxSnapshotPlanFixture::constraints(),
        ];
        yield 'StorageBoxStats' => [StorageBoxStatsFixture::build(), StorageBoxStatsFixture::constraints()];
        yield 'StorageBoxResponse' => [StorageBoxResponseFixture::build(), StorageBoxResponseFixture::constraints()];
        yield 'StorageBoxType' => [StorageBoxTypeFixture::build(), StorageBoxTypeFixture::constraints()];
        yield 'StorageBoxTypePricesItem' => [
            StorageBoxTypePricesItemFixture::build(),
            StorageBoxTypePricesItemFixture::constraints(),
        ];
        yield 'Subaccount' => [SubaccountFixture::build(), SubaccountFixture::constraints()];
        yield 'SubaccountAccessSettings' => [
            SubaccountAccessSettingsFixture::build(),
            SubaccountAccessSettingsFixture::constraints(),
        ];
        yield 'SubaccountResponse' => [SubaccountResponseFixture::build(), SubaccountResponseFixture::constraints()];
        yield 'ListCertificatesResponse200' => [
            ListCertificatesResponse200Fixture::build(),
            ListCertificatesResponse200Fixture::constraints(),
        ];
        yield 'CreateCertificateBody' => [
            CreateCertificateBodyFixture::build(),
            CreateCertificateBodyFixture::constraints(),
        ];
        yield 'CreateCertificateResponse201' => [
            CreateCertificateResponse201Fixture::build(),
            CreateCertificateResponse201Fixture::constraints(),
        ];
        yield 'UpdateCertificateBody' => [
            UpdateCertificateBodyFixture::build(),
            UpdateCertificateBodyFixture::constraints(),
        ];
        yield 'ListDatacentersResponse200' => [
            ListDatacentersResponse200Fixture::build(),
            ListDatacentersResponse200Fixture::constraints(),
        ];
        yield 'GetDatacenterResponse200' => [
            GetDatacenterResponse200Fixture::build(),
            GetDatacenterResponse200Fixture::constraints(),
        ];
        yield 'ListFirewallsResponse200' => [
            ListFirewallsResponse200Fixture::build(),
            ListFirewallsResponse200Fixture::constraints(),
        ];
        yield 'CreateFirewallBody' => [CreateFirewallBodyFixture::build(), CreateFirewallBodyFixture::constraints()];
        yield 'CreateFirewallResponse201' => [
            CreateFirewallResponse201Fixture::build(),
            CreateFirewallResponse201Fixture::constraints(),
        ];
        yield 'UpdateFirewallBody' => [UpdateFirewallBodyFixture::build(), UpdateFirewallBodyFixture::constraints()];
        yield 'ApplyFirewallToResourcesBody' => [
            ApplyFirewallToResourcesBodyFixture::build(),
            ApplyFirewallToResourcesBodyFixture::constraints(),
        ];
        yield 'RemoveFirewallFromResourcesBody' => [
            RemoveFirewallFromResourcesBodyFixture::build(),
            RemoveFirewallFromResourcesBodyFixture::constraints(),
        ];
        yield 'SetFirewallRulesBody' => [
            SetFirewallRulesBodyFixture::build(),
            SetFirewallRulesBodyFixture::constraints(),
        ];
        yield 'ListFloatingIpsResponse200' => [
            ListFloatingIpsResponse200Fixture::build(),
            ListFloatingIpsResponse200Fixture::constraints(),
        ];
        yield 'CreateFloatingIpBody' => [
            CreateFloatingIpBodyFixture::build(),
            CreateFloatingIpBodyFixture::constraints(),
        ];
        yield 'CreateFloatingIpResponse201' => [
            CreateFloatingIpResponse201Fixture::build(),
            CreateFloatingIpResponse201Fixture::constraints(),
        ];
        yield 'UpdateFloatingIpBody' => [
            UpdateFloatingIpBodyFixture::build(),
            UpdateFloatingIpBodyFixture::constraints(),
        ];
        yield 'AssignFloatingIpBody' => [
            AssignFloatingIpBodyFixture::build(),
            AssignFloatingIpBodyFixture::constraints(),
        ];
        yield 'ChangeFloatingIpDnsPtrBody' => [
            ChangeFloatingIpDnsPtrBodyFixture::build(),
            ChangeFloatingIpDnsPtrBodyFixture::constraints(),
        ];
        yield 'ChangeFloatingIpProtectionBody' => [
            ChangeFloatingIpProtectionBodyFixture::build(),
            ChangeFloatingIpProtectionBodyFixture::constraints(),
        ];
        yield 'ListImagesResponse200' => [
            ListImagesResponse200Fixture::build(),
            ListImagesResponse200Fixture::constraints(),
        ];
        yield 'UpdateImageBody' => [UpdateImageBodyFixture::build(), UpdateImageBodyFixture::constraints()];
        yield 'ListIsosResponse200' => [ListIsosResponse200Fixture::build(), ListIsosResponse200Fixture::constraints()];
        yield 'GetIsoResponse200' => [GetIsoResponse200Fixture::build(), GetIsoResponse200Fixture::constraints()];
        yield 'ListLoadBalancerTypesResponse200' => [
            ListLoadBalancerTypesResponse200Fixture::build(),
            ListLoadBalancerTypesResponse200Fixture::constraints(),
        ];
        yield 'GetLoadBalancerTypeResponse200' => [
            GetLoadBalancerTypeResponse200Fixture::build(),
            GetLoadBalancerTypeResponse200Fixture::constraints(),
        ];
        yield 'ListLoadBalancersResponse200' => [
            ListLoadBalancersResponse200Fixture::build(),
            ListLoadBalancersResponse200Fixture::constraints(),
        ];
        yield 'CreateLoadBalancerBody' => [
            CreateLoadBalancerBodyFixture::build(),
            CreateLoadBalancerBodyFixture::constraints(),
        ];
        yield 'CreateLoadBalancerBodyTargetsItem' => [
            CreateLoadBalancerBodyTargetsItemFixture::build(),
            CreateLoadBalancerBodyTargetsItemFixture::constraints(),
        ];
        yield 'CreateLoadBalancerBodyPublicNet' => [
            CreateLoadBalancerBodyPublicNetFixture::build(),
            CreateLoadBalancerBodyPublicNetFixture::constraints(),
        ];
        yield 'CreateLoadBalancerResponse201' => [
            CreateLoadBalancerResponse201Fixture::build(),
            CreateLoadBalancerResponse201Fixture::constraints(),
        ];
        yield 'UpdateLoadBalancerBody' => [
            UpdateLoadBalancerBodyFixture::build(),
            UpdateLoadBalancerBodyFixture::constraints(),
        ];
        yield 'AddLoadBalancerServiceBody' => [
            AddLoadBalancerServiceBodyFixture::build(),
            AddLoadBalancerServiceBodyFixture::constraints(),
        ];
        yield 'AddLoadBalancerServiceBodyHttp' => [
            AddLoadBalancerServiceBodyHttpFixture::build(),
            AddLoadBalancerServiceBodyHttpFixture::constraints(),
        ];
        yield 'AddLoadBalancerTargetBody' => [
            AddLoadBalancerTargetBodyFixture::build(),
            AddLoadBalancerTargetBodyFixture::constraints(),
        ];
        yield 'AttachLoadBalancerToNetworkBody' => [
            AttachLoadBalancerToNetworkBodyFixture::build(),
            AttachLoadBalancerToNetworkBodyFixture::constraints(),
        ];
        yield 'ChangeLoadBalancerDnsPtrBody' => [
            ChangeLoadBalancerDnsPtrBodyFixture::build(),
            ChangeLoadBalancerDnsPtrBodyFixture::constraints(),
        ];
        yield 'ChangeLoadBalancerTypeBody' => [
            ChangeLoadBalancerTypeBodyFixture::build(),
            ChangeLoadBalancerTypeBodyFixture::constraints(),
        ];
        yield 'DeleteLoadBalancerServiceBody' => [
            DeleteLoadBalancerServiceBodyFixture::build(),
            DeleteLoadBalancerServiceBodyFixture::constraints(),
        ];
        yield 'DetachLoadBalancerFromNetworkBody' => [
            DetachLoadBalancerFromNetworkBodyFixture::build(),
            DetachLoadBalancerFromNetworkBodyFixture::constraints(),
        ];
        yield 'UpdateLoadBalancerServiceBody' => [
            UpdateLoadBalancerServiceBodyFixture::build(),
            UpdateLoadBalancerServiceBodyFixture::constraints(),
        ];
        yield 'UpdateLoadBalancerServiceBodyHealthCheck' => [
            UpdateLoadBalancerServiceBodyHealthCheckFixture::build(),
            UpdateLoadBalancerServiceBodyHealthCheckFixture::constraints(),
        ];
        yield 'UpdateLoadBalancerServiceBodyHttp' => [
            UpdateLoadBalancerServiceBodyHttpFixture::build(),
            UpdateLoadBalancerServiceBodyHttpFixture::constraints(),
        ];
        yield 'ListLocationsResponse200' => [
            ListLocationsResponse200Fixture::build(),
            ListLocationsResponse200Fixture::constraints(),
        ];
        yield 'GetLocationResponse200' => [
            GetLocationResponse200Fixture::build(),
            GetLocationResponse200Fixture::constraints(),
        ];
        yield 'ListNetworksResponse200' => [
            ListNetworksResponse200Fixture::build(),
            ListNetworksResponse200Fixture::constraints(),
        ];
        yield 'CreateNetworkBody' => [CreateNetworkBodyFixture::build(), CreateNetworkBodyFixture::constraints()];
        yield 'CreateNetworkBodySubnetsItem' => [
            CreateNetworkBodySubnetsItemFixture::build(),
            CreateNetworkBodySubnetsItemFixture::constraints(),
        ];
        yield 'UpdateNetworkBody' => [UpdateNetworkBodyFixture::build(), UpdateNetworkBodyFixture::constraints()];
        yield 'AddNetworkSubnetBody' => [
            AddNetworkSubnetBodyFixture::build(),
            AddNetworkSubnetBodyFixture::constraints(),
        ];
        yield 'ChangeNetworkIpRangeBody' => [
            ChangeNetworkIpRangeBodyFixture::build(),
            ChangeNetworkIpRangeBodyFixture::constraints(),
        ];
        yield 'DeleteNetworkSubnetBody' => [
            DeleteNetworkSubnetBodyFixture::build(),
            DeleteNetworkSubnetBodyFixture::constraints(),
        ];
        yield 'ListNetworkMembersResponse200' => [
            ListNetworkMembersResponse200Fixture::build(),
            ListNetworkMembersResponse200Fixture::constraints(),
        ];
        yield 'ListNetworkMembersResponse200MembersItem' => [
            ListNetworkMembersResponse200MembersItemFixture::build(),
            ListNetworkMembersResponse200MembersItemFixture::constraints(),
        ];
        yield 'ListPlacementGroupsResponse200' => [
            ListPlacementGroupsResponse200Fixture::build(),
            ListPlacementGroupsResponse200Fixture::constraints(),
        ];
        yield 'CreatePlacementGroupBody' => [
            CreatePlacementGroupBodyFixture::build(),
            CreatePlacementGroupBodyFixture::constraints(),
        ];
        yield 'CreatePlacementGroupResponse201' => [
            CreatePlacementGroupResponse201Fixture::build(),
            CreatePlacementGroupResponse201Fixture::constraints(),
        ];
        yield 'UpdatePlacementGroupBody' => [
            UpdatePlacementGroupBodyFixture::build(),
            UpdatePlacementGroupBodyFixture::constraints(),
        ];
        yield 'GetPricingResponse200' => [
            GetPricingResponse200Fixture::build(),
            GetPricingResponse200Fixture::constraints(),
        ];
        yield 'GetPricingResponse200Pricing' => [
            GetPricingResponse200PricingFixture::build(),
            GetPricingResponse200PricingFixture::constraints(),
        ];
        yield 'GetPricingResponse200PricingPrimaryIpsItem' => [
            GetPricingResponse200PricingPrimaryIpsItemFixture::build(),
            GetPricingResponse200PricingPrimaryIpsItemFixture::constraints(),
        ];
        yield 'GetPricingResponse200PricingPrimaryIpsItemPricesItem' => [
            GetPricingResponse200PricingPrimaryIpsItemPricesItemFixture::build(),
            GetPricingResponse200PricingPrimaryIpsItemPricesItemFixture::constraints(),
        ];
        yield 'GetPricingResponse200PricingFloatingIpsItem' => [
            GetPricingResponse200PricingFloatingIpsItemFixture::build(),
            GetPricingResponse200PricingFloatingIpsItemFixture::constraints(),
        ];
        yield 'GetPricingResponse200PricingFloatingIpsItemPricesItem' => [
            GetPricingResponse200PricingFloatingIpsItemPricesItemFixture::build(),
            GetPricingResponse200PricingFloatingIpsItemPricesItemFixture::constraints(),
        ];
        yield 'GetPricingResponse200PricingServerBackup' => [
            GetPricingResponse200PricingServerBackupFixture::build(),
            GetPricingResponse200PricingServerBackupFixture::constraints(),
        ];
        yield 'GetPricingResponse200PricingFloatingIp' => [
            GetPricingResponse200PricingFloatingIpFixture::build(),
            GetPricingResponse200PricingFloatingIpFixture::constraints(),
        ];
        yield 'ListPrimaryIpsResponse200' => [
            ListPrimaryIpsResponse200Fixture::build(),
            ListPrimaryIpsResponse200Fixture::constraints(),
        ];
        yield 'CreatePrimaryIpBody' => [CreatePrimaryIpBodyFixture::build(), CreatePrimaryIpBodyFixture::constraints()];
        yield 'CreatePrimaryIpResponse201' => [
            CreatePrimaryIpResponse201Fixture::build(),
            CreatePrimaryIpResponse201Fixture::constraints(),
        ];
        yield 'UpdatePrimaryIpBody' => [UpdatePrimaryIpBodyFixture::build(), UpdatePrimaryIpBodyFixture::constraints()];
        yield 'AssignPrimaryIpBody' => [AssignPrimaryIpBodyFixture::build(), AssignPrimaryIpBodyFixture::constraints()];
        yield 'ChangePrimaryIpDnsPtrBody' => [
            ChangePrimaryIpDnsPtrBodyFixture::build(),
            ChangePrimaryIpDnsPtrBodyFixture::constraints(),
        ];
        yield 'ChangePrimaryIpProtectionBody' => [
            ChangePrimaryIpProtectionBodyFixture::build(),
            ChangePrimaryIpProtectionBodyFixture::constraints(),
        ];
        yield 'ListServerTypesResponse200' => [
            ListServerTypesResponse200Fixture::build(),
            ListServerTypesResponse200Fixture::constraints(),
        ];
        yield 'GetServerTypeResponse200' => [
            GetServerTypeResponse200Fixture::build(),
            GetServerTypeResponse200Fixture::constraints(),
        ];
        yield 'ListServersResponse200' => [
            ListServersResponse200Fixture::build(),
            ListServersResponse200Fixture::constraints(),
        ];
        yield 'CreateServerBody' => [CreateServerBodyFixture::build(), CreateServerBodyFixture::constraints()];
        yield 'CreateServerBodyFirewallsItem' => [
            CreateServerBodyFirewallsItemFixture::build(),
            CreateServerBodyFirewallsItemFixture::constraints(),
        ];
        yield 'CreateServerBodyPublicNet' => [
            CreateServerBodyPublicNetFixture::build(),
            CreateServerBodyPublicNetFixture::constraints(),
        ];
        yield 'CreateServerResponse201' => [
            CreateServerResponse201Fixture::build(),
            CreateServerResponse201Fixture::constraints(),
        ];
        yield 'UpdateServerBody' => [UpdateServerBodyFixture::build(), UpdateServerBodyFixture::constraints()];
        yield 'AddServerToPlacementGroupBody' => [
            AddServerToPlacementGroupBodyFixture::build(),
            AddServerToPlacementGroupBodyFixture::constraints(),
        ];
        yield 'AttachServerIsoBody' => [AttachServerIsoBodyFixture::build(), AttachServerIsoBodyFixture::constraints()];
        yield 'AttachServerToNetworkBody' => [
            AttachServerToNetworkBodyFixture::build(),
            AttachServerToNetworkBodyFixture::constraints(),
        ];
        yield 'ChangeServerAliasIpsBody' => [
            ChangeServerAliasIpsBodyFixture::build(),
            ChangeServerAliasIpsBodyFixture::constraints(),
        ];
        yield 'ChangeServerDnsPtrBody' => [
            ChangeServerDnsPtrBodyFixture::build(),
            ChangeServerDnsPtrBodyFixture::constraints(),
        ];
        yield 'ChangeServerProtectionBody' => [
            ChangeServerProtectionBodyFixture::build(),
            ChangeServerProtectionBodyFixture::constraints(),
        ];
        yield 'ChangeServerTypeBody' => [
            ChangeServerTypeBodyFixture::build(),
            ChangeServerTypeBodyFixture::constraints(),
        ];
        yield 'CreateServerImageBody' => [
            CreateServerImageBodyFixture::build(),
            CreateServerImageBodyFixture::constraints(),
        ];
        yield 'CreateServerImageResponse201' => [
            CreateServerImageResponse201Fixture::build(),
            CreateServerImageResponse201Fixture::constraints(),
        ];
        yield 'DetachServerFromNetworkBody' => [
            DetachServerFromNetworkBodyFixture::build(),
            DetachServerFromNetworkBodyFixture::constraints(),
        ];
        yield 'EnableServerRescueBody' => [
            EnableServerRescueBodyFixture::build(),
            EnableServerRescueBodyFixture::constraints(),
        ];
        yield 'RebuildServerBody' => [RebuildServerBodyFixture::build(), RebuildServerBodyFixture::constraints()];
        yield 'RebuildServerResponse201' => [
            RebuildServerResponse201Fixture::build(),
            RebuildServerResponse201Fixture::constraints(),
        ];
        yield 'RequestServerConsoleResponse201' => [
            RequestServerConsoleResponse201Fixture::build(),
            RequestServerConsoleResponse201Fixture::constraints(),
        ];
        yield 'ListSshKeysResponse200' => [
            ListSshKeysResponse200Fixture::build(),
            ListSshKeysResponse200Fixture::constraints(),
        ];
        yield 'CreateSshKeyBody' => [CreateSshKeyBodyFixture::build(), CreateSshKeyBodyFixture::constraints()];
        yield 'UpdateSshKeyBody' => [UpdateSshKeyBodyFixture::build(), UpdateSshKeyBodyFixture::constraints()];
        yield 'ListVolumesResponse200' => [
            ListVolumesResponse200Fixture::build(),
            ListVolumesResponse200Fixture::constraints(),
        ];
        yield 'CreateVolumeBody' => [CreateVolumeBodyFixture::build(), CreateVolumeBodyFixture::constraints()];
        yield 'CreateVolumeResponse201' => [
            CreateVolumeResponse201Fixture::build(),
            CreateVolumeResponse201Fixture::constraints(),
        ];
        yield 'UpdateVolumeBody' => [UpdateVolumeBodyFixture::build(), UpdateVolumeBodyFixture::constraints()];
        yield 'AttachVolumeBody' => [AttachVolumeBodyFixture::build(), AttachVolumeBodyFixture::constraints()];
        yield 'ResizeVolumeBody' => [ResizeVolumeBodyFixture::build(), ResizeVolumeBodyFixture::constraints()];
        yield 'ListZonesResponse200' => [
            ListZonesResponse200Fixture::build(),
            ListZonesResponse200Fixture::constraints(),
        ];
        yield 'CreateZoneBody' => [CreateZoneBodyFixture::build(), CreateZoneBodyFixture::constraints()];
        yield 'CreateZoneResponse201' => [
            CreateZoneResponse201Fixture::build(),
            CreateZoneResponse201Fixture::constraints(),
        ];
        yield 'UpdateZoneBody' => [UpdateZoneBodyFixture::build(), UpdateZoneBodyFixture::constraints()];
        yield 'ChangeZonePrimaryNameserversBody' => [
            ChangeZonePrimaryNameserversBodyFixture::build(),
            ChangeZonePrimaryNameserversBodyFixture::constraints(),
        ];
        yield 'ChangeZoneTtlBody' => [ChangeZoneTtlBodyFixture::build(), ChangeZoneTtlBodyFixture::constraints()];
        yield 'ListZoneRrsetsResponse200' => [
            ListZoneRrsetsResponse200Fixture::build(),
            ListZoneRrsetsResponse200Fixture::constraints(),
        ];
        yield 'ListZoneRrsetsResponse200Meta' => [
            ListZoneRrsetsResponse200MetaFixture::build(),
            ListZoneRrsetsResponse200MetaFixture::constraints(),
        ];
        yield 'ListZoneRrsetsResponse200MetaPagination' => [
            ListZoneRrsetsResponse200MetaPaginationFixture::build(),
            ListZoneRrsetsResponse200MetaPaginationFixture::constraints(),
        ];
        yield 'CreateZoneRrsetResponse201' => [
            CreateZoneRrsetResponse201Fixture::build(),
            CreateZoneRrsetResponse201Fixture::constraints(),
        ];
        yield 'UpdateZoneRrsetBody' => [UpdateZoneRrsetBodyFixture::build(), UpdateZoneRrsetBodyFixture::constraints()];
        yield 'ChangeZoneRrsetTtlBody' => [
            ChangeZoneRrsetTtlBodyFixture::build(),
            ChangeZoneRrsetTtlBodyFixture::constraints(),
        ];
        yield 'AddZoneRrsetRecordsBody' => [
            AddZoneRrsetRecordsBodyFixture::build(),
            AddZoneRrsetRecordsBodyFixture::constraints(),
        ];
        yield 'UpdateZoneRrsetRecordsBody' => [
            UpdateZoneRrsetRecordsBodyFixture::build(),
            UpdateZoneRrsetRecordsBodyFixture::constraints(),
        ];
        yield 'UpdateZoneRrsetRecordsBodyRecordsItem' => [
            UpdateZoneRrsetRecordsBodyRecordsItemFixture::build(),
            UpdateZoneRrsetRecordsBodyRecordsItemFixture::constraints(),
        ];
        yield 'ListStorageBoxesResponse200' => [
            ListStorageBoxesResponse200Fixture::build(),
            ListStorageBoxesResponse200Fixture::constraints(),
        ];
        yield 'CreateStorageBoxBody' => [
            CreateStorageBoxBodyFixture::build(),
            CreateStorageBoxBodyFixture::constraints(),
        ];
        yield 'CreateStorageBoxBodyAccessSettings' => [
            CreateStorageBoxBodyAccessSettingsFixture::build(),
            CreateStorageBoxBodyAccessSettingsFixture::constraints(),
        ];
        yield 'CreateStorageBoxResponse201' => [
            CreateStorageBoxResponse201Fixture::build(),
            CreateStorageBoxResponse201Fixture::constraints(),
        ];
        yield 'UpdateStorageBoxBody' => [
            UpdateStorageBoxBodyFixture::build(),
            UpdateStorageBoxBodyFixture::constraints(),
        ];
        yield 'ListStorageBoxFoldersResponse200' => [
            ListStorageBoxFoldersResponse200Fixture::build(),
            ListStorageBoxFoldersResponse200Fixture::constraints(),
        ];
        yield 'ChangeStorageBoxTypeBody' => [
            ChangeStorageBoxTypeBodyFixture::build(),
            ChangeStorageBoxTypeBodyFixture::constraints(),
        ];
        yield 'UpdateStorageBoxAccessSettingsBody' => [
            UpdateStorageBoxAccessSettingsBodyFixture::build(),
            UpdateStorageBoxAccessSettingsBodyFixture::constraints(),
        ];
        yield 'RollbackStorageBoxSnapshotBody' => [
            RollbackStorageBoxSnapshotBodyFixture::build(),
            RollbackStorageBoxSnapshotBodyFixture::constraints(),
        ];
        yield 'EnableStorageBoxSnapshotPlanBody' => [
            EnableStorageBoxSnapshotPlanBodyFixture::build(),
            EnableStorageBoxSnapshotPlanBodyFixture::constraints(),
        ];
        yield 'ListStorageBoxSubaccountsResponse200' => [
            ListStorageBoxSubaccountsResponse200Fixture::build(),
            ListStorageBoxSubaccountsResponse200Fixture::constraints(),
        ];
        yield 'CreateStorageBoxSubaccountBody' => [
            CreateStorageBoxSubaccountBodyFixture::build(),
            CreateStorageBoxSubaccountBodyFixture::constraints(),
        ];
        yield 'CreateStorageBoxSubaccountBodyAccessSettings' => [
            CreateStorageBoxSubaccountBodyAccessSettingsFixture::build(),
            CreateStorageBoxSubaccountBodyAccessSettingsFixture::constraints(),
        ];
        yield 'CreateStorageBoxSubaccountResponse201' => [
            CreateStorageBoxSubaccountResponse201Fixture::build(),
            CreateStorageBoxSubaccountResponse201Fixture::constraints(),
        ];
        yield 'CreateStorageBoxSubaccountResponse201Subaccount' => [
            CreateStorageBoxSubaccountResponse201SubaccountFixture::build(),
            CreateStorageBoxSubaccountResponse201SubaccountFixture::constraints(),
        ];
        yield 'UpdateStorageBoxSubaccountBody' => [
            UpdateStorageBoxSubaccountBodyFixture::build(),
            UpdateStorageBoxSubaccountBodyFixture::constraints(),
        ];
        yield 'ChangeStorageBoxSubaccountHomeDirectoryBody' => [
            ChangeStorageBoxSubaccountHomeDirectoryBodyFixture::build(),
            ChangeStorageBoxSubaccountHomeDirectoryBodyFixture::constraints(),
        ];
        yield 'UpdateStorageBoxSubaccountAccessSettingsBody' => [
            UpdateStorageBoxSubaccountAccessSettingsBodyFixture::build(),
            UpdateStorageBoxSubaccountAccessSettingsBodyFixture::constraints(),
        ];
        yield 'ListStorageBoxSnapshotsResponse200' => [
            ListStorageBoxSnapshotsResponse200Fixture::build(),
            ListStorageBoxSnapshotsResponse200Fixture::constraints(),
        ];
        yield 'CreateStorageBoxSnapshotBody' => [
            CreateStorageBoxSnapshotBodyFixture::build(),
            CreateStorageBoxSnapshotBodyFixture::constraints(),
        ];
        yield 'CreateStorageBoxSnapshotResponse201' => [
            CreateStorageBoxSnapshotResponse201Fixture::build(),
            CreateStorageBoxSnapshotResponse201Fixture::constraints(),
        ];
        yield 'CreateStorageBoxSnapshotResponse201Snapshot' => [
            CreateStorageBoxSnapshotResponse201SnapshotFixture::build(),
            CreateStorageBoxSnapshotResponse201SnapshotFixture::constraints(),
        ];
        yield 'UpdateStorageBoxSnapshotBody' => [
            UpdateStorageBoxSnapshotBodyFixture::build(),
            UpdateStorageBoxSnapshotBodyFixture::constraints(),
        ];
        yield 'ListStorageBoxTypesResponse200' => [
            ListStorageBoxTypesResponse200Fixture::build(),
            ListStorageBoxTypesResponse200Fixture::constraints(),
        ];
        yield 'GetStorageBoxTypeResponse200' => [
            GetStorageBoxTypeResponse200Fixture::build(),
            GetStorageBoxTypeResponse200Fixture::constraints(),
        ];
    }
}
