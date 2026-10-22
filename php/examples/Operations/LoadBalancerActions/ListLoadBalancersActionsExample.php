<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListLoadBalancersActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListLoadBalancersActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListLoadBalancersActionsQueryParameters;

final class ListLoadBalancersActionsExample
{
    /**
     * Returns all Action objects. You can `sort` the results by using the sort URI parameter, and
     * filter them with the `status` and `id` parameter.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListLoadBalancersActionsQueryParameters();
     *   ListLoadBalancersActionsExample::listLoadBalancersActions($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListLoadBalancersActionsClientErrorException
     * @throws ListLoadBalancersActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listLoadBalancersActions(
        Client $client,
        ListLoadBalancersActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->loadBalancerActions()->listLoadBalancersActions($queryParameters);
    }
}
