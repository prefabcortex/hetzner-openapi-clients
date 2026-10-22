<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ChangeStorageBoxProtectionClientErrorException;
use Prefabcortex\Hetzner\Exception\ChangeStorageBoxProtectionServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ChangeDeleteProtectionRequest;

final class ChangeStorageBoxProtectionExample
{
    /**
     * Changes the protection configuration of a [Storage Box](#tag/storage-boxes).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ChangeStorageBoxProtectionExample::changeStorageBoxProtection($client, $id, ChangeStorageBoxProtectionExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ChangeStorageBoxProtectionClientErrorException
     * @throws ChangeStorageBoxProtectionServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function changeStorageBoxProtection(
        Client $client,
        int $id,
        ChangeDeleteProtectionRequest $requestBody,
    ): ActionResponse {
        return $client->storageBoxActions()->changeStorageBoxProtection(
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
    public static function buildExampleRequestBody(): ChangeDeleteProtectionRequest
    {
        return ChangeDeleteProtectionRequest::builder()
            ->setDelete(true)
            ->build();
    }
}
