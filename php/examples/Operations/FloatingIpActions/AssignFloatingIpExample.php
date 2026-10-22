<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FloatingIpActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\AssignFloatingIpClientErrorException;
use Prefabcortex\Hetzner\Exception\AssignFloatingIpServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\AssignFloatingIpBody;

final class AssignFloatingIpExample
{
    /**
     * Assigns a [Floating IP](#tag/floating-ips) to a [Server](#tag/servers).
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `floating_ip_assigned` | The [Floating IP](#tag/floating-ips) is already assigned |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   AssignFloatingIpExample::assignFloatingIp($client, $id, AssignFloatingIpExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws AssignFloatingIpClientErrorException
     * @throws AssignFloatingIpServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function assignFloatingIp(
        Client $client,
        int $id,
        AssignFloatingIpBody $requestBody,
    ): ActionResponse {
        return $client->floatingIpActions()->assignFloatingIp(
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
    public static function buildExampleRequestBody(): AssignFloatingIpBody
    {
        return AssignFloatingIpBody::builder(42)->build();
    }
}
