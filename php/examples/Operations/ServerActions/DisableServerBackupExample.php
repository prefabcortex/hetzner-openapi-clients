<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DisableServerBackupClientErrorException;
use Prefabcortex\Hetzner\Exception\DisableServerBackupServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class DisableServerBackupExample
{
    /**
     * Disables the automatic backup option and deletes all existing Backups for a Server. No more
     * additional charges for backups will be made.
     *
     * Caution: This immediately removes all existing backups for the Server!
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DisableServerBackupExample::disableServerBackup($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DisableServerBackupClientErrorException
     * @throws DisableServerBackupServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function disableServerBackup(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->serverActions()->disableServerBackup($id);
    }
}
