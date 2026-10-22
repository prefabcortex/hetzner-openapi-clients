<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Certificates;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListCertificatesClientErrorException;
use Prefabcortex\Hetzner\Exception\ListCertificatesServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListCertificatesResponse200;
use Prefabcortex\Hetzner\Parameter\ListCertificatesQueryParameters;

final class ListCertificatesExample
{
    /**
     * Returns all Certificate objects.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListCertificatesQueryParameters();
     *   ListCertificatesExample::listCertificates($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListCertificatesClientErrorException
     * @throws ListCertificatesServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listCertificates(
        Client $client,
        ListCertificatesQueryParameters $queryParameters,
    ): ListCertificatesResponse200 {
        return $client->certificates()->listCertificates($queryParameters);
    }
}
