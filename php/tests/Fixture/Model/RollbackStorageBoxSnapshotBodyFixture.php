<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\RollbackStorageBoxSnapshotBody;
use Prefabcortex\Hetzner\Validator\RollbackStorageBoxSnapshotBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class RollbackStorageBoxSnapshotBodyFixture
{
    public static function build(): RollbackStorageBoxSnapshotBody
    {
        return RollbackStorageBoxSnapshotBody::builder('my-snapshot')->build();
    }

    /** @return callable(array<int|string, mixed>): RollbackStorageBoxSnapshotBody */
    public static function reader(): callable
    {
        return RollbackStorageBoxSnapshotBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return RollbackStorageBoxSnapshotBodyConstraint::constraints();
    }
}
