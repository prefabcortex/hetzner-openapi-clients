<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Architecture;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\LocationPrice;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Model\ServerType;
use Prefabcortex\Hetzner\Model\ServerTypeCpuType;
use Prefabcortex\Hetzner\Model\ServerTypeLocationsItem;
use Prefabcortex\Hetzner\Model\ServerTypeStorageType;
use Prefabcortex\Hetzner\Validator\ServerTypeConstraint;
use Symfony\Component\Validator\Constraint;

final class ServerTypeFixture
{
    public static function build(): ServerType
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

        return ServerType::builder(
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
    }

    /** @return callable(array<int|string, mixed>): ServerType */
    public static function reader(): callable
    {
        return ServerType::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ServerTypeConstraint::constraints();
    }
}
