<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Subaccount;
use Prefabcortex\Hetzner\Model\SubaccountAccessSettings;
use Prefabcortex\Hetzner\Validator\SubaccountConstraint;
use Symfony\Component\Validator\Constraint;

final class SubaccountFixture
{
    public static function build(): Subaccount
    {
        $accessSettings = SubaccountAccessSettings::builder(
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

        return Subaccount::builder(
            // storageBox
            42,
            // id
            42,
            // name
            'my-name',
            // homeDirectory
            'my-backup/server01',
            // accessSettings
            $accessSettings,
            // description
            'my-backup-server01',
            // labels
            [],
            // username
            'u1337-sub1',
            // server
            'u1337-sub1.your-storagebox.de',
            // created
            new DateTime('2024-01-01'),
        )->build();
    }

    /** @return callable(array<int|string, mixed>): Subaccount */
    public static function reader(): callable
    {
        return Subaccount::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return SubaccountConstraint::constraints();
    }
}
