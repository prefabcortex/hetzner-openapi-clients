<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthStatus;
use Prefabcortex\Hetzner\Model\HealthStatusDetail;
use Prefabcortex\Hetzner\Model\HealthStatusStatus;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetServer;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetTypeServerProperties;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetTypeServerPropertiesType;
use Prefabcortex\Hetzner\Validator\LoadBalancerTargetTypeServerPropertiesConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerTargetTypeServerPropertiesFixture
{
    public static function build(): LoadBalancerTargetTypeServerProperties
    {
        $server = LoadBalancerTargetServer::builder(
            // id
            80,
            // ip
            '2001:db8::1',
        )->build();
        $healthStatus = HealthStatus::builder(
            // listenPort
            443,
            // status
            HealthStatusStatus::healthy,
        )
            ->setDetail(HealthStatusDetail::unexpected_http_status)
            ->setHttpStatusCode(503)
            ->build();

        return LoadBalancerTargetTypeServerProperties::builder(
            // server
            $server,
            // healthStatus
            [$healthStatus],
            // usePrivateIp
            false,
        )
            ->setType(LoadBalancerTargetTypeServerPropertiesType::server)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerTargetTypeServerProperties */
    public static function reader(): callable
    {
        return LoadBalancerTargetTypeServerProperties::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerTargetTypeServerPropertiesConstraint::constraints();
    }
}
