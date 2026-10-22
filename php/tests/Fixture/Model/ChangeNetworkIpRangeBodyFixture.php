<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeNetworkIpRangeBody;
use Prefabcortex\Hetzner\Validator\ChangeNetworkIpRangeBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeNetworkIpRangeBodyFixture
{
    public static function build(): ChangeNetworkIpRangeBody
    {
        return ChangeNetworkIpRangeBody::builder('10.0.0.0/16')->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeNetworkIpRangeBody */
    public static function reader(): callable
    {
        return ChangeNetworkIpRangeBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeNetworkIpRangeBodyConstraint::constraints();
    }
}
