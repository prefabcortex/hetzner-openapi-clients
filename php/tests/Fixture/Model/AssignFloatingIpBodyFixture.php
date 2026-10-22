<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\AssignFloatingIpBody;
use Prefabcortex\Hetzner\Validator\AssignFloatingIpBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class AssignFloatingIpBodyFixture
{
    public static function build(): AssignFloatingIpBody
    {
        return AssignFloatingIpBody::builder(42)->build();
    }

    /** @return callable(array<int|string, mixed>): AssignFloatingIpBody */
    public static function reader(): callable
    {
        return AssignFloatingIpBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return AssignFloatingIpBodyConstraint::constraints();
    }
}
