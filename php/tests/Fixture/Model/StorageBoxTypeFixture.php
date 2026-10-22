<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Model\StorageBoxType;
use Prefabcortex\Hetzner\Model\StorageBoxTypePricesItem;
use Prefabcortex\Hetzner\Validator\StorageBoxTypeConstraint;
use Symfony\Component\Validator\Constraint;

final class StorageBoxTypeFixture
{
    public static function build(): StorageBoxType
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
        $setupFee = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $storageBoxTypePricesItem = StorageBoxTypePricesItem::builder(
            // location
            'fsn1',
            // priceHourly
            $priceHourly,
            // priceMonthly
            $priceMonthly,
            // setupFee
            $setupFee,
        )->build();
        $deprecation = DeprecationInfo::builder(
            // unavailableAfter
            new DateTime('2024-01-01'),
            // announced
            new DateTime('2024-01-01'),
        )->build();

        return StorageBoxType::builder(
            // id
            42,
            // name
            'bx11',
            // description
            'BX11',
            // snapshotLimit
            10,
            // automaticSnapshotLimit
            10,
            // subaccountsLimit
            200,
            // size
            1073741824,
            // prices
            [$storageBoxTypePricesItem],
            // deprecation
            $deprecation,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): StorageBoxType */
    public static function reader(): callable
    {
        return StorageBoxType::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return StorageBoxTypeConstraint::constraints();
    }
}
