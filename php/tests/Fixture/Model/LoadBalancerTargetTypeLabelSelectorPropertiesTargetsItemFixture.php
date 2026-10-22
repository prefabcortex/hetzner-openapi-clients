<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthStatus;
use Prefabcortex\Hetzner\Model\HealthStatusDetail;
use Prefabcortex\Hetzner\Model\HealthStatusStatus;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetServer;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItem;
use Prefabcortex\Hetzner\Validator\LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItemConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItemFixture
{
    public static function build(): LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItem
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

        return LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItem::builder(
            // type
            'server',
            // server
            $server,
            // healthStatus
            [$healthStatus],
            // usePrivateIp
            false,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItem */
    public static function reader(): callable
    {
        return LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItemConstraint::constraints();
    }
}
