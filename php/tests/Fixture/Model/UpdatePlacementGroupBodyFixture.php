<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdatePlacementGroupBody;
use Prefabcortex\Hetzner\Validator\UpdatePlacementGroupBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdatePlacementGroupBodyFixture
{
    public static function build(): UpdatePlacementGroupBody
    {
        return UpdatePlacementGroupBody::builder()
            ->setName('my Placement Group')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdatePlacementGroupBody */
    public static function reader(): callable
    {
        return UpdatePlacementGroupBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdatePlacementGroupBodyConstraint::constraints();
    }
}
