<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\DatacenterServerTypes;
use Prefabcortex\Hetzner\Validator\DatacenterServerTypesConstraint;
use Symfony\Component\Validator\Constraint;

final class DatacenterServerTypesFixture
{
    public static function build(): DatacenterServerTypes
    {
        return DatacenterServerTypes::builder(
            // supported
            [1, 2, 3],
            // available
            [1, 2, 3],
            // availableForMigration
            [1, 2, 3],
        )->build();
    }

    /** @return callable(array<int|string, mixed>): DatacenterServerTypes */
    public static function reader(): callable
    {
        return DatacenterServerTypes::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return DatacenterServerTypesConstraint::constraints();
    }
}
