<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PrimaryIpActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListPrimaryIpActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListPrimaryIpActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListPrimaryIpActionsQueryParameters;

final class ListPrimaryIpActionsExample
{
    /**
     * Returns all [Actions](#tag/actions) for a [Primary IP](#tag/primary-ips).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListPrimaryIpActionsQueryParameters();
     *   ListPrimaryIpActionsExample::listPrimaryIpActions($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListPrimaryIpActionsClientErrorException
     * @throws ListPrimaryIpActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listPrimaryIpActions(
        Client $client,
        int $id,
        ListPrimaryIpActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->primaryIpActions()->listPrimaryIpActions(
            $id,
            $queryParameters,
        );
    }
}
