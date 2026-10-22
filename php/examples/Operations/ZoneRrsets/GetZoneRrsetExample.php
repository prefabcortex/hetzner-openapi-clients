<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ZoneRrsets;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetZoneRrsetClientErrorException;
use Prefabcortex\Hetzner\Exception\GetZoneRrsetServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\RrsetResponse;
use Prefabcortex\Hetzner\Model\RRSetType;

final class GetZoneRrsetExample
{
    /**
     * Returns a single [RRSet](#tag/zone-rrsets) from the [Zone](#tag/zones).
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
     *   GetZoneRrsetExample::getZoneRrset($client, $idOrName, $rrName, $rrType);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetZoneRrsetClientErrorException
     * @throws GetZoneRrsetServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getZoneRrset(
        Client $client,
        string $idOrName,
        string $rrName,
        RRSetType $rrType,
    ): RrsetResponse {
        return $client->zoneRrsets()->getZoneRrset(
            $idOrName,
            $rrName,
            $rrType,
        );
    }
}
