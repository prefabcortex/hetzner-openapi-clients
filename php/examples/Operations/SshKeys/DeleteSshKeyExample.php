<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\SshKeys;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DeleteSshKeyClientErrorException;
use Prefabcortex\Hetzner\Exception\DeleteSshKeyServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;

final class DeleteSshKeyExample
{
    /**
     * Deletes an SSH key. It cannot be used anymore.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DeleteSshKeyExample::deleteSshKey($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DeleteSshKeyClientErrorException
     * @throws DeleteSshKeyServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function deleteSshKey(
        Client $client,
        int $id,
    ): null {
        return $client->sshKeys()->deleteSshKey($id);
    }
}
