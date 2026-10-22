<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\RemoveServerFromPlacementGroupClientErrorException;
use Prefabcortex\Hetzner\Exception\RemoveServerFromPlacementGroupServerErrorException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class RemoveServerFromPlacementGroupExample
{
    /**
     * Removes a Server from a Placement Group.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   RemoveServerFromPlacementGroupExample::removeServerFromPlacementGroup($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws RemoveServerFromPlacementGroupClientErrorException
     * @throws RemoveServerFromPlacementGroupServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function removeServerFromPlacementGroup(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->serverActions()->removeServerFromPlacementGroup($id);
    }
}
