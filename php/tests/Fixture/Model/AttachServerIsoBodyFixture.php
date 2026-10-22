<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\AttachServerIsoBody;
use Prefabcortex\Hetzner\Validator\AttachServerIsoBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class AttachServerIsoBodyFixture
{
    public static function build(): AttachServerIsoBody
    {
        return AttachServerIsoBody::builder('FreeBSD-11.0-RELEASE-amd64-dvd1')->build();
    }

    /** @return callable(array<int|string, mixed>): AttachServerIsoBody */
    public static function reader(): callable
    {
        return AttachServerIsoBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return AttachServerIsoBodyConstraint::constraints();
    }
}
