<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Locations;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListLocationsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListLocationsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListLocationsResponse200;
use Prefabcortex\Hetzner\Parameter\ListLocationsQueryParameters;

final class ListLocationsExample
{
    /**
     * Returns all [Locations](#tag/locations).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListLocationsQueryParameters();
     *   ListLocationsExample::listLocations($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListLocationsClientErrorException
     * @throws ListLocationsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listLocations(
        Client $client,
        ListLocationsQueryParameters $queryParameters,
    ): ListLocationsResponse200 {
        return $client->locations()->listLocations($queryParameters);
    }
}
