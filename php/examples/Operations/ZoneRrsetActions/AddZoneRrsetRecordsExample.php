<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ZoneRrsetActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\AddZoneRrsetRecordsClientErrorException;
use Prefabcortex\Hetzner\Exception\AddZoneRrsetRecordsServerErrorException;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\AddZoneRrsetRecordsBody;
use Prefabcortex\Hetzner\Model\Record;
use Prefabcortex\Hetzner\Model\RRSetType;

final class AddZoneRrsetRecordsExample
{
    /**
     * Adds resource records (RRs) to an [RRSet](#tag/zone-rrsets) in the [Zone](#tag/zones).
     *
     * For convenience, the [RRSet](#tag/zone-rrsets) will be automatically created if it doesn't
     * exist. Otherwise, the new records are appended to the existing [RRSet](#tag/zone-rrsets).
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
     *   AddZoneRrsetRecordsExample::addZoneRrsetRecords($client, $idOrName, $rrName, $rrType, AddZoneRrsetRecordsExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws AddZoneRrsetRecordsClientErrorException
     * @throws AddZoneRrsetRecordsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function addZoneRrsetRecords(
        Client $client,
        string $idOrName,
        string $rrName,
        RRSetType $rrType,
        AddZoneRrsetRecordsBody $requestBody,
    ): ActionResponse {
        return $client->zoneRrsetActions()->addZoneRrsetRecords(
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
    public static function buildExampleRequestBody(): AddZoneRrsetRecordsBody
    {
        $record = Record::builder('198.51.100.1')
            ->setComment('My web server at Hetzner Cloud.')
            ->build();

        return AddZoneRrsetRecordsBody::builder([$record])
            ->setTtl(3600)
            ->build();
    }
}
