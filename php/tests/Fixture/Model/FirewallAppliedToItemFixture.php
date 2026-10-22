<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\FirewallAppliedToItem;
use Prefabcortex\Hetzner\Model\FirewallResourceType;
use Prefabcortex\Hetzner\Validator\FirewallAppliedToItemConstraint;
use Symfony\Component\Validator\Constraint;

final class FirewallAppliedToItemFixture
{
    public static function build(): FirewallAppliedToItem
    {
        return FirewallAppliedToItem::builder(FirewallResourceType::server)->build();
    }

    /** @return callable(array<int|string, mixed>): FirewallAppliedToItem */
    public static function reader(): callable
    {
        return FirewallAppliedToItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return FirewallAppliedToItemConstraint::constraints();
    }
}
