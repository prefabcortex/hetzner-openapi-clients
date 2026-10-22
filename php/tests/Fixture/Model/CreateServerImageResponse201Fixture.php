<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Action;
use Prefabcortex\Hetzner\Model\ActionError;
use Prefabcortex\Hetzner\Model\ActionResource;
use Prefabcortex\Hetzner\Model\ActionStatus;
use Prefabcortex\Hetzner\Model\Architecture;
use Prefabcortex\Hetzner\Model\CreatedFrom;
use Prefabcortex\Hetzner\Model\CreateServerImageResponse201;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\Image;
use Prefabcortex\Hetzner\Model\ImageStatus;
use Prefabcortex\Hetzner\Model\ImageType;
use Prefabcortex\Hetzner\Model\OsFlavor;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Validator\CreateServerImageResponse201Constraint;
use Symfony\Component\Validator\Constraint;

final class CreateServerImageResponse201Fixture
{
    public static function build(): CreateServerImageResponse201
    {
        $createdFrom = CreatedFrom::builder(
            // id
            1,
            // name
            'Server',
        )->build();
        $protection = Protection::builder(false)->build();
        $deprecation = DeprecationInfo::builder(
            // unavailableAfter
            new DateTime('2024-01-01'),
            // announced
            new DateTime('2024-01-01'),
        )->build();
        $image = Image::builder(
            // id
            42,
            // type
            ImageType::system,
            // status
            ImageStatus::available,
            // name
            'ubuntu-24.04',
            // description
            'Ubuntu 24.04 Standard 64 bit',
            // imageSize
            2.3,
            // diskSize
            10.0,
            // created
            new DateTime('2024-01-01'),
            // createdFrom
            $createdFrom,
            // boundTo
            0,
            // osFlavor
            OsFlavor::ubuntu,
            // osVersion
            '24.04',
            // protection
            $protection,
            // deprecated
            new DateTime('2024-01-01'),
            // deprecation
            $deprecation,
            // deleted
            'REPLACE_ME',
            // labels
            [],
            // architecture
            Architecture::x86,
        )
            ->setRapidDeploy(false)
            ->build();
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

        return CreateServerImageResponse201::builder(
            // image
            $image,
            // action
            $action,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): CreateServerImageResponse201 */
    public static function reader(): callable
    {
        return CreateServerImageResponse201::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateServerImageResponse201Constraint::constraints();
    }
}
