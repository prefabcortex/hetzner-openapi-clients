<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetStorageBoxActionClientErrorException;
use Prefabcortex\Hetzner\Exception\GetStorageBoxActionServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class GetStorageBoxActionExample
{
    /**
     * Deprecated**: This operation is deprecated, see our
     * [changelog](https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
     * for more details.
     *
     * Returns a specific Action object for a Storage Box.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetStorageBoxActionExample::getStorageBoxAction($client, $id, $actionId);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetStorageBoxActionClientErrorException
     * @throws GetStorageBoxActionServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getStorageBoxAction(
        Client $client,
        int $id,
        int $actionId,
    ): ActionResponse {
        return $client->storageBoxActions()->getStorageBoxAction(
            $id,
            $actionId,
        );
    }
}
