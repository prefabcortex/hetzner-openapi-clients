<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Firewalls;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateFirewallClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateFirewallServerErrorException;
use Prefabcortex\Hetzner\Model\FirewallResponse;
use Prefabcortex\Hetzner\Model\UpdateFirewallBody;

final class UpdateFirewallExample
{
    /**
     * Update a [Firewall](#tag/firewalls).
     *
     * In case of a parallel running change on the [Firewall](#tag/firewalls) a `conflict` error
     * will be returned.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateFirewallExample::updateFirewall($client, $id, UpdateFirewallExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateFirewallClientErrorException
     * @throws UpdateFirewallServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateFirewall(
        Client $client,
        int $id,
        UpdateFirewallBody $requestBody,
    ): FirewallResponse {
        return $client->firewalls()->updateFirewall(
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
    public static function buildExampleRequestBody(): UpdateFirewallBody
    {
        return UpdateFirewallBody::builder()
            ->setName('new-name')
            ->build();
    }
}
