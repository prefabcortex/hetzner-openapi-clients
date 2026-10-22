<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateServerBodyFirewallsItem;
use Prefabcortex\Hetzner\Validator\CreateServerBodyFirewallsItemConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateServerBodyFirewallsItemFixture
{
    public static function build(): CreateServerBodyFirewallsItem
    {
        return CreateServerBodyFirewallsItem::builder(0)->build();
    }

    /** @return callable(array<int|string, mixed>): CreateServerBodyFirewallsItem */
    public static function reader(): callable
    {
        return CreateServerBodyFirewallsItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateServerBodyFirewallsItemConstraint::constraints();
    }
}
