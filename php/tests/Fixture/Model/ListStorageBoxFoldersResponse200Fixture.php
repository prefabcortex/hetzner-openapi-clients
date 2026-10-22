<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ListStorageBoxFoldersResponse200;
use Prefabcortex\Hetzner\Validator\ListStorageBoxFoldersResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListStorageBoxFoldersResponse200Fixture
{
    public static function build(): ListStorageBoxFoldersResponse200
    {
        return ListStorageBoxFoldersResponse200::builder(['REPLACE_ME'])->build();
    }

    /** @return callable(array<int|string, mixed>): ListStorageBoxFoldersResponse200 */
    public static function reader(): callable
    {
        return ListStorageBoxFoldersResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListStorageBoxFoldersResponse200Constraint::constraints();
    }
}
