<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerTargetServerRequest;
use Prefabcortex\Hetzner\Validator\LoadBalancerTargetServerRequestConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerTargetServerRequestFixture
{
    public static function build(): LoadBalancerTargetServerRequest
    {
        return LoadBalancerTargetServerRequest::builder(80)
            ->setIp('2001:db8::1')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerTargetServerRequest */
    public static function reader(): callable
    {
        return LoadBalancerTargetServerRequest::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerTargetServerRequestConstraint::constraints();
    }
}
