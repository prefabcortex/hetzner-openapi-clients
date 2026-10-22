<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ResizeVolumeBody;
use Prefabcortex\Hetzner\Validator\ResizeVolumeBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ResizeVolumeBodyFixture
{
    public static function build(): ResizeVolumeBody
    {
        return ResizeVolumeBody::builder(50.0)->build();
    }

    /** @return callable(array<int|string, mixed>): ResizeVolumeBody */
    public static function reader(): callable
    {
        return ResizeVolumeBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ResizeVolumeBodyConstraint::constraints();
    }
}
