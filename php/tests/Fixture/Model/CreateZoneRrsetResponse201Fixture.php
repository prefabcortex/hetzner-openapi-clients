<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Action;
use Prefabcortex\Hetzner\Model\ActionError;
use Prefabcortex\Hetzner\Model\ActionResource;
use Prefabcortex\Hetzner\Model\ActionStatus;
use Prefabcortex\Hetzner\Model\CreateZoneRrsetResponse201;
use Prefabcortex\Hetzner\Model\Record;
use Prefabcortex\Hetzner\Model\RRSet;
use Prefabcortex\Hetzner\Model\RRSetProtection;
use Prefabcortex\Hetzner\Model\RRSetType;
use Prefabcortex\Hetzner\Validator\CreateZoneRrsetResponse201Constraint;
use Symfony\Component\Validator\Constraint;

final class CreateZoneRrsetResponse201Fixture
{
    public static function build(): CreateZoneRrsetResponse201
    {
        $protection = RRSetProtection::builder(false)->build();
        $record = Record::builder('198.51.100.1')
            ->setComment('My web server at Hetzner Cloud.')
            ->build();
        $rrset = RRSet::builder(
            // id
            'REPLACE_ME',
            // name
            'www',
            // type
            RRSetType::A,
            // ttl
            3600,
            // labels
            [],
            // protection
            $protection,
            // records
            [$record],
            // zone
            42,
        )->build();
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

        return CreateZoneRrsetResponse201::builder(
            // rrset
            $rrset,
            // action
            $action,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): CreateZoneRrsetResponse201 */
    public static function reader(): callable
    {
        return CreateZoneRrsetResponse201::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateZoneRrsetResponse201Constraint::constraints();
    }
}
