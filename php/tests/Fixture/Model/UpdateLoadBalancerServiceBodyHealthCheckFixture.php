<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateLoadBalancerServiceBodyHealthCheck;
use Prefabcortex\Hetzner\Validator\UpdateLoadBalancerServiceBodyHealthCheckConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateLoadBalancerServiceBodyHealthCheckFixture
{
    public static function build(): UpdateLoadBalancerServiceBodyHealthCheck
    {
        return UpdateLoadBalancerServiceBodyHealthCheck::builder()
            ->setPort(4711)
            ->setInterval(15)
            ->setTimeout(10)
            ->setRetries(3)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateLoadBalancerServiceBodyHealthCheck */
    public static function reader(): callable
    {
        return UpdateLoadBalancerServiceBodyHealthCheck::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateLoadBalancerServiceBodyHealthCheckConstraint::constraints();
    }
}
