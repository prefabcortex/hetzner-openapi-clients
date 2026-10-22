<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\StorageBoxAccessSettings;
use Prefabcortex\Hetzner\Validator\StorageBoxAccessSettingsConstraint;
use Symfony\Component\Validator\Constraint;

final class StorageBoxAccessSettingsFixture
{
    public static function build(): StorageBoxAccessSettings
    {
        return StorageBoxAccessSettings::builder(
            // reachableExternally
            true,
            // sambaEnabled
            true,
            // sshEnabled
            true,
            // webdavEnabled
            true,
            // zfsEnabled
            true,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): StorageBoxAccessSettings */
    public static function reader(): callable
    {
        return StorageBoxAccessSettings::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return StorageBoxAccessSettingsConstraint::constraints();
    }
}
