<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Certificate;
use Prefabcortex\Hetzner\Model\CertificateUsedByItem;
use Prefabcortex\Hetzner\Model\CreateCertificateResponse201;
use Prefabcortex\Hetzner\Validator\CreateCertificateResponse201Constraint;
use Symfony\Component\Validator\Constraint;

final class CreateCertificateResponse201Fixture
{
    public static function build(): CreateCertificateResponse201
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

        return CreateCertificateResponse201::builder($certificate)->build();
    }

    /** @return callable(array<int|string, mixed>): CreateCertificateResponse201 */
    public static function reader(): callable
    {
        return CreateCertificateResponse201::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateCertificateResponse201Constraint::constraints();
    }
}
