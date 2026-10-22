<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ChangeStorageBoxTypeClientErrorException;
use Prefabcortex\Hetzner\Exception\ChangeStorageBoxTypeServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ChangeStorageBoxTypeBody;

final class ChangeStorageBoxTypeExample
{
    /**
     * Changes the type of a [Storage Box](#tag/storage-boxes).
     *
     * Upgrades or downgrades a [Storage Box](#tag/storage-boxes) to another [Storage Box
     * Type](#tag/storage-box-types).
     *
     * It is not possible to downgrade to a [Storage Box Type](#tag/storage-box-types) that offers
     * less disk space than you are currently using.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ChangeStorageBoxTypeExample::changeStorageBoxType($client, $id, ChangeStorageBoxTypeExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ChangeStorageBoxTypeClientErrorException
     * @throws ChangeStorageBoxTypeServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function changeStorageBoxType(
        Client $client,
        int $id,
        ChangeStorageBoxTypeBody $requestBody,
    ): ActionResponse {
        return $client->storageBoxActions()->changeStorageBoxType(
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
    public static function buildExampleRequestBody(): ChangeStorageBoxTypeBody
    {
        return ChangeStorageBoxTypeBody::builder('bx20')->build();
    }
}
