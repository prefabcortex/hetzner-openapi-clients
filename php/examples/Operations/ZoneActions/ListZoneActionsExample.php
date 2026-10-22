<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ZoneActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListZoneActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListZoneActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListZoneActionsQueryParameters;

final class ListZoneActionsExample
{
    /**
     * Returns all [Actions](#tag/actions) for a [Zone](#tag/zones).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListZoneActionsQueryParameters();
     *   ListZoneActionsExample::listZoneActions($client, $idOrName, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListZoneActionsClientErrorException
     * @throws ListZoneActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listZoneActions(
        Client $client,
        string $idOrName,
        ListZoneActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->zoneActions()->listZoneActions(
            $idOrName,
            $queryParameters,
        );
    }
}
