<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ZonePrimaryNameserver;
use Prefabcortex\Hetzner\Validator\ZonePrimaryNameserverConstraint;
use Symfony\Component\Validator\Constraint;

final class ZonePrimaryNameserverFixture
{
    public static function build(): ZonePrimaryNameserver
    {
        return ZonePrimaryNameserver::builder('198.51.100.1')
            ->setPort(5353)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): ZonePrimaryNameserver */
    public static function reader(): callable
    {
        return ZonePrimaryNameserver::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ZonePrimaryNameserverConstraint::constraints();
    }
}
