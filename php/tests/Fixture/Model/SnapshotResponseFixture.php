<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Snapshot;
use Prefabcortex\Hetzner\Model\SnapshotResponse;
use Prefabcortex\Hetzner\Model\SnapshotStats;
use Prefabcortex\Hetzner\Validator\SnapshotResponseConstraint;
use Symfony\Component\Validator\Constraint;

final class SnapshotResponseFixture
{
    public static function build(): SnapshotResponse
    {
        $stats = SnapshotStats::builder(
            // size
            0,
            // sizeFilesystem
            0,
        )->build();
        $snapshot = Snapshot::builder(
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

        return SnapshotResponse::builder($snapshot)->build();
    }

    /** @return callable(array<int|string, mixed>): SnapshotResponse */
    public static function reader(): callable
    {
        return SnapshotResponse::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return SnapshotResponseConstraint::constraints();
    }
}
