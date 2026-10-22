<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingFloatingIp;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Validator\GetPricingResponse200PricingFloatingIpConstraint;
use Symfony\Component\Validator\Constraint;

final class GetPricingResponse200PricingFloatingIpFixture
{
    public static function build(): GetPricingResponse200PricingFloatingIp
    {
        $priceMonthly = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();

        return GetPricingResponse200PricingFloatingIp::builder($priceMonthly)->build();
    }

    /** @return callable(array<int|string, mixed>): GetPricingResponse200PricingFloatingIp */
    public static function reader(): callable
    {
        return GetPricingResponse200PricingFloatingIp::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return GetPricingResponse200PricingFloatingIpConstraint::constraints();
    }
}
