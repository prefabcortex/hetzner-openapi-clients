<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\AddLoadBalancerServiceClientErrorException;
use Prefabcortex\Hetzner\Exception\AddLoadBalancerServiceServerErrorException;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\AddLoadBalancerServiceBody;
use Prefabcortex\Hetzner\Model\HealthCheckProtocol;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceHealthCheck;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceProtocol;

final class AddLoadBalancerServiceExample
{
    /**
     * Adds a service to a Load Balancer.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `412` | `source_port_already_used` | The source port you are trying to add is already in use |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   AddLoadBalancerServiceExample::addLoadBalancerService($client, $id, AddLoadBalancerServiceExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws AddLoadBalancerServiceClientErrorException
     * @throws AddLoadBalancerServiceServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function addLoadBalancerService(
        Client $client,
        int $id,
        AddLoadBalancerServiceBody $requestBody,
    ): ActionResponse {
        return $client->loadBalancerActions()->addLoadBalancerService(
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
    public static function buildExampleRequestBody(): AddLoadBalancerServiceBody
    {
        $healthCheck = LoadBalancerServiceHealthCheck::builder(
            // protocol
            HealthCheckProtocol::tcp,
            // port
            4711,
            // interval
            15,
            // timeout
            10,
            // retries
            3,
        )->build();

        return AddLoadBalancerServiceBody::builder(
            // protocol
            LoadBalancerServiceProtocol::tcp,
            // listenPort
            443,
            // destinationPort
            80,
            // proxyprotocol
            false,
            // healthCheck
            $healthCheck,
        )->build();
    }
}
