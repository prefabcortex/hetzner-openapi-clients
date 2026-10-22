<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\DnsPtr;
use Prefabcortex\Hetzner\Validator\DnsPtrConstraint;
use Symfony\Component\Validator\Constraint;

final class DnsPtrFixture
{
    public static function build(): DnsPtr
    {
        return DnsPtr::builder(
            // ip
            '2001:db8::1',
            // dnsPtr
            'server.example.com',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): DnsPtr */
    public static function reader(): callable
    {
        return DnsPtr::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return DnsPtrConstraint::constraints();
    }
}
