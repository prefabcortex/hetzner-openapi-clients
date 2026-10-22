<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PrimaryIps;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DeletePrimaryIpClientErrorException;
use Prefabcortex\Hetzner\Exception\DeletePrimaryIpServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;

final class DeletePrimaryIpExample
{
    /**
     * Deletes a [Primary IP](#tag/primary-ips).
     *
     * The [Server](#tag/servers) must be powered off (status `off`) in order for this operation to
     * succeed. If assigned to a [Server](#tag/servers) the [Primary IP](#tag/primary-ips) will be
     * unassigned automatically until 1 May 2026. After this date, the [Primary
     * IP](#tag/primary-ips) needs to be unassigned before it can be deleted.
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
     *   DeletePrimaryIpExample::deletePrimaryIp($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DeletePrimaryIpClientErrorException
     * @throws DeletePrimaryIpServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function deletePrimaryIp(
        Client $client,
        int $id,
    ): null {
        return $client->primaryIps()->deletePrimaryIp($id);
    }
}
