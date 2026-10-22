<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PrimaryIpActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\AssignPrimaryIpClientErrorException;
use Prefabcortex\Hetzner\Exception\AssignPrimaryIpServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\AssignPrimaryIpBody;
use Prefabcortex\Hetzner\Model\AssignPrimaryIpBodyAssigneeType;

final class AssignPrimaryIpExample
{
    /**
     * Assign a [Primary IP](#tag/primary-ips) to a resource.
     *
     * A [Server](#tag/servers) can only have one [Primary IP](#tag/primary-ips) of type `ipv4` and
     * one of type `ipv6` assigned. If you need more IPs use [Floating IPs](#tag/floating-ips).
     *
     * A [Server](#tag/servers) must be powered off (status `off`) in order for this operation to
     * succeed.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `server_not_stopped` | The [Server](#tag/servers) is running, but needs to be powered off |
     * | `422` | `primary_ip_already_assigned` | [Primary IP](#tag/primary-ips) is already assigned to a different [Server](#tag/servers) |
     * | `422` | `server_has_ipv4` | The [Server](#tag/servers) already has an IPv4 address |
     * | `422` | `server_has_ipv6` | The [Server](#tag/servers) already has an IPv6 address |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   AssignPrimaryIpExample::assignPrimaryIp($client, $id, AssignPrimaryIpExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws AssignPrimaryIpClientErrorException
     * @throws AssignPrimaryIpServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function assignPrimaryIp(
        Client $client,
        int $id,
        AssignPrimaryIpBody $requestBody,
    ): ActionResponse {
        return $client->primaryIpActions()->assignPrimaryIp(
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
    public static function buildExampleRequestBody(): AssignPrimaryIpBody
    {
        return AssignPrimaryIpBody::builder(
            // assigneeType
            AssignPrimaryIpBodyAssigneeType::server,
            // assigneeId
            4711,
        )->build();
    }
}
