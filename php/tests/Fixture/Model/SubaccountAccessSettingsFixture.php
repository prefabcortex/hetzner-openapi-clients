<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\SubaccountAccessSettings;
use Prefabcortex\Hetzner\Validator\SubaccountAccessSettingsConstraint;
use Symfony\Component\Validator\Constraint;

final class SubaccountAccessSettingsFixture
{
    public static function build(): SubaccountAccessSettings
    {
        return SubaccountAccessSettings::builder(
            // reachableExternally
            true,
            // sambaEnabled
            true,
            // sshEnabled
            true,
            // webdavEnabled
            true,
            // readonly
            true,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): SubaccountAccessSettings */
    public static function reader(): callable
    {
        return SubaccountAccessSettings::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return SubaccountAccessSettingsConstraint::constraints();
    }
}
