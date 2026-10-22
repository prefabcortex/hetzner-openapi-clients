<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PrimaryIps;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreatePrimaryIpClientErrorException;
use Prefabcortex\Hetzner\Exception\CreatePrimaryIpServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreatePrimaryIpBody;
use Prefabcortex\Hetzner\Model\CreatePrimaryIpResponse201;
use Prefabcortex\Hetzner\Model\IpType;

final class CreatePrimaryIpExample
{
    /**
     * Create a new [Primary IP](#tag/primary-ips).
     *
     * Can optionally be assigned to a resource by providing an `assignee_id` and `assignee_type`.
     *
     * If not assigned to a resource the `location` key needs to be provided. This can be either the
     * ID or the name of the [Location](#tag/locations) this [Primary IP](#tag/primary-ips) shall be
     * created in.
     *
     * A [Primary IP](#tag/primary-ips) can only be assigned to resource in the same
     * [Location](#tag/locations) later on.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `server_not_stopped` | The specified [Server](#tag/servers) is running, but needs to be powered off |
     * | `422` | `server_has_ipv4` | The [Server](#tag/servers) already has an ipv4 address |
     * | `422` | `server_has_ipv6` | The [Server](#tag/servers) already has an ipv6 address |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreatePrimaryIpExample::createPrimaryIp($client, CreatePrimaryIpExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreatePrimaryIpClientErrorException
     * @throws CreatePrimaryIpServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createPrimaryIp(
        Client $client,
        CreatePrimaryIpBody $requestBody,
    ): CreatePrimaryIpResponse201 {
        return $client->primaryIps()->createPrimaryIp($requestBody);
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildExampleRequestBody(): CreatePrimaryIpBody
    {
        return CreatePrimaryIpBody::builder(
            // name
            'my-resource',
            // type
            IpType::ipv4,
        )
            ->setAssigneeId(17)
            ->setAutoDelete(false)
            ->build();
    }
}
