<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ZoneRrsetActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\SetZoneRrsetRecordsClientErrorException;
use Prefabcortex\Hetzner\Exception\SetZoneRrsetRecordsServerErrorException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\Record;
use Prefabcortex\Hetzner\Model\RRSetRecordsRequest;
use Prefabcortex\Hetzner\Model\RRSetType;

final class SetZoneRrsetRecordsExample
{
    /**
     * Overwrites the resource records (RRs) of an existing [RRSet](#tag/zone-rrsets) in the
     * [Zone](#tag/zones).
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
     *   SetZoneRrsetRecordsExample::setZoneRrsetRecords($client, $idOrName, $rrName, $rrType, SetZoneRrsetRecordsExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws SetZoneRrsetRecordsClientErrorException
     * @throws SetZoneRrsetRecordsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function setZoneRrsetRecords(
        Client $client,
        string $idOrName,
        string $rrName,
        RRSetType $rrType,
        RRSetRecordsRequest $requestBody,
    ): ActionResponse {
        return $client->zoneRrsetActions()->setZoneRrsetRecords(
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
    public static function buildExampleRequestBody(): RRSetRecordsRequest
    {
        $record = Record::builder('198.51.100.1')
            ->setComment('My web server at Hetzner Cloud.')
            ->build();

        return RRSetRecordsRequest::builder([$record])->build();
    }
}
