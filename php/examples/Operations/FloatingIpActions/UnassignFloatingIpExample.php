<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FloatingIpActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnassignFloatingIpClientErrorException;
use Prefabcortex\Hetzner\Exception\UnassignFloatingIpServerErrorException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class UnassignFloatingIpExample
{
    /**
     * Unassigns a [Floating IP](#tag/floating-ips).
     *
     * Results in the IP being unreachable. Can be assigned to another resource again.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UnassignFloatingIpExample::unassignFloatingIp($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UnassignFloatingIpClientErrorException
     * @throws UnassignFloatingIpServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function unassignFloatingIp(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->floatingIpActions()->unassignFloatingIp($id);
    }
}
