<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ApplyFirewallToResourcesBody;
use Prefabcortex\Hetzner\Model\FirewallResource;
use Prefabcortex\Hetzner\Model\FirewallResourceType;
use Prefabcortex\Hetzner\Validator\ApplyFirewallToResourcesBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ApplyFirewallToResourcesBodyFixture
{
    public static function build(): ApplyFirewallToResourcesBody
    {
        $firewallResource = FirewallResource::builder(FirewallResourceType::server)->build();

        return ApplyFirewallToResourcesBody::builder([$firewallResource])->build();
    }

    /** @return callable(array<int|string, mixed>): ApplyFirewallToResourcesBody */
    public static function reader(): callable
    {
        return ApplyFirewallToResourcesBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ApplyFirewallToResourcesBodyConstraint::constraints();
    }
}
