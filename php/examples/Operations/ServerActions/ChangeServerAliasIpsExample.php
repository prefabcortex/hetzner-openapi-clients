<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ChangeServerAliasIpsClientErrorException;
use Prefabcortex\Hetzner\Exception\ChangeServerAliasIpsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ChangeServerAliasIpsBody;

final class ChangeServerAliasIpsExample
{
    /**
     * Changes the alias IPs of an already attached Network. Note that the existing aliases for the
     * specified Network will be replaced with these provided in the request body. So if you want to
     * add an alias IP, you have to provide the existing ones from the Network plus the new alias IP
     * in the request body.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ChangeServerAliasIpsExample::changeServerAliasIps($client, $id, ChangeServerAliasIpsExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ChangeServerAliasIpsClientErrorException
     * @throws ChangeServerAliasIpsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function changeServerAliasIps(
        Client $client,
        int $id,
        ChangeServerAliasIpsBody $requestBody,
    ): ActionResponse {
        return $client->serverActions()->changeServerAliasIps(
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
    public static function buildExampleRequestBody(): ChangeServerAliasIpsBody
    {
        return ChangeServerAliasIpsBody::builder(
            // network
            4711,
            // aliasIps
            ['10.0.1.2'],
        )->build();
    }
}
