<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Action;
use Prefabcortex\Hetzner\Model\ActionError;
use Prefabcortex\Hetzner\Model\ActionResource;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ActionStatus;
use Prefabcortex\Hetzner\Validator\ActionResponseConstraint;
use Symfony\Component\Validator\Constraint;

final class ActionResponseFixture
{
    public static function build(): ActionResponse
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

        return ActionResponse::builder($action)->build();
    }

    /** @return callable(array<int|string, mixed>): ActionResponse */
    public static function reader(): callable
    {
        return ActionResponse::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ActionResponseConstraint::constraints();
    }
}
