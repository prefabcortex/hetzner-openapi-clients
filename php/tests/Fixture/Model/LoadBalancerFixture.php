<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\HealthCheckProtocol;
use Prefabcortex\Hetzner\Model\HealthStatus;
use Prefabcortex\Hetzner\Model\HealthStatusDetail;
use Prefabcortex\Hetzner\Model\HealthStatusStatus;
use Prefabcortex\Hetzner\Model\LoadBalancer;
use Prefabcortex\Hetzner\Model\LoadBalancerAlgorithm2;
use Prefabcortex\Hetzner\Model\LoadBalancerAlgorithmType;
use Prefabcortex\Hetzner\Model\LoadBalancerPrivateNetItem;
use Prefabcortex\Hetzner\Model\LoadBalancerPublicIp;
use Prefabcortex\Hetzner\Model\LoadBalancerPublicNet;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceBaseHealthCheck;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceProtocol;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetServer;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetType;
use Prefabcortex\Hetzner\Model\LoadBalancerType;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Model\LocationPrice;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Model\ServiceTCP;
use Prefabcortex\Hetzner\Model\TargetTypeServer;
use Prefabcortex\Hetzner\Validator\LoadBalancerConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerFixture
{
    public static function build(): LoadBalancer
    {
        $ipv4 = LoadBalancerPublicIp::builder(
            // id
            42,
            // ip
            '1.2.3.4',
            // blocked
            false,
            // dnsPtr
            'lb1.example.com',
        )->build();
        $ipv6 = LoadBalancerPublicIp::builder(
            // id
            42,
            // ip
            '1.2.3.4',
            // blocked
            false,
            // dnsPtr
            'lb1.example.com',
        )->build();
        $publicNet = LoadBalancerPublicNet::builder(
            // enabled
            true,
            // ipv4
            $ipv4,
            // ipv6
            $ipv6,
        )->build();
        $loadBalancerPrivateNetItem = LoadBalancerPrivateNetItem::builder(
            // network
            4711,
            // ip
            '10.0.0.2',
        )->build();
        $location = Location::builder(
            // id
            42,
            // name
            'fsn1',
            // description
            'Falkenstein DC Park 1',
            // country
            'DE',
            // city
            'Falkenstein',
            // latitude
            50.47612,
            // longitude
            12.370071,
            // networkZone
            'eu-central',
        )->build();
        $deprecation = DeprecationInfo::builder(
            // unavailableAfter
            new DateTime('2024-01-01'),
            // announced
            new DateTime('2024-01-01'),
        )->build();
        $priceHourly = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $priceMonthly = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $pricePerTbTraffic = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $locationPrice = LocationPrice::builder(
            // location
            'fsn1',
            // priceHourly
            $priceHourly,
            // priceMonthly
            $priceMonthly,
            // includedTraffic
            654321,
            // pricePerTbTraffic
            $pricePerTbTraffic,
        )->build();
        $loadBalancerType = LoadBalancerType::builder(
            // id
            1,
            // name
            'lb11',
            // description
            'LB11',
            // maxConnections
            20000,
            // maxServices
            5,
            // maxTargets
            25,
            // maxAssignedCertificates
            10,
            // deprecated
            new DateTime('2024-01-01'),
            // deprecation
            $deprecation,
            // prices
            [$locationPrice],
        )->build();
        $protection = Protection::builder(false)->build();
        $healthCheck = LoadBalancerServiceBaseHealthCheck::builder(
            // protocol
            HealthCheckProtocol::tcp,
            // port
            4711,
            // interval
            15,
            // timeout
            10,
            // retries
            3,
        )->build();
        $services = ServiceTCP::builder(
            // protocol
            LoadBalancerServiceProtocol::tcp,
            // listenPort
            443,
            // destinationPort
            80,
            // proxyprotocol
            false,
            // healthCheck
            $healthCheck,
        )->build();
        $server = LoadBalancerTargetServer::builder(
            // id
            80,
            // ip
            '2001:db8::1',
        )->build();
        $healthStatus = HealthStatus::builder(
            // listenPort
            443,
            // status
            HealthStatusStatus::healthy,
        )
            ->setDetail(HealthStatusDetail::unexpected_http_status)
            ->setHttpStatusCode(503)
            ->build();
        $targets = TargetTypeServer::builder(
            // type
            LoadBalancerTargetType::server,
            // server
            $server,
            // healthStatus
            [$healthStatus],
            // usePrivateIp
            false,
        )->build();
        $algorithm = LoadBalancerAlgorithm2::builder(LoadBalancerAlgorithmType::round_robin)->build();

        return LoadBalancer::builder(
            // id
            42,
            // name
            'my-resource',
            // publicNet
            $publicNet,
            // privateNet
            [$loadBalancerPrivateNetItem],
            // location
            $location,
            // loadBalancerType
            $loadBalancerType,
            // protection
            $protection,
            // labels
            [],
            // created
            new DateTime('2024-01-01'),
            // services
            [$services],
            // targets
            [$targets],
            // algorithm
            $algorithm,
            // outgoingTraffic
            0,
            // ingoingTraffic
            0,
            // includedTraffic
            10000,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancer */
    public static function reader(): callable
    {
        return LoadBalancer::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerConstraint::constraints();
    }
}
