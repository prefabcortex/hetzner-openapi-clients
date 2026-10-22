<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeServerDnsPtrBody;
use Prefabcortex\Hetzner\Validator\ChangeServerDnsPtrBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeServerDnsPtrBodyFixture
{
    public static function build(): ChangeServerDnsPtrBody
    {
        return ChangeServerDnsPtrBody::builder(
            // ip
            '2001:db8::1',
            // dnsPtr
            'server.example.com',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeServerDnsPtrBody */
    public static function reader(): callable
    {
        return ChangeServerDnsPtrBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeServerDnsPtrBodyConstraint::constraints();
    }
}
