<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\AddLoadBalancerTargetBody;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetType;
use Prefabcortex\Hetzner\Validator\AddLoadBalancerTargetBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class AddLoadBalancerTargetBodyFixture
{
    public static function build(): AddLoadBalancerTargetBody
    {
        return AddLoadBalancerTargetBody::builder(LoadBalancerTargetType::server)
            ->setUsePrivateIp(true)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): AddLoadBalancerTargetBody */
    public static function reader(): callable
    {
        return AddLoadBalancerTargetBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return AddLoadBalancerTargetBodyConstraint::constraints();
    }
}
