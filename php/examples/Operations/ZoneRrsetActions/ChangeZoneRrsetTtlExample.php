<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ZoneRrsetActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ChangeZoneRrsetTtlClientErrorException;
use Prefabcortex\Hetzner\Exception\ChangeZoneRrsetTtlServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ChangeZoneRrsetTtlBody;
use Prefabcortex\Hetzner\Model\RRSetType;

final class ChangeZoneRrsetTtlExample
{
    /**
     * Changes the Time To Live (TTL) of an [RRSet](#tag/zone-rrsets) in the [Zone](#tag/zones).
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
     *   ChangeZoneRrsetTtlExample::changeZoneRrsetTtl($client, $idOrName, $rrName, $rrType, ChangeZoneRrsetTtlExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ChangeZoneRrsetTtlClientErrorException
     * @throws ChangeZoneRrsetTtlServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function changeZoneRrsetTtl(
        Client $client,
        string $idOrName,
        string $rrName,
        RRSetType $rrType,
        ChangeZoneRrsetTtlBody $requestBody,
    ): ActionResponse {
        return $client->zoneRrsetActions()->changeZoneRrsetTtl(
            $idOrName,
            $rrName,
            $rrType,
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
    public static function buildExampleRequestBody(): ChangeZoneRrsetTtlBody
    {
        return ChangeZoneRrsetTtlBody::builder(3600)->build();
    }
}
