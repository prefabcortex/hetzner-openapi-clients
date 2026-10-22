<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeServerProtectionBody;
use Prefabcortex\Hetzner\Validator\ChangeServerProtectionBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeServerProtectionBodyFixture
{
    public static function build(): ChangeServerProtectionBody
    {
        return ChangeServerProtectionBody::builder()
            ->setDelete(true)
            ->setRebuild(true)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeServerProtectionBody */
    public static function reader(): callable
    {
        return ChangeServerProtectionBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeServerProtectionBodyConstraint::constraints();
    }
}
