<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Zones;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetZoneZonefileClientErrorException;
use Prefabcortex\Hetzner\Exception\GetZoneZonefileServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\Zonefile;

final class GetZoneZonefileExample
{
    /**
     * Returns a generated [Zone](#tag/zones) file in BIND (RFC
     * [1034](https://datatracker.ietf.org/doc/html/rfc1034)/[1035](https://datatracker.ietf.org/doc/html/rfc1035))
     * format.
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
     *   GetZoneZonefileExample::getZoneZonefile($client, $idOrName);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetZoneZonefileClientErrorException
     * @throws GetZoneZonefileServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getZoneZonefile(
        Client $client,
        string $idOrName,
    ): Zonefile {
        return $client->zones()->getZoneZonefile($idOrName);
    }
}
