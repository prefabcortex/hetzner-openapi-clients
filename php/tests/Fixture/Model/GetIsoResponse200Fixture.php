<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Architecture;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\GetIsoResponse200;
use Prefabcortex\Hetzner\Model\Iso;
use Prefabcortex\Hetzner\Model\IsoType;
use Prefabcortex\Hetzner\Validator\GetIsoResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class GetIsoResponse200Fixture
{
    public static function build(): GetIsoResponse200
    {
        $deprecation = DeprecationInfo::builder(
            // unavailableAfter
            new DateTime('2024-01-01'),
            // announced
            new DateTime('2024-01-01'),
        )->build();
        $iso = Iso::builder(
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

        return GetIsoResponse200::builder($iso)->build();
    }

    /** @return callable(array<int|string, mixed>): GetIsoResponse200 */
    public static function reader(): callable
    {
        return GetIsoResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return GetIsoResponse200Constraint::constraints();
    }
}
