<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Architecture;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\Iso;
use Prefabcortex\Hetzner\Model\IsoType;
use Prefabcortex\Hetzner\Validator\IsoConstraint;
use Symfony\Component\Validator\Constraint;

final class IsoFixture
{
    public static function build(): Iso
    {
        $deprecation = DeprecationInfo::builder(
            // unavailableAfter
            new DateTime('2024-01-01'),
            // announced
            new DateTime('2024-01-01'),
        )->build();

        return Iso::builder(
            // id
            42,
            // name
            'FreeBSD-11.0-RELEASE-amd64-dvd1',
            // description
            'FreeBSD 11.0 x64',
            // type
            IsoType::public,
            // deprecation
            $deprecation,
            // architecture
            Architecture::x86,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): Iso */
    public static function reader(): callable
    {
        return Iso::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return IsoConstraint::constraints();
    }
}
