<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthCheckProtocol;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceBaseHealthCheck;
use Prefabcortex\Hetzner\Validator\LoadBalancerServiceBaseHealthCheckConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerServiceBaseHealthCheckFixture
{
    public static function build(): LoadBalancerServiceBaseHealthCheck
    {
        return LoadBalancerServiceBaseHealthCheck::builder(
            // protocol
            HealthCheckProtocol::tcp,
            // port
            4711,
            // interval
            15,
            // timeout
            10,
            // retries
            3,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerServiceBaseHealthCheck */
    public static function reader(): callable
    {
        return LoadBalancerServiceBaseHealthCheck::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerServiceBaseHealthCheckConstraint::constraints();
    }
}
