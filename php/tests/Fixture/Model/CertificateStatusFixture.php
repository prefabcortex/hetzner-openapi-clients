<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CertificateStatus;
use Prefabcortex\Hetzner\Model\CertificateStatusIssuance;
use Prefabcortex\Hetzner\Model\CertificateStatusRenewal;
use Prefabcortex\Hetzner\Validator\CertificateStatusConstraint;
use Symfony\Component\Validator\Constraint;

final class CertificateStatusFixture
{
    public static function build(): CertificateStatus
    {
        return CertificateStatus::builder()
            ->setIssuance(CertificateStatusIssuance::completed)
            ->setRenewal(CertificateStatusRenewal::scheduled)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CertificateStatus */
    public static function reader(): callable
    {
        return CertificateStatus::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CertificateStatusConstraint::constraints();
    }
}
