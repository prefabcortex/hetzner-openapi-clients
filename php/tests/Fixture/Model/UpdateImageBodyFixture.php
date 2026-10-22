<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateImageBody;
use Prefabcortex\Hetzner\Validator\UpdateImageBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateImageBodyFixture
{
    public static function build(): UpdateImageBody
    {
        return UpdateImageBody::builder()
            ->setDescription('My new Image description')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateImageBody */
    public static function reader(): callable
    {
        return UpdateImageBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateImageBodyConstraint::constraints();
    }
}
