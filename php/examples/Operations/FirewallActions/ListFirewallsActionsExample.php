<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FirewallActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListFirewallsActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListFirewallsActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListFirewallsActionsQueryParameters;

final class ListFirewallsActionsExample
{
    /**
     * Returns all [Actions](#tag/actions) for [Firewalls](#tag/firewalls).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListFirewallsActionsQueryParameters();
     *   ListFirewallsActionsExample::listFirewallsActions($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListFirewallsActionsClientErrorException
     * @throws ListFirewallsActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listFirewallsActions(
        Client $client,
        ListFirewallsActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->firewallActions()->listFirewallsActions($queryParameters);
    }
}
