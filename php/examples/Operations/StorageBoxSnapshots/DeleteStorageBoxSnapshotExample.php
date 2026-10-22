<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxSnapshots;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DeleteStorageBoxSnapshotClientErrorException;
use Prefabcortex\Hetzner\Exception\DeleteStorageBoxSnapshotServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class DeleteStorageBoxSnapshotExample
{
    /**
     * Deletes a [Storage Box Snapshot](#tag/storage-box-snapshots).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DeleteStorageBoxSnapshotExample::deleteStorageBoxSnapshot($client, $id, $snapshotId);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DeleteStorageBoxSnapshotClientErrorException
     * @throws DeleteStorageBoxSnapshotServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function deleteStorageBoxSnapshot(
        Client $client,
        int $id,
        int $snapshotId,
    ): ActionResponse {
        return $client->storageBoxSnapshots()->deleteStorageBoxSnapshot(
            $id,
            $snapshotId,
        );
    }
}
