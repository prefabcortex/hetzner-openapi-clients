<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\DnsPtr;
use Prefabcortex\Hetzner\Model\ServerPublicNet;
use Prefabcortex\Hetzner\Model\ServerPublicNetIpv4;
use Prefabcortex\Hetzner\Model\ServerPublicNetIpv6;
use Prefabcortex\Hetzner\Validator\ServerPublicNetConstraint;
use Symfony\Component\Validator\Constraint;

final class ServerPublicNetFixture
{
    public static function build(): ServerPublicNet
    {
        $ipv4 = ServerPublicNetIpv4::builder(
            // ip
            '1.2.3.4',
            // blocked
            false,
            // dnsPtr
            'server01.example.com',
        )
            ->setId(42)
            ->build();
        $dnsPtr = DnsPtr::builder(
            // ip
            '2001:db8::1',
            // dnsPtr
            'server.example.com',
        )->build();
        $ipv6 = ServerPublicNetIpv6::builder(
            // ip
            '2001:db8::/64',
            // blocked
            false,
            // dnsPtr
            [$dnsPtr],
        )
            ->setId(42)
            ->build();

        return ServerPublicNet::builder(
            // ipv4
            $ipv4,
            // ipv6
            $ipv6,
            // floatingIps
            [478],
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ServerPublicNet */
    public static function reader(): callable
    {
        return ServerPublicNet::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ServerPublicNetConstraint::constraints();
    }
}
