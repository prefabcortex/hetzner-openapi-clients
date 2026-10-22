<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Volumes;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DeleteVolumeClientErrorException;
use Prefabcortex\Hetzner\Exception\DeleteVolumeServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;

final class DeleteVolumeExample
{
    /**
     * Deletes a volume. All Volume data is irreversibly destroyed. The Volume must not be attached
     * to a Server and it must not have delete protection enabled.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DeleteVolumeExample::deleteVolume($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DeleteVolumeClientErrorException
     * @throws DeleteVolumeServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function deleteVolume(
        Client $client,
        int $id,
    ): null {
        return $client->volumes()->deleteVolume($id);
    }
}
