<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ImageActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListImagesActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListImagesActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListImagesActionsQueryParameters;

final class ListImagesActionsExample
{
    /**
     * Returns all Action objects. You can `sort` the results by using the sort URI parameter, and
     * filter them with the `status` and `id` parameter.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListImagesActionsQueryParameters();
     *   ListImagesActionsExample::listImagesActions($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListImagesActionsClientErrorException
     * @throws ListImagesActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listImagesActions(
        Client $client,
        ListImagesActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->imageActions()->listImagesActions($queryParameters);
    }
}
