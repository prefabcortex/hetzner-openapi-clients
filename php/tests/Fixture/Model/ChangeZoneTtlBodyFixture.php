<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeZoneTtlBody;
use Prefabcortex\Hetzner\Validator\ChangeZoneTtlBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeZoneTtlBodyFixture
{
    public static function build(): ChangeZoneTtlBody
    {
        return ChangeZoneTtlBody::builder(10800)->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeZoneTtlBody */
    public static function reader(): callable
    {
        return ChangeZoneTtlBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeZoneTtlBodyConstraint::constraints();
    }
}
