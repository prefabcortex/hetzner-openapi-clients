<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PrimaryIpActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ChangePrimaryIpDnsPtrClientErrorException;
use Prefabcortex\Hetzner\Exception\ChangePrimaryIpDnsPtrServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ChangePrimaryIpDnsPtrBody;

final class ChangePrimaryIpDnsPtrExample
{
    /**
     * Change the reverse DNS records for this [Primary IP](#tag/primary-ips).
     *
     * Allows to modify the PTR records set for the IP address.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ChangePrimaryIpDnsPtrExample::changePrimaryIpDnsPtr($client, $id, ChangePrimaryIpDnsPtrExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ChangePrimaryIpDnsPtrClientErrorException
     * @throws ChangePrimaryIpDnsPtrServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function changePrimaryIpDnsPtr(
        Client $client,
        int $id,
        ChangePrimaryIpDnsPtrBody $requestBody,
    ): ActionResponse {
        return $client->primaryIpActions()->changePrimaryIpDnsPtr(
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
    public static function buildExampleRequestBody(): ChangePrimaryIpDnsPtrBody
    {
        return ChangePrimaryIpDnsPtrBody::builder(
            // ip
            '2001:db8::1',
            // dnsPtr
            'server.example.com',
        )->build();
    }
}
