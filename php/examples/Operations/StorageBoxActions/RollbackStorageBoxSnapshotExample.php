<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\RollbackStorageBoxSnapshotClientErrorException;
use Prefabcortex\Hetzner\Exception\RollbackStorageBoxSnapshotServerErrorException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\RollbackStorageBoxSnapshotBody;

final class RollbackStorageBoxSnapshotExample
{
    /**
     * Rolls back a [Storage Box](#tag/storage-boxes) to the given [Storage Box
     * Snapshot](#tag/storage-box-snapshots).
     *
     * This will remove all newer [Storage Box Snapshot](#tag/storage-box-snapshots) and irrevocably
     * delete all data that was since written to the [Storage Box](#tag/storage-boxes).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   RollbackStorageBoxSnapshotExample::rollbackStorageBoxSnapshot($client, $id, RollbackStorageBoxSnapshotExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws RollbackStorageBoxSnapshotClientErrorException
     * @throws RollbackStorageBoxSnapshotServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function rollbackStorageBoxSnapshot(
        Client $client,
        int $id,
        RollbackStorageBoxSnapshotBody $requestBody,
    ): ActionResponse {
        return $client->storageBoxActions()->rollbackStorageBoxSnapshot(
            $id,
            $requestBody,
        );
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildExampleRequestBody(): RollbackStorageBoxSnapshotBody
    {
        return RollbackStorageBoxSnapshotBody::builder('my-snapshot')->build();
    }
}
