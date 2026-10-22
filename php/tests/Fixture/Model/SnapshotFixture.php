<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Snapshot;
use Prefabcortex\Hetzner\Model\SnapshotStats;
use Prefabcortex\Hetzner\Validator\SnapshotConstraint;
use Symfony\Component\Validator\Constraint;

final class SnapshotFixture
{
    public static function build(): Snapshot
    {
        $stats = SnapshotStats::builder(
            // size
            0,
            // sizeFilesystem
            0,
        )->build();

        return Snapshot::builder(
            // storageBox
            42,
            // id
            42,
            // name
            'my-snapshot',
            // description
            'snapshot-0001',
            // labels
            [],
            // stats
            $stats,
            // isAutomatic
            true,
            // created
            new DateTime('2024-01-01'),
        )->build();
    }

    /** @return callable(array<int|string, mixed>): Snapshot */
    public static function reader(): callable
    {
        return Snapshot::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return SnapshotConstraint::constraints();
    }
}
