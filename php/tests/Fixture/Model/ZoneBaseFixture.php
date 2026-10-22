<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Model\ZoneBase;
use Prefabcortex\Hetzner\Model\ZoneBaseAuthoritativeNameservers;
use Prefabcortex\Hetzner\Model\ZoneBaseRegistrar;
use Prefabcortex\Hetzner\Model\ZoneBaseStatus;
use Prefabcortex\Hetzner\Model\ZonePrimaryNameserver;
use Prefabcortex\Hetzner\Validator\ZoneBaseConstraint;
use Symfony\Component\Validator\Constraint;

final class ZoneBaseFixture
{
    public static function build(): ZoneBase
    {
        $protection = Protection::builder(false)->build();
        $authoritativeNameservers = ZoneBaseAuthoritativeNameservers::builder(
            // assigned
            ['hydrogen.ns.hetzner.com.', 'oxygen.ns.hetzner.com.', 'helium.ns.hetzner.de.'],
            // delegated
            ['hydrogen.ns.hetzner.com.', 'oxygen.ns.hetzner.com.', 'helium.ns.hetzner.de.'],
            // delegationLastCheck
            new DateTime('2024-01-01'),
        )->build();
        $zonePrimaryNameserver = ZonePrimaryNameserver::builder('198.51.100.1')
            ->setPort(53)
            ->build();
        $zonePrimaryNameserver_1 = ZonePrimaryNameserver::builder('203.0.113.1')
            ->setPort(53)
            ->build();

        return ZoneBase::builder(
            // id
            42,
            // name
            'example.com',
            // created
            new DateTime('2024-01-01'),
            // labels
            [],
            // protection
            $protection,
            // ttl
            10800,
            // status
            ZoneBaseStatus::ok,
            // recordCount
            0,
            // authoritativeNameservers
            $authoritativeNameservers,
            // registrar
            ZoneBaseRegistrar::hetzner,
        )
            ->setPrimaryNameservers([$zonePrimaryNameserver, $zonePrimaryNameserver_1])
            ->build();
    }

    /** @return callable(array<int|string, mixed>): ZoneBase */
    public static function reader(): callable
    {
        return ZoneBase::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ZoneBaseConstraint::constraints();
    }
}
