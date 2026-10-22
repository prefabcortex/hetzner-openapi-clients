<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthStatus;
use Prefabcortex\Hetzner\Model\HealthStatusDetail;
use Prefabcortex\Hetzner\Model\HealthStatusStatus;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetLabelSelector;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetServer;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetTypeLabelSelectorProperties;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetTypeLabelSelectorPropertiesTargetsItem;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetTypeLabelSelectorPropertiesType;
use Prefabcortex\Hetzner\Validator\LoadBalancerTargetTypeLabelSelectorPropertiesConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerTargetTypeLabelSelectorPropertiesFixture
{
    public static function build(): LoadBalancerTargetTypeLabelSelectorProperties
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

        return LoadBalancerTargetTypeLabelSelectorProperties::builder(
            // labelSelector
            $labelSelector,
            // targets
            [$loadBalancerTargetTypeLabelSelectorPropertiesTargetsItem],
            // usePrivateIp
            false,
        )
            ->setType(LoadBalancerTargetTypeLabelSelectorPropertiesType::label_selector)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerTargetTypeLabelSelectorProperties */
    public static function reader(): callable
    {
        return LoadBalancerTargetTypeLabelSelectorProperties::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerTargetTypeLabelSelectorPropertiesConstraint::constraints();
    }
}
