<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Action;
use Prefabcortex\Hetzner\Model\ActionError;
use Prefabcortex\Hetzner\Model\ActionResource;
use Prefabcortex\Hetzner\Model\ActionStatus;
use Prefabcortex\Hetzner\Model\RequestServerConsoleResponse201;
use Prefabcortex\Hetzner\Validator\RequestServerConsoleResponse201Constraint;
use Symfony\Component\Validator\Constraint;

final class RequestServerConsoleResponse201Fixture
{
    public static function build(): RequestServerConsoleResponse201
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

        return RequestServerConsoleResponse201::builder(
            // wssUrl
            'wss://console.hetzner.cloud/?server_id=1&token=3db32d15-af2f-459c-8bf8-dee1fd05f49c',
            // password
            '9MQaTg2VAGI0FIpc10k3UpRXcHj2wQ6x',
            // action
            $action,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): RequestServerConsoleResponse201 */
    public static function reader(): callable
    {
        return RequestServerConsoleResponse201::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return RequestServerConsoleResponse201Constraint::constraints();
    }
}
