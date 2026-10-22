<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateFirewallBody;
use Prefabcortex\Hetzner\Model\FirewallRuleDirection;
use Prefabcortex\Hetzner\Model\FirewallRuleProtocol;
use Prefabcortex\Hetzner\Model\Rule;
use Prefabcortex\Hetzner\Validator\CreateFirewallBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateFirewallBodyFixture
{
    public static function build(): CreateFirewallBody
    {
        $rule = Rule::builder(
            // direction
            FirewallRuleDirection::in,
            // protocol
            FirewallRuleProtocol::tcp,
        )
            ->setSourceIps(['192.0.2.2/32', '192.0.2.0/24', '2001:0db8:9a3b:ee58:5ca:990c:8bc9:c03b/128'])
            ->setPort('80')
            ->build();

        return CreateFirewallBody::builder('new-name')
            ->setRules([$rule])
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateFirewallBody */
    public static function reader(): callable
    {
        return CreateFirewallBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateFirewallBodyConstraint::constraints();
    }
}
