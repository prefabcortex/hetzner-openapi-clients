<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateFloatingIpBody;
use Prefabcortex\Hetzner\Model\IpType;
use Prefabcortex\Hetzner\Validator\CreateFloatingIpBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateFloatingIpBodyFixture
{
    public static function build(): CreateFloatingIpBody
    {
        return CreateFloatingIpBody::builder(IpType::ipv4)
            ->setServer(42)
            ->setDescription('This describes my resource')
            ->setName('my-resource')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateFloatingIpBody */
    public static function reader(): callable
    {
        return CreateFloatingIpBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateFloatingIpBodyConstraint::constraints();
    }
}
