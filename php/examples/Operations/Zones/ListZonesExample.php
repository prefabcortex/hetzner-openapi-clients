<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Zones;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListZonesClientErrorException;
use Prefabcortex\Hetzner\Exception\ListZonesServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListZonesResponse200;
use Prefabcortex\Hetzner\Parameter\ListZonesQueryParameters;

final class ListZonesExample
{
    /**
     * Returns all [Zones](#tag/zones).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListZonesQueryParameters();
     *   ListZonesExample::listZones($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListZonesClientErrorException
     * @throws ListZonesServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listZones(
        Client $client,
        ListZonesQueryParameters $queryParameters,
    ): ListZonesResponse200 {
        return $client->zones()->listZones($queryParameters);
    }
}
