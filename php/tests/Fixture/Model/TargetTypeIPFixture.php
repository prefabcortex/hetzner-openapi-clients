<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthStatus;
use Prefabcortex\Hetzner\Model\HealthStatusDetail;
use Prefabcortex\Hetzner\Model\HealthStatusStatus;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetIP;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetType;
use Prefabcortex\Hetzner\Model\TargetTypeIP;
use Prefabcortex\Hetzner\Validator\TargetTypeIPConstraint;
use Symfony\Component\Validator\Constraint;

final class TargetTypeIPFixture
{
    public static function build(): TargetTypeIP
    {
        $ip = LoadBalancerTargetIP::builder('203.0.113.1')->build();
        $healthStatus = HealthStatus::builder(
            // listenPort
            443,
            // status
            HealthStatusStatus::healthy,
        )
            ->setDetail(HealthStatusDetail::unexpected_http_status)
            ->setHttpStatusCode(503)
            ->build();

        return TargetTypeIP::builder(
            // type
            LoadBalancerTargetType::ip,
            // ip
            $ip,
            // healthStatus
            [$healthStatus],
        )->build();
    }

    /** @return callable(array<int|string, mixed>): TargetTypeIP */
    public static function reader(): callable
    {
        return TargetTypeIP::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return TargetTypeIPConstraint::constraints();
    }
}
