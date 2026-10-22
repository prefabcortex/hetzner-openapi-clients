<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxSubaccounts;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreateStorageBoxSubaccountClientErrorException;
use Prefabcortex\Hetzner\Exception\CreateStorageBoxSubaccountServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreateStorageBoxSubaccountBody;
use Prefabcortex\Hetzner\Model\CreateStorageBoxSubaccountResponse201;

final class CreateStorageBoxSubaccountExample
{
    /**
     * Creates a [Storage Box Subaccount](#tag/storage-box-subaccounts).
     *
     * A [Storage Box Subaccount](#tag/storage-box-subaccounts) will use a separate home directory.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreateStorageBoxSubaccountExample::createStorageBoxSubaccount($client, $id, CreateStorageBoxSubaccountExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreateStorageBoxSubaccountClientErrorException
     * @throws CreateStorageBoxSubaccountServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createStorageBoxSubaccount(
        Client $client,
        int $id,
        CreateStorageBoxSubaccountBody $requestBody,
    ): CreateStorageBoxSubaccountResponse201 {
        return $client->storageBoxSubaccounts()->createStorageBoxSubaccount(
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
    public static function buildExampleRequestBody(): CreateStorageBoxSubaccountBody
    {
        return CreateStorageBoxSubaccountBody::builder(
            // homeDirectory
            'my-backup/server01',
            // password
            'REPLACE_ME',
        )
            ->setName('my-name')
            ->setDescription('my-backup-server01')
            ->build();
    }
}
