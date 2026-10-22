<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateZoneRrsetRecordsBody;
use Prefabcortex\Hetzner\Model\UpdateZoneRrsetRecordsBodyRecordsItem;
use Prefabcortex\Hetzner\Validator\UpdateZoneRrsetRecordsBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateZoneRrsetRecordsBodyFixture
{
    public static function build(): UpdateZoneRrsetRecordsBody
    {
        $updateZoneRrsetRecordsBodyRecordsItem = UpdateZoneRrsetRecordsBodyRecordsItem::builder(
            // value
            '198.51.100.1',
            // comment
            'My web server at Hetzner Cloud.',
        )->build();

        return UpdateZoneRrsetRecordsBody::builder([$updateZoneRrsetRecordsBodyRecordsItem])->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateZoneRrsetRecordsBody */
    public static function reader(): callable
    {
        return UpdateZoneRrsetRecordsBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateZoneRrsetRecordsBodyConstraint::constraints();
    }
}
