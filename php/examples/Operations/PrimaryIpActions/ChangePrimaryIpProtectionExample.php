<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PrimaryIpActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ChangePrimaryIpProtectionClientErrorException;
use Prefabcortex\Hetzner\Exception\ChangePrimaryIpProtectionServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ChangePrimaryIpProtectionBody;

final class ChangePrimaryIpProtectionExample
{
    /**
     * Changes the protection configuration of a [Primary IP](#tag/primary-ips).
     *
     * A [Primary IPs](#tag/primary-ips) deletion protection can only be enabled if its
     * `auto_delete` property is set to `false`.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ChangePrimaryIpProtectionExample::changePrimaryIpProtection($client, $id, ChangePrimaryIpProtectionExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ChangePrimaryIpProtectionClientErrorException
     * @throws ChangePrimaryIpProtectionServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function changePrimaryIpProtection(
        Client $client,
        int $id,
        ChangePrimaryIpProtectionBody $requestBody,
    ): ActionResponse {
        return $client->primaryIpActions()->changePrimaryIpProtection(
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
    public static function buildExampleRequestBody(): ChangePrimaryIpProtectionBody
    {
        return ChangePrimaryIpProtectionBody::builder(false)->build();
    }
}
