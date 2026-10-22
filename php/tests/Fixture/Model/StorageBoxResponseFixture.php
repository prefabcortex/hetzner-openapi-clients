<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Model\StorageBox;
use Prefabcortex\Hetzner\Model\StorageBoxAccessSettings;
use Prefabcortex\Hetzner\Model\StorageBoxResponse;
use Prefabcortex\Hetzner\Model\StorageBoxSnapshotPlan;
use Prefabcortex\Hetzner\Model\StorageBoxStats;
use Prefabcortex\Hetzner\Model\StorageBoxStatus;
use Prefabcortex\Hetzner\Model\StorageBoxType;
use Prefabcortex\Hetzner\Model\StorageBoxTypePricesItem;
use Prefabcortex\Hetzner\Validator\StorageBoxResponseConstraint;
use Symfony\Component\Validator\Constraint;

final class StorageBoxResponseFixture
{
    public static function build(): StorageBoxResponse
    {
        $priceHourly = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $priceMonthly = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $setupFee = Price::builder(
            // net
            '1.0000',
            // gross
            '1.1900',
        )->build();
        $storageBoxTypePricesItem = StorageBoxTypePricesItem::builder(
            // location
            'fsn1',
            // priceHourly
            $priceHourly,
            // priceMonthly
            $priceMonthly,
            // setupFee
            $setupFee,
        )->build();
        $deprecation = DeprecationInfo::builder(
            // unavailableAfter
            new DateTime('2024-01-01'),
            // announced
            new DateTime('2024-01-01'),
        )->build();
        $storageBoxType = StorageBoxType::builder(
            // id
            42,
            // name
            'bx11',
            // description
            'BX11',
            // snapshotLimit
            10,
            // automaticSnapshotLimit
            10,
            // subaccountsLimit
            200,
            // size
            1073741824,
            // prices
            [$storageBoxTypePricesItem],
            // deprecation
            $deprecation,
        )->build();
        $location = Location::builder(
            // id
            42,
            // name
            'fsn1',
            // description
            'Falkenstein DC Park 1',
            // country
            'DE',
            // city
            'Falkenstein',
            // latitude
            50.47612,
            // longitude
            12.370071,
            // networkZone
            'eu-central',
        )->build();
        $accessSettings = StorageBoxAccessSettings::builder(
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
        $snapshotPlan = StorageBoxSnapshotPlan::builder(
            // maxSnapshots
            10,
            // minute
            30,
            // hour
            3,
            // dayOfWeek
            7,
            // dayOfMonth
            1,
        )->build();
        $protection = Protection::builder(false)->build();
        $stats = StorageBoxStats::builder(
            // size
            0,
            // sizeData
            0,
            // sizeSnapshots
            0,
        )->build();
        $storageBox = StorageBox::builder(
            // id
            42,
            // name
            'REPLACE_ME',
            // storageBoxType
            $storageBoxType,
            // location
            $location,
            // accessSettings
            $accessSettings,
            // snapshotPlan
            $snapshotPlan,
            // protection
            $protection,
            // labels
            [],
            // status
            StorageBoxStatus::active,
            // username
            'u12345',
            // server
            'u1337.your-storagebox.de',
            // system
            'FSN1-BX355',
            // stats
            $stats,
            // created
            new DateTime('2024-01-01'),
        )->build();

        return StorageBoxResponse::builder($storageBox)->build();
    }

    /** @return callable(array<int|string, mixed>): StorageBoxResponse */
    public static function reader(): callable
    {
        return StorageBoxResponse::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return StorageBoxResponseConstraint::constraints();
    }
}
