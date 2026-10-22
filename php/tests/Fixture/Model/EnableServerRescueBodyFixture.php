<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\EnableServerRescueBody;
use Prefabcortex\Hetzner\Model\EnableServerRescueBodyType;
use Prefabcortex\Hetzner\Validator\EnableServerRescueBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class EnableServerRescueBodyFixture
{
    public static function build(): EnableServerRescueBody
    {
        return EnableServerRescueBody::builder()
            ->setType(EnableServerRescueBodyType::linux64)
            ->setSshKeys([2323])
            ->build();
    }

    /** @return callable(array<int|string, mixed>): EnableServerRescueBody */
    public static function reader(): callable
    {
        return EnableServerRescueBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return EnableServerRescueBodyConstraint::constraints();
    }
}
