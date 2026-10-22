<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthCheckProtocol;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceBase;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceBaseHealthCheck;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceProtocol;
use Prefabcortex\Hetzner\Validator\LoadBalancerServiceBaseConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerServiceBaseFixture
{
    public static function build(): LoadBalancerServiceBase
    {
        $healthCheck = LoadBalancerServiceBaseHealthCheck::builder(
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

        return LoadBalancerServiceBase::builder(
            // protocol
            LoadBalancerServiceProtocol::tcp,
            // listenPort
            443,
            // destinationPort
            80,
            // proxyprotocol
            false,
            // healthCheck
            $healthCheck,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerServiceBase */
    public static function reader(): callable
    {
        return LoadBalancerServiceBase::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerServiceBaseConstraint::constraints();
    }
}
