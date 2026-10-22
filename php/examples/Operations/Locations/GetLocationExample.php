<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Locations;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetLocationClientErrorException;
use Prefabcortex\Hetzner\Exception\GetLocationServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\GetLocationResponse200;

final class GetLocationExample
{
    /**
     * Returns a [Location](#tag/locations).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetLocationExample::getLocation($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetLocationClientErrorException
     * @throws GetLocationServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getLocation(
        Client $client,
        int $id,
    ): GetLocationResponse200 {
        return $client->locations()->getLocation($id);
    }
}
