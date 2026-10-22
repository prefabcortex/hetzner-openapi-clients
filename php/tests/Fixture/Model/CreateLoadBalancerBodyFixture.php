<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateLoadBalancerBody;
use Prefabcortex\Hetzner\Model\LoadBalancerAlgorithm;
use Prefabcortex\Hetzner\Model\LoadBalancerAlgorithmType;
use Prefabcortex\Hetzner\Validator\CreateLoadBalancerBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateLoadBalancerBodyFixture
{
    public static function build(): CreateLoadBalancerBody
    {
        $algorithm = LoadBalancerAlgorithm::builder(LoadBalancerAlgorithmType::round_robin)->build();

        return CreateLoadBalancerBody::builder(
            // name
            'Web Frontend',
            // loadBalancerType
            'lb11',
        )
            ->setAlgorithm($algorithm)
            ->setPublicInterface(true)
            ->setNetwork(123)
            ->setNetworkZone('eu-central')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateLoadBalancerBody */
    public static function reader(): callable
    {
        return CreateLoadBalancerBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateLoadBalancerBodyConstraint::constraints();
    }
}
