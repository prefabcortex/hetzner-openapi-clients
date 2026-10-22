<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerPublicIp;
use Prefabcortex\Hetzner\Model\LoadBalancerPublicNet;
use Prefabcortex\Hetzner\Validator\LoadBalancerPublicNetConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerPublicNetFixture
{
    public static function build(): LoadBalancerPublicNet
    {
        $ipv4 = LoadBalancerPublicIp::builder(
            // id
            42,
            // ip
            '1.2.3.4',
            // blocked
            false,
            // dnsPtr
            'lb1.example.com',
        )->build();
        $ipv6 = LoadBalancerPublicIp::builder(
            // id
            42,
            // ip
            '1.2.3.4',
            // blocked
            false,
            // dnsPtr
            'lb1.example.com',
        )->build();

        return LoadBalancerPublicNet::builder(
            // enabled
            true,
            // ipv4
            $ipv4,
            // ipv6
            $ipv6,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerPublicNet */
    public static function reader(): callable
    {
        return LoadBalancerPublicNet::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerPublicNetConstraint::constraints();
    }
}
