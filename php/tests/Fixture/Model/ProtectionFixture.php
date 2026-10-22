<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Validator\ProtectionConstraint;
use Symfony\Component\Validator\Constraint;

final class ProtectionFixture
{
    public static function build(): Protection
    {
        return Protection::builder(false)->build();
    }

    /** @return callable(array<int|string, mixed>): Protection */
    public static function reader(): callable
    {
        return Protection::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ProtectionConstraint::constraints();
    }
}
