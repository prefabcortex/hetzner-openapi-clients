<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateStorageBoxBody;
use Prefabcortex\Hetzner\Validator\CreateStorageBoxBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateStorageBoxBodyFixture
{
    public static function build(): CreateStorageBoxBody
    {
        return CreateStorageBoxBody::builder(
            // name
            'REPLACE_ME',
            // location
            'fsn1',
            // storageBoxType
            'bx20',
            // password
            'REPLACE_ME',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): CreateStorageBoxBody */
    public static function reader(): callable
    {
        return CreateStorageBoxBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateStorageBoxBodyConstraint::constraints();
    }
}
