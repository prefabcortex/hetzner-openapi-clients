<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ZoneActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ImportZoneZonefileClientErrorException;
use Prefabcortex\Hetzner\Exception\ImportZoneZonefileServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\Zonefile;

final class ImportZoneZonefileExample
{
    /**
     * Imports a zone file, replacing all resource record sets ([RRSets](#tag/zone-rrsets)).
     *
     * The import will fail if existing [RRSet](#tag/zone-rrsets) are `change` protected.
     *
     * See [Zone file import](#tag/zones/zone-file-import) for more details. Only applicable for
     * [Zones](#tag/zones) in primary mode.
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
     *   ImportZoneZonefileExample::importZoneZonefile($client, $idOrName, ImportZoneZonefileExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ImportZoneZonefileClientErrorException
     * @throws ImportZoneZonefileServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function importZoneZonefile(
        Client $client,
        string $idOrName,
        Zonefile $requestBody,
    ): ActionResponse {
        return $client->zoneActions()->importZoneZonefile(
            $idOrName,
            $requestBody,
        );
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildExampleRequestBody(): Zonefile
    {
        return Zonefile::builder('$ORIGIN	example.com.
$TTL	3600

@	IN	SOA	hydrogen.ns.hetzner.com. dns.hetzner.com. 2024010100 86400 10800 3600000 3600

@	IN	10800	NS	hydrogen.ns.hetzner.com. ; Some comment.
@	IN	10800	NS	oxygen.ns.hetzner.com.
@	IN	10800	NS	helium.ns.hetzner.de.
')->build();
    }
}
