<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateLoadBalancerBodyTargetsItem;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetType;
use Prefabcortex\Hetzner\Validator\CreateLoadBalancerBodyTargetsItemConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateLoadBalancerBodyTargetsItemFixture
{
    public static function build(): CreateLoadBalancerBodyTargetsItem
    {
        return CreateLoadBalancerBodyTargetsItem::builder(LoadBalancerTargetType::server)
            ->setUsePrivateIp(true)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateLoadBalancerBodyTargetsItem */
    public static function reader(): callable
    {
        return CreateLoadBalancerBodyTargetsItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateLoadBalancerBodyTargetsItemConstraint::constraints();
    }
}
