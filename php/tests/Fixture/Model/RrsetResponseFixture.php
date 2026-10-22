<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Record;
use Prefabcortex\Hetzner\Model\RRSet;
use Prefabcortex\Hetzner\Model\RRSetProtection;
use Prefabcortex\Hetzner\Model\RrsetResponse;
use Prefabcortex\Hetzner\Model\RRSetType;
use Prefabcortex\Hetzner\Validator\RrsetResponseConstraint;
use Symfony\Component\Validator\Constraint;

final class RrsetResponseFixture
{
    public static function build(): RrsetResponse
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

        return RrsetResponse::builder($rrset)->build();
    }

    /** @return callable(array<int|string, mixed>): RrsetResponse */
    public static function reader(): callable
    {
        return RrsetResponse::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return RrsetResponseConstraint::constraints();
    }
}
