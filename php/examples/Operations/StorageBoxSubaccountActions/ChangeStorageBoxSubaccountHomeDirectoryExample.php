<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxSubaccountActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ChangeStorageBoxSubaccountHomeDirectoryClientErrorException;
use Prefabcortex\Hetzner\Exception\ChangeStorageBoxSubaccountHomeDirectoryServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ChangeStorageBoxSubaccountHomeDirectoryBody;

final class ChangeStorageBoxSubaccountHomeDirectoryExample
{
    /**
     * Change the home directory of a [Storage Box Subaccount](#tag/storage-box-subaccounts).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ChangeStorageBoxSubaccountHomeDirectoryExample::changeStorageBoxSubaccountHomeDirectory($client, $id, $subaccountId, ChangeStorageBoxSubaccountHomeDirectoryExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ChangeStorageBoxSubaccountHomeDirectoryClientErrorException
     * @throws ChangeStorageBoxSubaccountHomeDirectoryServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function changeStorageBoxSubaccountHomeDirectory(
        Client $client,
        int $id,
        int $subaccountId,
        ChangeStorageBoxSubaccountHomeDirectoryBody $requestBody,
    ): ActionResponse {
        return $client->storageBoxSubaccountActions()->changeStorageBoxSubaccountHomeDirectory(
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
    public static function buildExampleRequestBody(): ChangeStorageBoxSubaccountHomeDirectoryBody
    {
        return ChangeStorageBoxSubaccountHomeDirectoryBody::builder('my-backup/server01')->build();
    }
}
