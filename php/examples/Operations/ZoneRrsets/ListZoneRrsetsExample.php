<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ZoneRrsets;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListZoneRrsetsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListZoneRrsetsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListZoneRrsetsResponse200;
use Prefabcortex\Hetzner\Parameter\ListZoneRrsetsQueryParameters;

final class ListZoneRrsetsExample
{
    /**
     * Returns all [RRSets](#tag/zone-rrsets) in the [Zone](#tag/zones).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Only applicable for [Zones](#tag/zones) in primary mode.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `incorrect_zone_mode` | This operation is not supported for this Zone's `mode`. |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListZoneRrsetsQueryParameters();
     *   ListZoneRrsetsExample::listZoneRrsets($client, $idOrName, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListZoneRrsetsClientErrorException
     * @throws ListZoneRrsetsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listZoneRrsets(
        Client $client,
        string $idOrName,
        ListZoneRrsetsQueryParameters $queryParameters,
    ): ListZoneRrsetsResponse200 {
        return $client->zoneRrsets()->listZoneRrsets(
            $idOrName,
            $queryParameters,
        );
    }
}
