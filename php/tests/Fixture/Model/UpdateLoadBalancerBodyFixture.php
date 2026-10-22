<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateLoadBalancerBody;
use Prefabcortex\Hetzner\Validator\UpdateLoadBalancerBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateLoadBalancerBodyFixture
{
    public static function build(): UpdateLoadBalancerBody
    {
        return UpdateLoadBalancerBody::builder()
            ->setName('new-name')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateLoadBalancerBody */
    public static function reader(): callable
    {
        return UpdateLoadBalancerBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateLoadBalancerBodyConstraint::constraints();
    }
}
