<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PrimaryIpActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListPrimaryIpsActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListPrimaryIpsActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListPrimaryIpsActionsQueryParameters;

final class ListPrimaryIpsActionsExample
{
    /**
     * Lists multiple [Actions](#tag/actions).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListPrimaryIpsActionsQueryParameters();
     *   ListPrimaryIpsActionsExample::listPrimaryIpsActions($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListPrimaryIpsActionsClientErrorException
     * @throws ListPrimaryIpsActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listPrimaryIpsActions(
        Client $client,
        ListPrimaryIpsActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->primaryIpActions()->listPrimaryIpsActions($queryParameters);
    }
}
