<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetLoadBalancersActionClientErrorException;
use Prefabcortex\Hetzner\Exception\GetLoadBalancersActionServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class GetLoadBalancersActionExample
{
    /**
     * Returns a specific Action object.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetLoadBalancersActionExample::getLoadBalancersAction($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetLoadBalancersActionClientErrorException
     * @throws GetLoadBalancersActionServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getLoadBalancersAction(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->loadBalancerActions()->getLoadBalancersAction($id);
    }
}
