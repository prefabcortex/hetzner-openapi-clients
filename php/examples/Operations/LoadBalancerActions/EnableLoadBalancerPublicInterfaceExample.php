<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\EnableLoadBalancerPublicInterfaceClientErrorException;
use Prefabcortex\Hetzner\Exception\EnableLoadBalancerPublicInterfaceServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class EnableLoadBalancerPublicInterfaceExample
{
    /**
     * Enable the public interface of a Load Balancer. The Load Balancer will be accessible from the
     * internet via its public IPs.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   EnableLoadBalancerPublicInterfaceExample::enableLoadBalancerPublicInterface($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws EnableLoadBalancerPublicInterfaceClientErrorException
     * @throws EnableLoadBalancerPublicInterfaceServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function enableLoadBalancerPublicInterface(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->loadBalancerActions()->enableLoadBalancerPublicInterface($id);
    }
}
