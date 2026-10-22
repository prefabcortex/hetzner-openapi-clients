<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateServerBody;
use Prefabcortex\Hetzner\Validator\UpdateServerBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateServerBodyFixture
{
    public static function build(): UpdateServerBody
    {
        return UpdateServerBody::builder()
            ->setName('my-server')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateServerBody */
    public static function reader(): callable
    {
        return UpdateServerBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateServerBodyConstraint::constraints();
    }
}
