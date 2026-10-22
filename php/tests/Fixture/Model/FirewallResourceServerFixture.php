<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\FirewallResourceServer;
use Prefabcortex\Hetzner\Validator\FirewallResourceServerConstraint;
use Symfony\Component\Validator\Constraint;

final class FirewallResourceServerFixture
{
    public static function build(): FirewallResourceServer
    {
        return FirewallResourceServer::builder(0)->build();
    }

    /** @return callable(array<int|string, mixed>): FirewallResourceServer */
    public static function reader(): callable
    {
        return FirewallResourceServer::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return FirewallResourceServerConstraint::constraints();
    }
}
