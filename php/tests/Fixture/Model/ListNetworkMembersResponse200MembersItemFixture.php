<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ListNetworkMembersResponse200MembersItem;
use Prefabcortex\Hetzner\Model\NetworkMemberStatus;
use Prefabcortex\Hetzner\Model\NetworkMemberType;
use Prefabcortex\Hetzner\Validator\ListNetworkMembersResponse200MembersItemConstraint;
use Symfony\Component\Validator\Constraint;

final class ListNetworkMembersResponse200MembersItemFixture
{
    public static function build(): ListNetworkMembersResponse200MembersItem
    {
        return ListNetworkMembersResponse200MembersItem::builder(
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
    }

    /** @return callable(array<int|string, mixed>): ListNetworkMembersResponse200MembersItem */
    public static function reader(): callable
    {
        return ListNetworkMembersResponse200MembersItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListNetworkMembersResponse200MembersItemConstraint::constraints();
    }
}
