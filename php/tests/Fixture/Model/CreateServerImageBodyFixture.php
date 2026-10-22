<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateServerImageBody;
use Prefabcortex\Hetzner\Model\CreateServerImageBodyType;
use Prefabcortex\Hetzner\Validator\CreateServerImageBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateServerImageBodyFixture
{
    public static function build(): CreateServerImageBody
    {
        return CreateServerImageBody::builder()
            ->setDescription('my image')
            ->setType(CreateServerImageBodyType::snapshot)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateServerImageBody */
    public static function reader(): callable
    {
        return CreateServerImageBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateServerImageBodyConstraint::constraints();
    }
}
