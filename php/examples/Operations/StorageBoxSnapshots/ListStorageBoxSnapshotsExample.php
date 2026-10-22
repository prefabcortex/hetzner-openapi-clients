<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxSnapshots;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListStorageBoxSnapshotsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListStorageBoxSnapshotsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListStorageBoxSnapshotsResponse200;
use Prefabcortex\Hetzner\Parameter\ListStorageBoxSnapshotsQueryParameters;

final class ListStorageBoxSnapshotsExample
{
    /**
     * Returns a list of [Storage Box Snapshot](#tag/storage-box-snapshots).
     *
     * Both snapshots created manually and by the snapshot plan are returned.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListStorageBoxSnapshotsQueryParameters();
     *   ListStorageBoxSnapshotsExample::listStorageBoxSnapshots($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListStorageBoxSnapshotsClientErrorException
     * @throws ListStorageBoxSnapshotsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listStorageBoxSnapshots(
        Client $client,
        int $id,
        ListStorageBoxSnapshotsQueryParameters $queryParameters,
    ): ListStorageBoxSnapshotsResponse200 {
        return $client->storageBoxSnapshots()->listStorageBoxSnapshots(
            $id,
            $queryParameters,
        );
    }
}
