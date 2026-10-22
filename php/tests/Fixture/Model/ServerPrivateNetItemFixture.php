<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ServerPrivateNetItem;
use Prefabcortex\Hetzner\Validator\ServerPrivateNetItemConstraint;
use Symfony\Component\Validator\Constraint;

final class ServerPrivateNetItemFixture
{
    public static function build(): ServerPrivateNetItem
    {
        return ServerPrivateNetItem::builder()
            ->setNetwork(4711)
            ->setIp('10.0.0.2')
            ->setAliasIps(['10.0.0.3', '10.0.0.4'])
            ->setMacAddress('86:00:ff:2a:7d:e1')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): ServerPrivateNetItem */
    public static function reader(): callable
    {
        return ServerPrivateNetItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ServerPrivateNetItemConstraint::constraints();
    }
}
