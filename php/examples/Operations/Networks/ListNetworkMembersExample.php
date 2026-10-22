<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Networks;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListNetworkMembersClientErrorException;
use Prefabcortex\Hetzner\Exception\ListNetworkMembersServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListNetworkMembersResponse200;
use Prefabcortex\Hetzner\Parameter\ListNetworkMembersQueryParameters;

final class ListNetworkMembersExample
{
    /**
     * List the resources attached to a specific [Network](#tag/networks).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListNetworkMembersQueryParameters();
     *   ListNetworkMembersExample::listNetworkMembers($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListNetworkMembersClientErrorException
     * @throws ListNetworkMembersServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listNetworkMembers(
        Client $client,
        int $id,
        ListNetworkMembersQueryParameters $queryParameters,
    ): ListNetworkMembersResponse200 {
        return $client->networks()->listNetworkMembers(
            $id,
            $queryParameters,
        );
    }
}
