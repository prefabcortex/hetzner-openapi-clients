<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Firewalls;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetFirewallClientErrorException;
use Prefabcortex\Hetzner\Exception\GetFirewallServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\FirewallResponse;

final class GetFirewallExample
{
    /**
     * Returns a single [Firewall](#tag/firewalls).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetFirewallExample::getFirewall($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetFirewallClientErrorException
     * @throws GetFirewallServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getFirewall(
        Client $client,
        int $id,
    ): FirewallResponse {
        return $client->firewalls()->getFirewall($id);
    }
}
