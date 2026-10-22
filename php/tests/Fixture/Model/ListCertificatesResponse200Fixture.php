<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Certificate;
use Prefabcortex\Hetzner\Model\CertificateUsedByItem;
use Prefabcortex\Hetzner\Model\ListCertificatesResponse200;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Validator\ListCertificatesResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListCertificatesResponse200Fixture
{
    public static function build(): ListCertificatesResponse200
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
        $pagination = ListMetaPagination::builder(
            // page
            3,
            // perPage
            25,
            // previousPage
            2,
            // nextPage
            4,
            // lastPage
            4,
            // totalEntries
            100,
        )->build();
        $meta = ListMeta::builder($pagination)->build();

        return ListCertificatesResponse200::builder(
            // certificates
            [$certificate],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListCertificatesResponse200 */
    public static function reader(): callable
    {
        return ListCertificatesResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListCertificatesResponse200Constraint::constraints();
    }
}
