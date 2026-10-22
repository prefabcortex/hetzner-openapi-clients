<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Validator\DeprecationInfoConstraint;
use Symfony\Component\Validator\Constraint;

final class DeprecationInfoFixture
{
    public static function build(): DeprecationInfo
    {
        return DeprecationInfo::builder(
            // unavailableAfter
            new DateTime('2024-01-01'),
            // announced
            new DateTime('2024-01-01'),
        )->build();
    }

    /** @return callable(array<int|string, mixed>): DeprecationInfo */
    public static function reader(): callable
    {
        return DeprecationInfo::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return DeprecationInfoConstraint::constraints();
    }
}
