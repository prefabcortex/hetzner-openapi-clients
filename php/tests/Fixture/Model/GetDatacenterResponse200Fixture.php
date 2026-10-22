<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Datacenter;
use Prefabcortex\Hetzner\Model\DatacenterServerTypes;
use Prefabcortex\Hetzner\Model\GetDatacenterResponse200;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Validator\GetDatacenterResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class GetDatacenterResponse200Fixture
{
    public static function build(): GetDatacenterResponse200
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

        return GetDatacenterResponse200::builder($datacenter)->build();
    }

    /** @return callable(array<int|string, mixed>): GetDatacenterResponse200 */
    public static function reader(): callable
    {
        return GetDatacenterResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return GetDatacenterResponse200Constraint::constraints();
    }
}
