<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeServerAliasIpsBody;
use Prefabcortex\Hetzner\Validator\ChangeServerAliasIpsBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeServerAliasIpsBodyFixture
{
    public static function build(): ChangeServerAliasIpsBody
    {
        return ChangeServerAliasIpsBody::builder(
            // network
            4711,
            // aliasIps
            ['10.0.1.2'],
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeServerAliasIpsBody */
    public static function reader(): callable
    {
        return ChangeServerAliasIpsBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeServerAliasIpsBodyConstraint::constraints();
    }
}
