<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\DetachServerFromNetworkBody;
use Prefabcortex\Hetzner\Validator\DetachServerFromNetworkBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class DetachServerFromNetworkBodyFixture
{
    public static function build(): DetachServerFromNetworkBody
    {
        return DetachServerFromNetworkBody::builder(4711)->build();
    }

    /** @return callable(array<int|string, mixed>): DetachServerFromNetworkBody */
    public static function reader(): callable
    {
        return DetachServerFromNetworkBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return DetachServerFromNetworkBodyConstraint::constraints();
    }
}
