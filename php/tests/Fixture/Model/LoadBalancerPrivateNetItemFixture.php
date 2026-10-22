<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerPrivateNetItem;
use Prefabcortex\Hetzner\Validator\LoadBalancerPrivateNetItemConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerPrivateNetItemFixture
{
    public static function build(): LoadBalancerPrivateNetItem
    {
        return LoadBalancerPrivateNetItem::builder(
            // network
            4711,
            // ip
            '10.0.0.2',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerPrivateNetItem */
    public static function reader(): callable
    {
        return LoadBalancerPrivateNetItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerPrivateNetItemConstraint::constraints();
    }
}
