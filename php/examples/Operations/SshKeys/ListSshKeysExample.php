<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\SshKeys;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListSshKeysClientErrorException;
use Prefabcortex\Hetzner\Exception\ListSshKeysServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListSshKeysResponse200;
use Prefabcortex\Hetzner\Parameter\ListSshKeysQueryParameters;

final class ListSshKeysExample
{
    /**
     * Returns all SSH key objects.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListSshKeysQueryParameters();
     *   ListSshKeysExample::listSshKeys($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListSshKeysClientErrorException
     * @throws ListSshKeysServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listSshKeys(
        Client $client,
        ListSshKeysQueryParameters $queryParameters,
    ): ListSshKeysResponse200 {
        return $client->sshKeys()->listSshKeys($queryParameters);
    }
}
