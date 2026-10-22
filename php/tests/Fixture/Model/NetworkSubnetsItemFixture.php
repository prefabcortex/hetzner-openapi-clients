<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\NetworkSubnetsItem;
use Prefabcortex\Hetzner\Model\SubnetType;
use Prefabcortex\Hetzner\Validator\NetworkSubnetsItemConstraint;
use Symfony\Component\Validator\Constraint;

final class NetworkSubnetsItemFixture
{
    public static function build(): NetworkSubnetsItem
    {
        return NetworkSubnetsItem::builder(
            // type
            SubnetType::cloud,
            // networkZone
            'eu-central',
            // gateway
            '10.0.0.1',
        )
            ->setIpRange('10.0.1.0/24')
            ->setVswitchId(1000)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): NetworkSubnetsItem */
    public static function reader(): callable
    {
        return NetworkSubnetsItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return NetworkSubnetsItemConstraint::constraints();
    }
}
