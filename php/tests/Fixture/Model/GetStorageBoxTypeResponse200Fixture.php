<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\GetStorageBoxTypeResponse200;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Model\StorageBoxType;
use Prefabcortex\Hetzner\Model\StorageBoxTypePricesItem;
use Prefabcortex\Hetzner\Validator\GetStorageBoxTypeResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class GetStorageBoxTypeResponse200Fixture
{
    public static function build(): GetStorageBoxTypeResponse200
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

        return GetStorageBoxTypeResponse200::builder($storageBoxType)->build();
    }

    /** @return callable(array<int|string, mixed>): GetStorageBoxTypeResponse200 */
    public static function reader(): callable
    {
        return GetStorageBoxTypeResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return GetStorageBoxTypeResponse200Constraint::constraints();
    }
}
