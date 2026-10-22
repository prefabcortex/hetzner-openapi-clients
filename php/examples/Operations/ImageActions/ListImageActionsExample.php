<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ImageActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListImageActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListImageActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListImageActionsQueryParameters;

final class ListImageActionsExample
{
    /**
     * Returns all Action objects for an Image. You can sort the results by using the `sort` URI
     * parameter, and filter them with the `status` parameter.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListImageActionsQueryParameters();
     *   ListImageActionsExample::listImageActions($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListImageActionsClientErrorException
     * @throws ListImageActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listImageActions(
        Client $client,
        int $id,
        ListImageActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->imageActions()->listImageActions(
            $id,
            $queryParameters,
        );
    }
}
