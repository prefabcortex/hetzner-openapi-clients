<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Validator\ListMetaPaginationConstraint;
use Symfony\Component\Validator\Constraint;

final class ListMetaPaginationFixture
{
    public static function build(): ListMetaPagination
    {
        return ListMetaPagination::builder(
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
    }

    /** @return callable(array<int|string, mixed>): ListMetaPagination */
    public static function reader(): callable
    {
        return ListMetaPagination::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListMetaPaginationConstraint::constraints();
    }
}
