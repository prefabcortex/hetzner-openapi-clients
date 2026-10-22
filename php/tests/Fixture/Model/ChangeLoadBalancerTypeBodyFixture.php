<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeLoadBalancerTypeBody;
use Prefabcortex\Hetzner\Validator\ChangeLoadBalancerTypeBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeLoadBalancerTypeBodyFixture
{
    public static function build(): ChangeLoadBalancerTypeBody
    {
        return ChangeLoadBalancerTypeBody::builder('lb11')->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeLoadBalancerTypeBody */
    public static function reader(): callable
    {
        return ChangeLoadBalancerTypeBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeLoadBalancerTypeBodyConstraint::constraints();
    }
}
