<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateStorageBoxSubaccountResponse201Subaccount;
use Prefabcortex\Hetzner\Validator\CreateStorageBoxSubaccountResponse201SubaccountConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateStorageBoxSubaccountResponse201SubaccountFixture
{
    public static function build(): CreateStorageBoxSubaccountResponse201Subaccount
    {
        return CreateStorageBoxSubaccountResponse201Subaccount::builder(
            // id
            42,
            // storageBox
            42,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): CreateStorageBoxSubaccountResponse201Subaccount */
    public static function reader(): callable
    {
        return CreateStorageBoxSubaccountResponse201Subaccount::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateStorageBoxSubaccountResponse201SubaccountConstraint::constraints();
    }
}
