<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateStorageBoxAccessSettingsClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateStorageBoxAccessSettingsServerErrorException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\UpdateStorageBoxAccessSettingsBody;

final class UpdateStorageBoxAccessSettingsExample
{
    /**
     * Update access settings of a primary [Storage Box](#tag/storage-boxes) account.
     *
     * This endpoints supports partial updates. Omitted optional parameters do not result in any
     * changes to the respective properties.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateStorageBoxAccessSettingsExample::updateStorageBoxAccessSettings($client, $id, UpdateStorageBoxAccessSettingsExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateStorageBoxAccessSettingsClientErrorException
     * @throws UpdateStorageBoxAccessSettingsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateStorageBoxAccessSettings(
        Client $client,
        int $id,
        UpdateStorageBoxAccessSettingsBody $requestBody,
    ): ActionResponse {
        return $client->storageBoxActions()->updateStorageBoxAccessSettings(
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
    public static function buildExampleRequestBody(): UpdateStorageBoxAccessSettingsBody
    {
        return UpdateStorageBoxAccessSettingsBody::builder()->build();
    }
}
