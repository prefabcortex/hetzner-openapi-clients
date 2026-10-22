<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\RequestServerConsoleClientErrorException;
use Prefabcortex\Hetzner\Exception\RequestServerConsoleServerErrorException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\RequestServerConsoleResponse201;

final class RequestServerConsoleExample
{
    /**
     * Requests credentials for remote access via VNC over websocket to keyboard, monitor, and mouse
     * for a Server. The provided URL is valid for 1 minute, after this period a new url needs to be
     * created to connect to the Server. How long the connection is open after the initial connect
     * is not subject to this timeout.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   RequestServerConsoleExample::requestServerConsole($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws RequestServerConsoleClientErrorException
     * @throws RequestServerConsoleServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function requestServerConsole(
        Client $client,
        int $id,
    ): RequestServerConsoleResponse201 {
        return $client->serverActions()->requestServerConsole($id);
    }
}
