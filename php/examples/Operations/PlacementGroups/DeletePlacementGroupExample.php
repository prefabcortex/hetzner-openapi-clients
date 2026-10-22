<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PlacementGroups;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DeletePlacementGroupClientErrorException;
use Prefabcortex\Hetzner\Exception\DeletePlacementGroupServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;

final class DeletePlacementGroupExample
{
    /**
     * Deletes a Placement Group.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DeletePlacementGroupExample::deletePlacementGroup($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DeletePlacementGroupClientErrorException
     * @throws DeletePlacementGroupServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function deletePlacementGroup(
        Client $client,
        int $id,
    ): null {
        return $client->placementGroups()->deletePlacementGroup($id);
    }
}
