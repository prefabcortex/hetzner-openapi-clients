<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Certificate;
use Prefabcortex\Hetzner\Model\CertificateResponse;
use Prefabcortex\Hetzner\Model\CertificateUsedByItem;
use Prefabcortex\Hetzner\Validator\CertificateResponseConstraint;
use Symfony\Component\Validator\Constraint;

final class CertificateResponseFixture
{
    public static function build(): CertificateResponse
    {
        $certificateUsedByItem = CertificateUsedByItem::builder(
            // id
            4711,
            // type
            'load_balancer',
        )->build();
        $certificate = Certificate::builder(
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

        return CertificateResponse::builder($certificate)->build();
    }

    /** @return callable(array<int|string, mixed>): CertificateResponse */
    public static function reader(): callable
    {
        return CertificateResponse::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CertificateResponseConstraint::constraints();
    }
}
