<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeFloatingIpDnsPtrBody;
use Prefabcortex\Hetzner\Validator\ChangeFloatingIpDnsPtrBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeFloatingIpDnsPtrBodyFixture
{
    public static function build(): ChangeFloatingIpDnsPtrBody
    {
        return ChangeFloatingIpDnsPtrBody::builder(
            // ip
            '2001:db8::1',
            // dnsPtr
            'server.example.com',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeFloatingIpDnsPtrBody */
    public static function reader(): callable
    {
        return ChangeFloatingIpDnsPtrBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeFloatingIpDnsPtrBodyConstraint::constraints();
    }
}
