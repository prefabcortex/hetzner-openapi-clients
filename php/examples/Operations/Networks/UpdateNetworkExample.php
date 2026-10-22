<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Networks;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateNetworkClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateNetworkServerErrorException;
use Prefabcortex\Hetzner\Model\NetworkResponse;
use Prefabcortex\Hetzner\Model\UpdateNetworkBody;

final class UpdateNetworkExample
{
    /**
     * Update a [Network](#tag/networks).
     *
     * If a change is currently being performed on this [Network](#tag/networks), a error response
     * with code `conflict` will be returned.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateNetworkExample::updateNetwork($client, $id, UpdateNetworkExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateNetworkClientErrorException
     * @throws UpdateNetworkServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateNetwork(
        Client $client,
        int $id,
        UpdateNetworkBody $requestBody,
    ): NetworkResponse {
        return $client->networks()->updateNetwork(
            $id,
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
    public static function buildExampleRequestBody(): UpdateNetworkBody
    {
        return UpdateNetworkBody::builder()
            ->setName('new-name')
            ->setExposeRoutesToVswitch(false)
            ->build();
    }
}
