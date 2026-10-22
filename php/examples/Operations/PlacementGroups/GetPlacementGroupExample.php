<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PlacementGroups;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetPlacementGroupClientErrorException;
use Prefabcortex\Hetzner\Exception\GetPlacementGroupServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\PlacementGroupResponse;

final class GetPlacementGroupExample
{
    /**
     * Gets a specific Placement Group object.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetPlacementGroupExample::getPlacementGroup($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetPlacementGroupClientErrorException
     * @throws GetPlacementGroupServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getPlacementGroup(
        Client $client,
        int $id,
    ): PlacementGroupResponse {
        return $client->placementGroups()->getPlacementGroup($id);
    }
}
