<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Firewalls;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreateFirewallClientErrorException;
use Prefabcortex\Hetzner\Exception\CreateFirewallServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreateFirewallBody;
use Prefabcortex\Hetzner\Model\CreateFirewallResponse201;
use Prefabcortex\Hetzner\Model\FirewallResource;
use Prefabcortex\Hetzner\Model\FirewallResourceServer;
use Prefabcortex\Hetzner\Model\FirewallResourceType;
use Prefabcortex\Hetzner\Model\FirewallRuleDirection;
use Prefabcortex\Hetzner\Model\FirewallRuleProtocol;
use Prefabcortex\Hetzner\Model\Rule;

final class CreateFirewallExample
{
    /**
     * Create a [Firewall](#tag/firewalls).
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `server_already_added` | The [Server](#tag/servers) was applied more than once. |
     * | `422` | `incompatible_network_type` | The resources network type is not supported by [Firewalls](#tag/firewalls). |
     * | `422` | `firewall_resource_not_found` | The resource the [Firewall](#tag/firewalls) should be attached to was not found. |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreateFirewallExample::createFirewall($client, CreateFirewallExample::buildDefault());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreateFirewallClientErrorException
     * @throws CreateFirewallServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createFirewall(
        Client $client,
        CreateFirewallBody $requestBody,
    ): CreateFirewallResponse201 {
        return $client->firewalls()->createFirewall($requestBody);
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildDefault(): CreateFirewallBody
    {
        $rule = Rule::builder(
            // direction
            FirewallRuleDirection::in,
            // protocol
            FirewallRuleProtocol::tcp,
        )
            ->setDescription('Allow port 80')
            ->setSourceIps(['192.0.2.2/32', '192.0.2.0/24', '2001:0db8:9a3b:ee58:5ca:990c:8bc9:c03b/128'])
            ->setPort('80')
            ->build();
        $server = FirewallResourceServer::builder(42)->build();
        $firewallResource = FirewallResource::builder(FirewallResourceType::server)
            ->setServer($server)
            ->build();

        return CreateFirewallBody::builder('Corporate Intranet Protection')
            ->setLabels(['key' => 'value'])
            ->setRules([$rule])
            ->setApplyTo([$firewallResource])
            ->build();
    }
}
