<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancers;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreateLoadBalancerClientErrorException;
use Prefabcortex\Hetzner\Exception\CreateLoadBalancerServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreateLoadBalancerBody;
use Prefabcortex\Hetzner\Model\CreateLoadBalancerResponse201;
use Prefabcortex\Hetzner\Model\LoadBalancerAlgorithm;
use Prefabcortex\Hetzner\Model\LoadBalancerAlgorithmType;

final class CreateLoadBalancerExample
{
    /**
     * Creates a Load Balancer.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `412` | `source_port_already_used` | The source port you are trying to add is already in use |
     * | `412` | `primary_ip_version_mismatch` | The specified Primary IP has the wrong IP version |
     * | `422` | `ip_not_owned` | The IP is not owned by the owner of the project of the Load Balancer |
     * | `422` | `load_balancer_not_attached_to_network` | The Load Balancer is not attached to a network |
     * | `422` | `resolve_cloud_private_targets_error` | The server you are trying to add as a target is not attached to the same network as the Load Balancer |
     * | `422` | `resolve_cloud_public_targets_error` | The server that you are trying to add as a public target does not have a public IPv4 address |
     * | `422` | `target_already_defined` | The Load Balancer target you are trying to define is already defined |
     * | `422` | `primary_ip_assigned` | The specified Primary IP is already assigned to a resource |
     * | `422` | `primary_ip_blocked` | The specified Primary IP is blocked |
     * | `422` | `primary_ip_location_mismatch` | The specified Primary IP is bound to a different Location than the Load Balancer |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreateLoadBalancerExample::createLoadBalancer($client, CreateLoadBalancerExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreateLoadBalancerClientErrorException
     * @throws CreateLoadBalancerServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createLoadBalancer(
        Client $client,
        CreateLoadBalancerBody $requestBody,
    ): CreateLoadBalancerResponse201 {
        return $client->loadBalancers()->createLoadBalancer($requestBody);
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildExampleRequestBody(): CreateLoadBalancerBody
    {
        $algorithm = LoadBalancerAlgorithm::builder(LoadBalancerAlgorithmType::round_robin)->build();

        return CreateLoadBalancerBody::builder(
            // name
            'Web Frontend',
            // loadBalancerType
            'lb11',
        )
            ->setAlgorithm($algorithm)
            ->setPublicInterface(true)
            ->setNetwork(123)
            ->setNetworkZone('eu-central')
            ->build();
    }
}
