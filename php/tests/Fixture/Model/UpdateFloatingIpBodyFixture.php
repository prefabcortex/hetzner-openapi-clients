<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateFloatingIpBody;
use Prefabcortex\Hetzner\Validator\UpdateFloatingIpBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateFloatingIpBodyFixture
{
    public static function build(): UpdateFloatingIpBody
    {
        return UpdateFloatingIpBody::builder()
            ->setDescription('This describes my resource')
            ->setName('my-resource')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateFloatingIpBody */
    public static function reader(): callable
    {
        return UpdateFloatingIpBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateFloatingIpBodyConstraint::constraints();
    }
}
