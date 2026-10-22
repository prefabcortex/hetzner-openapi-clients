<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreatePrimaryIpBody;
use Prefabcortex\Hetzner\Model\IpType;
use Prefabcortex\Hetzner\Validator\CreatePrimaryIpBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreatePrimaryIpBodyFixture
{
    public static function build(): CreatePrimaryIpBody
    {
        return CreatePrimaryIpBody::builder(
            // name
            'my-resource',
            // type
            IpType::ipv4,
        )
            ->setAssigneeId(17)
            ->setAutoDelete(false)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreatePrimaryIpBody */
    public static function reader(): callable
    {
        return CreatePrimaryIpBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreatePrimaryIpBodyConstraint::constraints();
    }
}
