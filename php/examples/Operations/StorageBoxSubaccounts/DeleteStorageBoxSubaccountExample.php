<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxSubaccounts;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DeleteStorageBoxSubaccountClientErrorException;
use Prefabcortex\Hetzner\Exception\DeleteStorageBoxSubaccountServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class DeleteStorageBoxSubaccountExample
{
    /**
     * Deletes a [Storage Box Subaccount](#tag/storage-box-subaccounts).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DeleteStorageBoxSubaccountExample::deleteStorageBoxSubaccount($client, $id, $subaccountId);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DeleteStorageBoxSubaccountClientErrorException
     * @throws DeleteStorageBoxSubaccountServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function deleteStorageBoxSubaccount(
        Client $client,
        int $id,
        int $subaccountId,
    ): ActionResponse {
        return $client->storageBoxSubaccounts()->deleteStorageBoxSubaccount(
            $id,
            $subaccountId,
        );
    }
}
