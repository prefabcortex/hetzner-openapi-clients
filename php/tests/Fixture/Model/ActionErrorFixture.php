<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ActionError;
use Prefabcortex\Hetzner\Validator\ActionErrorConstraint;
use Symfony\Component\Validator\Constraint;

final class ActionErrorFixture
{
    public static function build(): ActionError
    {
        return ActionError::builder(
            // code
            'action_failed',
            // message
            'Action failed',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ActionError */
    public static function reader(): callable
    {
        return ActionError::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ActionErrorConstraint::constraints();
    }
}
