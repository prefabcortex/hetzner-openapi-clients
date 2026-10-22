<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeZoneRrsetTtlBody;
use Prefabcortex\Hetzner\Validator\ChangeZoneRrsetTtlBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeZoneRrsetTtlBodyFixture
{
    public static function build(): ChangeZoneRrsetTtlBody
    {
        return ChangeZoneRrsetTtlBody::builder(3600)->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeZoneRrsetTtlBody */
    public static function reader(): callable
    {
        return ChangeZoneRrsetTtlBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeZoneRrsetTtlBodyConstraint::constraints();
    }
}
