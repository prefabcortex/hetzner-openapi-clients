<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\SecondaryZoneProperties;
use Prefabcortex\Hetzner\Model\SecondaryZonePropertiesMode;
use Prefabcortex\Hetzner\Validator\SecondaryZonePropertiesConstraint;
use Symfony\Component\Validator\Constraint;

final class SecondaryZonePropertiesFixture
{
    public static function build(): SecondaryZoneProperties
    {
        return SecondaryZoneProperties::builder(SecondaryZonePropertiesMode::secondary)->build();
    }

    /** @return callable(array<int|string, mixed>): SecondaryZoneProperties */
    public static function reader(): callable
    {
        return SecondaryZoneProperties::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return SecondaryZonePropertiesConstraint::constraints();
    }
}
