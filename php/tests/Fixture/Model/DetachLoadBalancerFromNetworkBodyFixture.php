<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\DetachLoadBalancerFromNetworkBody;
use Prefabcortex\Hetzner\Validator\DetachLoadBalancerFromNetworkBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class DetachLoadBalancerFromNetworkBodyFixture
{
    public static function build(): DetachLoadBalancerFromNetworkBody
    {
        return DetachLoadBalancerFromNetworkBody::builder(4711)->build();
    }

    /** @return callable(array<int|string, mixed>): DetachLoadBalancerFromNetworkBody */
    public static function reader(): callable
    {
        return DetachLoadBalancerFromNetworkBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return DetachLoadBalancerFromNetworkBodyConstraint::constraints();
    }
}
