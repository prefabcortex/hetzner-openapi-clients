<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Action;
use Prefabcortex\Hetzner\Model\ActionError;
use Prefabcortex\Hetzner\Model\ActionResource;
use Prefabcortex\Hetzner\Model\ActionStatus;
use Prefabcortex\Hetzner\Model\CreateStorageBoxSubaccountResponse201;
use Prefabcortex\Hetzner\Model\CreateStorageBoxSubaccountResponse201Subaccount;
use Prefabcortex\Hetzner\Validator\CreateStorageBoxSubaccountResponse201Constraint;
use Symfony\Component\Validator\Constraint;

final class CreateStorageBoxSubaccountResponse201Fixture
{
    public static function build(): CreateStorageBoxSubaccountResponse201
    {
        $subaccount = CreateStorageBoxSubaccountResponse201Subaccount::builder(
            // id
            42,
            // storageBox
            42,
        )->build();
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

        return CreateStorageBoxSubaccountResponse201::builder(
            // subaccount
            $subaccount,
            // action
            $action,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): CreateStorageBoxSubaccountResponse201 */
    public static function reader(): callable
    {
        return CreateStorageBoxSubaccountResponse201::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateStorageBoxSubaccountResponse201Constraint::constraints();
    }
}
