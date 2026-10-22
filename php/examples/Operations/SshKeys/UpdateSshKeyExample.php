<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\SshKeys;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateSshKeyClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateSshKeyServerErrorException;
use Prefabcortex\Hetzner\Model\SshKeyResponse;
use Prefabcortex\Hetzner\Model\UpdateSshKeyBody;

final class UpdateSshKeyExample
{
    /**
     * Updates an SSH key. You can update an SSH key name and an SSH key labels.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateSshKeyExample::updateSshKey($client, $id, UpdateSshKeyExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateSshKeyClientErrorException
     * @throws UpdateSshKeyServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateSshKey(
        Client $client,
        int $id,
        UpdateSshKeyBody $requestBody,
    ): SshKeyResponse {
        return $client->sshKeys()->updateSshKey(
            $id,
            $requestBody,
        );
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildExampleRequestBody(): UpdateSshKeyBody
    {
        return UpdateSshKeyBody::builder()
            ->setName('My ssh key')
            ->build();
    }
}
