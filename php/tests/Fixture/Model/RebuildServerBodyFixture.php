<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\RebuildServerBody;
use Prefabcortex\Hetzner\Validator\RebuildServerBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class RebuildServerBodyFixture
{
    public static function build(): RebuildServerBody
    {
        return RebuildServerBody::builder('ubuntu-24.04')
            ->setUserData('#cloud-config
runcmd:
- [touch, /root/cloud-init-worked]
')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): RebuildServerBody */
    public static function reader(): callable
    {
        return RebuildServerBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return RebuildServerBodyConstraint::constraints();
    }
}
