<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Datacenter;
use Prefabcortex\Hetzner\Model\DatacenterServerTypes;
use Prefabcortex\Hetzner\Model\ListDatacentersResponse200;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Validator\ListDatacentersResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListDatacentersResponse200Fixture
{
    public static function build(): ListDatacentersResponse200
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
        $serverTypes = DatacenterServerTypes::builder(
            // supported
            [1, 2, 3],
            // available
            [1, 2, 3],
            // availableForMigration
            [1, 2, 3],
        )->build();
        $datacenter = Datacenter::builder(
            // id
            42,
            // name
            'fsn1-dc8',
            // description
            'Falkenstein DC Park 8',
            // location
            $location,
            // serverTypes
            $serverTypes,
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

        return ListDatacentersResponse200::builder(
            // datacenters
            [$datacenter],
            // recommendation
            1,
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListDatacentersResponse200 */
    public static function reader(): callable
    {
        return ListDatacentersResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListDatacentersResponse200Constraint::constraints();
    }
}
