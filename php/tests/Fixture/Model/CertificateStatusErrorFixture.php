<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CertificateStatusError;
use Prefabcortex\Hetzner\Validator\CertificateStatusErrorConstraint;
use Symfony\Component\Validator\Constraint;

final class CertificateStatusErrorFixture
{
    public static function build(): CertificateStatusError
    {
        return CertificateStatusError::builder()->build();
    }

    /** @return callable(array<int|string, mixed>): CertificateStatusError */
    public static function reader(): callable
    {
        return CertificateStatusError::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CertificateStatusErrorConstraint::constraints();
    }
}
