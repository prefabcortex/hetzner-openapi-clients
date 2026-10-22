<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Firewall;
use Prefabcortex\Hetzner\Model\FirewallAppliedToItem;
use Prefabcortex\Hetzner\Model\FirewallResourceType;
use Prefabcortex\Hetzner\Model\FirewallResponse;
use Prefabcortex\Hetzner\Model\FirewallRuleDirection;
use Prefabcortex\Hetzner\Model\FirewallRuleProtocol;
use Prefabcortex\Hetzner\Model\FirewallRulesItem;
use Prefabcortex\Hetzner\Validator\FirewallResponseConstraint;
use Symfony\Component\Validator\Constraint;

final class FirewallResponseFixture
{
    public static function build(): FirewallResponse
    {
        $firewallRulesItem = FirewallRulesItem::builder(
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
        $firewallAppliedToItem = FirewallAppliedToItem::builder(FirewallResourceType::server)->build();
        $firewall = Firewall::builder(
            // id
            42,
            // name
            'new-name',
            // created
            new DateTime('2024-01-01'),
            // rules
            [$firewallRulesItem],
            // appliedTo
            [$firewallAppliedToItem],
        )->build();

        return FirewallResponse::builder($firewall)->build();
    }

    /** @return callable(array<int|string, mixed>): FirewallResponse */
    public static function reader(): callable
    {
        return FirewallResponse::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return FirewallResponseConstraint::constraints();
    }
}
