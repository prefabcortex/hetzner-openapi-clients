<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CertificateUsedByItem;
use Prefabcortex\Hetzner\Validator\CertificateUsedByItemConstraint;
use Symfony\Component\Validator\Constraint;

final class CertificateUsedByItemFixture
{
    public static function build(): CertificateUsedByItem
    {
        return CertificateUsedByItem::builder(
            // id
            4711,
            // type
            'load_balancer',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): CertificateUsedByItem */
    public static function reader(): callable
    {
        return CertificateUsedByItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CertificateUsedByItemConstraint::constraints();
    }
}
