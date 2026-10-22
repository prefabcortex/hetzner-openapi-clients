<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\PrimaryZoneProperties;
use Prefabcortex\Hetzner\Model\PrimaryZonePropertiesMode;
use Prefabcortex\Hetzner\Validator\PrimaryZonePropertiesConstraint;
use Symfony\Component\Validator\Constraint;

final class PrimaryZonePropertiesFixture
{
    public static function build(): PrimaryZoneProperties
    {
        return PrimaryZoneProperties::builder(PrimaryZonePropertiesMode::primary)->build();
    }

    /** @return callable(array<int|string, mixed>): PrimaryZoneProperties */
    public static function reader(): callable
    {
        return PrimaryZoneProperties::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return PrimaryZonePropertiesConstraint::constraints();
    }
}
