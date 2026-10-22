<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\EnableStorageBoxSnapshotPlanBody;
use Prefabcortex\Hetzner\Validator\EnableStorageBoxSnapshotPlanBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class EnableStorageBoxSnapshotPlanBodyFixture
{
    public static function build(): EnableStorageBoxSnapshotPlanBody
    {
        return EnableStorageBoxSnapshotPlanBody::builder(
            // maxSnapshots
            10,
            // minute
            30,
            // hour
            3,
        )
            ->setDayOfWeek(7)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): EnableStorageBoxSnapshotPlanBody */
    public static function reader(): callable
    {
        return EnableStorageBoxSnapshotPlanBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return EnableStorageBoxSnapshotPlanBodyConstraint::constraints();
    }
}
