<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ActionResource;
use Prefabcortex\Hetzner\Validator\ActionResourceConstraint;
use Symfony\Component\Validator\Constraint;

final class ActionResourceFixture
{
    public static function build(): ActionResource
    {
        return ActionResource::builder(
            // id
            42,
            // type
            'server',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ActionResource */
    public static function reader(): callable
    {
        return ActionResource::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ActionResourceConstraint::constraints();
    }
}
