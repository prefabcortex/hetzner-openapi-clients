<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FirewallActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListFirewallActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListFirewallActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListFirewallActionsQueryParameters;

final class ListFirewallActionsExample
{
    /**
     * Returns all [Actions](#tag/actions) for the [Firewall](#tag/firewalls).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListFirewallActionsQueryParameters();
     *   ListFirewallActionsExample::listFirewallActions($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListFirewallActionsClientErrorException
     * @throws ListFirewallActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listFirewallActions(
        Client $client,
        int $id,
        ListFirewallActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->firewallActions()->listFirewallActions(
            $id,
            $queryParameters,
        );
    }
}
