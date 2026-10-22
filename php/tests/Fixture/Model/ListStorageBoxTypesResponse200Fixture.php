<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Model\ListStorageBoxTypesResponse200;
use Prefabcortex\Hetzner\Model\Price;
use Prefabcortex\Hetzner\Model\StorageBoxType;
use Prefabcortex\Hetzner\Model\StorageBoxTypePricesItem;
use Prefabcortex\Hetzner\Validator\ListStorageBoxTypesResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListStorageBoxTypesResponse200Fixture
{
    public static function build(): ListStorageBoxTypesResponse200
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
        $pagination = ListMetaPagination::builder(
            // page
            3,
            // perPage
            25,
            // previousPage
            2,
            // nextPage
            4,
            // lastPage
            4,
            // totalEntries
            100,
        )->build();
        $meta = ListMeta::builder($pagination)->build();

        return ListStorageBoxTypesResponse200::builder(
            // storageBoxTypes
            [$storageBoxType],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListStorageBoxTypesResponse200 */
    public static function reader(): callable
    {
        return ListStorageBoxTypesResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListStorageBoxTypesResponse200Constraint::constraints();
    }
}
