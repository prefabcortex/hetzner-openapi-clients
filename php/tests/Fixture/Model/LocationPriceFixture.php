<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LocationPrice;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Validator\LocationPriceConstraint;
use Symfony\Component\Validator\Constraint;

final class LocationPriceFixture
{
    public static function build(): LocationPrice
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

        return LocationPrice::builder(
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
    }

    /** @return callable(array<int|string, mixed>): LocationPrice */
    public static function reader(): callable
    {
        return LocationPrice::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LocationPriceConstraint::constraints();
    }
}
