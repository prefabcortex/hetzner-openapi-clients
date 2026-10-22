<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\AddLoadBalancerServiceBody;
use Prefabcortex\Hetzner\Model\HealthCheckProtocol;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceHealthCheck;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceProtocol;
use Prefabcortex\Hetzner\Validator\AddLoadBalancerServiceBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class AddLoadBalancerServiceBodyFixture
{
    public static function build(): AddLoadBalancerServiceBody
    {
        $healthCheck = LoadBalancerServiceHealthCheck::builder(
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

        return AddLoadBalancerServiceBody::builder(
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

    /** @return callable(array<int|string, mixed>): AddLoadBalancerServiceBody */
    public static function reader(): callable
    {
        return AddLoadBalancerServiceBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return AddLoadBalancerServiceBodyConstraint::constraints();
    }
}
