<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreatePlacementGroupBody;
use Prefabcortex\Hetzner\Model\CreatePlacementGroupBodyType;
use Prefabcortex\Hetzner\Validator\CreatePlacementGroupBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreatePlacementGroupBodyFixture
{
    public static function build(): CreatePlacementGroupBody
    {
        return CreatePlacementGroupBody::builder(
            // name
            'my Placement Group',
            // type
            CreatePlacementGroupBodyType::spread,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): CreatePlacementGroupBody */
    public static function reader(): callable
    {
        return CreatePlacementGroupBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreatePlacementGroupBodyConstraint::constraints();
    }
}
