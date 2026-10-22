<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\VolumeActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListVolumesActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListVolumesActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListVolumesActionsQueryParameters;

final class ListVolumesActionsExample
{
    /**
     * Returns all Action objects. You can `sort` the results by using the sort URI parameter, and
     * filter them with the `status` and `id` parameter.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListVolumesActionsQueryParameters();
     *   ListVolumesActionsExample::listVolumesActions($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListVolumesActionsClientErrorException
     * @throws ListVolumesActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listVolumesActions(
        Client $client,
        ListVolumesActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->volumeActions()->listVolumesActions($queryParameters);
    }
}
