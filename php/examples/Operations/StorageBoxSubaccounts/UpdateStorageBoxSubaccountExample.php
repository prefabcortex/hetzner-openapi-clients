<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxSubaccounts;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateStorageBoxSubaccountClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateStorageBoxSubaccountServerErrorException;
use Prefabcortex\Hetzner\Model\SubaccountResponse;
use Prefabcortex\Hetzner\Model\UpdateStorageBoxSubaccountBody;

final class UpdateStorageBoxSubaccountExample
{
    /**
     * Updates a [Storage Box Subaccount](#tag/storage-box-subaccounts).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateStorageBoxSubaccountExample::updateStorageBoxSubaccount($client, $id, $subaccountId, UpdateStorageBoxSubaccountExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateStorageBoxSubaccountClientErrorException
     * @throws UpdateStorageBoxSubaccountServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateStorageBoxSubaccount(
        Client $client,
        int $id,
        int $subaccountId,
        UpdateStorageBoxSubaccountBody $requestBody,
    ): SubaccountResponse {
        return $client->storageBoxSubaccounts()->updateStorageBoxSubaccount(
            $id,
            $subaccountId,
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
    public static function buildExampleRequestBody(): UpdateStorageBoxSubaccountBody
    {
        return UpdateStorageBoxSubaccountBody::builder()
            ->setName('my-name')
            ->setDescription('my-backup-server01')
            ->build();
    }
}
