<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\StorageBoxSnapshotPlan;
use Prefabcortex\Hetzner\Validator\StorageBoxSnapshotPlanConstraint;
use Symfony\Component\Validator\Constraint;

final class StorageBoxSnapshotPlanFixture
{
    public static function build(): StorageBoxSnapshotPlan
    {
        return StorageBoxSnapshotPlan::builder(
            // maxSnapshots
            10,
            // minute
            30,
            // hour
            3,
            // dayOfWeek
            7,
            // dayOfMonth
            1,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): StorageBoxSnapshotPlan */
    public static function reader(): callable
    {
        return StorageBoxSnapshotPlan::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return StorageBoxSnapshotPlanConstraint::constraints();
    }
}
