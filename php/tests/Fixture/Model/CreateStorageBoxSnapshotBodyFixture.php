<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateStorageBoxSnapshotBody;
use Prefabcortex\Hetzner\Validator\CreateStorageBoxSnapshotBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateStorageBoxSnapshotBodyFixture
{
    public static function build(): CreateStorageBoxSnapshotBody
    {
        return CreateStorageBoxSnapshotBody::builder()
            ->setDescription('snapshot-0001')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateStorageBoxSnapshotBody */
    public static function reader(): callable
    {
        return CreateStorageBoxSnapshotBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateStorageBoxSnapshotBodyConstraint::constraints();
    }
}
