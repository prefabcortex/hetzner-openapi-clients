<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeZonePrimaryNameserversBody;
use Prefabcortex\Hetzner\Model\ZonePrimaryNameserver;
use Prefabcortex\Hetzner\Validator\ChangeZonePrimaryNameserversBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeZonePrimaryNameserversBodyFixture
{
    public static function build(): ChangeZonePrimaryNameserversBody
    {
        $zonePrimaryNameserver = ZonePrimaryNameserver::builder('198.51.100.1')
            ->setPort(53)
            ->build();
        $zonePrimaryNameserver_1 = ZonePrimaryNameserver::builder('203.0.113.1')
            ->setPort(53)
            ->build();

        return ChangeZonePrimaryNameserversBody::builder([$zonePrimaryNameserver, $zonePrimaryNameserver_1])->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeZonePrimaryNameserversBody */
    public static function reader(): callable
    {
        return ChangeZonePrimaryNameserversBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeZonePrimaryNameserversBodyConstraint::constraints();
    }
}
