<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\CreateCertificateBody;
use Prefabcortex\Hetzner\Validator\CreateCertificateBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class CreateCertificateBodyFixture
{
    public static function build(): CreateCertificateBody
    {
        return CreateCertificateBody::builder('my website cert')
            ->setCertificate('-----BEGIN CERTIFICATE-----
...')
            ->setPrivateKey('-----BEGIN PRIVATE KEY-----
...')
            ->setDomainNames(['example.com', 'www.example.com'])
            ->build();
    }

    /** @return callable(array<int|string, mixed>): CreateCertificateBody */
    public static function reader(): callable
    {
        return CreateCertificateBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return CreateCertificateBodyConstraint::constraints();
    }
}
