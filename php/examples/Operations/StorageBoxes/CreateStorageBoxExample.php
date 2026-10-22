<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxes;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreateStorageBoxClientErrorException;
use Prefabcortex\Hetzner\Exception\CreateStorageBoxServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreateStorageBoxBody;
use Prefabcortex\Hetzner\Model\CreateStorageBoxResponse201;

final class CreateStorageBoxExample
{
    /**
     * Creates a [Storage Box](#tag/storage-boxes).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreateStorageBoxExample::createStorageBox($client, CreateStorageBoxExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreateStorageBoxClientErrorException
     * @throws CreateStorageBoxServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createStorageBox(
        Client $client,
        CreateStorageBoxBody $requestBody,
    ): CreateStorageBoxResponse201 {
        return $client->storageBoxes()->createStorageBox($requestBody);
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildExampleRequestBody(): CreateStorageBoxBody
    {
        return CreateStorageBoxBody::builder(
            // name
            'REPLACE_ME',
            // location
            'fsn1',
            // storageBoxType
            'bx20',
            // password
            'REPLACE_ME',
        )->build();
    }
}
