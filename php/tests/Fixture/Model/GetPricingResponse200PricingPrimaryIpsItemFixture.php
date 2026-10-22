<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingPrimaryIpsItem;
use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingPrimaryIpsItemPricesItem;
use Prefabcortex\Hetzner\Model\IpType;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Validator\GetPricingResponse200PricingPrimaryIpsItemConstraint;
use Symfony\Component\Validator\Constraint;

final class GetPricingResponse200PricingPrimaryIpsItemFixture
{
    public static function build(): GetPricingResponse200PricingPrimaryIpsItem
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
        $getPricingResponse200PricingPrimaryIpsItemPricesItem = GetPricingResponse200PricingPrimaryIpsItemPricesItem::builder(
            // location
            'fsn1',
            // priceHourly
            $priceHourly,
            // priceMonthly
            $priceMonthly,
        )->build();

        return GetPricingResponse200PricingPrimaryIpsItem::builder(
            // type
            IpType::ipv4,
            // prices
            [$getPricingResponse200PricingPrimaryIpsItemPricesItem],
        )->build();
    }

    /** @return callable(array<int|string, mixed>): GetPricingResponse200PricingPrimaryIpsItem */
    public static function reader(): callable
    {
        return GetPricingResponse200PricingPrimaryIpsItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return GetPricingResponse200PricingPrimaryIpsItemConstraint::constraints();
    }
}
