<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Networks;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreateNetworkClientErrorException;
use Prefabcortex\Hetzner\Exception\CreateNetworkServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreateNetworkBody;
use Prefabcortex\Hetzner\Model\NetworkResponse;

final class CreateNetworkExample
{
    /**
     * Creates a [Network](#tag/networks).
     *
     * The provided `ip_range` can only be extended later on, but not reduced.
     *
     * Subnets can be added now or later on using the [add subnet
     * action](#tag/network-actions/add_network_subnet). If you do not specify an `ip_range` for the
     * subnet the first available /24 range will be used.
     *
     * Routes can be added now or later by using the [add route
     * action](#tag/network-actions/add_network_route).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreateNetworkExample::createNetwork($client, CreateNetworkExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreateNetworkClientErrorException
     * @throws CreateNetworkServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createNetwork(
        Client $client,
        CreateNetworkBody $requestBody,
    ): NetworkResponse {
        return $client->networks()->createNetwork($requestBody);
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildExampleRequestBody(): CreateNetworkBody
    {
        return CreateNetworkBody::builder(
            // name
            'mynet',
            // ipRange
            '10.0.0.0/16',
        )
            ->setExposeRoutesToVswitch(false)
            ->build();
    }
}
