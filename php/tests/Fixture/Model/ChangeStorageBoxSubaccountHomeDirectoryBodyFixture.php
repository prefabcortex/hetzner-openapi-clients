<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeStorageBoxSubaccountHomeDirectoryBody;
use Prefabcortex\Hetzner\Validator\ChangeStorageBoxSubaccountHomeDirectoryBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeStorageBoxSubaccountHomeDirectoryBodyFixture
{
    public static function build(): ChangeStorageBoxSubaccountHomeDirectoryBody
    {
        return ChangeStorageBoxSubaccountHomeDirectoryBody::builder('my-backup/server01')->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeStorageBoxSubaccountHomeDirectoryBody */
    public static function reader(): callable
    {
        return ChangeStorageBoxSubaccountHomeDirectoryBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeStorageBoxSubaccountHomeDirectoryBodyConstraint::constraints();
    }
}
