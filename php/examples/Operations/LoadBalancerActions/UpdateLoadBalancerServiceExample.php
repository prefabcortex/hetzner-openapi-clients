<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateLoadBalancerServiceClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateLoadBalancerServiceServerErrorException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\UpdateLoadBalancerServiceBody;

final class UpdateLoadBalancerServiceExample
{
    /**
     * Updates a Load Balancer Service.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `source_port_already_used` | The source port you are trying to add is already in use |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateLoadBalancerServiceExample::updateLoadBalancerService($client, $id, UpdateLoadBalancerServiceExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateLoadBalancerServiceClientErrorException
     * @throws UpdateLoadBalancerServiceServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateLoadBalancerService(
        Client $client,
        int $id,
        UpdateLoadBalancerServiceBody $requestBody,
    ): ActionResponse {
        return $client->loadBalancerActions()->updateLoadBalancerService(
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
    public static function buildExampleRequestBody(): UpdateLoadBalancerServiceBody
    {
        return UpdateLoadBalancerServiceBody::builder(443)
            ->setDestinationPort(80)
            ->setProxyprotocol(false)
            ->build();
    }
}
