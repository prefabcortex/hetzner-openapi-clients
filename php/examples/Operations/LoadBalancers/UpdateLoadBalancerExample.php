<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancers;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateLoadBalancerClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateLoadBalancerServerErrorException;
use Prefabcortex\Hetzner\Model\LoadBalancerResponse;
use Prefabcortex\Hetzner\Model\UpdateLoadBalancerBody;

final class UpdateLoadBalancerExample
{
    /**
     * Updates a Load Balancer. You can update a Load Balancer’s name and a Load Balancer’s labels.
     *
     * Note: if the Load Balancer object changes during the request, the response will be a
     * “conflict” error.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateLoadBalancerExample::updateLoadBalancer($client, $id, UpdateLoadBalancerExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateLoadBalancerClientErrorException
     * @throws UpdateLoadBalancerServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateLoadBalancer(
        Client $client,
        int $id,
        UpdateLoadBalancerBody $requestBody,
    ): LoadBalancerResponse {
        return $client->loadBalancers()->updateLoadBalancer(
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
    public static function buildExampleRequestBody(): UpdateLoadBalancerBody
    {
        return UpdateLoadBalancerBody::builder()
            ->setName('new-name')
            ->build();
    }
}
