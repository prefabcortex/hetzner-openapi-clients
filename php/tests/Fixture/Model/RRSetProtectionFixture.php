<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\RRSetProtection;
use Prefabcortex\Hetzner\Validator\RRSetProtectionConstraint;
use Symfony\Component\Validator\Constraint;

final class RRSetProtectionFixture
{
    public static function build(): RRSetProtection
    {
        return RRSetProtection::builder(false)->build();
    }

    /** @return callable(array<int|string, mixed>): RRSetProtection */
    public static function reader(): callable
    {
        return RRSetProtection::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return RRSetProtectionConstraint::constraints();
    }
}
