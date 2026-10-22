<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PrimaryIpActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnassignPrimaryIpClientErrorException;
use Prefabcortex\Hetzner\Exception\UnassignPrimaryIpServerErrorException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class UnassignPrimaryIpExample
{
    /**
     * Unassign a [Primary IP](#tag/primary-ips) from a resource.
     *
     * A [Server](#tag/servers) must be powered off (status `off`) in order for this operation to
     * succeed.
     *
     * A [Server](#tag/servers) requires at least one network interface (public or private) to be
     * powered on.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `server_not_stopped` | The [Server](#tag/servers) is running, but needs to be powered off |
     * | `422` | `server_is_load_balancer_target` | The [Server](#tag/servers) IPv4 address is a loadbalancer target |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UnassignPrimaryIpExample::unassignPrimaryIp($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UnassignPrimaryIpClientErrorException
     * @throws UnassignPrimaryIpServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function unassignPrimaryIp(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->primaryIpActions()->unassignPrimaryIp($id);
    }
}
