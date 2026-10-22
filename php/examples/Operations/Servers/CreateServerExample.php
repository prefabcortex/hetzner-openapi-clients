<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Servers;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreateServerClientErrorException;
use Prefabcortex\Hetzner\Exception\CreateServerServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreateServerBody;
use Prefabcortex\Hetzner\Model\CreateServerBodyFirewallsItem;
use Prefabcortex\Hetzner\Model\CreateServerResponse201;

final class CreateServerExample
{
    /**
     * Creates a new Server. Returns preliminary information about the Server as well as an Action
     * that covers progress of creation.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `412` | `primary_ip_version_mismatch` | The specified Primary IP has the wrong IP Version |
     * | `422` | `placement_error` | An error during the placement occurred |
     * | `422` | `primary_ip_assigned` | The specified Primary IP is already assigned to a server |
     * | `422` | `primary_ip_datacenter_mismatch` | The specified Primary IP is in a different location |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreateServerExample::createServer($client, CreateServerExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreateServerClientErrorException
     * @throws CreateServerServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createServer(
        Client $client,
        CreateServerBody $requestBody,
    ): CreateServerResponse201 {
        return $client->servers()->createServer($requestBody);
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildExampleRequestBody(): CreateServerBody
    {
        $createServerBodyFirewallsItem = CreateServerBodyFirewallsItem::builder(38)->build();

        return CreateServerBody::builder(
            // name
            'my-server',
            // serverType
            'cpx22',
            // image
            'ubuntu-24.04',
        )
            ->setStartAfterCreate(true)
            ->setPlacementGroup(1)
            ->setSshKeys(['my-ssh-key'])
            ->setVolumes([123])
            ->setNetworks([456])
            ->setFirewalls([$createServerBodyFirewallsItem])
            ->setUserData('#cloud-config
runcmd:
- [touch, /root/cloud-init-worked]
')
            ->setAutomount(false)
            ->build();
    }
}
