<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\ListStorageBoxSnapshotsResponse200;
use Prefabcortex\Hetzner\Model\Snapshot;
use Prefabcortex\Hetzner\Model\SnapshotStats;
use Prefabcortex\Hetzner\Validator\ListStorageBoxSnapshotsResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListStorageBoxSnapshotsResponse200Fixture
{
    public static function build(): ListStorageBoxSnapshotsResponse200
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

        return ListStorageBoxSnapshotsResponse200::builder([$snapshot])->build();
    }

    /** @return callable(array<int|string, mixed>): ListStorageBoxSnapshotsResponse200 */
    public static function reader(): callable
    {
        return ListStorageBoxSnapshotsResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListStorageBoxSnapshotsResponse200Constraint::constraints();
    }
}
