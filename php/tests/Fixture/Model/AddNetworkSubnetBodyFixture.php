<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\AddNetworkSubnetBody;
use Prefabcortex\Hetzner\Model\SubnetType;
use Prefabcortex\Hetzner\Validator\AddNetworkSubnetBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class AddNetworkSubnetBodyFixture
{
    public static function build(): AddNetworkSubnetBody
    {
        return AddNetworkSubnetBody::builder(
            // type
            SubnetType::cloud,
            // networkZone
            'eu-central',
        )
            ->setIpRange('10.0.1.0/24')
            ->setVswitchId(1000)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): AddNetworkSubnetBody */
    public static function reader(): callable
    {
        return AddNetworkSubnetBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return AddNetworkSubnetBodyConstraint::constraints();
    }
}
