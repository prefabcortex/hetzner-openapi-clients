<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateStorageBoxBody;
use Prefabcortex\Hetzner\Validator\UpdateStorageBoxBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateStorageBoxBodyFixture
{
    public static function build(): UpdateStorageBoxBody
    {
        return UpdateStorageBoxBody::builder()->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateStorageBoxBody */
    public static function reader(): callable
    {
        return UpdateStorageBoxBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateStorageBoxBodyConstraint::constraints();
    }
}
