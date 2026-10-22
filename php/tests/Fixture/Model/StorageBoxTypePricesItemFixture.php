<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Model\StorageBoxTypePricesItem;
use Prefabcortex\Hetzner\Validator\StorageBoxTypePricesItemConstraint;
use Symfony\Component\Validator\Constraint;

final class StorageBoxTypePricesItemFixture
{
    public static function build(): StorageBoxTypePricesItem
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

        return StorageBoxTypePricesItem::builder(
            // location
            'fsn1',
            // priceHourly
            $priceHourly,
            // priceMonthly
            $priceMonthly,
            // setupFee
            $setupFee,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): StorageBoxTypePricesItem */
    public static function reader(): callable
    {
        return StorageBoxTypePricesItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return StorageBoxTypePricesItemConstraint::constraints();
    }
}
