<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateStorageBoxSnapshotBody;
use Prefabcortex\Hetzner\Validator\UpdateStorageBoxSnapshotBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateStorageBoxSnapshotBodyFixture
{
    public static function build(): UpdateStorageBoxSnapshotBody
    {
        return UpdateStorageBoxSnapshotBody::builder()
            ->setDescription('snapshot-0001')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateStorageBoxSnapshotBody */
    public static function reader(): callable
    {
        return UpdateStorageBoxSnapshotBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateStorageBoxSnapshotBodyConstraint::constraints();
    }
}
