<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Zones;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateZoneClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateZoneServerErrorException;
use Prefabcortex\Hetzner\Model\UpdateZoneBody;
use Prefabcortex\Hetzner\Model\ZoneResponse;

final class UpdateZoneExample
{
    /**
     * Updates a [Zone](#tag/zones).
     *
     * To modify resource record sets ([RRSets](#tag/zone-rrsets)), use the [RRSet Actions
     * endpoints](#tag/zone-rrset-actions).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateZoneExample::updateZone($client, $idOrName, UpdateZoneExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateZoneClientErrorException
     * @throws UpdateZoneServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateZone(
        Client $client,
        string $idOrName,
        UpdateZoneBody $requestBody,
    ): ZoneResponse {
        return $client->zones()->updateZone(
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
    public static function buildExampleRequestBody(): UpdateZoneBody
    {
        return UpdateZoneBody::builder()->build();
    }
}
