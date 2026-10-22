<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\ShutdownServerClientErrorException;
use Prefabcortex\Hetzner\Exception\ShutdownServerServerErrorException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class ShutdownServerExample
{
    /**
     * Shuts down a Server gracefully by sending an ACPI shutdown request. The Server operating
     * system must support ACPI and react to the request, otherwise the Server will not shut down.
     * Please note that the `action` status in this case only reflects whether the action was sent
     * to the server. It does not mean that the server actually shut down successfully. If you need
     * to ensure that the server is off, use the `poweroff` action.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ShutdownServerExample::shutdownServer($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ShutdownServerClientErrorException
     * @throws ShutdownServerServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function shutdownServer(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->serverActions()->shutdownServer($id);
    }
}
