<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxes;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListStorageBoxesClientErrorException;
use Prefabcortex\Hetzner\Exception\ListStorageBoxesServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListStorageBoxesResponse200;
use Prefabcortex\Hetzner\Parameter\ListStorageBoxesQueryParameters;

final class ListStorageBoxesExample
{
    /**
     * Returns a paginated list of [Storage Boxes](#tag/storage-boxes).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListStorageBoxesQueryParameters();
     *   ListStorageBoxesExample::listStorageBoxes($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListStorageBoxesClientErrorException
     * @throws ListStorageBoxesServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listStorageBoxes(
        Client $client,
        ListStorageBoxesQueryParameters $queryParameters,
    ): ListStorageBoxesResponse200 {
        return $client->storageBoxes()->listStorageBoxes($queryParameters);
    }
}
