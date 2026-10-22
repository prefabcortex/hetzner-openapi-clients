<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Record;
use Prefabcortex\Hetzner\Model\RRSetRequest;
use Prefabcortex\Hetzner\Model\RRSetType;
use Prefabcortex\Hetzner\Validator\RRSetRequestConstraint;
use Symfony\Component\Validator\Constraint;

final class RRSetRequestFixture
{
    public static function build(): RRSetRequest
    {
        $record = Record::builder('198.51.100.1')
            ->setComment('My web server at Hetzner Cloud.')
            ->build();

        return RRSetRequest::builder(
            // name
            'www',
            // type
            RRSetType::A,
            // records
            [$record],
        )
            ->setTtl(3600)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): RRSetRequest */
    public static function reader(): callable
    {
        return RRSetRequest::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return RRSetRequestConstraint::constraints();
    }
}
