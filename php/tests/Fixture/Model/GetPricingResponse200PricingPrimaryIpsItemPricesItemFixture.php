<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingPrimaryIpsItemPricesItem;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Validator\GetPricingResponse200PricingPrimaryIpsItemPricesItemConstraint;
use Symfony\Component\Validator\Constraint;

final class GetPricingResponse200PricingPrimaryIpsItemPricesItemFixture
{
    public static function build(): GetPricingResponse200PricingPrimaryIpsItemPricesItem
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

        return GetPricingResponse200PricingPrimaryIpsItemPricesItem::builder(
            // location
            'fsn1',
            // priceHourly
            $priceHourly,
            // priceMonthly
            $priceMonthly,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): GetPricingResponse200PricingPrimaryIpsItemPricesItem */
    public static function reader(): callable
    {
        return GetPricingResponse200PricingPrimaryIpsItemPricesItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return GetPricingResponse200PricingPrimaryIpsItemPricesItemConstraint::constraints();
    }
}
