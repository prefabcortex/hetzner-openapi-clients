<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ServerProtection;
use Prefabcortex\Hetzner\Validator\ServerProtectionConstraint;
use Symfony\Component\Validator\Constraint;

final class ServerProtectionFixture
{
    public static function build(): ServerProtection
    {
        return ServerProtection::builder(
            // delete
            false,
            // rebuild
            false,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ServerProtection */
    public static function reader(): callable
    {
        return ServerProtection::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ServerProtectionConstraint::constraints();
    }
}
