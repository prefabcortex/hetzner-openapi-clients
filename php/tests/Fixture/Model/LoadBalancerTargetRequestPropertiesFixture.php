<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerTargetRequestProperties;
use Prefabcortex\Hetzner\Validator\LoadBalancerTargetRequestPropertiesConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerTargetRequestPropertiesFixture
{
    public static function build(): LoadBalancerTargetRequestProperties
    {
        return LoadBalancerTargetRequestProperties::builder()
            ->setUsePrivateIp(true)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerTargetRequestProperties */
    public static function reader(): callable
    {
        return LoadBalancerTargetRequestProperties::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerTargetRequestPropertiesConstraint::constraints();
    }
}
