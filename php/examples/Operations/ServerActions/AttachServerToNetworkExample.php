<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\AttachServerToNetworkClientErrorException;
use Prefabcortex\Hetzner\Exception\AttachServerToNetworkServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\AttachServerToNetworkBody;

final class AttachServerToNetworkExample
{
    /**
     * Attaches a Server to a network. This will complement the fixed public Server interface by
     * adding an additional ethernet interface to the Server which is connected to the specified
     * network.
     *
     * The Server will get an IP auto assigned from a subnet of type `server` in the same
     * `network_zone`.
     *
     * Using the `alias_ips` attribute you can also define one or more additional IPs to the
     * Servers. Please note that you will have to configure these IPs by hand on your Server since
     * only the primary IP will be given out by DHCP.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `server_already_attached` | The server is already attached to the network |
     * | `422` | `ip_not_available` | The provided Network IP is not available |
     * | `422` | `no_subnet_available` | No Subnet or IP is available for the Server within the network |
     * | `422` | `networks_overlap` | The network IP range overlaps with one of the server networks |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   AttachServerToNetworkExample::attachServerToNetwork($client, $id, AttachServerToNetworkExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws AttachServerToNetworkClientErrorException
     * @throws AttachServerToNetworkServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function attachServerToNetwork(
        Client $client,
        int $id,
        AttachServerToNetworkBody $requestBody,
    ): ActionResponse {
        return $client->serverActions()->attachServerToNetwork(
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
    public static function buildExampleRequestBody(): AttachServerToNetworkBody
    {
        return AttachServerToNetworkBody::builder(4711)
            ->setIp('10.0.1.1')
            ->setAliasIps(['10.0.1.2'])
            ->setIpRange('10.0.1.0/24')
            ->build();
    }
}
