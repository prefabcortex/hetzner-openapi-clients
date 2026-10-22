<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Zones;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreateZoneClientErrorException;
use Prefabcortex\Hetzner\Exception\CreateZoneServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreateZoneBody;
use Prefabcortex\Hetzner\Model\CreateZoneResponse201;
use Prefabcortex\Hetzner\Model\Record;
use Prefabcortex\Hetzner\Model\RRSetRequest;
use Prefabcortex\Hetzner\Model\RRSetType;
use Prefabcortex\Hetzner\Model\ZoneMode;
use Prefabcortex\Hetzner\Model\ZonePrimaryNameserver;

final class CreateZoneExample
{
    /**
     * Creates a [Zone](#tag/zones).
     *
     * A default `SOA` and three `NS` resource records with the assigned Hetzner nameservers are
     * created automatically.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     * Request body: pass the result of one of buildPrimary(), buildPrimaryFromZoneFile(),
     * buildSecondary().
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreateZoneExample::createZone($client, CreateZoneExample::buildPrimary());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreateZoneClientErrorException
     * @throws CreateZoneServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createZone(
        Client $client,
        CreateZoneBody $requestBody,
    ): CreateZoneResponse201 {
        return $client->zones()->createZone($requestBody);
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildPrimary(): CreateZoneBody
    {
        $record = Record::builder('198.51.100.1')
            ->setComment('My web server at Hetzner Cloud.')
            ->build();
        $rRSetRequest = RRSetRequest::builder(
            // name
            'www',
            // type
            RRSetType::A,
            // records
            [$record],
        )->build();

        return CreateZoneBody::builder(
            // name
            'example.com',
            // mode
            ZoneMode::primary,
        )
            ->setTtl(10800)
            ->setLabels(['key' => 'value'])
            ->setRrsets([$rRSetRequest])
            ->build();
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildPrimaryFromZoneFile(): CreateZoneBody
    {
        return CreateZoneBody::builder(
            // name
            'example.com',
            // mode
            ZoneMode::primary,
        )
            ->setTtl(10800)
            ->setLabels(['key' => 'value'])
            ->setZonefile('$ORIGIN	example.com.
$TTL	10800

@	IN	A	198.51.100.1 ; My web server at Hetzner Cloud.
')
            ->build();
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildSecondary(): CreateZoneBody
    {
        $zonePrimaryNameserver = ZonePrimaryNameserver::builder('198.51.100.1')
            ->setPort(53)
            ->build();
        $zonePrimaryNameserver_1 = ZonePrimaryNameserver::builder('203.0.113.1')
            ->setPort(53)
            ->build();

        return CreateZoneBody::builder(
            // name
            'example.com',
            // mode
            ZoneMode::secondary,
        )
            ->setTtl(10800)
            ->setLabels(['key' => 'value'])
            ->setPrimaryNameservers([$zonePrimaryNameserver, $zonePrimaryNameserver_1])
            ->build();
    }
}
