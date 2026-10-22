<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FirewallActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ApplyFirewallToResourcesClientErrorException;
use Prefabcortex\Hetzner\Exception\ApplyFirewallToResourcesServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponse;
use Prefabcortex\Hetzner\Model\ApplyFirewallToResourcesBody;
use Prefabcortex\Hetzner\Model\FirewallResource;
use Prefabcortex\Hetzner\Model\FirewallResourceServer;
use Prefabcortex\Hetzner\Model\FirewallResourceType;

final class ApplyFirewallToResourcesExample
{
    /**
     * Applies a [Firewall](#tag/firewalls) to multiple resources.
     *
     * Supported resources:
     * - [Servers](#tag/servers) (with a public network interface)
     * - [Label Selectors](#description/label-selector)
     *
     * A [Server](#tag/servers) can be applied to [a maximum of 5
     * Firewalls](https://docs.hetzner.com/cloud/firewalls/overview#limits). This limit applies to
     * [Servers](#tag/servers) applied via a matching [Label Selector](#description/label-selector)
     * as well.
     *
     * Updates to resources matching or no longer matching a [Label
     * Selector](#description/label-selector) can take up to a few seconds to be processed.
     *
     * A [Firewall](#tag/firewalls) is applied to a resource once the related [Action](#tag/actions)
     * with command `apply_firewall` successfully finished.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `404` | `firewall_resource_not_found` | The resource the [Firewall](#tag/firewalls) should be applied to was not found |
     * | `422` | `firewall_already_applied` | [Firewall](#tag/firewalls) is already applied to resource |
     * | `422` | `incompatible_network_type` | The network type of the resource is not supported by [Firewalls](#tag/firewalls) |
     * | `422` | `private_net_only_server` | The [Server](#tag/servers) the [Firewall](#tag/firewalls) should be applied to has no public interface |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ApplyFirewallToResourcesExample::applyFirewallToResources($client, $id, ApplyFirewallToResourcesExample::buildDefault());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ApplyFirewallToResourcesClientErrorException
     * @throws ApplyFirewallToResourcesServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function applyFirewallToResources(
        Client $client,
        int $id,
        ApplyFirewallToResourcesBody $requestBody,
    ): ActionListResponse {
        return $client->firewallActions()->applyFirewallToResources(
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
    public static function buildDefault(): ApplyFirewallToResourcesBody
    {
        $server = FirewallResourceServer::builder(42)->build();
        $firewallResource = FirewallResource::builder(FirewallResourceType::server)
            ->setServer($server)
            ->build();

        return ApplyFirewallToResourcesBody::builder([$firewallResource])->build();
    }
}
