<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateStorageBoxSnapshotResponse201Snapshot;
use Prefabcortex\Hetzner\Validator\CreateStorageBoxSnapshotResponse201SnapshotConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateStorageBoxSnapshotResponse201SnapshotFixture
{
    public static function build(): CreateStorageBoxSnapshotResponse201Snapshot
    {
        return CreateStorageBoxSnapshotResponse201Snapshot::builder(
            // id
            42,
            // storageBox
            42,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): CreateStorageBoxSnapshotResponse201Snapshot */
    public static function reader(): callable
    {
        return CreateStorageBoxSnapshotResponse201Snapshot::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateStorageBoxSnapshotResponse201SnapshotConstraint::constraints();
    }
}
