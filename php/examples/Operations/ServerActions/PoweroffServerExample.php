<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\PoweroffServerClientErrorException;
use Prefabcortex\Hetzner\Exception\PoweroffServerServerErrorException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class PoweroffServerExample
{
    /**
     * Cuts power to the Server. This forcefully stops it without giving the Server operating system
     * time to gracefully stop. May lead to data loss, equivalent to pulling the power cord. Power
     * off should only be used when shutdown does not work.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   PoweroffServerExample::poweroffServer($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws PoweroffServerClientErrorException
     * @throws PoweroffServerServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function poweroffServer(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->serverActions()->poweroffServer($id);
    }
}
