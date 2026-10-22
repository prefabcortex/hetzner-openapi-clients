<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingFloatingIpsItem;
use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingFloatingIpsItemPricesItem;
use Prefabcortex\Hetzner\Model\IpType;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Validator\GetPricingResponse200PricingFloatingIpsItemConstraint;
use Symfony\Component\Validator\Constraint;

final class GetPricingResponse200PricingFloatingIpsItemFixture
{
    public static function build(): GetPricingResponse200PricingFloatingIpsItem
    {
        $priceMonthly = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $getPricingResponse200PricingFloatingIpsItemPricesItem = GetPricingResponse200PricingFloatingIpsItemPricesItem::builder(
            // location
            'fsn1',
            // priceMonthly
            $priceMonthly,
        )->build();

        return GetPricingResponse200PricingFloatingIpsItem::builder(
            // type
            IpType::ipv4,
            // prices
            [$getPricingResponse200PricingFloatingIpsItemPricesItem],
        )->build();
    }

    /** @return callable(array<int|string, mixed>): GetPricingResponse200PricingFloatingIpsItem */
    public static function reader(): callable
    {
        return GetPricingResponse200PricingFloatingIpsItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return GetPricingResponse200PricingFloatingIpsItemConstraint::constraints();
    }
}
