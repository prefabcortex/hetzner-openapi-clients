<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Zonefile;
use Prefabcortex\Hetzner\Validator\ZonefileConstraint;
use Symfony\Component\Validator\Constraint;

final class ZonefileFixture
{
    public static function build(): Zonefile
    {
        return Zonefile::builder('$ORIGIN	example.com.
$TTL	3600

@	IN	SOA	hydrogen.ns.hetzner.com. dns.hetzner.com. 2024010100 86400 10800 3600000 3600

@	IN	10800	NS	hydrogen.ns.hetzner.com. ; Some comment.
@	IN	10800	NS	oxygen.ns.hetzner.com.
@	IN	10800	NS	helium.ns.hetzner.de.
')->build();
    }

    /** @return callable(array<int|string, mixed>): Zonefile */
    public static function reader(): callable
    {
        return Zonefile::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ZonefileConstraint::constraints();
    }
}
