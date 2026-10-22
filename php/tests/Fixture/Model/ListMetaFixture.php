<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Validator\ListMetaConstraint;
use Symfony\Component\Validator\Constraint;

final class ListMetaFixture
{
    public static function build(): ListMeta
    {
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

        return ListMeta::builder($pagination)->build();
    }

    /** @return callable(array<int|string, mixed>): ListMeta */
    public static function reader(): callable
    {
        return ListMeta::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListMetaConstraint::constraints();
    }
}
