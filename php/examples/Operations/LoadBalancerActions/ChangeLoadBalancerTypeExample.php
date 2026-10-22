<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ChangeLoadBalancerTypeClientErrorException;
use Prefabcortex\Hetzner\Exception\ChangeLoadBalancerTypeServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ChangeLoadBalancerTypeBody;

final class ChangeLoadBalancerTypeExample
{
    /**
     * Changes the type (Max Services, Max Targets and Max Connections) of a Load Balancer.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `invalid_load_balancer_type` | The Load Balancer type does not fit for the given Load Balancer |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ChangeLoadBalancerTypeExample::changeLoadBalancerType($client, $id, ChangeLoadBalancerTypeExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ChangeLoadBalancerTypeClientErrorException
     * @throws ChangeLoadBalancerTypeServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function changeLoadBalancerType(
        Client $client,
        int $id,
        ChangeLoadBalancerTypeBody $requestBody,
    ): ActionResponse {
        return $client->loadBalancerActions()->changeLoadBalancerType(
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
    public static function buildExampleRequestBody(): ChangeLoadBalancerTypeBody
    {
        return ChangeLoadBalancerTypeBody::builder('lb11')->build();
    }
}
