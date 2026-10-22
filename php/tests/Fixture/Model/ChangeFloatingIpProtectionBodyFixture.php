<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeFloatingIpProtectionBody;
use Prefabcortex\Hetzner\Validator\ChangeFloatingIpProtectionBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeFloatingIpProtectionBodyFixture
{
    public static function build(): ChangeFloatingIpProtectionBody
    {
        return ChangeFloatingIpProtectionBody::builder(false)->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeFloatingIpProtectionBody */
    public static function reader(): callable
    {
        return ChangeFloatingIpProtectionBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeFloatingIpProtectionBodyConstraint::constraints();
    }
}
