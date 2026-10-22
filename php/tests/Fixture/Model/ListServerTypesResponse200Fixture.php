<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Architecture;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Model\ListServerTypesResponse200;
use Prefabcortex\Hetzner\Model\LocationPrice;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Model\ServerType;
use Prefabcortex\Hetzner\Model\ServerTypeCpuType;
use Prefabcortex\Hetzner\Model\ServerTypeLocationsItem;
use Prefabcortex\Hetzner\Model\ServerTypeStorageType;
use Prefabcortex\Hetzner\Validator\ListServerTypesResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListServerTypesResponse200Fixture
{
    public static function build(): ListServerTypesResponse200
    {
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
        $deprecation = DeprecationInfo::builder(
            // unavailableAfter
            new DateTime('2024-01-01'),
            // announced
            new DateTime('2024-01-01'),
        )->build();
        $serverTypeLocationsItem = ServerTypeLocationsItem::builder(
            // id
            42,
            // name
            'fsn1',
            // deprecation
            $deprecation,
            // recommended
            false,
            // available
            true,
        )->build();
        $serverType = ServerType::builder(
            // id
            1,
            // name
            'cpx22',
            // description
            'CPX22',
            // cores
            2,
            // memory
            4.0,
            // disk
            80.0,
            // deprecated
            false,
            // prices
            [$locationPrice],
            // storageType
            ServerTypeStorageType::local,
            // cpuType
            ServerTypeCpuType::shared,
            // architecture
            Architecture::x86,
            // locations
            [$serverTypeLocationsItem],
        )
            ->setCategory('Shared vCPU')
            ->build();
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

        return ListServerTypesResponse200::builder(
            // serverTypes
            [$serverType],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListServerTypesResponse200 */
    public static function reader(): callable
    {
        return ListServerTypesResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListServerTypesResponse200Constraint::constraints();
    }
}
