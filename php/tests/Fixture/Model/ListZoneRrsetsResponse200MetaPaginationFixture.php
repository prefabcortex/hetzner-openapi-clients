<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ListZoneRrsetsResponse200MetaPagination;
use Prefabcortex\Hetzner\Validator\ListZoneRrsetsResponse200MetaPaginationConstraint;
use Symfony\Component\Validator\Constraint;

final class ListZoneRrsetsResponse200MetaPaginationFixture
{
    public static function build(): ListZoneRrsetsResponse200MetaPagination
    {
        return ListZoneRrsetsResponse200MetaPagination::builder(
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
    }

    /** @return callable(array<int|string, mixed>): ListZoneRrsetsResponse200MetaPagination */
    public static function reader(): callable
    {
        return ListZoneRrsetsResponse200MetaPagination::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListZoneRrsetsResponse200MetaPaginationConstraint::constraints();
    }
}
