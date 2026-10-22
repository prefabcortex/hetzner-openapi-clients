<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ListLocationsResponse200;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Validator\ListLocationsResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListLocationsResponse200Fixture
{
    public static function build(): ListLocationsResponse200
    {
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

        return ListLocationsResponse200::builder(
            // locations
            [$location],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListLocationsResponse200 */
    public static function reader(): callable
    {
        return ListLocationsResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListLocationsResponse200Constraint::constraints();
    }
}
