<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DisableServerRescueClientErrorException;
use Prefabcortex\Hetzner\Exception\DisableServerRescueServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class DisableServerRescueExample
{
    /**
     * Disables the Hetzner Rescue System for a Server. This makes a Server start from its disks on
     * next reboot.
     *
     * Rescue Mode is automatically disabled when you first boot into it or if you do not use it for
     * 60 minutes.
     *
     * Disabling rescue mode will not reboot your Server — you will have to do this yourself.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DisableServerRescueExample::disableServerRescue($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DisableServerRescueClientErrorException
     * @throws DisableServerRescueServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function disableServerRescue(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->serverActions()->disableServerRescue($id);
    }
}
