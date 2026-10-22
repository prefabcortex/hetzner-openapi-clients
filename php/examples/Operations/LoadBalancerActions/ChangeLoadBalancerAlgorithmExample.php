<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ChangeLoadBalancerAlgorithmClientErrorException;
use Prefabcortex\Hetzner\Exception\ChangeLoadBalancerAlgorithmServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\LoadBalancerAlgorithm;
use Prefabcortex\Hetzner\Model\LoadBalancerAlgorithmType;

final class ChangeLoadBalancerAlgorithmExample
{
    /**
     * Change the algorithm that determines to which target new requests are sent.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ChangeLoadBalancerAlgorithmExample::changeLoadBalancerAlgorithm($client, $id, ChangeLoadBalancerAlgorithmExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ChangeLoadBalancerAlgorithmClientErrorException
     * @throws ChangeLoadBalancerAlgorithmServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function changeLoadBalancerAlgorithm(
        Client $client,
        int $id,
        LoadBalancerAlgorithm $requestBody,
    ): ActionResponse {
        return $client->loadBalancerActions()->changeLoadBalancerAlgorithm(
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
    public static function buildExampleRequestBody(): LoadBalancerAlgorithm
    {
        return LoadBalancerAlgorithm::builder(LoadBalancerAlgorithmType::round_robin)->build();
    }
}
