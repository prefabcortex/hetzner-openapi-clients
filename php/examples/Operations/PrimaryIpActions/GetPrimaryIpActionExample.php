<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PrimaryIpActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetPrimaryIpActionClientErrorException;
use Prefabcortex\Hetzner\Exception\GetPrimaryIpActionServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class GetPrimaryIpActionExample
{
    /**
     * Deprecated**: This operation is deprecated, see our
     * [changelog](https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
     * for more details.
     *
     * Returns a specific [Action](#tag/actions) for a [Primary IP](#tag/primary-ips).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetPrimaryIpActionExample::getPrimaryIpAction($client, $id, $actionId);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetPrimaryIpActionClientErrorException
     * @throws GetPrimaryIpActionServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getPrimaryIpAction(
        Client $client,
        int $id,
        int $actionId,
    ): ActionResponse {
        return $client->primaryIpActions()->getPrimaryIpAction(
            $id,
            $actionId,
        );
    }
}
