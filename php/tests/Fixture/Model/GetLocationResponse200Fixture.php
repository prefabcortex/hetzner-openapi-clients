<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\GetLocationResponse200;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Validator\GetLocationResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class GetLocationResponse200Fixture
{
    public static function build(): GetLocationResponse200
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

        return GetLocationResponse200::builder($location)->build();
    }

    /** @return callable(array<int|string, mixed>): GetLocationResponse200 */
    public static function reader(): callable
    {
        return GetLocationResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return GetLocationResponse200Constraint::constraints();
    }
}
