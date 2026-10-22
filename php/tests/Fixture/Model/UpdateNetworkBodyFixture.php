<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateNetworkBody;
use Prefabcortex\Hetzner\Validator\UpdateNetworkBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateNetworkBodyFixture
{
    public static function build(): UpdateNetworkBody
    {
        return UpdateNetworkBody::builder()
            ->setName('new-name')
            ->setExposeRoutesToVswitch(false)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateNetworkBody */
    public static function reader(): callable
    {
        return UpdateNetworkBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateNetworkBodyConstraint::constraints();
    }
}
