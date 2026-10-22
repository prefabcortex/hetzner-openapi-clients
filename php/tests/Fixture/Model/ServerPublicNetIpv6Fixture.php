<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\DnsPtr;
use Prefabcortex\Hetzner\Model\ServerPublicNetIpv6;
use Prefabcortex\Hetzner\Validator\ServerPublicNetIpv6Constraint;
use Symfony\Component\Validator\Constraint;

final class ServerPublicNetIpv6Fixture
{
    public static function build(): ServerPublicNetIpv6
    {
        $dnsPtr = DnsPtr::builder(
            // ip
            '2001:db8::1',
            // dnsPtr
            'server.example.com',
        )->build();

        return ServerPublicNetIpv6::builder(
            // ip
            '2001:db8::/64',
            // blocked
            false,
            // dnsPtr
            [$dnsPtr],
        )
            ->setId(42)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): ServerPublicNetIpv6 */
    public static function reader(): callable
    {
        return ServerPublicNetIpv6::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ServerPublicNetIpv6Constraint::constraints();
    }
}
