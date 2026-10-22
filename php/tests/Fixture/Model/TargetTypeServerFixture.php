<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthStatus;
use Prefabcortex\Hetzner\Model\HealthStatusDetail;
use Prefabcortex\Hetzner\Model\HealthStatusStatus;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetServer;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetType;
use Prefabcortex\Hetzner\Model\TargetTypeServer;
use Prefabcortex\Hetzner\Validator\TargetTypeServerConstraint;
use Symfony\Component\Validator\Constraint;

final class TargetTypeServerFixture
{
    public static function build(): TargetTypeServer
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

        return TargetTypeServer::builder(
            // type
            LoadBalancerTargetType::server,
            // server
            $server,
            // healthStatus
            [$healthStatus],
            // usePrivateIp
            false,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): TargetTypeServer */
    public static function reader(): callable
    {
        return TargetTypeServer::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return TargetTypeServerConstraint::constraints();
    }
}
