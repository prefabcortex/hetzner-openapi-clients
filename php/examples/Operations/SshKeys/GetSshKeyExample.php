<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\SshKeys;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetSshKeyClientErrorException;
use Prefabcortex\Hetzner\Exception\GetSshKeyServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\SshKeyResponse;

final class GetSshKeyExample
{
    /**
     * Returns a specific SSH key object.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetSshKeyExample::getSshKey($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetSshKeyClientErrorException
     * @throws GetSshKeyServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getSshKey(
        Client $client,
        int $id,
    ): SshKeyResponse {
        return $client->sshKeys()->getSshKey($id);
    }
}
