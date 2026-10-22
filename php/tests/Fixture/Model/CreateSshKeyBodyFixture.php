<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateSshKeyBody;
use Prefabcortex\Hetzner\Validator\CreateSshKeyBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateSshKeyBodyFixture
{
    public static function build(): CreateSshKeyBody
    {
        return CreateSshKeyBody::builder(
            // name
            'My ssh key',
            // publicKey
            'ssh-rsa AAAjjk76kgf...Xt',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): CreateSshKeyBody */
    public static function reader(): callable
    {
        return CreateSshKeyBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateSshKeyBodyConstraint::constraints();
    }
}
