<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Networks;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DeleteNetworkClientErrorException;
use Prefabcortex\Hetzner\Exception\DeleteNetworkServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;

final class DeleteNetworkExample
{
    /**
     * Deletes a [Network](#tag/networks).
     *
     * Attached resources will be detached automatically.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DeleteNetworkExample::deleteNetwork($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DeleteNetworkClientErrorException
     * @throws DeleteNetworkServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function deleteNetwork(
        Client $client,
        int $id,
    ): null {
        return $client->networks()->deleteNetwork($id);
    }
}
