<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\NetworkActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListNetworkActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListNetworkActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListNetworkActionsQueryParameters;

final class ListNetworkActionsExample
{
    /**
     * Lists [Actions](#tag/actions) for a [Network](#tag/networks).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListNetworkActionsQueryParameters();
     *   ListNetworkActionsExample::listNetworkActions($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListNetworkActionsClientErrorException
     * @throws ListNetworkActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listNetworkActions(
        Client $client,
        int $id,
        ListNetworkActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->networkActions()->listNetworkActions(
            $id,
            $queryParameters,
        );
    }
}
