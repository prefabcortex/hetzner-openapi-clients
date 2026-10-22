<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateStorageBoxBodyAccessSettings;
use Prefabcortex\Hetzner\Validator\CreateStorageBoxBodyAccessSettingsConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateStorageBoxBodyAccessSettingsFixture
{
    public static function build(): CreateStorageBoxBodyAccessSettings
    {
        return CreateStorageBoxBodyAccessSettings::builder()->build();
    }

    /** @return callable(array<int|string, mixed>): CreateStorageBoxBodyAccessSettings */
    public static function reader(): callable
    {
        return CreateStorageBoxBodyAccessSettings::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateStorageBoxBodyAccessSettingsConstraint::constraints();
    }
}
