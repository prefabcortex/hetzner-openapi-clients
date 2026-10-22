<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ListZoneRrsetsResponse200;
use Prefabcortex\Hetzner\Model\ListZoneRrsetsResponse200Meta;
use Prefabcortex\Hetzner\Model\ListZoneRrsetsResponse200MetaPagination;
use Prefabcortex\Hetzner\Model\Record;
use Prefabcortex\Hetzner\Model\RRSet;
use Prefabcortex\Hetzner\Model\RRSetProtection;
use Prefabcortex\Hetzner\Model\RRSetType;
use Prefabcortex\Hetzner\Validator\ListZoneRrsetsResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListZoneRrsetsResponse200Fixture
{
    public static function build(): ListZoneRrsetsResponse200
    {
        $protection = RRSetProtection::builder(false)->build();
        $record = Record::builder('198.51.100.1')
            ->setComment('My web server at Hetzner Cloud.')
            ->build();
        $rRSet = RRSet::builder(
            // id
            'REPLACE_ME',
            // name
            'www',
            // type
            RRSetType::A,
            // ttl
            3600,
            // labels
            [],
            // protection
            $protection,
            // records
            [$record],
            // zone
            42,
        )->build();
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
        $meta = ListZoneRrsetsResponse200Meta::builder($pagination)->build();

        return ListZoneRrsetsResponse200::builder(
            // rrsets
            [$rRSet],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListZoneRrsetsResponse200 */
    public static function reader(): callable
    {
        return ListZoneRrsetsResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListZoneRrsetsResponse200Constraint::constraints();
    }
}
