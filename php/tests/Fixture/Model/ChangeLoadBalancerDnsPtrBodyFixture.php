<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeLoadBalancerDnsPtrBody;
use Prefabcortex\Hetzner\Validator\ChangeLoadBalancerDnsPtrBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeLoadBalancerDnsPtrBodyFixture
{
    public static function build(): ChangeLoadBalancerDnsPtrBody
    {
        return ChangeLoadBalancerDnsPtrBody::builder(
            // ip
            '2001:db8::1',
            // dnsPtr
            'server.example.com',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeLoadBalancerDnsPtrBody */
    public static function reader(): callable
    {
        return ChangeLoadBalancerDnsPtrBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeLoadBalancerDnsPtrBodyConstraint::constraints();
    }
}
