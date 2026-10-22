<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\AttachLoadBalancerToNetworkBody;
use Prefabcortex\Hetzner\Validator\AttachLoadBalancerToNetworkBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class AttachLoadBalancerToNetworkBodyFixture
{
    public static function build(): AttachLoadBalancerToNetworkBody
    {
        return AttachLoadBalancerToNetworkBody::builder(123)
            ->setIp('10.0.1.1')
            ->setIpRange('10.0.1.0/24')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): AttachLoadBalancerToNetworkBody */
    public static function reader(): callable
    {
        return AttachLoadBalancerToNetworkBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return AttachLoadBalancerToNetworkBodyConstraint::constraints();
    }
}
