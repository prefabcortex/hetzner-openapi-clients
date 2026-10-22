<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\NetworkActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\AddNetworkSubnetClientErrorException;
use Prefabcortex\Hetzner\Exception\AddNetworkSubnetServerErrorException;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\AddNetworkSubnetBody;
use Prefabcortex\Hetzner\Model\SubnetType;

final class AddNetworkSubnetExample
{
    /**
     * Adds a new subnet to the [Network](#tag/networks).
     *
     * If the subnet `ip_range` is not provided, the first available `/24` IP range will be used.
     *
     * If a change is currently being performed on this [Network](#tag/networks), a error response
     * with code `conflict` will be returned.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   AddNetworkSubnetExample::addNetworkSubnet($client, $id, AddNetworkSubnetExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws AddNetworkSubnetClientErrorException
     * @throws AddNetworkSubnetServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function addNetworkSubnet(
        Client $client,
        int $id,
        AddNetworkSubnetBody $requestBody,
    ): ActionResponse {
        return $client->networkActions()->addNetworkSubnet(
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
    public static function buildExampleRequestBody(): AddNetworkSubnetBody
    {
        return AddNetworkSubnetBody::builder(
            // type
            SubnetType::cloud,
            // networkZone
            'eu-central',
        )
            ->setIpRange('10.0.1.0/24')
            ->setVswitchId(1000)
            ->build();
    }
}
