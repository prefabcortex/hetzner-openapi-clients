<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FirewallActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetFirewallsActionClientErrorException;
use Prefabcortex\Hetzner\Exception\GetFirewallsActionServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class GetFirewallsActionExample
{
    /**
     * Returns the specific [Action](#tag/actions).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetFirewallsActionExample::getFirewallsAction($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetFirewallsActionClientErrorException
     * @throws GetFirewallsActionServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getFirewallsAction(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->firewallActions()->getFirewallsAction($id);
    }
}
