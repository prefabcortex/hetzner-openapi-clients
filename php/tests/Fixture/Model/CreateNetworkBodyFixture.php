<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateNetworkBody;
use Prefabcortex\Hetzner\Validator\CreateNetworkBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateNetworkBodyFixture
{
    public static function build(): CreateNetworkBody
    {
        return CreateNetworkBody::builder(
            // name
            'mynet',
            // ipRange
            '10.0.0.0/16',
        )
            ->setExposeRoutesToVswitch(false)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateNetworkBody */
    public static function reader(): callable
    {
        return CreateNetworkBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateNetworkBodyConstraint::constraints();
    }
}
