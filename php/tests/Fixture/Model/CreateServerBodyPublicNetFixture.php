<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateServerBodyPublicNet;
use Prefabcortex\Hetzner\Validator\CreateServerBodyPublicNetConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateServerBodyPublicNetFixture
{
    public static function build(): CreateServerBodyPublicNet
    {
        return CreateServerBodyPublicNet::builder()
            ->setEnableIpv4(true)
            ->setEnableIpv6(true)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateServerBodyPublicNet */
    public static function reader(): callable
    {
        return CreateServerBodyPublicNet::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateServerBodyPublicNetConstraint::constraints();
    }
}
