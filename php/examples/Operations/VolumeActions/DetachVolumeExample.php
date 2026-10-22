<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\VolumeActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DetachVolumeClientErrorException;
use Prefabcortex\Hetzner\Exception\DetachVolumeServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class DetachVolumeExample
{
    /**
     * Detaches a Volume from the Server it’s attached to. You may attach it to a Server again at a
     * later time.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DetachVolumeExample::detachVolume($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DetachVolumeClientErrorException
     * @throws DetachVolumeServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function detachVolume(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->volumeActions()->detachVolume($id);
    }
}
