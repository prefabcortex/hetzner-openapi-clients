<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Model\ListNetworkMembersResponse200;
use Prefabcortex\Hetzner\Model\ListNetworkMembersResponse200MembersItem;
use Prefabcortex\Hetzner\Model\NetworkMemberStatus;
use Prefabcortex\Hetzner\Model\NetworkMemberType;
use Prefabcortex\Hetzner\Validator\ListNetworkMembersResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListNetworkMembersResponse200Fixture
{
    public static function build(): ListNetworkMembersResponse200
    {
        $listNetworkMembersResponse200MembersItem = ListNetworkMembersResponse200MembersItem::builder(
            // type
            NetworkMemberType::server,
            // id
            42,
            // ip
            '10.0.1.2',
            // status
            NetworkMemberStatus::ok,
            // aliasIps
            ['10.0.1.20'],
            // subnet
            '10.0.1.0/24',
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

        return ListNetworkMembersResponse200::builder(
            // members
            [$listNetworkMembersResponse200MembersItem],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListNetworkMembersResponse200 */
    public static function reader(): callable
    {
        return ListNetworkMembersResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListNetworkMembersResponse200Constraint::constraints();
    }
}
