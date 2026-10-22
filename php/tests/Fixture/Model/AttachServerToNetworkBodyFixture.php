<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\AttachServerToNetworkBody;
use Prefabcortex\Hetzner\Validator\AttachServerToNetworkBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class AttachServerToNetworkBodyFixture
{
    public static function build(): AttachServerToNetworkBody
    {
        return AttachServerToNetworkBody::builder(4711)
            ->setIp('10.0.1.1')
            ->setAliasIps(['10.0.1.2'])
            ->setIpRange('10.0.1.0/24')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): AttachServerToNetworkBody */
    public static function reader(): callable
    {
        return AttachServerToNetworkBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return AttachServerToNetworkBodyConstraint::constraints();
    }
}
