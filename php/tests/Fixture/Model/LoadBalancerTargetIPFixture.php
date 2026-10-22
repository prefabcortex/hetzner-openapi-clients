<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerTargetIP;
use Prefabcortex\Hetzner\Validator\LoadBalancerTargetIPConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerTargetIPFixture
{
    public static function build(): LoadBalancerTargetIP
    {
        return LoadBalancerTargetIP::builder('203.0.113.1')->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerTargetIP */
    public static function reader(): callable
    {
        return LoadBalancerTargetIP::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerTargetIPConstraint::constraints();
    }
}
