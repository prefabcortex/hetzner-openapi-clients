<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\CreatePlacementGroupResponse201;
use Prefabcortex\Hetzner\Model\PlacementGroup;
use Prefabcortex\Hetzner\Model\PlacementGroupType;
use Prefabcortex\Hetzner\Validator\CreatePlacementGroupResponse201Constraint;
use Symfony\Component\Validator\Constraint;

final class CreatePlacementGroupResponse201Fixture
{
    public static function build(): CreatePlacementGroupResponse201
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

        return CreatePlacementGroupResponse201::builder($placementGroup)->build();
    }

    /** @return callable(array<int|string, mixed>): CreatePlacementGroupResponse201 */
    public static function reader(): callable
    {
        return CreatePlacementGroupResponse201::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreatePlacementGroupResponse201Constraint::constraints();
    }
}
