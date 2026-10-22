<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateLoadBalancerBodyPublicNet;
use Prefabcortex\Hetzner\Validator\CreateLoadBalancerBodyPublicNetConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateLoadBalancerBodyPublicNetFixture
{
    public static function build(): CreateLoadBalancerBodyPublicNet
    {
        return CreateLoadBalancerBodyPublicNet::builder()
            ->setIpv4(42)
            ->setIpv6(42)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateLoadBalancerBodyPublicNet */
    public static function reader(): callable
    {
        return CreateLoadBalancerBodyPublicNet::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateLoadBalancerBodyPublicNetConstraint::constraints();
    }
}
