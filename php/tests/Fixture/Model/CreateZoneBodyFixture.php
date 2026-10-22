<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateZoneBody;
use Prefabcortex\Hetzner\Model\ZoneMode;
use Prefabcortex\Hetzner\Model\ZonePrimaryNameserver;
use Prefabcortex\Hetzner\Validator\CreateZoneBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateZoneBodyFixture
{
    public static function build(): CreateZoneBody
    {
        $zonePrimaryNameserver = ZonePrimaryNameserver::builder('198.51.100.1')
            ->setPort(53)
            ->build();
        $zonePrimaryNameserver_1 = ZonePrimaryNameserver::builder('203.0.113.1')
            ->setPort(53)
            ->build();

        return CreateZoneBody::builder(
            // name
            'example.com',
            // mode
            ZoneMode::primary,
        )
            ->setTtl(10800)
            ->setPrimaryNameservers([$zonePrimaryNameserver, $zonePrimaryNameserver_1])
            ->setZonefile('$ORIGIN	example.com.
$TTL	3600

@	IN	SOA	hydrogen.ns.hetzner.com. dns.hetzner.com. 2024010100 86400 10800 3600000 3600

@	IN	10800	NS	hydrogen.ns.hetzner.com. ; Some comment.
@	IN	10800	NS	oxygen.ns.hetzner.com.
@	IN	10800	NS	helium.ns.hetzner.de.
')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateZoneBody */
    public static function reader(): callable
    {
        return CreateZoneBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateZoneBodyConstraint::constraints();
    }
}
