<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxSnapshots;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateStorageBoxSnapshotClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateStorageBoxSnapshotServerErrorException;
use Prefabcortex\Hetzner\Model\SnapshotResponse;
use Prefabcortex\Hetzner\Model\UpdateStorageBoxSnapshotBody;

final class UpdateStorageBoxSnapshotExample
{
    /**
     * Updates a [Storage Box Snapshot](#tag/storage-box-snapshots).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateStorageBoxSnapshotExample::updateStorageBoxSnapshot($client, $id, $snapshotId, UpdateStorageBoxSnapshotExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateStorageBoxSnapshotClientErrorException
     * @throws UpdateStorageBoxSnapshotServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateStorageBoxSnapshot(
        Client $client,
        int $id,
        int $snapshotId,
        UpdateStorageBoxSnapshotBody $requestBody,
    ): SnapshotResponse {
        return $client->storageBoxSnapshots()->updateStorageBoxSnapshot(
            $id,
            $snapshotId,
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
    public static function buildExampleRequestBody(): UpdateStorageBoxSnapshotBody
    {
        return UpdateStorageBoxSnapshotBody::builder()
            ->setDescription('snapshot-0001')
            ->build();
    }
}
