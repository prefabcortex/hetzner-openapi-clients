<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Record;
use Prefabcortex\Hetzner\Model\RRSetRecordsRequest;
use Prefabcortex\Hetzner\Validator\RRSetRecordsRequestConstraint;
use Symfony\Component\Validator\Constraint;

final class RRSetRecordsRequestFixture
{
    public static function build(): RRSetRecordsRequest
    {
        $record = Record::builder('198.51.100.1')
            ->setComment('My web server at Hetzner Cloud.')
            ->build();

        return RRSetRecordsRequest::builder([$record])->build();
    }

    /** @return callable(array<int|string, mixed>): RRSetRecordsRequest */
    public static function reader(): callable
    {
        return RRSetRecordsRequest::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return RRSetRecordsRequestConstraint::constraints();
    }
}
