<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DisableLoadBalancerPublicInterfaceClientErrorException;
use Prefabcortex\Hetzner\Exception\DisableLoadBalancerPublicInterfaceServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class DisableLoadBalancerPublicInterfaceExample
{
    /**
     * Disable the public interface of a Load Balancer. The Load Balancer will be not accessible
     * from the internet via its public IPs.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `load_balancer_not_attached_to_network` | The Load Balancer is not attached to a network |
     * | `422` | `targets_without_use_private_ip` | The Load Balancer has targets that use the public IP instead of the private IP |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DisableLoadBalancerPublicInterfaceExample::disableLoadBalancerPublicInterface($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DisableLoadBalancerPublicInterfaceClientErrorException
     * @throws DisableLoadBalancerPublicInterfaceServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function disableLoadBalancerPublicInterface(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->loadBalancerActions()->disableLoadBalancerPublicInterface($id);
    }
}
