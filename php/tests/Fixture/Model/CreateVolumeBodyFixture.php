<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateVolumeBody;
use Prefabcortex\Hetzner\Validator\CreateVolumeBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateVolumeBodyFixture
{
    public static function build(): CreateVolumeBody
    {
        return CreateVolumeBody::builder(
            // size
            42,
            // name
            'databases-storage',
        )
            ->setAutomount(false)
            ->setFormat('xfs')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateVolumeBody */
    public static function reader(): callable
    {
        return CreateVolumeBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateVolumeBodyConstraint::constraints();
    }
}
