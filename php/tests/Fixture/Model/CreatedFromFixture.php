<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreatedFrom;
use Prefabcortex\Hetzner\Validator\CreatedFromConstraint;
use Symfony\Component\Validator\Constraint;

final class CreatedFromFixture
{
    public static function build(): CreatedFrom
    {
        return CreatedFrom::builder(
            // id
            1,
            // name
            'Server',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): CreatedFrom */
    public static function reader(): callable
    {
        return CreatedFrom::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreatedFromConstraint::constraints();
    }
}
