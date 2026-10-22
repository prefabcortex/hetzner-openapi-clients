<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\AddZoneRrsetRecordsBody;
use Prefabcortex\Hetzner\Model\Record;
use Prefabcortex\Hetzner\Validator\AddZoneRrsetRecordsBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class AddZoneRrsetRecordsBodyFixture
{
    public static function build(): AddZoneRrsetRecordsBody
    {
        $record = Record::builder('198.51.100.1')
            ->setComment('My web server at Hetzner Cloud.')
            ->build();

        return AddZoneRrsetRecordsBody::builder([$record])
            ->setTtl(3600)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): AddZoneRrsetRecordsBody */
    public static function reader(): callable
    {
        return AddZoneRrsetRecordsBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return AddZoneRrsetRecordsBodyConstraint::constraints();
    }
}
