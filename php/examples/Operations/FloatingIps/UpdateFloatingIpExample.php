<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FloatingIps;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateFloatingIpClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateFloatingIpServerErrorException;
use Prefabcortex\Hetzner\Model\FloatingIpResponse;
use Prefabcortex\Hetzner\Model\UpdateFloatingIpBody;

final class UpdateFloatingIpExample
{
    /**
     * Update a [Floating IP](#tag/floating-ips).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateFloatingIpExample::updateFloatingIp($client, $id, UpdateFloatingIpExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateFloatingIpClientErrorException
     * @throws UpdateFloatingIpServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateFloatingIp(
        Client $client,
        int $id,
        UpdateFloatingIpBody $requestBody,
    ): FloatingIpResponse {
        return $client->floatingIps()->updateFloatingIp(
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
    public static function buildExampleRequestBody(): UpdateFloatingIpBody
    {
        return UpdateFloatingIpBody::builder()
            ->setDescription('This describes my resource')
            ->setName('my-resource')
            ->build();
    }
}
