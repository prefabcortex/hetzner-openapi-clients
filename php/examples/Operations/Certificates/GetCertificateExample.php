<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Certificates;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetCertificateClientErrorException;
use Prefabcortex\Hetzner\Exception\GetCertificateServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CertificateResponse;

final class GetCertificateExample
{
    /**
     * Gets a specific Certificate object.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetCertificateExample::getCertificate($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetCertificateClientErrorException
     * @throws GetCertificateServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getCertificate(
        Client $client,
        int $id,
    ): CertificateResponse {
        return $client->certificates()->getCertificate($id);
    }
}
