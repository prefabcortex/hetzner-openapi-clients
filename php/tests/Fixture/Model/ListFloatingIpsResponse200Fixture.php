<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\DnsPtr;
use Prefabcortex\Hetzner\Model\FloatingIp;
use Prefabcortex\Hetzner\Model\IpType;
use Prefabcortex\Hetzner\Model\ListFloatingIpsResponse200;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Validator\ListFloatingIpsResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListFloatingIpsResponse200Fixture
{
    public static function build(): ListFloatingIpsResponse200
    {
        $dnsPtr = DnsPtr::builder(
            // ip
            '2001:db8::1',
            // dnsPtr
            'server.example.com',
        )->build();
        $homeLocation = Location::builder(
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
        $protection = Protection::builder(false)->build();
        $floatingIp = FloatingIp::builder(
            // id
            42,
            // name
            'my-resource',
            // description
            'This describes my resource',
            // ip
            '2001:db8::/64',
            // type
            IpType::ipv4,
            // server
            42,
            // dnsPtr
            [$dnsPtr],
            // homeLocation
            $homeLocation,
            // blocked
            false,
            // protection
            $protection,
            // labels
            [],
            // created
            new DateTime('2024-01-01'),
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

        return ListFloatingIpsResponse200::builder(
            // floatingIps
            [$floatingIp],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListFloatingIpsResponse200 */
    public static function reader(): callable
    {
        return ListFloatingIpsResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListFloatingIpsResponse200Constraint::constraints();
    }
}
