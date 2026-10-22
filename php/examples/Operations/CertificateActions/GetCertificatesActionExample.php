<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\CertificateActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetCertificatesActionClientErrorException;
use Prefabcortex\Hetzner\Exception\GetCertificatesActionServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class GetCertificatesActionExample
{
    /**
     * Returns a specific Action object.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetCertificatesActionExample::getCertificatesAction($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetCertificatesActionClientErrorException
     * @throws GetCertificatesActionServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getCertificatesAction(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->certificateActions()->getCertificatesAction($id);
    }
}
