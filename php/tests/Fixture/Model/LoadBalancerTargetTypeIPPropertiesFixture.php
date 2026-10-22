<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthStatus;
use Prefabcortex\Hetzner\Model\HealthStatusDetail;
use Prefabcortex\Hetzner\Model\HealthStatusStatus;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetIP;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetTypeIPProperties;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetTypeIPPropertiesType;
use Prefabcortex\Hetzner\Validator\LoadBalancerTargetTypeIPPropertiesConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerTargetTypeIPPropertiesFixture
{
    public static function build(): LoadBalancerTargetTypeIPProperties
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

        return LoadBalancerTargetTypeIPProperties::builder(
            // ip
            $ip,
            // healthStatus
            [$healthStatus],
        )
            ->setType(LoadBalancerTargetTypeIPPropertiesType::ip)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerTargetTypeIPProperties */
    public static function reader(): callable
    {
        return LoadBalancerTargetTypeIPProperties::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerTargetTypeIPPropertiesConstraint::constraints();
    }
}
