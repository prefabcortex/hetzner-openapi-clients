<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\SshKeys;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreateSshKeyClientErrorException;
use Prefabcortex\Hetzner\Exception\CreateSshKeyServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreateSshKeyBody;
use Prefabcortex\Hetzner\Model\SshKeyResponse;

final class CreateSshKeyExample
{
    /**
     * Creates a new SSH key with the given `name` and `public_key`. Once an SSH key is created, it
     * can be used in other calls such as creating Servers.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreateSshKeyExample::createSshKey($client, CreateSshKeyExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreateSshKeyClientErrorException
     * @throws CreateSshKeyServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createSshKey(
        Client $client,
        CreateSshKeyBody $requestBody,
    ): SshKeyResponse {
        return $client->sshKeys()->createSshKey($requestBody);
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildExampleRequestBody(): CreateSshKeyBody
    {
        return CreateSshKeyBody::builder(
            // name
            'My ssh key',
            // publicKey
            'ssh-rsa AAAjjk76kgf...Xt',
        )->build();
    }
}
