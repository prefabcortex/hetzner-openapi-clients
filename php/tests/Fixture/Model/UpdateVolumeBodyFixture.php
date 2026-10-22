<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateVolumeBody;
use Prefabcortex\Hetzner\Validator\UpdateVolumeBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateVolumeBodyFixture
{
    public static function build(): UpdateVolumeBody
    {
        return UpdateVolumeBody::builder()
            ->setName('database-storage')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateVolumeBody */
    public static function reader(): callable
    {
        return UpdateVolumeBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateVolumeBodyConstraint::constraints();
    }
}
