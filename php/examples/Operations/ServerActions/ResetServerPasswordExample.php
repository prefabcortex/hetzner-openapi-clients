<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResetServerPasswordClientErrorException;
use Prefabcortex\Hetzner\Exception\ResetServerPasswordServerErrorException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\RootPasswordResponse;

final class ResetServerPasswordExample
{
    /**
     * Resets the root password. Only works for Linux systems that are running the qemu guest agent.
     * Server must be powered on (status `running`) in order for this operation to succeed.
     *
     * This will generate a new password for this Server and return it.
     *
     * If this does not succeed you can use the rescue system to netboot the Server and manually
     * change your Server password by hand.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ResetServerPasswordExample::resetServerPassword($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ResetServerPasswordClientErrorException
     * @throws ResetServerPasswordServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function resetServerPassword(
        Client $client,
        int $id,
    ): RootPasswordResponse {
        return $client->serverActions()->resetServerPassword($id);
    }
}
