<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ServerPublicNetFirewallsItem;
use Prefabcortex\Hetzner\Model\ServerPublicNetFirewallsItemStatus;
use Prefabcortex\Hetzner\Validator\ServerPublicNetFirewallsItemConstraint;
use Symfony\Component\Validator\Constraint;

final class ServerPublicNetFirewallsItemFixture
{
    public static function build(): ServerPublicNetFirewallsItem
    {
        return ServerPublicNetFirewallsItem::builder()
            ->setId(42)
            ->setStatus(ServerPublicNetFirewallsItemStatus::applied)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): ServerPublicNetFirewallsItem */
    public static function reader(): callable
    {
        return ServerPublicNetFirewallsItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ServerPublicNetFirewallsItemConstraint::constraints();
    }
}
