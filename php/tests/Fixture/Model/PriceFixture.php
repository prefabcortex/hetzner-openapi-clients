<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Validator\PriceConstraint;
use Symfony\Component\Validator\Constraint;

final class PriceFixture
{
    public static function build(): Price
    {
        return Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): Price */
    public static function reader(): callable
    {
        return Price::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return PriceConstraint::constraints();
    }
}
