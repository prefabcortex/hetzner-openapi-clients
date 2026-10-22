<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangePrimaryIpProtectionBody;
use Prefabcortex\Hetzner\Validator\ChangePrimaryIpProtectionBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangePrimaryIpProtectionBodyFixture
{
    public static function build(): ChangePrimaryIpProtectionBody
    {
        return ChangePrimaryIpProtectionBody::builder(false)->build();
    }

    /** @return callable(array<int|string, mixed>): ChangePrimaryIpProtectionBody */
    public static function reader(): callable
    {
        return ChangePrimaryIpProtectionBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangePrimaryIpProtectionBodyConstraint::constraints();
    }
}
