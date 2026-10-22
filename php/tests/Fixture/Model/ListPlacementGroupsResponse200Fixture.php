<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Model\ListPlacementGroupsResponse200;
use Prefabcortex\Hetzner\Model\PlacementGroup;
use Prefabcortex\Hetzner\Model\PlacementGroupType;
use Prefabcortex\Hetzner\Validator\ListPlacementGroupsResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListPlacementGroupsResponse200Fixture
{
    public static function build(): ListPlacementGroupsResponse200
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
        $pagination = ListMetaPagination::builder(
            // page
            3,
            // perPage
            25,
            // previousPage
            2,
            // nextPage
            4,
            // lastPage
            4,
            // totalEntries
            100,
        )->build();
        $meta = ListMeta::builder($pagination)->build();

        return ListPlacementGroupsResponse200::builder(
            // placementGroups
            [$placementGroup],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListPlacementGroupsResponse200 */
    public static function reader(): callable
    {
        return ListPlacementGroupsResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListPlacementGroupsResponse200Constraint::constraints();
    }
}
