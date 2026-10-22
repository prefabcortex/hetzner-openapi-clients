<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\VolumeActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetVolumeActionClientErrorException;
use Prefabcortex\Hetzner\Exception\GetVolumeActionServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class GetVolumeActionExample
{
    /**
     * Deprecated**: This operation is deprecated, see our
     * [changelog](https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
     * for more details.
     *
     * Returns a specific Action for a Volume.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetVolumeActionExample::getVolumeAction($client, $id, $actionId);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetVolumeActionClientErrorException
     * @throws GetVolumeActionServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getVolumeAction(
        Client $client,
        int $id,
        int $actionId,
    ): ActionResponse {
        return $client->volumeActions()->getVolumeAction(
            $id,
            $actionId,
        );
    }
}
