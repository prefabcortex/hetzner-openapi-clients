<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Subaccount;
use Prefabcortex\Hetzner\Model\SubaccountAccessSettings;
use Prefabcortex\Hetzner\Model\SubaccountResponse;
use Prefabcortex\Hetzner\Validator\SubaccountResponseConstraint;
use Symfony\Component\Validator\Constraint;

final class SubaccountResponseFixture
{
    public static function build(): SubaccountResponse
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
        $subaccount = Subaccount::builder(
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

        return SubaccountResponse::builder($subaccount)->build();
    }

    /** @return callable(array<int|string, mixed>): SubaccountResponse */
    public static function reader(): callable
    {
        return SubaccountResponse::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return SubaccountResponseConstraint::constraints();
    }
}
