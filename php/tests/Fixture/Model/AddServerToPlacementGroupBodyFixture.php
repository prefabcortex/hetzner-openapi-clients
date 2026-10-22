<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\AddServerToPlacementGroupBody;
use Prefabcortex\Hetzner\Validator\AddServerToPlacementGroupBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class AddServerToPlacementGroupBodyFixture
{
    public static function build(): AddServerToPlacementGroupBody
    {
        return AddServerToPlacementGroupBody::builder(1)->build();
    }

    /** @return callable(array<int|string, mixed>): AddServerToPlacementGroupBody */
    public static function reader(): callable
    {
        return AddServerToPlacementGroupBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return AddServerToPlacementGroupBodyConstraint::constraints();
    }
}
