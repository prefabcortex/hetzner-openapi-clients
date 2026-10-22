<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ZoneRrsetActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\RemoveZoneRrsetRecordsClientErrorException;
use Prefabcortex\Hetzner\Exception\RemoveZoneRrsetRecordsServerErrorException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\Record;
use Prefabcortex\Hetzner\Model\RRSetRecordsRequest;
use Prefabcortex\Hetzner\Model\RRSetType;

final class RemoveZoneRrsetRecordsExample
{
    /**
     * Removes resource records (RRs) from an existing [RRSet](#tag/zone-rrsets) in the
     * [Zone](#tag/zones).
     *
     * For convenience, the [RRSet](#tag/zone-rrsets) will be automatically deleted if it doesn't
     * contain any RRs afterwards.
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
     *   RemoveZoneRrsetRecordsExample::removeZoneRrsetRecords($client, $idOrName, $rrName, $rrType, RemoveZoneRrsetRecordsExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws RemoveZoneRrsetRecordsClientErrorException
     * @throws RemoveZoneRrsetRecordsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function removeZoneRrsetRecords(
        Client $client,
        string $idOrName,
        string $rrName,
        RRSetType $rrType,
        RRSetRecordsRequest $requestBody,
    ): ActionResponse {
        return $client->zoneRrsetActions()->removeZoneRrsetRecords(
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
