<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerTypes;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetLoadBalancerTypeClientErrorException;
use Prefabcortex\Hetzner\Exception\GetLoadBalancerTypeServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\GetLoadBalancerTypeResponse200;

final class GetLoadBalancerTypeExample
{
    /**
     * Gets a specific Load Balancer type object.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetLoadBalancerTypeExample::getLoadBalancerType($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetLoadBalancerTypeClientErrorException
     * @throws GetLoadBalancerTypeServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getLoadBalancerType(
        Client $client,
        int $id,
    ): GetLoadBalancerTypeResponse200 {
        return $client->loadBalancerTypes()->getLoadBalancerType($id);
    }
}
