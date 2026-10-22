<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\AssigneeType;
use Prefabcortex\Hetzner\Model\DnsPtr;
use Prefabcortex\Hetzner\Model\IpType;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Model\ListPrimaryIpsResponse200;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Model\PrimaryIP;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Validator\ListPrimaryIpsResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListPrimaryIpsResponse200Fixture
{
    public static function build(): ListPrimaryIpsResponse200
    {
        $location = Location::builder(
            // id
            42,
            // name
            'fsn1',
            // description
            'Falkenstein DC Park 1',
            // country
            'DE',
            // city
            'Falkenstein',
            // latitude
            50.47612,
            // longitude
            12.370071,
            // networkZone
            'eu-central',
        )->build();
        $dnsPtr = DnsPtr::builder(
            // ip
            '2001:db8::1',
            // dnsPtr
            'server.example.com',
        )->build();
        $protection = Protection::builder(false)->build();
        $primaryIP = PrimaryIP::builder(
            // id
            42,
            // name
            'my-resource',
            // labels
            [],
            // created
            new DateTime('2024-01-01'),
            // blocked
            false,
            // location
            $location,
            // ip
            '2001:db8::/64',
            // dnsPtr
            [$dnsPtr],
            // protection
            $protection,
            // type
            IpType::ipv4,
            // autoDelete
            true,
            // assigneeType
            AssigneeType::server,
            // assigneeId
            17,
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

        return ListPrimaryIpsResponse200::builder(
            // primaryIps
            [$primaryIP],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListPrimaryIpsResponse200 */
    public static function reader(): callable
    {
        return ListPrimaryIpsResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListPrimaryIpsResponse200Constraint::constraints();
    }
}
