<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerServiceTCPProperties;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceTCPPropertiesProtocol;
use Prefabcortex\Hetzner\Validator\LoadBalancerServiceTCPPropertiesConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerServiceTCPPropertiesFixture
{
    public static function build(): LoadBalancerServiceTCPProperties
    {
        return LoadBalancerServiceTCPProperties::builder()
            ->setProtocol(LoadBalancerServiceTCPPropertiesProtocol::tcp)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerServiceTCPProperties */
    public static function reader(): callable
    {
        return LoadBalancerServiceTCPProperties::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerServiceTCPPropertiesConstraint::constraints();
    }
}
