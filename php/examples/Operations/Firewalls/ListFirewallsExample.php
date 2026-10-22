<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Firewalls;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListFirewallsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListFirewallsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListFirewallsResponse200;
use Prefabcortex\Hetzner\Parameter\ListFirewallsQueryParameters;

final class ListFirewallsExample
{
    /**
     * Returns all [Firewalls](#tag/firewalls).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListFirewallsQueryParameters();
     *   ListFirewallsExample::listFirewalls($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListFirewallsClientErrorException
     * @throws ListFirewallsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listFirewalls(
        Client $client,
        ListFirewallsQueryParameters $queryParameters,
    ): ListFirewallsResponse200 {
        return $client->firewalls()->listFirewalls($queryParameters);
    }
}
