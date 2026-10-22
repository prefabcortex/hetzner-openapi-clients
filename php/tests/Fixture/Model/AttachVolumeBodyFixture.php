<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\AttachVolumeBody;
use Prefabcortex\Hetzner\Validator\AttachVolumeBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class AttachVolumeBodyFixture
{
    public static function build(): AttachVolumeBody
    {
        return AttachVolumeBody::builder(43)
            ->setAutomount(false)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): AttachVolumeBody */
    public static function reader(): callable
    {
        return AttachVolumeBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return AttachVolumeBodyConstraint::constraints();
    }
}
