<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\GetLoadBalancerTypeResponse200;
use Prefabcortex\Hetzner\Model\LoadBalancerType;
use Prefabcortex\Hetzner\Model\LocationPrice;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Validator\GetLoadBalancerTypeResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class GetLoadBalancerTypeResponse200Fixture
{
    public static function build(): GetLoadBalancerTypeResponse200
    {
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

        return GetLoadBalancerTypeResponse200::builder($loadBalancerType)->build();
    }

    /** @return callable(array<int|string, mixed>): GetLoadBalancerTypeResponse200 */
    public static function reader(): callable
    {
        return GetLoadBalancerTypeResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return GetLoadBalancerTypeResponse200Constraint::constraints();
    }
}
