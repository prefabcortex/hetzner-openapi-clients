<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxSubaccounts;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetStorageBoxSubaccountClientErrorException;
use Prefabcortex\Hetzner\Exception\GetStorageBoxSubaccountServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\SubaccountResponse;

final class GetStorageBoxSubaccountExample
{
    /**
     * Returns a specific [Storage Box Subaccount](#tag/storage-box-subaccounts).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetStorageBoxSubaccountExample::getStorageBoxSubaccount($client, $id, $subaccountId);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetStorageBoxSubaccountClientErrorException
     * @throws GetStorageBoxSubaccountServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getStorageBoxSubaccount(
        Client $client,
        int $id,
        int $subaccountId,
    ): SubaccountResponse {
        return $client->storageBoxSubaccounts()->getStorageBoxSubaccount(
            $id,
            $subaccountId,
        );
    }
}
