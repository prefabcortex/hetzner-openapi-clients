<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\ListStorageBoxSubaccountsResponse200;
use Prefabcortex\Hetzner\Model\Subaccount;
use Prefabcortex\Hetzner\Model\SubaccountAccessSettings;
use Prefabcortex\Hetzner\Validator\ListStorageBoxSubaccountsResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListStorageBoxSubaccountsResponse200Fixture
{
    public static function build(): ListStorageBoxSubaccountsResponse200
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

        return ListStorageBoxSubaccountsResponse200::builder([$subaccount])->build();
    }

    /** @return callable(array<int|string, mixed>): ListStorageBoxSubaccountsResponse200 */
    public static function reader(): callable
    {
        return ListStorageBoxSubaccountsResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListStorageBoxSubaccountsResponse200Constraint::constraints();
    }
}
