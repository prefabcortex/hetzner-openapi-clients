<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Servers;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DeleteServerClientErrorException;
use Prefabcortex\Hetzner\Exception\DeleteServerServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class DeleteServerExample
{
    /**
     * Deletes a Server.
     *
     * This immediately removes the Server from your account, and it is no longer accessible. Any
     * resources attached to the server (like Volumes, Primary IPs, Floating IPs, Firewalls,
     * Placement Groups) are detached while the server is deleted.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DeleteServerExample::deleteServer($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DeleteServerClientErrorException
     * @throws DeleteServerServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function deleteServer(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->servers()->deleteServer($id);
    }
}
