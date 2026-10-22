<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateZoneRrsetRecordsBodyRecordsItem;
use Prefabcortex\Hetzner\Validator\UpdateZoneRrsetRecordsBodyRecordsItemConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateZoneRrsetRecordsBodyRecordsItemFixture
{
    public static function build(): UpdateZoneRrsetRecordsBodyRecordsItem
    {
        return UpdateZoneRrsetRecordsBodyRecordsItem::builder(
            // value
            '198.51.100.1',
            // comment
            'My web server at Hetzner Cloud.',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateZoneRrsetRecordsBodyRecordsItem */
    public static function reader(): callable
    {
        return UpdateZoneRrsetRecordsBodyRecordsItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateZoneRrsetRecordsBodyRecordsItemConstraint::constraints();
    }
}
