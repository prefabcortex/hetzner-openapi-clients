<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\FirewallAppliedToServer;
use Prefabcortex\Hetzner\Validator\FirewallAppliedToServerConstraint;
use Symfony\Component\Validator\Constraint;

final class FirewallAppliedToServerFixture
{
    public static function build(): FirewallAppliedToServer
    {
        return FirewallAppliedToServer::builder(42)->build();
    }

    /** @return callable(array<int|string, mixed>): FirewallAppliedToServer */
    public static function reader(): callable
    {
        return FirewallAppliedToServer::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return FirewallAppliedToServerConstraint::constraints();
    }
}
