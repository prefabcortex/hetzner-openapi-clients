<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FloatingIps;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DeleteFloatingIpClientErrorException;
use Prefabcortex\Hetzner\Exception\DeleteFloatingIpServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;

final class DeleteFloatingIpExample
{
    /**
     * Deletes a [Floating IP](#tag/floating-ips).
     *
     * If assigned to a [Server](#tag/servers) the [Floating IP](#tag/floating-ips) will be
     * unassigned automatically until 1 May 2026. After this date, the [Floating
     * IP](#tag/floating-ips) needs to be unassigned before it can be deleted.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `must_be_unassigned` | Error when IP is still assigned to a Resource. This error will appear as of 1 May 2026. |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DeleteFloatingIpExample::deleteFloatingIp($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DeleteFloatingIpClientErrorException
     * @throws DeleteFloatingIpServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function deleteFloatingIp(
        Client $client,
        int $id,
    ): null {
        return $client->floatingIps()->deleteFloatingIp($id);
    }
}
