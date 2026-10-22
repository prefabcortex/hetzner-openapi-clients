<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxSubaccountActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResetStorageBoxSubaccountPasswordClientErrorException;
use Prefabcortex\Hetzner\Exception\ResetStorageBoxSubaccountPasswordServerErrorException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ResetPasswordRequest;

final class ResetStorageBoxSubaccountPasswordExample
{
    /**
     * Reset the password of a [Storage Box Subaccount](#tag/storage-box-subaccounts).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ResetStorageBoxSubaccountPasswordExample::resetStorageBoxSubaccountPassword($client, $id, $subaccountId, ResetStorageBoxSubaccountPasswordExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ResetStorageBoxSubaccountPasswordClientErrorException
     * @throws ResetStorageBoxSubaccountPasswordServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function resetStorageBoxSubaccountPassword(
        Client $client,
        int $id,
        int $subaccountId,
        ResetPasswordRequest $requestBody,
    ): ActionResponse {
        return $client->storageBoxSubaccountActions()->resetStorageBoxSubaccountPassword(
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
    public static function buildExampleRequestBody(): ResetPasswordRequest
    {
        return ResetPasswordRequest::builder('REPLACE_ME')->build();
    }
}
