<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FloatingIps;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreateFloatingIpClientErrorException;
use Prefabcortex\Hetzner\Exception\CreateFloatingIpServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreateFloatingIpBody;
use Prefabcortex\Hetzner\Model\CreateFloatingIpResponse201;
use Prefabcortex\Hetzner\Model\IpType;

final class CreateFloatingIpExample
{
    /**
     * Create a [Floating IP](#tag/floating-ips).
     *
     * Provide the `server` attribute to assign the [Floating IP](#tag/floating-ips) to that server
     * or provide a `home_location` to locate the [Floating IP](#tag/floating-ips) at. Note that the
     * [Floating IP](#tag/floating-ips) can be assigned to a [Server](#tag/servers) in any
     * [Location](#tag/locations) later on. For optimal routing it is advised to use the [Floating
     * IP](#tag/floating-ips) in the same [Location](#tag/locations) it was created in.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreateFloatingIpExample::createFloatingIp($client, CreateFloatingIpExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreateFloatingIpClientErrorException
     * @throws CreateFloatingIpServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createFloatingIp(
        Client $client,
        CreateFloatingIpBody $requestBody,
    ): CreateFloatingIpResponse201 {
        return $client->floatingIps()->createFloatingIp($requestBody);
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildExampleRequestBody(): CreateFloatingIpBody
    {
        return CreateFloatingIpBody::builder(IpType::ipv4)
            ->setServer(42)
            ->setDescription('This describes my resource')
            ->setName('my-resource')
            ->build();
    }
}
