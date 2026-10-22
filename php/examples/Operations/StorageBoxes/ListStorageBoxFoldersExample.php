<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxes;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListStorageBoxFoldersClientErrorException;
use Prefabcortex\Hetzner\Exception\ListStorageBoxFoldersServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListStorageBoxFoldersResponse200;
use Prefabcortex\Hetzner\Parameter\ListStorageBoxFoldersQueryParameters;

final class ListStorageBoxFoldersExample
{
    /**
     * Returns a list of (sub)folders in a [Storage Box](#tag/storage-boxes).
     *
     * The folder location is specified by the `path` query parameter.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListStorageBoxFoldersQueryParameters();
     *   ListStorageBoxFoldersExample::listStorageBoxFolders($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListStorageBoxFoldersClientErrorException
     * @throws ListStorageBoxFoldersServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listStorageBoxFolders(
        Client $client,
        int $id,
        ListStorageBoxFoldersQueryParameters $queryParameters,
    ): ListStorageBoxFoldersResponse200 {
        return $client->storageBoxes()->listStorageBoxFolders(
            $id,
            $queryParameters,
        );
    }
}
