<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListServerActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListServerActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListServerActionsQueryParameters;

final class ListServerActionsExample
{
    /**
     * Returns all Action objects for a Server. You can `sort` the results by using the sort URI
     * parameter, and filter them with the `status` parameter.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListServerActionsQueryParameters();
     *   ListServerActionsExample::listServerActions($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListServerActionsClientErrorException
     * @throws ListServerActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listServerActions(
        Client $client,
        int $id,
        ListServerActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->serverActions()->listServerActions(
            $id,
            $queryParameters,
        );
    }
}
