<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerTargetType;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetTypeBase;
use Prefabcortex\Hetzner\Validator\LoadBalancerTargetTypeBaseConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerTargetTypeBaseFixture
{
    public static function build(): LoadBalancerTargetTypeBase
    {
        return LoadBalancerTargetTypeBase::builder(LoadBalancerTargetType::server)->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerTargetTypeBase */
    public static function reader(): callable
    {
        return LoadBalancerTargetTypeBase::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerTargetTypeBaseConstraint::constraints();
    }
}
