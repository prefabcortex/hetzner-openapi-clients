<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateStorageBoxSubaccountAccessSettingsBody;
use Prefabcortex\Hetzner\Validator\UpdateStorageBoxSubaccountAccessSettingsBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateStorageBoxSubaccountAccessSettingsBodyFixture
{
    public static function build(): UpdateStorageBoxSubaccountAccessSettingsBody
    {
        return UpdateStorageBoxSubaccountAccessSettingsBody::builder()->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateStorageBoxSubaccountAccessSettingsBody */
    public static function reader(): callable
    {
        return UpdateStorageBoxSubaccountAccessSettingsBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateStorageBoxSubaccountAccessSettingsBodyConstraint::constraints();
    }
}
