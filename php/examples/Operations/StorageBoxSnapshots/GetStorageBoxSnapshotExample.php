<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxSnapshots;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetStorageBoxSnapshotClientErrorException;
use Prefabcortex\Hetzner\Exception\GetStorageBoxSnapshotServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\SnapshotResponse;

final class GetStorageBoxSnapshotExample
{
    /**
     * Returns a specific [Storage Box Snapshot](#tag/storage-box-snapshots).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetStorageBoxSnapshotExample::getStorageBoxSnapshot($client, $id, $snapshotId);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetStorageBoxSnapshotClientErrorException
     * @throws GetStorageBoxSnapshotServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getStorageBoxSnapshot(
        Client $client,
        int $id,
        int $snapshotId,
    ): SnapshotResponse {
        return $client->storageBoxSnapshots()->getStorageBoxSnapshot(
            $id,
            $snapshotId,
        );
    }
}
