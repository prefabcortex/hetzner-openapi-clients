<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\NetworkActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListNetworksActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListNetworksActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListNetworksActionsQueryParameters;

final class ListNetworksActionsExample
{
    /**
     * Lists multiple [Actions](#tag/actions).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListNetworksActionsQueryParameters();
     *   ListNetworksActionsExample::listNetworksActions($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListNetworksActionsClientErrorException
     * @throws ListNetworksActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listNetworksActions(
        Client $client,
        ListNetworksActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->networkActions()->listNetworksActions($queryParameters);
    }
}
