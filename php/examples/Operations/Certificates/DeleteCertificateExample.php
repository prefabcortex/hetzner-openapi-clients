<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Certificates;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DeleteCertificateClientErrorException;
use Prefabcortex\Hetzner\Exception\DeleteCertificateServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;

final class DeleteCertificateExample
{
    /**
     * Deletes a Certificate.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DeleteCertificateExample::deleteCertificate($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DeleteCertificateClientErrorException
     * @throws DeleteCertificateServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function deleteCertificate(
        Client $client,
        int $id,
    ): null {
        return $client->certificates()->deleteCertificate($id);
    }
}
