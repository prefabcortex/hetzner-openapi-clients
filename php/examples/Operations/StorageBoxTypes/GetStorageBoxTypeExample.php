<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxTypes;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetStorageBoxTypeClientErrorException;
use Prefabcortex\Hetzner\Exception\GetStorageBoxTypeServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\GetStorageBoxTypeResponse200;

final class GetStorageBoxTypeExample
{
    /**
     * Returns a specific [Storage Box Type](#tag/storage-box-types).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetStorageBoxTypeExample::getStorageBoxType($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetStorageBoxTypeClientErrorException
     * @throws GetStorageBoxTypeServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getStorageBoxType(
        Client $client,
        int $id,
    ): GetStorageBoxTypeResponse200 {
        return $client->storageBoxTypes()->getStorageBoxType($id);
    }
}
