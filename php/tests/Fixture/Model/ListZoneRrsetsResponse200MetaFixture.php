<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ListZoneRrsetsResponse200Meta;
use Prefabcortex\Hetzner\Model\ListZoneRrsetsResponse200MetaPagination;
use Prefabcortex\Hetzner\Validator\ListZoneRrsetsResponse200MetaConstraint;
use Symfony\Component\Validator\Constraint;

final class ListZoneRrsetsResponse200MetaFixture
{
    public static function build(): ListZoneRrsetsResponse200Meta
    {
        $pagination = ListZoneRrsetsResponse200MetaPagination::builder(
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

        return ListZoneRrsetsResponse200Meta::builder($pagination)->build();
    }

    /** @return callable(array<int|string, mixed>): ListZoneRrsetsResponse200Meta */
    public static function reader(): callable
    {
        return ListZoneRrsetsResponse200Meta::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListZoneRrsetsResponse200MetaConstraint::constraints();
    }
}
