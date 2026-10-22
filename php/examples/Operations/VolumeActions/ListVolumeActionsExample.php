<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\VolumeActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListVolumeActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListVolumeActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListVolumeActionsQueryParameters;

final class ListVolumeActionsExample
{
    /**
     * Returns all Action objects for a Volume. You can `sort` the results by using the sort URI
     * parameter, and filter them with the `status` parameter.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListVolumeActionsQueryParameters();
     *   ListVolumeActionsExample::listVolumeActions($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListVolumeActionsClientErrorException
     * @throws ListVolumeActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listVolumeActions(
        Client $client,
        int $id,
        ListVolumeActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->volumeActions()->listVolumeActions(
            $id,
            $queryParameters,
        );
    }
}
