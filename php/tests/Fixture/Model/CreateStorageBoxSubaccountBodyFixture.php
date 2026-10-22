<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateStorageBoxSubaccountBody;
use Prefabcortex\Hetzner\Validator\CreateStorageBoxSubaccountBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateStorageBoxSubaccountBodyFixture
{
    public static function build(): CreateStorageBoxSubaccountBody
    {
        return CreateStorageBoxSubaccountBody::builder(
            // homeDirectory
            'my-backup/server01',
            // password
            'REPLACE_ME',
        )
            ->setName('my-name')
            ->setDescription('my-backup-server01')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateStorageBoxSubaccountBody */
    public static function reader(): callable
    {
        return CreateStorageBoxSubaccountBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateStorageBoxSubaccountBodyConstraint::constraints();
    }
}
