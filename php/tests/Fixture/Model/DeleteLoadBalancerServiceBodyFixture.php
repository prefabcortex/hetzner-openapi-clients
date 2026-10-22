<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\DeleteLoadBalancerServiceBody;
use Prefabcortex\Hetzner\Validator\DeleteLoadBalancerServiceBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class DeleteLoadBalancerServiceBodyFixture
{
    public static function build(): DeleteLoadBalancerServiceBody
    {
        return DeleteLoadBalancerServiceBody::builder(443)->build();
    }

    /** @return callable(array<int|string, mixed>): DeleteLoadBalancerServiceBody */
    public static function reader(): callable
    {
        return DeleteLoadBalancerServiceBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return DeleteLoadBalancerServiceBodyConstraint::constraints();
    }
}
