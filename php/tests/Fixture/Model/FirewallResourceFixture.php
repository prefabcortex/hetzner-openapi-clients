<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\FirewallResource;
use Prefabcortex\Hetzner\Model\FirewallResourceType;
use Prefabcortex\Hetzner\Validator\FirewallResourceConstraint;
use Symfony\Component\Validator\Constraint;

final class FirewallResourceFixture
{
    public static function build(): FirewallResource
    {
        return FirewallResource::builder(FirewallResourceType::server)->build();
    }

    /** @return callable(array<int|string, mixed>): FirewallResource */
    public static function reader(): callable
    {
        return FirewallResource::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return FirewallResourceConstraint::constraints();
    }
}
