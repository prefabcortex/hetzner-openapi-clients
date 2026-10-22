<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FloatingIpActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListFloatingIpActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListFloatingIpActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListFloatingIpActionsQueryParameters;

final class ListFloatingIpActionsExample
{
    /**
     * Lists [Actions](#tag/actions) for a [Floating IP](#tag/floating-ips).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListFloatingIpActionsQueryParameters();
     *   ListFloatingIpActionsExample::listFloatingIpActions($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListFloatingIpActionsClientErrorException
     * @throws ListFloatingIpActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listFloatingIpActions(
        Client $client,
        int $id,
        ListFloatingIpActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->floatingIpActions()->listFloatingIpActions(
            $id,
            $queryParameters,
        );
    }
}
