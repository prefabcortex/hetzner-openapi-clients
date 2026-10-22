<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Model\PricePerGbMonth;
use Prefabcortex\Hetzner\Validator\PricePerGbMonthConstraint;
use Symfony\Component\Validator\Constraint;

final class PricePerGbMonthFixture
{
    public static function build(): PricePerGbMonth
    {
        $pricePerGbMonth = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();

        return PricePerGbMonth::builder($pricePerGbMonth)->build();
    }

    /** @return callable(array<int|string, mixed>): PricePerGbMonth */
    public static function reader(): callable
    {
        return PricePerGbMonth::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return PricePerGbMonthConstraint::constraints();
    }
}
