<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthStatus;
use Prefabcortex\Hetzner\Model\HealthStatusDetail;
use Prefabcortex\Hetzner\Model\HealthStatusStatus;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetLabelSelector;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetServer;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetType;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItem;
use Prefabcortex\Hetzner\Model\TargetTypeLabelSelector;
use Prefabcortex\Hetzner\Validator\TargetTypeLabelSelectorConstraint;
use Symfony\Component\Validator\Constraint;

final class TargetTypeLabelSelectorFixture
{
    public static function build(): TargetTypeLabelSelector
    {
        $labelSelector = LoadBalancerTargetLabelSelector::builder('env=prod')->build();
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
        $loadBalancerTargetTypeLabelSelectorPropertiesTargetsItem = LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItem::builder(
            // type
            'server',
            // server
            $server,
            // healthStatus
            [$healthStatus],
            // usePrivateIp
            false,
        )->build();

        return TargetTypeLabelSelector::builder(
            // type
            LoadBalancerTargetType::label_selector,
            // labelSelector
            $labelSelector,
            // targets
            [$loadBalancerTargetTypeLabelSelectorPropertiesTargetsItem],
            // usePrivateIp
            false,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): TargetTypeLabelSelector */
    public static function reader(): callable
    {
        return TargetTypeLabelSelector::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return TargetTypeLabelSelectorConstraint::constraints();
    }
}
