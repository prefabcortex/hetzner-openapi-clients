<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeStorageBoxTypeBody;
use Prefabcortex\Hetzner\Validator\ChangeStorageBoxTypeBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeStorageBoxTypeBodyFixture
{
    public static function build(): ChangeStorageBoxTypeBody
    {
        return ChangeStorageBoxTypeBody::builder('bx20')->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeStorageBoxTypeBody */
    public static function reader(): callable
    {
        return ChangeStorageBoxTypeBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeStorageBoxTypeBodyConstraint::constraints();
    }
}
