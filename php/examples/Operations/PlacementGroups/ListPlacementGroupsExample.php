<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PlacementGroups;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListPlacementGroupsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListPlacementGroupsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListPlacementGroupsResponse200;
use Prefabcortex\Hetzner\Parameter\ListPlacementGroupsQueryParameters;

final class ListPlacementGroupsExample
{
    /**
     * Returns all Placement Group objects.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListPlacementGroupsQueryParameters();
     *   ListPlacementGroupsExample::listPlacementGroups($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListPlacementGroupsClientErrorException
     * @throws ListPlacementGroupsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listPlacementGroups(
        Client $client,
        ListPlacementGroupsQueryParameters $queryParameters,
    ): ListPlacementGroupsResponse200 {
        return $client->placementGroups()->listPlacementGroups($queryParameters);
    }
}
