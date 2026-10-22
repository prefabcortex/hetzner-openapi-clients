<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LocationPrice;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Model\TypePricing;
use Prefabcortex\Hetzner\Validator\TypePricingConstraint;
use Symfony\Component\Validator\Constraint;

final class TypePricingFixture
{
    public static function build(): TypePricing
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

        return TypePricing::builder(
            // id
            104,
            // name
            'cpx22',
            // prices
            [$locationPrice],
        )->build();
    }

    /** @return callable(array<int|string, mixed>): TypePricing */
    public static function reader(): callable
    {
        return TypePricing::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return TypePricingConstraint::constraints();
    }
}
