<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateNetworkBodySubnetsItem;
use Prefabcortex\Hetzner\Model\SubnetType;
use Prefabcortex\Hetzner\Validator\CreateNetworkBodySubnetsItemConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateNetworkBodySubnetsItemFixture
{
    public static function build(): CreateNetworkBodySubnetsItem
    {
        return CreateNetworkBodySubnetsItem::builder(
            // type
            SubnetType::cloud,
            // networkZone
            'eu-central',
        )
            ->setIpRange('10.0.1.0/24')
            ->setVswitchId(1000)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateNetworkBodySubnetsItem */
    public static function reader(): callable
    {
        return CreateNetworkBodySubnetsItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateNetworkBodySubnetsItemConstraint::constraints();
    }
}
