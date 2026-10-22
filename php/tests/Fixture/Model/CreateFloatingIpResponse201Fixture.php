<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\CreateFloatingIpResponse201;
use Prefabcortex\Hetzner\Model\DnsPtr;
use Prefabcortex\Hetzner\Model\FloatingIp;
use Prefabcortex\Hetzner\Model\IpType;
use Prefabcortex\Hetzner\Model\Location;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Validator\CreateFloatingIpResponse201Constraint;
use Symfony\Component\Validator\Constraint;

final class CreateFloatingIpResponse201Fixture
{
    public static function build(): CreateFloatingIpResponse201
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

        return CreateFloatingIpResponse201::builder($floatingIp)->build();
    }

    /** @return callable(array<int|string, mixed>): CreateFloatingIpResponse201 */
    public static function reader(): callable
    {
        return CreateFloatingIpResponse201::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateFloatingIpResponse201Constraint::constraints();
    }
}
