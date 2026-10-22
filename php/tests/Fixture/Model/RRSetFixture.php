<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Record;
use Prefabcortex\Hetzner\Model\RRSet;
use Prefabcortex\Hetzner\Model\RRSetProtection;
use Prefabcortex\Hetzner\Model\RRSetType;
use Prefabcortex\Hetzner\Validator\RRSetConstraint;
use Symfony\Component\Validator\Constraint;

final class RRSetFixture
{
    public static function build(): RRSet
    {
        $protection = RRSetProtection::builder(false)->build();
        $record = Record::builder('198.51.100.1')
            ->setComment('My web server at Hetzner Cloud.')
            ->build();

        return RRSet::builder(
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
    }

    /** @return callable(array<int|string, mixed>): RRSet */
    public static function reader(): callable
    {
        return RRSet::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return RRSetConstraint::constraints();
    }
}
