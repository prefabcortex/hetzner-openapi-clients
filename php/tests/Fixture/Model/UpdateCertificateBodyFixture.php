<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateCertificateBody;
use Prefabcortex\Hetzner\Validator\UpdateCertificateBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateCertificateBodyFixture
{
    public static function build(): UpdateCertificateBody
    {
        return UpdateCertificateBody::builder()
            ->setName('my website cert')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateCertificateBody */
    public static function reader(): callable
    {
        return UpdateCertificateBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateCertificateBodyConstraint::constraints();
    }
}
