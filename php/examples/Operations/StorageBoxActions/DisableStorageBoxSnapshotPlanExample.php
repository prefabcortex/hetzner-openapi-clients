<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DisableStorageBoxSnapshotPlanClientErrorException;
use Prefabcortex\Hetzner\Exception\DisableStorageBoxSnapshotPlanServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class DisableStorageBoxSnapshotPlanExample
{
    /**
     * Disables the active Snapshot Plan of a [Storage Box](#tag/storage-boxes).
     *
     * Existing [Storage Box Snapshots](#tag/storage-box-snapshots) created by the Snapshot Plan
     * will not be delete, they must be removed manually.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DisableStorageBoxSnapshotPlanExample::disableStorageBoxSnapshotPlan($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DisableStorageBoxSnapshotPlanClientErrorException
     * @throws DisableStorageBoxSnapshotPlanServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function disableStorageBoxSnapshotPlan(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->storageBoxActions()->disableStorageBoxSnapshotPlan($id);
    }
}
