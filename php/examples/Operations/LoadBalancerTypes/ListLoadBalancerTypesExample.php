<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerTypes;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListLoadBalancerTypesClientErrorException;
use Prefabcortex\Hetzner\Exception\ListLoadBalancerTypesServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListLoadBalancerTypesResponse200;
use Prefabcortex\Hetzner\Parameter\ListLoadBalancerTypesQueryParameters;

final class ListLoadBalancerTypesExample
{
    /**
     * Gets all Load Balancer type objects.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListLoadBalancerTypesQueryParameters();
     *   ListLoadBalancerTypesExample::listLoadBalancerTypes($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListLoadBalancerTypesClientErrorException
     * @throws ListLoadBalancerTypesServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listLoadBalancerTypes(
        Client $client,
        ListLoadBalancerTypesQueryParameters $queryParameters,
    ): ListLoadBalancerTypesResponse200 {
        return $client->loadBalancerTypes()->listLoadBalancerTypes($queryParameters);
    }
}
