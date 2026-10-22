<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Isos;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListIsosClientErrorException;
use Prefabcortex\Hetzner\Exception\ListIsosServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListIsosResponse200;
use Prefabcortex\Hetzner\Parameter\ListIsosQueryParameters;

final class ListIsosExample
{
    /**
     * Returns all available ISO objects.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListIsosQueryParameters();
     *   ListIsosExample::listIsos($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListIsosClientErrorException
     * @throws ListIsosServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listIsos(
        Client $client,
        ListIsosQueryParameters $queryParameters,
    ): ListIsosResponse200 {
        return $client->isos()->listIsos($queryParameters);
    }
}
