<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Action;
use Prefabcortex\Hetzner\Model\ActionError;
use Prefabcortex\Hetzner\Model\ActionResource;
use Prefabcortex\Hetzner\Model\ActionStatus;
use Prefabcortex\Hetzner\Model\CreateStorageBoxSnapshotResponse201;
use Prefabcortex\Hetzner\Model\CreateStorageBoxSnapshotResponse201Snapshot;
use Prefabcortex\Hetzner\Validator\CreateStorageBoxSnapshotResponse201Constraint;
use Symfony\Component\Validator\Constraint;

final class CreateStorageBoxSnapshotResponse201Fixture
{
    public static function build(): CreateStorageBoxSnapshotResponse201
    {
        $snapshot = CreateStorageBoxSnapshotResponse201Snapshot::builder(
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

        return CreateStorageBoxSnapshotResponse201::builder(
            // snapshot
            $snapshot,
            // action
            $action,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): CreateStorageBoxSnapshotResponse201 */
    public static function reader(): callable
    {
        return CreateStorageBoxSnapshotResponse201::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateStorageBoxSnapshotResponse201Constraint::constraints();
    }
}
