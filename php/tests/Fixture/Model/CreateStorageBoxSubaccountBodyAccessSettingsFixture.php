<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateStorageBoxSubaccountBodyAccessSettings;
use Prefabcortex\Hetzner\Validator\CreateStorageBoxSubaccountBodyAccessSettingsConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateStorageBoxSubaccountBodyAccessSettingsFixture
{
    public static function build(): CreateStorageBoxSubaccountBodyAccessSettings
    {
        return CreateStorageBoxSubaccountBodyAccessSettings::builder()->build();
    }

    /** @return callable(array<int|string, mixed>): CreateStorageBoxSubaccountBodyAccessSettings */
    public static function reader(): callable
    {
        return CreateStorageBoxSubaccountBodyAccessSettings::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateStorageBoxSubaccountBodyAccessSettingsConstraint::constraints();
    }
}
