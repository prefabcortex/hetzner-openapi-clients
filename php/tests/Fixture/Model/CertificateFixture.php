<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Certificate;
use Prefabcortex\Hetzner\Model\CertificateUsedByItem;
use Prefabcortex\Hetzner\Validator\CertificateConstraint;
use Symfony\Component\Validator\Constraint;

final class CertificateFixture
{
    public static function build(): Certificate
    {
        $certificateUsedByItem = CertificateUsedByItem::builder(
            // id
            4711,
            // type
            'load_balancer',
        )->build();

        return Certificate::builder(
            // id
            42,
            // name
            'my-resource',
            // labels
            [],
            // certificate
            '-----BEGIN CERTIFICATE-----
...',
            // created
            new DateTime('2024-01-01'),
            // notValidBefore
            new DateTime('2024-01-01'),
            // notValidAfter
            new DateTime('2024-01-01'),
            // domainNames
            ['example.com', 'webmail.example.com', 'www.example.com'],
            // fingerprint
            '03:c7:55:9b:2a:d1:04:17:09:f6:d0:7f:18:34:63:d4:3e:5f',
            // usedBy
            [$certificateUsedByItem],
        )->build();
    }

    /** @return callable(array<int|string, mixed>): Certificate */
    public static function reader(): callable
    {
        return Certificate::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CertificateConstraint::constraints();
    }
}
