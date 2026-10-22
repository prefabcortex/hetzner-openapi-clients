<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthCheckProtocol;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceHealthCheck;
use Prefabcortex\Hetzner\Validator\LoadBalancerServiceHealthCheckConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerServiceHealthCheckFixture
{
    public static function build(): LoadBalancerServiceHealthCheck
    {
        return LoadBalancerServiceHealthCheck::builder(
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

    /** @return callable(array<int|string, mixed>): LoadBalancerServiceHealthCheck */
    public static function reader(): callable
    {
        return LoadBalancerServiceHealthCheck::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerServiceHealthCheckConstraint::constraints();
    }
}
