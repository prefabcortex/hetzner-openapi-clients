<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Model\Volume;
use Prefabcortex\Hetzner\Model\VolumeStatus;
use Prefabcortex\Hetzner\Validator\VolumeConstraint;
use Symfony\Component\Validator\Constraint;

final class VolumeFixture
{
    public static function build(): Volume
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
        $protection = Protection::builder(false)->build();

        return Volume::builder(
            // id
            42,
            // created
            new DateTime('2024-01-01'),
            // name
            'my-resource',
            // server
            12,
            // location
            $location,
            // size
            42.0,
            // linuxDevice
            '/dev/disk/by-id/scsi-0HC_Volume_4711',
            // protection
            $protection,
            // labels
            [],
            // status
            VolumeStatus::available,
            // format
            'xfs',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): Volume */
    public static function reader(): callable
    {
        return Volume::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return VolumeConstraint::constraints();
    }
}
