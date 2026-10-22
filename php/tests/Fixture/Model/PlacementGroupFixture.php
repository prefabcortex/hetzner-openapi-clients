<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\PlacementGroup;
use Prefabcortex\Hetzner\Model\PlacementGroupType;
use Prefabcortex\Hetzner\Validator\PlacementGroupConstraint;
use Symfony\Component\Validator\Constraint;

final class PlacementGroupFixture
{
    public static function build(): PlacementGroup
    {
        return PlacementGroup::builder(
            // id
            42,
            // name
            'my-resource',
            // labels
            [],
            // type
            PlacementGroupType::spread,
            // created
            new DateTime('2024-01-01'),
            // servers
            [42],
        )->build();
    }

    /** @return callable(array<int|string, mixed>): PlacementGroup */
    public static function reader(): callable
    {
        return PlacementGroup::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return PlacementGroupConstraint::constraints();
    }
}
