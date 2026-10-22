<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Action;
use Prefabcortex\Hetzner\Model\ActionError;
use Prefabcortex\Hetzner\Model\ActionResource;
use Prefabcortex\Hetzner\Model\ActionStatus;
use Prefabcortex\Hetzner\Model\CreateVolumeResponse201;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Model\Volume;
use Prefabcortex\Hetzner\Model\VolumeStatus;
use Prefabcortex\Hetzner\Validator\CreateVolumeResponse201Constraint;
use Symfony\Component\Validator\Constraint;

final class CreateVolumeResponse201Fixture
{
    public static function build(): CreateVolumeResponse201
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
        $actionResource = ActionResource::builder(
            // id
            42,
            // type
            'server',
        )->build();
        $error = ActionError::builder(
            // code
            'action_failed',
            // message
            'Action failed',
        )->build();
        $action = Action::builder(
            // id
            42,
            // command
            'start_resource',
            // status
            ActionStatus::running,
            // started
            new DateTime('2024-01-01'),
            // finished
            new DateTime('2024-01-01'),
            // progress
            100,
            // resources
            [$actionResource],
            // error
            $error,
        )->build();
        $actionResource_1 = ActionResource::builder(
            // id
            42,
            // type
            'server',
        )->build();
        $error_1 = ActionError::builder(
            // code
            'action_failed',
            // message
            'Action failed',
        )->build();
        $action_1 = Action::builder(
            // id
            42,
            // command
            'start_resource',
            // status
            ActionStatus::running,
            // started
            new DateTime('2024-01-01'),
            // finished
            new DateTime('2024-01-01'),
            // progress
            100,
            // resources
            [$actionResource_1],
            // error
            $error_1,
        )->build();

        return CreateVolumeResponse201::builder(
            // volume
            $volume,
            // action
            $action,
            // nextActions
            [$action_1],
        )->build();
    }

    /** @return callable(array<int|string, mixed>): CreateVolumeResponse201 */
    public static function reader(): callable
    {
        return CreateVolumeResponse201::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateVolumeResponse201Constraint::constraints();
    }
}
