<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\AssignPrimaryIpBody;
use Prefabcortex\Hetzner\Model\AssignPrimaryIpBodyAssigneeType;
use Prefabcortex\Hetzner\Validator\AssignPrimaryIpBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class AssignPrimaryIpBodyFixture
{
    public static function build(): AssignPrimaryIpBody
    {
        return AssignPrimaryIpBody::builder(
            // assigneeType
            AssignPrimaryIpBodyAssigneeType::server,
            // assigneeId
            4711,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): AssignPrimaryIpBody */
    public static function reader(): callable
    {
        return AssignPrimaryIpBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return AssignPrimaryIpBodyConstraint::constraints();
    }
}
