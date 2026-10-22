<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ZoneActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetZoneActionClientErrorException;
use Prefabcortex\Hetzner\Exception\GetZoneActionServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class GetZoneActionExample
{
    /**
     * Deprecated**: This operation is deprecated, see our
     * [changelog](https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
     * for more details.
     *
     * Returns a specific [Action](#tag/actions) for a [Zone](#tag/zones).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetZoneActionExample::getZoneAction($client, $idOrName, $actionId);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetZoneActionClientErrorException
     * @throws GetZoneActionServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getZoneAction(
        Client $client,
        string $idOrName,
        int $actionId,
    ): ActionResponse {
        return $client->zoneActions()->getZoneAction(
            $idOrName,
            $actionId,
        );
    }
}
