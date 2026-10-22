<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateZoneBody;
use Prefabcortex\Hetzner\Validator\UpdateZoneBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateZoneBodyFixture
{
    public static function build(): UpdateZoneBody
    {
        return UpdateZoneBody::builder()->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateZoneBody */
    public static function reader(): callable
    {
        return UpdateZoneBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateZoneBodyConstraint::constraints();
    }
}
