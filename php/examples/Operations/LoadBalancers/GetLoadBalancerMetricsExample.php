<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\LoadBalancers;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetLoadBalancerMetricsClientErrorException;
use Prefabcortex\Hetzner\Exception\GetLoadBalancerMetricsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\MetricsResponse;
use Prefabcortex\Hetzner\Parameter\GetLoadBalancerMetricsQueryParameters;

final class GetLoadBalancerMetricsExample
{
    /**
     * You must specify the type of metric to get: `open_connections`, `connections_per_second`,
     * `requests_per_second` or `bandwidth`. You can also specify more than one type by comma
     * separation, e.g. `requests_per_second,bandwidth`.
     *
     * Depending on the type you will get different time series data:
     *
     * |Type | Timeseries | Unit | Description |
     * |---- |------------|------|-------------|
     * | open_connections | open_connections | number | Open connections |
     * | connections_per_second | connections_per_second | connections/s | Connections per second |
     * | requests_per_second | requests_per_second | requests/s | Requests per second |
     * | bandwidth | bandwidth.in | bytes/s | Ingress bandwidth |
     * || bandwidth.out | bytes/s | Egress bandwidth |
     *
     * Metrics are available for the last 30 days only.
     *
     * If you do not provide the step argument we will automatically adjust it so that 200 samples
     * are returned.
     *
     * We limit the number of samples to a maximum of 500 and will adjust the step parameter
     * accordingly.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new GetLoadBalancerMetricsQueryParameters($type, $start, $end);
     *   GetLoadBalancerMetricsExample::getLoadBalancerMetrics($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetLoadBalancerMetricsClientErrorException
     * @throws GetLoadBalancerMetricsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getLoadBalancerMetrics(
        Client $client,
        int $id,
        GetLoadBalancerMetricsQueryParameters $queryParameters,
    ): MetricsResponse {
        return $client->loadBalancers()->getLoadBalancerMetrics(
            $id,
            $queryParameters,
        );
    }
}
