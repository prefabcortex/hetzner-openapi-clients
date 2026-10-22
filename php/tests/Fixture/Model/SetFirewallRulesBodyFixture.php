<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\FirewallRuleDirection;
use Prefabcortex\Hetzner\Model\FirewallRuleProtocol;
use Prefabcortex\Hetzner\Model\Rule;
use Prefabcortex\Hetzner\Model\SetFirewallRulesBody;
use Prefabcortex\Hetzner\Validator\SetFirewallRulesBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class SetFirewallRulesBodyFixture
{
    public static function build(): SetFirewallRulesBody
    {
        $rule = Rule::builder(
            // direction
            FirewallRuleDirection::in,
            // protocol
            FirewallRuleProtocol::tcp,
        )
            ->setSourceIps(['192.0.2.2/32', '192.0.2.0/24', '2001:0db8:9a3b:ee58:5ca:990c:8bc9:c03b/128'])
            ->setDestinationIps(['REPLACE_ME'])
            ->setPort('80')
            ->build();

        return SetFirewallRulesBody::builder([$rule])->build();
    }

    /** @return callable(array<int|string, mixed>): SetFirewallRulesBody */
    public static function reader(): callable
    {
        return SetFirewallRulesBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return SetFirewallRulesBodyConstraint::constraints();
    }
}
