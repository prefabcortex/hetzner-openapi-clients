<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\NetworkActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\AddNetworkRouteClientErrorException;
use Prefabcortex\Hetzner\Exception\AddNetworkRouteServerErrorException;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\Route;

final class AddNetworkRouteExample
{
    /**
     * Adds a route entry to a [Network](#tag/networks).
     *
     * If a change is currently being performed on this [Network](#tag/networks), a error response
     * with code `conflict` will be returned.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   AddNetworkRouteExample::addNetworkRoute($client, $id, AddNetworkRouteExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws AddNetworkRouteClientErrorException
     * @throws AddNetworkRouteServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function addNetworkRoute(
        Client $client,
        int $id,
        Route $requestBody,
    ): ActionResponse {
        return $client->networkActions()->addNetworkRoute(
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
    public static function buildExampleRequestBody(): Route
    {
        return Route::builder(
            // destination
            '10.100.1.0/24',
            // gateway
            '10.0.1.1',
        )->build();
    }
}
