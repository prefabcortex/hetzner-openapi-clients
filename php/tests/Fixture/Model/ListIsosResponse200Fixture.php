<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Architecture;
use Prefabcortex\Hetzner\Model\DeprecationInfo;
use Prefabcortex\Hetzner\Model\Iso;
use Prefabcortex\Hetzner\Model\IsoType;
use Prefabcortex\Hetzner\Model\ListIsosResponse200;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Validator\ListIsosResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListIsosResponse200Fixture
{
    public static function build(): ListIsosResponse200
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
        $pagination = ListMetaPagination::builder(
            // page
            3,
            // perPage
            25,
            // previousPage
            2,
            // nextPage
            4,
            // lastPage
            4,
            // totalEntries
            100,
        )->build();
        $meta = ListMeta::builder($pagination)->build();

        return ListIsosResponse200::builder(
            // isos
            [$iso],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListIsosResponse200 */
    public static function reader(): callable
    {
        return ListIsosResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListIsosResponse200Constraint::constraints();
    }
}
