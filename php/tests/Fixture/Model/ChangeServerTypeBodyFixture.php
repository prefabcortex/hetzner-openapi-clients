<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeServerTypeBody;
use Prefabcortex\Hetzner\Validator\ChangeServerTypeBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeServerTypeBodyFixture
{
    public static function build(): ChangeServerTypeBody
    {
        return ChangeServerTypeBody::builder(
            // upgradeDisk
            true,
            // serverType
            'cpx22',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeServerTypeBody */
    public static function reader(): callable
    {
        return ChangeServerTypeBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeServerTypeBodyConstraint::constraints();
    }
}
