<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Zones;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetZoneClientErrorException;
use Prefabcortex\Hetzner\Exception\GetZoneServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ZoneResponse;

final class GetZoneExample
{
    /**
     * Returns a single [Zone](#tag/zones).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetZoneExample::getZone($client, $idOrName);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetZoneClientErrorException
     * @throws GetZoneServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getZone(
        Client $client,
        string $idOrName,
    ): ZoneResponse {
        return $client->zones()->getZone($idOrName);
    }
}
