<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Action;
use Prefabcortex\Hetzner\Model\ActionError;
use Prefabcortex\Hetzner\Model\ActionResource;
use Prefabcortex\Hetzner\Model\ActionStatus;
use Prefabcortex\Hetzner\Model\CreateZoneResponse201;
use Prefabcortex\Hetzner\Model\PrimaryZonePropertiesMode;
use Prefabcortex\Hetzner\Model\Protection;
use Prefabcortex\Hetzner\Model\ZoneBaseAuthoritativeNameservers;
use Prefabcortex\Hetzner\Model\ZoneBaseRegistrar;
use Prefabcortex\Hetzner\Model\ZoneBaseStatus;
use Prefabcortex\Hetzner\Model\ZonePrimary;
use Prefabcortex\Hetzner\Model\ZonePrimaryNameserver;
use Prefabcortex\Hetzner\Validator\CreateZoneResponse201Constraint;
use Symfony\Component\Validator\Constraint;

final class CreateZoneResponse201Fixture
{
    public static function build(): CreateZoneResponse201
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
        $zone = ZonePrimary::builder(
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
        $actionResource = ActionResource::builder(
            // id
            42,
            // type
            'server',
        )->build();
        $error = ActionError::builder(
            // code
            'action_failed',
            // message
            'Action failed',
        )->build();
        $action = Action::builder(
            // id
            42,
            // command
            'start_resource',
            // status
            ActionStatus::running,
            // started
            new DateTime('2024-01-01'),
            // finished
            new DateTime('2024-01-01'),
            // progress
            100,
            // resources
            [$actionResource],
            // error
            $error,
        )->build();

        return CreateZoneResponse201::builder(
            // zone
            $zone,
            // action
            $action,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): CreateZoneResponse201 */
    public static function reader(): callable
    {
        return CreateZoneResponse201::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateZoneResponse201Constraint::constraints();
    }
}
