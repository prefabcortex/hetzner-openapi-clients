<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\AddLoadBalancerTargetClientErrorException;
use Prefabcortex\Hetzner\Exception\AddLoadBalancerTargetServerErrorException;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\AddLoadBalancerTargetBody;
use Prefabcortex\Hetzner\Model\LoadBalancerTargetType;

final class AddLoadBalancerTargetExample
{
    /**
     * Adds a target to a Load Balancer.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `ip_not_in_vswitch_subnet` | The IP you are trying to add does not belong to the vswitch subnet of the attached network |
     * | `422` | `ip_not_owned` | The IP you are trying to add as a target is not owned by the Project owner |
     * | `422` | `ip_not_assigned_to_server` | The specified IP is neither the Primary IPv4 address nor in the IPv6 subnet of the given Server |
     * | `422` | `load_balancer_public_interface_disabled` | The Load Balancer's public network interface is disabled |
     * | `422` | `load_balancer_not_attached_to_network` | The Load Balancer is not attached to a network |
     * | `422` | `network_has_no_vswitch_subnet` | The given IP is private but attached network does not have a vswitch subnet |
     * | `422` | `resolve_cloud_private_targets_error` | The server you are trying to add as a target is not attached to the same network as the Load Balancer |
     * | `422` | `resolve_cloud_public_targets_error` | The server that you are trying to add as a public target does not have a public IPv4 address |
     * | `422` | `target_already_defined` | The Load Balancer target you are trying to define is already defined |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   AddLoadBalancerTargetExample::addLoadBalancerTarget($client, $id, AddLoadBalancerTargetExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws AddLoadBalancerTargetClientErrorException
     * @throws AddLoadBalancerTargetServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function addLoadBalancerTarget(
        Client $client,
        int $id,
        AddLoadBalancerTargetBody $requestBody,
    ): ActionResponse {
        return $client->loadBalancerActions()->addLoadBalancerTarget(
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
    public static function buildExampleRequestBody(): AddLoadBalancerTargetBody
    {
        return AddLoadBalancerTargetBody::builder(LoadBalancerTargetType::server)
            ->setUsePrivateIp(true)
            ->build();
    }
}
