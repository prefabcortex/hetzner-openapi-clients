<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerAlgorithm2;
use Prefabcortex\Hetzner\Model\LoadBalancerAlgorithmType;
use Prefabcortex\Hetzner\Validator\LoadBalancerAlgorithm2Constraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerAlgorithm2Fixture
{
    public static function build(): LoadBalancerAlgorithm2
    {
        return LoadBalancerAlgorithm2::builder(LoadBalancerAlgorithmType::round_robin)->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerAlgorithm2 */
    public static function reader(): callable
    {
        return LoadBalancerAlgorithm2::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerAlgorithm2Constraint::constraints();
    }
}
