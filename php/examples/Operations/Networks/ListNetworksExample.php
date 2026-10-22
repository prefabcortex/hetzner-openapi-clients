<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Networks;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListNetworksClientErrorException;
use Prefabcortex\Hetzner\Exception\ListNetworksServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListNetworksResponse200;
use Prefabcortex\Hetzner\Parameter\ListNetworksQueryParameters;

final class ListNetworksExample
{
    /**
     * List multiple [Networks](#tag/networks).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListNetworksQueryParameters();
     *   ListNetworksExample::listNetworks($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListNetworksClientErrorException
     * @throws ListNetworksServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listNetworks(
        Client $client,
        ListNetworksQueryParameters $queryParameters,
    ): ListNetworksResponse200 {
        return $client->networks()->listNetworks($queryParameters);
    }
}
