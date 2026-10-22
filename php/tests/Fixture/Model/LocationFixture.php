<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Validator\LocationConstraint;
use Symfony\Component\Validator\Constraint;

final class LocationFixture
{
    public static function build(): Location
    {
        return Location::builder(
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
    }

    /** @return callable(array<int|string, mixed>): Location */
    public static function reader(): callable
    {
        return Location::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LocationConstraint::constraints();
    }
}
