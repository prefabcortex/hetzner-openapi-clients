<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerTargetServer;
use Prefabcortex\Hetzner\Validator\LoadBalancerTargetServerConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerTargetServerFixture
{
    public static function build(): LoadBalancerTargetServer
    {
        return LoadBalancerTargetServer::builder(
            // id
            80,
            // ip
            '2001:db8::1',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerTargetServer */
    public static function reader(): callable
    {
        return LoadBalancerTargetServer::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerTargetServerConstraint::constraints();
    }
}
