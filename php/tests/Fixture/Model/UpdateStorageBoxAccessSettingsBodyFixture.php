<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateStorageBoxAccessSettingsBody;
use Prefabcortex\Hetzner\Validator\UpdateStorageBoxAccessSettingsBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateStorageBoxAccessSettingsBodyFixture
{
    public static function build(): UpdateStorageBoxAccessSettingsBody
    {
        return UpdateStorageBoxAccessSettingsBody::builder()->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateStorageBoxAccessSettingsBody */
    public static function reader(): callable
    {
        return UpdateStorageBoxAccessSettingsBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateStorageBoxAccessSettingsBodyConstraint::constraints();
    }
}
