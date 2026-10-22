<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Network;
use Prefabcortex\Hetzner\Model\NetworkSubnetsItem;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Model\Route;
use Prefabcortex\Hetzner\Model\SubnetType;
use Prefabcortex\Hetzner\Validator\NetworkConstraint;
use Symfony\Component\Validator\Constraint;

final class NetworkFixture
{
    public static function build(): Network
    {
        $networkSubnetsItem = NetworkSubnetsItem::builder(
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
        $route = Route::builder(
            // destination
            '10.100.1.0/24',
            // gateway
            '10.0.1.1',
        )->build();
        $protection = Protection::builder(false)->build();

        return Network::builder(
            // id
            4711,
            // name
            'mynet',
            // ipRange
            '10.0.0.0/16',
            // subnets
            [$networkSubnetsItem],
            // routes
            [$route],
            // servers
            [42],
            // protection
            $protection,
            // labels
            [],
            // created
            new DateTime('2024-01-01'),
            // exposeRoutesToVswitch
            false,
        )
            ->setLoadBalancers([42])
            ->build();
    }

    /** @return callable(array<int|string, mixed>): Network */
    public static function reader(): callable
    {
        return Network::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return NetworkConstraint::constraints();
    }
}
