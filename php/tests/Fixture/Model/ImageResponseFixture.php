<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Architecture;
use Prefabcortex\Hetzner\Model\CreatedFrom;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\Image;
use Prefabcortex\Hetzner\Model\ImageResponse;
use Prefabcortex\Hetzner\Model\ImageStatus;
use Prefabcortex\Hetzner\Model\ImageType;
use Prefabcortex\Hetzner\Model\OsFlavor;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Validator\ImageResponseConstraint;
use Symfony\Component\Validator\Constraint;

final class ImageResponseFixture
{
    public static function build(): ImageResponse
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

        return ImageResponse::builder($image)->build();
    }

    /** @return callable(array<int|string, mixed>): ImageResponse */
    public static function reader(): callable
    {
        return ImageResponse::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ImageResponseConstraint::constraints();
    }
}
