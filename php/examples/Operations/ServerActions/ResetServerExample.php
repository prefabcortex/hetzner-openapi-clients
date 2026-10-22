<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResetServerClientErrorException;
use Prefabcortex\Hetzner\Exception\ResetServerServerErrorException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class ResetServerExample
{
    /**
     * Cuts power to a Server and starts it again. This forcefully stops it without giving the
     * Server operating system time to gracefully stop. This may lead to data loss, it’s equivalent
     * to pulling the power cord and plugging it in again. Reset should only be used when reboot
     * does not work.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ResetServerExample::resetServer($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ResetServerClientErrorException
     * @throws ResetServerServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function resetServer(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->serverActions()->resetServer($id);
    }
}
