<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateZoneRrsetBody;
use Prefabcortex\Hetzner\Validator\UpdateZoneRrsetBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateZoneRrsetBodyFixture
{
    public static function build(): UpdateZoneRrsetBody
    {
        return UpdateZoneRrsetBody::builder()->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateZoneRrsetBody */
    public static function reader(): callable
    {
        return UpdateZoneRrsetBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateZoneRrsetBodyConstraint::constraints();
    }
}
