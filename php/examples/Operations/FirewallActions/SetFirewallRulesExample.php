<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FirewallActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\SetFirewallRulesClientErrorException;
use Prefabcortex\Hetzner\Exception\SetFirewallRulesServerErrorException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponse;
use Prefabcortex\Hetzner\Model\FirewallRuleDirection;
use Prefabcortex\Hetzner\Model\FirewallRuleProtocol;
use Prefabcortex\Hetzner\Model\Rule;
use Prefabcortex\Hetzner\Model\SetFirewallRulesBody;

final class SetFirewallRulesExample
{
    /**
     * Set the rules of a [Firewall](#tag/firewalls).
     *
     * Overwrites the existing rules with the given ones. Pass an empty array to remove all rules.
     *
     * Rules are limited to 50 entries per [Firewall](#tag/firewalls) and [500 effective
     * rules](https://docs.hetzner.com/cloud/firewalls/overview#limits).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   SetFirewallRulesExample::setFirewallRules($client, $id, SetFirewallRulesExample::buildDefault());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws SetFirewallRulesClientErrorException
     * @throws SetFirewallRulesServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function setFirewallRules(
        Client $client,
        int $id,
        SetFirewallRulesBody $requestBody,
    ): ActionListResponse {
        return $client->firewallActions()->setFirewallRules(
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
    public static function buildDefault(): SetFirewallRulesBody
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

        return SetFirewallRulesBody::builder([$rule])->build();
    }
}
