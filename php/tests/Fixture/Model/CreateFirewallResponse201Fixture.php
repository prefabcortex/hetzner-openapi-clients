<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Action;
use Prefabcortex\Hetzner\Model\ActionError;
use Prefabcortex\Hetzner\Model\ActionResource;
use Prefabcortex\Hetzner\Model\ActionStatus;
use Prefabcortex\Hetzner\Model\CreateFirewallResponse201;
use Prefabcortex\Hetzner\Model\Firewall;
use Prefabcortex\Hetzner\Model\FirewallAppliedToItem;
use Prefabcortex\Hetzner\Model\FirewallResourceType;
use Prefabcortex\Hetzner\Model\FirewallRuleDirection;
use Prefabcortex\Hetzner\Model\FirewallRuleProtocol;
use Prefabcortex\Hetzner\Model\FirewallRulesItem;
use Prefabcortex\Hetzner\Validator\CreateFirewallResponse201Constraint;
use Symfony\Component\Validator\Constraint;

final class CreateFirewallResponse201Fixture
{
    public static function build(): CreateFirewallResponse201
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
        $actionResource = ActionResource::builder(
            // id
            38,
            // type
            'firewall',
        )->build();
        $error = ActionError::builder(
            // code
            'action_failed',
            // message
            'Action failed',
        )->build();
        $action = Action::builder(
            // id
            13,
            // command
            'set_firewall_rules',
            // status
            ActionStatus::success,
            // started
            new DateTime('2016-01-30T23:55:00Z'),
            // finished
            new DateTime('2024-01-01'),
            // progress
            100,
            // resources
            [$actionResource],
            // error
            $error,
        )->build();
        $actionResource_1 = ActionResource::builder(
            // id
            42,
            // type
            'server',
        )->build();
        $actionResource_2 = ActionResource::builder(
            // id
            38,
            // type
            'firewall',
        )->build();
        $error_1 = ActionError::builder(
            // code
            'action_failed',
            // message
            'Action failed',
        )->build();
        $action_1 = Action::builder(
            // id
            14,
            // command
            'apply_firewall',
            // status
            ActionStatus::success,
            // started
            new DateTime('2016-01-30T23:55:00Z'),
            // finished
            new DateTime('2024-01-01'),
            // progress
            100,
            // resources
            [$actionResource_1, $actionResource_2],
            // error
            $error_1,
        )->build();

        return CreateFirewallResponse201::builder($firewall)
            ->setActions([$action, $action_1])
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateFirewallResponse201 */
    public static function reader(): callable
    {
        return CreateFirewallResponse201::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateFirewallResponse201Constraint::constraints();
    }
}
