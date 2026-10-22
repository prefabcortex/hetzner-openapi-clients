<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxSnapshots;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreateStorageBoxSnapshotClientErrorException;
use Prefabcortex\Hetzner\Exception\CreateStorageBoxSnapshotServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreateStorageBoxSnapshotBody;
use Prefabcortex\Hetzner\Model\CreateStorageBoxSnapshotResponse201;

final class CreateStorageBoxSnapshotExample
{
    /**
     * Creates a [Storage Box Snapshot](#tag/storage-box-snapshots).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreateStorageBoxSnapshotExample::createStorageBoxSnapshot($client, $id, CreateStorageBoxSnapshotExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreateStorageBoxSnapshotClientErrorException
     * @throws CreateStorageBoxSnapshotServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createStorageBoxSnapshot(
        Client $client,
        int $id,
        CreateStorageBoxSnapshotBody $requestBody,
    ): CreateStorageBoxSnapshotResponse201 {
        return $client->storageBoxSnapshots()->createStorageBoxSnapshot(
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
    public static function buildExampleRequestBody(): CreateStorageBoxSnapshotBody
    {
        return CreateStorageBoxSnapshotBody::builder()
            ->setDescription('snapshot-0001')
            ->build();
    }
}
