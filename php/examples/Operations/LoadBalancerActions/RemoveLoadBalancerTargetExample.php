<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\RemoveLoadBalancerTargetClientErrorException;
use Prefabcortex\Hetzner\Exception\RemoveLoadBalancerTargetServerErrorException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\LoadBalancerTarget;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetType;

final class RemoveLoadBalancerTargetExample
{
    /**
     * Removes a target from a Load Balancer.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   RemoveLoadBalancerTargetExample::removeLoadBalancerTarget($client, $id, RemoveLoadBalancerTargetExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws RemoveLoadBalancerTargetClientErrorException
     * @throws RemoveLoadBalancerTargetServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function removeLoadBalancerTarget(
        Client $client,
        int $id,
        LoadBalancerTarget $requestBody,
    ): ActionResponse {
        return $client->loadBalancerActions()->removeLoadBalancerTarget(
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
    public static function buildExampleRequestBody(): LoadBalancerTarget
    {
        return LoadBalancerTarget::builder(LoadBalancerTargetType::server)->build();
    }
}
