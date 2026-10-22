<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\FirewallResource;
use Prefabcortex\Hetzner\Model\FirewallResourceType;
use Prefabcortex\Hetzner\Model\RemoveFirewallFromResourcesBody;
use Prefabcortex\Hetzner\Validator\RemoveFirewallFromResourcesBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class RemoveFirewallFromResourcesBodyFixture
{
    public static function build(): RemoveFirewallFromResourcesBody
    {
        $firewallResource = FirewallResource::builder(FirewallResourceType::server)->build();

        return RemoveFirewallFromResourcesBody::builder([$firewallResource])->build();
    }

    /** @return callable(array<int|string, mixed>): RemoveFirewallFromResourcesBody */
    public static function reader(): callable
    {
        return RemoveFirewallFromResourcesBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return RemoveFirewallFromResourcesBodyConstraint::constraints();
    }
}
