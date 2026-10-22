<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Model\ListVolumesResponse200;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Model\Volume;
use Prefabcortex\Hetzner\Model\VolumeStatus;
use Prefabcortex\Hetzner\Validator\ListVolumesResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListVolumesResponse200Fixture
{
    public static function build(): ListVolumesResponse200
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
        $volume = Volume::builder(
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

        return ListVolumesResponse200::builder(
            // volumes
            [$volume],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListVolumesResponse200 */
    public static function reader(): callable
    {
        return ListVolumesResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListVolumesResponse200Constraint::constraints();
    }
}
