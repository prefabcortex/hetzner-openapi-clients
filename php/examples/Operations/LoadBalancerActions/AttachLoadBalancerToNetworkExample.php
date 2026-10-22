<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\AttachLoadBalancerToNetworkClientErrorException;
use Prefabcortex\Hetzner\Exception\AttachLoadBalancerToNetworkServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\AttachLoadBalancerToNetworkBody;

final class AttachLoadBalancerToNetworkExample
{
    /**
     * Attach a Load Balancer to a Network.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `load_balancer_already_attached` | The Load Balancer is already attached to a network |
     * | `422` | `ip_not_available` | The provided Network IP is not available |
     * | `422` | `no_subnet_available` | No Subnet or IP is available for the Load Balancer within the network |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   AttachLoadBalancerToNetworkExample::attachLoadBalancerToNetwork($client, $id, AttachLoadBalancerToNetworkExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws AttachLoadBalancerToNetworkClientErrorException
     * @throws AttachLoadBalancerToNetworkServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function attachLoadBalancerToNetwork(
        Client $client,
        int $id,
        AttachLoadBalancerToNetworkBody $requestBody,
    ): ActionResponse {
        return $client->loadBalancerActions()->attachLoadBalancerToNetwork(
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
    public static function buildExampleRequestBody(): AttachLoadBalancerToNetworkBody
    {
        return AttachLoadBalancerToNetworkBody::builder(123)
            ->setIp('10.0.1.1')
            ->setIpRange('10.0.1.0/24')
            ->build();
    }
}
