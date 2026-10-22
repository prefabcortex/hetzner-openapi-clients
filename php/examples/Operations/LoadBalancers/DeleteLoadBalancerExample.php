<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancers;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DeleteLoadBalancerClientErrorException;
use Prefabcortex\Hetzner\Exception\DeleteLoadBalancerServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class DeleteLoadBalancerExample
{
    /**
     * Deletes a Load Balancer.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DeleteLoadBalancerExample::deleteLoadBalancer($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DeleteLoadBalancerClientErrorException
     * @throws DeleteLoadBalancerServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function deleteLoadBalancer(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->loadBalancers()->deleteLoadBalancer($id);
    }
}
