<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\EnableServerBackupClientErrorException;
use Prefabcortex\Hetzner\Exception\EnableServerBackupServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class EnableServerBackupExample
{
    /**
     * Enables and configures the automatic daily backup option for the Server. Enabling automatic
     * backups will increase the price of the Server by 20%. In return, you will get seven slots
     * where Images of type backup can be stored.
     *
     * Backups are automatically created daily.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   EnableServerBackupExample::enableServerBackup($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws EnableServerBackupClientErrorException
     * @throws EnableServerBackupServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function enableServerBackup(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->serverActions()->enableServerBackup($id);
    }
}
