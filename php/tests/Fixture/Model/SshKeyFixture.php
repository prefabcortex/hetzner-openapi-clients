<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\SshKey;
use Prefabcortex\Hetzner\Validator\SshKeyConstraint;
use Symfony\Component\Validator\Constraint;

final class SshKeyFixture
{
    public static function build(): SshKey
    {
        return SshKey::builder(
            // id
            42,
            // name
            'my-resource',
            // fingerprint
            'b7:2f:30:a0:2f:6c:58:6c:21:04:58:61:ba:06:3b:2f',
            // publicKey
            'ssh-rsa AAAjjk76kgf...Xt',
            // labels
            [],
            // created
            new DateTime('2024-01-01'),
        )->build();
    }

    /** @return callable(array<int|string, mixed>): SshKey */
    public static function reader(): callable
    {
        return SshKey::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return SshKeyConstraint::constraints();
    }
}
