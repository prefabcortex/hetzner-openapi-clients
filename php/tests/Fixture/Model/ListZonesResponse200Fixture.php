<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Model\ListZonesResponse200;
use Prefabcortex\Hetzner\Model\PrimaryZonePropertiesMode;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Model\ZoneBaseAuthoritativeNameservers;
use Prefabcortex\Hetzner\Model\ZoneBaseRegistrar;
use Prefabcortex\Hetzner\Model\ZoneBaseStatus;
use Prefabcortex\Hetzner\Model\ZonePrimary;
use Prefabcortex\Hetzner\Model\ZonePrimaryNameserver;
use Prefabcortex\Hetzner\Validator\ListZonesResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListZonesResponse200Fixture
{
    public static function build(): ListZonesResponse200
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
        $zones = ZonePrimary::builder(
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
            // mode
            PrimaryZonePropertiesMode::primary,
        )
            ->setPrimaryNameservers([$zonePrimaryNameserver, $zonePrimaryNameserver_1])
            ->build();
        $pagination = ListMetaPagination::builder(
            // page
            3,
            // perPage
            25,
            // previousPage
            2,
            // nextPage
            4,
            // lastPage
            4,
            // totalEntries
            100,
        )->build();
        $meta = ListMeta::builder($pagination)->build();

        return ListZonesResponse200::builder(
            // zones
            [$zones],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListZonesResponse200 */
    public static function reader(): callable
    {
        return ListZonesResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListZonesResponse200Constraint::constraints();
    }
}
