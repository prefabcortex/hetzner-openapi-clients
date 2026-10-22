<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FloatingIpActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListFloatingIpsActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListFloatingIpsActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListFloatingIpsActionsQueryParameters;

final class ListFloatingIpsActionsExample
{
    /**
     * Lists multiple [Actions](#tag/actions).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListFloatingIpsActionsQueryParameters();
     *   ListFloatingIpsActionsExample::listFloatingIpsActions($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListFloatingIpsActionsClientErrorException
     * @throws ListFloatingIpsActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listFloatingIpsActions(
        Client $client,
        ListFloatingIpsActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->floatingIpActions()->listFloatingIpsActions($queryParameters);
    }
}
