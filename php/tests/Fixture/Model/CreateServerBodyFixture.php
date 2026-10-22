<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateServerBody;
use Prefabcortex\Hetzner\Model\CreateServerBodyFirewallsItem;
use Prefabcortex\Hetzner\Validator\CreateServerBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateServerBodyFixture
{
    public static function build(): CreateServerBody
    {
        $createServerBodyFirewallsItem = CreateServerBodyFirewallsItem::builder(38)->build();

        return CreateServerBody::builder(
            // name
            'my-server',
            // serverType
            'cpx22',
            // image
            'ubuntu-24.04',
        )
            ->setStartAfterCreate(true)
            ->setPlacementGroup(1)
            ->setSshKeys(['my-ssh-key'])
            ->setVolumes([123])
            ->setNetworks([456])
            ->setFirewalls([$createServerBodyFirewallsItem])
            ->setUserData('#cloud-config
runcmd:
- [touch, /root/cloud-init-worked]
')
            ->setAutomount(false)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateServerBody */
    public static function reader(): callable
    {
        return CreateServerBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateServerBodyConstraint::constraints();
    }
}
