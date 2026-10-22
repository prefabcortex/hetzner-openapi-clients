<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateLoadBalancerServiceBody;
use Prefabcortex\Hetzner\Validator\UpdateLoadBalancerServiceBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateLoadBalancerServiceBodyFixture
{
    public static function build(): UpdateLoadBalancerServiceBody
    {
        return UpdateLoadBalancerServiceBody::builder(443)
            ->setDestinationPort(80)
            ->setProxyprotocol(false)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateLoadBalancerServiceBody */
    public static function reader(): callable
    {
        return UpdateLoadBalancerServiceBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateLoadBalancerServiceBodyConstraint::constraints();
    }
}
