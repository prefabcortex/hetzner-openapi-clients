<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ZoneActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ChangeZonePrimaryNameserversClientErrorException;
use Prefabcortex\Hetzner\Exception\ChangeZonePrimaryNameserversServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ChangeZonePrimaryNameserversBody;
use Prefabcortex\Hetzner\Model\ZonePrimaryNameserver;

final class ChangeZonePrimaryNameserversExample
{
    /**
     * Overwrites the primary nameservers of a [Zone](#tag/zones).
     *
     * Only applicable for [Zones](#tag/zones) in secondary mode.
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
     *   ChangeZonePrimaryNameserversExample::changeZonePrimaryNameservers($client, $idOrName, ChangeZonePrimaryNameserversExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ChangeZonePrimaryNameserversClientErrorException
     * @throws ChangeZonePrimaryNameserversServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function changeZonePrimaryNameservers(
        Client $client,
        string $idOrName,
        ChangeZonePrimaryNameserversBody $requestBody,
    ): ActionResponse {
        return $client->zoneActions()->changeZonePrimaryNameservers(
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
    public static function buildExampleRequestBody(): ChangeZonePrimaryNameserversBody
    {
        $zonePrimaryNameserver = ZonePrimaryNameserver::builder('198.51.100.1')
            ->setPort(53)
            ->build();
        $zonePrimaryNameserver_1 = ZonePrimaryNameserver::builder('203.0.113.1')
            ->setPort(53)
            ->build();

        return ChangeZonePrimaryNameserversBody::builder([$zonePrimaryNameserver, $zonePrimaryNameserver_1])->build();
    }
}
