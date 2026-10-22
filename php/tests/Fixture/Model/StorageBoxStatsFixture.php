<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\StorageBoxStats;
use Prefabcortex\Hetzner\Validator\StorageBoxStatsConstraint;
use Symfony\Component\Validator\Constraint;

final class StorageBoxStatsFixture
{
    public static function build(): StorageBoxStats
    {
        return StorageBoxStats::builder(
            // size
            0,
            // sizeData
            0,
            // sizeSnapshots
            0,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): StorageBoxStats */
    public static function reader(): callable
    {
        return StorageBoxStats::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return StorageBoxStatsConstraint::constraints();
    }
}
