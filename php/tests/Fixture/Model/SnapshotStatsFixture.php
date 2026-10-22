<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\SnapshotStats;
use Prefabcortex\Hetzner\Validator\SnapshotStatsConstraint;
use Symfony\Component\Validator\Constraint;

final class SnapshotStatsFixture
{
    public static function build(): SnapshotStats
    {
        return SnapshotStats::builder(
            // size
            0,
            // sizeFilesystem
            0,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): SnapshotStats */
    public static function reader(): callable
    {
        return SnapshotStats::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return SnapshotStatsConstraint::constraints();
    }
}
