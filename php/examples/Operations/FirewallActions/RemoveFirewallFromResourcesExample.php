<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FirewallActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\RemoveFirewallFromResourcesClientErrorException;
use Prefabcortex\Hetzner\Exception\RemoveFirewallFromResourcesServerErrorException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponse;
use Prefabcortex\Hetzner\Model\FirewallResource;
use Prefabcortex\Hetzner\Model\FirewallResourceServer;
use Prefabcortex\Hetzner\Model\FirewallResourceType;
use Prefabcortex\Hetzner\Model\RemoveFirewallFromResourcesBody;

final class RemoveFirewallFromResourcesExample
{
    /**
     * Removes a [Firewall](#tag/firewalls) from multiple resources.
     *
     * Supported resources:
     * - [Servers](#tag/servers) (with a public network interface)
     *
     * A [Firewall](#tag/firewalls) is removed from a resource once the related
     * [Action](#tag/actions) with command `remove_firewall` successfully finished.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `404` | `firewall_resource_not_found` | The resource the [Firewall](#tag/firewalls) should be removed from was not found |
     * | `422` | `firewall_managed_by_label_selector` | [Firewall](#tag/firewall) is applied via a [Label Selector](#description/label-selector) and cannot be removed manually |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   RemoveFirewallFromResourcesExample::removeFirewallFromResources($client, $id, RemoveFirewallFromResourcesExample::buildDefault());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws RemoveFirewallFromResourcesClientErrorException
     * @throws RemoveFirewallFromResourcesServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function removeFirewallFromResources(
        Client $client,
        int $id,
        RemoveFirewallFromResourcesBody $requestBody,
    ): ActionListResponse {
        return $client->firewallActions()->removeFirewallFromResources(
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
    public static function buildDefault(): RemoveFirewallFromResourcesBody
    {
        $server = FirewallResourceServer::builder(42)->build();
        $firewallResource = FirewallResource::builder(FirewallResourceType::server)
            ->setServer($server)
            ->build();

        return RemoveFirewallFromResourcesBody::builder([$firewallResource])->build();
    }
}
