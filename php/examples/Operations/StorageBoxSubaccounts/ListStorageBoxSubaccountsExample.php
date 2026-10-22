<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxSubaccounts;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListStorageBoxSubaccountsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListStorageBoxSubaccountsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListStorageBoxSubaccountsResponse200;
use Prefabcortex\Hetzner\Parameter\ListStorageBoxSubaccountsQueryParameters;

final class ListStorageBoxSubaccountsExample
{
    /**
     * Returns a list of [Storage Box Subaccount](#tag/storage-box-subaccounts).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListStorageBoxSubaccountsQueryParameters();
     *   ListStorageBoxSubaccountsExample::listStorageBoxSubaccounts($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListStorageBoxSubaccountsClientErrorException
     * @throws ListStorageBoxSubaccountsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listStorageBoxSubaccounts(
        Client $client,
        int $id,
        ListStorageBoxSubaccountsQueryParameters $queryParameters,
    ): ListStorageBoxSubaccountsResponse200 {
        return $client->storageBoxSubaccounts()->listStorageBoxSubaccounts(
            $id,
            $queryParameters,
        );
    }
}
