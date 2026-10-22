<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingFloatingIpsItemPricesItem;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Validator\GetPricingResponse200PricingFloatingIpsItemPricesItemConstraint;
use Symfony\Component\Validator\Constraint;

final class GetPricingResponse200PricingFloatingIpsItemPricesItemFixture
{
    public static function build(): GetPricingResponse200PricingFloatingIpsItemPricesItem
    {
        $priceMonthly = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();

        return GetPricingResponse200PricingFloatingIpsItemPricesItem::builder(
            // location
            'fsn1',
            // priceMonthly
            $priceMonthly,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): GetPricingResponse200PricingFloatingIpsItemPricesItem */
    public static function reader(): callable
    {
        return GetPricingResponse200PricingFloatingIpsItemPricesItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return GetPricingResponse200PricingFloatingIpsItemPricesItemConstraint::constraints();
    }
}
