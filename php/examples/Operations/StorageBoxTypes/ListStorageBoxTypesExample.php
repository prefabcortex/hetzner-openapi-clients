<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxTypes;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListStorageBoxTypesClientErrorException;
use Prefabcortex\Hetzner\Exception\ListStorageBoxTypesServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListStorageBoxTypesResponse200;
use Prefabcortex\Hetzner\Parameter\ListStorageBoxTypesQueryParameters;

final class ListStorageBoxTypesExample
{
    /**
     * Returns a paginated list of [Storage Box Types](#tag/storage-box-types).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListStorageBoxTypesQueryParameters();
     *   ListStorageBoxTypesExample::listStorageBoxTypes($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListStorageBoxTypesClientErrorException
     * @throws ListStorageBoxTypesServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listStorageBoxTypes(
        Client $client,
        ListStorageBoxTypesQueryParameters $queryParameters,
    ): ListStorageBoxTypesResponse200 {
        return $client->storageBoxTypes()->listStorageBoxTypes($queryParameters);
    }
}
