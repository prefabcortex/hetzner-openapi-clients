<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerPublicIp;
use Prefabcortex\Hetzner\Validator\LoadBalancerPublicIpConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerPublicIpFixture
{
    public static function build(): LoadBalancerPublicIp
    {
        return LoadBalancerPublicIp::builder(
            // id
            42,
            // ip
            '1.2.3.4',
            // blocked
            false,
            // dnsPtr
            'lb1.example.com',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerPublicIp */
    public static function reader(): callable
    {
        return LoadBalancerPublicIp::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerPublicIpConstraint::constraints();
    }
}
