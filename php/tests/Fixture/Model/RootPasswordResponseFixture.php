<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Action;
use Prefabcortex\Hetzner\Model\ActionError;
use Prefabcortex\Hetzner\Model\ActionResource;
use Prefabcortex\Hetzner\Model\ActionStatus;
use Prefabcortex\Hetzner\Model\RootPasswordResponse;
use Prefabcortex\Hetzner\Validator\RootPasswordResponseConstraint;
use Symfony\Component\Validator\Constraint;

final class RootPasswordResponseFixture
{
    public static function build(): RootPasswordResponse
    {
        $actionResource = ActionResource::builder(
            // id
            42,
            // type
            'server',
        )->build();
        $error = ActionError::builder(
            // code
            'action_failed',
            // message
            'Action failed',
        )->build();
        $action = Action::builder(
            // id
            42,
            // command
            'start_resource',
            // status
            ActionStatus::running,
            // started
            new DateTime('2024-01-01'),
            // finished
            new DateTime('2024-01-01'),
            // progress
            100,
            // resources
            [$actionResource],
            // error
            $error,
        )->build();

        return RootPasswordResponse::builder(
            // rootPassword
            'zCWbFhnu950dUTko5f40',
            // action
            $action,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): RootPasswordResponse */
    public static function reader(): callable
    {
        return RootPasswordResponse::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return RootPasswordResponseConstraint::constraints();
    }
}
