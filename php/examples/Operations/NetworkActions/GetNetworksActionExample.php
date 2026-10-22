<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\NetworkActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetNetworksActionClientErrorException;
use Prefabcortex\Hetzner\Exception\GetNetworksActionServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class GetNetworksActionExample
{
    /**
     * Returns a single [Action](#tag/actions).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetNetworksActionExample::getNetworksAction($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetNetworksActionClientErrorException
     * @throws GetNetworksActionServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getNetworksAction(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->networkActions()->getNetworksAction($id);
    }
}
