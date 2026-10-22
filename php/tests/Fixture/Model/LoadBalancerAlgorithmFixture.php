<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerAlgorithm;
use Prefabcortex\Hetzner\Model\LoadBalancerAlgorithmType;
use Prefabcortex\Hetzner\Validator\LoadBalancerAlgorithmConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerAlgorithmFixture
{
    public static function build(): LoadBalancerAlgorithm
    {
        return LoadBalancerAlgorithm::builder(LoadBalancerAlgorithmType::round_robin)->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerAlgorithm */
    public static function reader(): callable
    {
        return LoadBalancerAlgorithm::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerAlgorithmConstraint::constraints();
    }
}
