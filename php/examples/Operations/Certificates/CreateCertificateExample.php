<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Certificates;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreateCertificateClientErrorException;
use Prefabcortex\Hetzner\Exception\CreateCertificateServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CertificateType;
use Prefabcortex\Hetzner\Model\CreateCertificateBody;
use Prefabcortex\Hetzner\Model\CreateCertificateResponse201;

final class CreateCertificateExample
{
    /**
     * Creates a new Certificate.
     *
     * The default type **uploaded** allows for uploading your existing `certificate` and
     * `private_key` in PEM format. You have to monitor its expiration date and handle renewal
     * yourself.
     *
     * In contrast, type **managed** requests a new Certificate from *Let's Encrypt* for the
     * specified `domain_names`. Only domains managed by *Hetzner DNS* are supported. We handle
     * renewal and timely alert the project owner via email if problems occur.
     *
     * For type `managed` Certificates the `action` key of the response contains the Action that
     * allows for tracking the issuance process. For type `uploaded` Certificates the `action` is
     * always null.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     * Request body: pass the result of one of buildUploaded(), buildManaged().
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreateCertificateExample::createCertificate($client, CreateCertificateExample::buildUploaded());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreateCertificateClientErrorException
     * @throws CreateCertificateServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createCertificate(
        Client $client,
        CreateCertificateBody $requestBody,
    ): CreateCertificateResponse201 {
        return $client->certificates()->createCertificate($requestBody);
    }

    /**
     * Creating a type `uploaded` Certificate.
     */
    public static function buildUploaded(): CreateCertificateBody
    {
        return CreateCertificateBody::builder('my website cert')
            ->setType(CertificateType::uploaded)
            ->setCertificate('-----BEGIN CERTIFICATE-----
...')
            ->setPrivateKey('-----BEGIN PRIVATE KEY-----
...')
            ->build();
    }

    /**
     * Creating a type `managed` Certificate.
     */
    public static function buildManaged(): CreateCertificateBody
    {
        return CreateCertificateBody::builder('my website cert')
            ->setType(CertificateType::managed)
            ->setDomainNames(['example.com', 'webmail.example.com', 'www.example.com'])
            ->build();
    }
}
