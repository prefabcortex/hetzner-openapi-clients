<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DetachLoadBalancerFromNetworkClientErrorException;
use Prefabcortex\Hetzner\Exception\DetachLoadBalancerFromNetworkServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\DetachLoadBalancerFromNetworkBody;

final class DetachLoadBalancerFromNetworkExample
{
    /**
     * Detaches a Load Balancer from a network.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DetachLoadBalancerFromNetworkExample::detachLoadBalancerFromNetwork($client, $id, DetachLoadBalancerFromNetworkExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DetachLoadBalancerFromNetworkClientErrorException
     * @throws DetachLoadBalancerFromNetworkServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function detachLoadBalancerFromNetwork(
        Client $client,
        int $id,
        DetachLoadBalancerFromNetworkBody $requestBody,
    ): ActionResponse {
        return $client->loadBalancerActions()->detachLoadBalancerFromNetwork(
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
    public static function buildExampleRequestBody(): DetachLoadBalancerFromNetworkBody
    {
        return DetachLoadBalancerFromNetworkBody::builder(4711)->build();
    }
}
