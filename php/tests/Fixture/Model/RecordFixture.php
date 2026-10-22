<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Record;
use Prefabcortex\Hetzner\Validator\RecordConstraint;
use Symfony\Component\Validator\Constraint;

final class RecordFixture
{
    public static function build(): Record
    {
        return Record::builder('198.51.100.1')
            ->setComment('My web server at Hetzner Cloud.')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): Record */
    public static function reader(): callable
    {
        return Record::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return RecordConstraint::constraints();
    }
}
