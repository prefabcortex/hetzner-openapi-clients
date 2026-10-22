<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\DeleteNetworkSubnetBody;
use Prefabcortex\Hetzner\Validator\DeleteNetworkSubnetBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class DeleteNetworkSubnetBodyFixture
{
    public static function build(): DeleteNetworkSubnetBody
    {
        return DeleteNetworkSubnetBody::builder('10.0.1.0/24')->build();
    }

    /** @return callable(array<int|string, mixed>): DeleteNetworkSubnetBody */
    public static function reader(): callable
    {
        return DeleteNetworkSubnetBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return DeleteNetworkSubnetBodyConstraint::constraints();
    }
}
