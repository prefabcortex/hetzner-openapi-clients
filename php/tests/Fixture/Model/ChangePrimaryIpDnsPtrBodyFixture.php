<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangePrimaryIpDnsPtrBody;
use Prefabcortex\Hetzner\Validator\ChangePrimaryIpDnsPtrBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangePrimaryIpDnsPtrBodyFixture
{
    public static function build(): ChangePrimaryIpDnsPtrBody
    {
        return ChangePrimaryIpDnsPtrBody::builder(
            // ip
            '2001:db8::1',
            // dnsPtr
            'server.example.com',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ChangePrimaryIpDnsPtrBody */
    public static function reader(): callable
    {
        return ChangePrimaryIpDnsPtrBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangePrimaryIpDnsPtrBodyConstraint::constraints();
    }
}
