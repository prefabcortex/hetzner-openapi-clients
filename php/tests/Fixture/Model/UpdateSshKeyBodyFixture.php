<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateSshKeyBody;
use Prefabcortex\Hetzner\Validator\UpdateSshKeyBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateSshKeyBodyFixture
{
    public static function build(): UpdateSshKeyBody
    {
        return UpdateSshKeyBody::builder()
            ->setName('My ssh key')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateSshKeyBody */
    public static function reader(): callable
    {
        return UpdateSshKeyBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateSshKeyBodyConstraint::constraints();
    }
}
