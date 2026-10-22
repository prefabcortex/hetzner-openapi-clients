<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\ListLoadBalancerTypesResponse200;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Model\LoadBalancerType;
use Prefabcortex\Hetzner\Model\LocationPrice;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Validator\ListLoadBalancerTypesResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListLoadBalancerTypesResponse200Fixture
{
    public static function build(): ListLoadBalancerTypesResponse200
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
        $pagination = ListMetaPagination::builder(
            // page
            3,
            // perPage
            25,
            // previousPage
            2,
            // nextPage
            4,
            // lastPage
            4,
            // totalEntries
            100,
        )->build();
        $meta = ListMeta::builder($pagination)->build();

        return ListLoadBalancerTypesResponse200::builder(
            // loadBalancerTypes
            [$loadBalancerType],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListLoadBalancerTypesResponse200 */
    public static function reader(): callable
    {
        return ListLoadBalancerTypesResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListLoadBalancerTypesResponse200Constraint::constraints();
    }
}
