<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\ZoneBaseAuthoritativeNameservers;
use Prefabcortex\Hetzner\Validator\ZoneBaseAuthoritativeNameserversConstraint;
use Symfony\Component\Validator\Constraint;

final class ZoneBaseAuthoritativeNameserversFixture
{
    public static function build(): ZoneBaseAuthoritativeNameservers
    {
        return ZoneBaseAuthoritativeNameservers::builder(
            // assigned
            ['hydrogen.ns.hetzner.com.', 'oxygen.ns.hetzner.com.', 'helium.ns.hetzner.de.'],
            // delegated
            ['hydrogen.ns.hetzner.com.', 'oxygen.ns.hetzner.com.', 'helium.ns.hetzner.de.'],
            // delegationLastCheck
            new DateTime('2024-01-01'),
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ZoneBaseAuthoritativeNameservers */
    public static function reader(): callable
    {
        return ZoneBaseAuthoritativeNameservers::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ZoneBaseAuthoritativeNameserversConstraint::constraints();
    }
}
