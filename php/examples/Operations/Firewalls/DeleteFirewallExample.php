<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Firewalls;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DeleteFirewallClientErrorException;
use Prefabcortex\Hetzner\Exception\DeleteFirewallServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;

final class DeleteFirewallExample
{
    /**
     * Deletes the [Firewall](#tag/firewalls).
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `resource_in_use` | [Firewall](#tag/firewalls) still applied to a resource |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DeleteFirewallExample::deleteFirewall($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DeleteFirewallClientErrorException
     * @throws DeleteFirewallServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function deleteFirewall(
        Client $client,
        int $id,
    ): null {
        return $client->firewalls()->deleteFirewall($id);
    }
}
