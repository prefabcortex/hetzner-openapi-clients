<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\ServerTypeLocationsItem;
use Prefabcortex\Hetzner\Validator\ServerTypeLocationsItemConstraint;
use Symfony\Component\Validator\Constraint;

final class ServerTypeLocationsItemFixture
{
    public static function build(): ServerTypeLocationsItem
    {
        $deprecation = DeprecationInfo::builder(
            // unavailableAfter
            new DateTime('2024-01-01'),
            // announced
            new DateTime('2024-01-01'),
        )->build();

        return ServerTypeLocationsItem::builder(
            // id
            42,
            // name
            'fsn1',
            // deprecation
            $deprecation,
            // recommended
            false,
            // available
            true,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ServerTypeLocationsItem */
    public static function reader(): callable
    {
        return ServerTypeLocationsItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ServerTypeLocationsItemConstraint::constraints();
    }
}
