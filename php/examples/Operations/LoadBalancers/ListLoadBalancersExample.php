<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancers;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListLoadBalancersClientErrorException;
use Prefabcortex\Hetzner\Exception\ListLoadBalancersServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListLoadBalancersResponse200;
use Prefabcortex\Hetzner\Parameter\ListLoadBalancersQueryParameters;

final class ListLoadBalancersExample
{
    /**
     * Gets all existing Load Balancers that you have available.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListLoadBalancersQueryParameters();
     *   ListLoadBalancersExample::listLoadBalancers($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListLoadBalancersClientErrorException
     * @throws ListLoadBalancersServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listLoadBalancers(
        Client $client,
        ListLoadBalancersQueryParameters $queryParameters,
    ): ListLoadBalancersResponse200 {
        return $client->loadBalancers()->listLoadBalancers($queryParameters);
    }
}
