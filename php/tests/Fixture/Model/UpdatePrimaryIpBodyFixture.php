<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdatePrimaryIpBody;
use Prefabcortex\Hetzner\Validator\UpdatePrimaryIpBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdatePrimaryIpBodyFixture
{
    public static function build(): UpdatePrimaryIpBody
    {
        return UpdatePrimaryIpBody::builder()
            ->setName('my-resource')
            ->setAutoDelete(true)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdatePrimaryIpBody */
    public static function reader(): callable
    {
        return UpdatePrimaryIpBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdatePrimaryIpBodyConstraint::constraints();
    }
}
