<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\PlacementGroup;
use Prefabcortex\Hetzner\Model\PlacementGroupResponse;
use Prefabcortex\Hetzner\Model\PlacementGroupType;
use Prefabcortex\Hetzner\Validator\PlacementGroupResponseConstraint;
use Symfony\Component\Validator\Constraint;

final class PlacementGroupResponseFixture
{
    public static function build(): PlacementGroupResponse
    {
        $placementGroup = PlacementGroup::builder(
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

        return PlacementGroupResponse::builder($placementGroup)->build();
    }

    /** @return callable(array<int|string, mixed>): PlacementGroupResponse */
    public static function reader(): callable
    {
        return PlacementGroupResponse::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return PlacementGroupResponseConstraint::constraints();
    }
}
