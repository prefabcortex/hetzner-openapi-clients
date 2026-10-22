<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxSubaccountActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateStorageBoxSubaccountAccessSettingsClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateStorageBoxSubaccountAccessSettingsServerErrorException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\UpdateStorageBoxSubaccountAccessSettingsBody;

final class UpdateStorageBoxSubaccountAccessSettingsExample
{
    /**
     * Updates the access settings of a [Storage Box Subaccount](#tag/storage-box-subaccounts).
     *
     * This endpoints supports partial updates. Omitted optional parameters do not result in any
     * changes to the respective properties.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateStorageBoxSubaccountAccessSettingsExample::updateStorageBoxSubaccountAccessSettings($client, $id, $subaccountId, UpdateStorageBoxSubaccountAccessSettingsExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateStorageBoxSubaccountAccessSettingsClientErrorException
     * @throws UpdateStorageBoxSubaccountAccessSettingsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateStorageBoxSubaccountAccessSettings(
        Client $client,
        int $id,
        int $subaccountId,
        UpdateStorageBoxSubaccountAccessSettingsBody $requestBody,
    ): ActionResponse {
        return $client->storageBoxSubaccountActions()->updateStorageBoxSubaccountAccessSettings(
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
    public static function buildExampleRequestBody(): UpdateStorageBoxSubaccountAccessSettingsBody
    {
        return UpdateStorageBoxSubaccountAccessSettingsBody::builder()->build();
    }
}
