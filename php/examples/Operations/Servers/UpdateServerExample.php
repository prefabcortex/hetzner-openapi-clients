<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Servers;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateServerClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateServerServerErrorException;
use Prefabcortex\Hetzner\Model\ServerResponse;
use Prefabcortex\Hetzner\Model\UpdateServerBody;

final class UpdateServerExample
{
    /**
     * Updates a Server. You can update a Server’s name and a Server’s labels.
     *
     * Please note that Server names must be unique per Project and valid hostnames as per RFC 1123
     * (i.e. may only contain letters, digits, periods, and dashes).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateServerExample::updateServer($client, $id, UpdateServerExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateServerClientErrorException
     * @throws UpdateServerServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateServer(
        Client $client,
        int $id,
        UpdateServerBody $requestBody,
    ): ServerResponse {
        return $client->servers()->updateServer(
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
    public static function buildExampleRequestBody(): UpdateServerBody
    {
        return UpdateServerBody::builder()
            ->setName('my-server')
            ->build();
    }
}
