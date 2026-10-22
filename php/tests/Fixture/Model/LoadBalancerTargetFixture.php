<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerTarget;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetType;
use Prefabcortex\Hetzner\Validator\LoadBalancerTargetConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerTargetFixture
{
    public static function build(): LoadBalancerTarget
    {
        return LoadBalancerTarget::builder(LoadBalancerTargetType::server)->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerTarget */
    public static function reader(): callable
    {
        return LoadBalancerTarget::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerTargetConstraint::constraints();
    }
}
