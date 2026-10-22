<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateStorageBoxSubaccountBody;
use Prefabcortex\Hetzner\Validator\UpdateStorageBoxSubaccountBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateStorageBoxSubaccountBodyFixture
{
    public static function build(): UpdateStorageBoxSubaccountBody
    {
        return UpdateStorageBoxSubaccountBody::builder()
            ->setName('my-name')
            ->setDescription('my-backup-server01')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateStorageBoxSubaccountBody */
    public static function reader(): callable
    {
        return UpdateStorageBoxSubaccountBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateStorageBoxSubaccountBodyConstraint::constraints();
    }
}
