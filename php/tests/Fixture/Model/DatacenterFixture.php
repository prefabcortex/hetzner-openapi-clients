<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Datacenter;
use Prefabcortex\Hetzner\Model\DatacenterServerTypes;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Validator\DatacenterConstraint;
use Symfony\Component\Validator\Constraint;

final class DatacenterFixture
{
    public static function build(): Datacenter
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

        return Datacenter::builder(
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
    }

    /** @return callable(array<int|string, mixed>): Datacenter */
    public static function reader(): callable
    {
        return Datacenter::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return DatacenterConstraint::constraints();
    }
}
