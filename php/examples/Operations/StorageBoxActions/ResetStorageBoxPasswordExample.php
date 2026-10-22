<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResetStorageBoxPasswordClientErrorException;
use Prefabcortex\Hetzner\Exception\ResetStorageBoxPasswordServerErrorException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ResetPasswordRequest;

final class ResetStorageBoxPasswordExample
{
    /**
     * Reset the password of a [Storage Box](#tag/storage-boxes).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ResetStorageBoxPasswordExample::resetStorageBoxPassword($client, $id, ResetStorageBoxPasswordExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ResetStorageBoxPasswordClientErrorException
     * @throws ResetStorageBoxPasswordServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function resetStorageBoxPassword(
        Client $client,
        int $id,
        ResetPasswordRequest $requestBody,
    ): ActionResponse {
        return $client->storageBoxActions()->resetStorageBoxPassword(
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
    public static function buildExampleRequestBody(): ResetPasswordRequest
    {
        return ResetPasswordRequest::builder('REPLACE_ME')->build();
    }
}
