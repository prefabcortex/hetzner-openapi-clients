<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\FirewallRuleDirection;
use Prefabcortex\Hetzner\Model\FirewallRuleProtocol;
use Prefabcortex\Hetzner\Model\FirewallRulesItem;
use Prefabcortex\Hetzner\Validator\FirewallRulesItemConstraint;
use Symfony\Component\Validator\Constraint;

final class FirewallRulesItemFixture
{
    public static function build(): FirewallRulesItem
    {
        return FirewallRulesItem::builder(
            // direction
            FirewallRuleDirection::in,
            // sourceIps
            ['192.0.2.2/32', '192.0.2.0/24', '2001:0db8:9a3b:ee58:5ca:990c:8bc9:c03b/128'],
            // destinationIps
            ['REPLACE_ME'],
            // protocol
            FirewallRuleProtocol::tcp,
            // port
            '80',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): FirewallRulesItem */
    public static function reader(): callable
    {
        return FirewallRulesItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return FirewallRulesItemConstraint::constraints();
    }
}
