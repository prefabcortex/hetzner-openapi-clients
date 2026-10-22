<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Servers;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetServerMetricsClientErrorException;
use Prefabcortex\Hetzner\Exception\GetServerMetricsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\MetricsResponse;
use Prefabcortex\Hetzner\Parameter\GetServerMetricsQueryParameters;

final class GetServerMetricsExample
{
    /**
     * Get Metrics for specified Server.
     *
     * You must specify the type of metric to get: cpu, disk or network. You can also specify more
     * than one type by comma separation, e.g. cpu,disk.
     *
     * Depending on the type you will get different time series data
     *
     * | Type    | Timeseries              | Unit      | Description                                          |
     * |---------|-------------------------|-----------|------------------------------------------------------|
     * | cpu     | cpu                     | percent   | Percent CPU usage                                    |
     * | disk    | disk.0.iops.read        | iop/s     | Number of read IO operations per second              |
     * |         | disk.0.iops.write       | iop/s     | Number of write IO operations per second             |
     * |         | disk.0.bandwidth.read   | bytes/s   | Bytes read per second                                |
     * |         | disk.0.bandwidth.write  | bytes/s   | Bytes written per second                             |
     * | network | network.0.pps.in        | packets/s | Public Network interface packets per second received |
     * |         | network.0.pps.out       | packets/s | Public Network interface packets per second sent     |
     * |         | network.0.bandwidth.in  | bytes/s   | Public Network interface bytes/s received            |
     * |         | network.0.bandwidth.out | bytes/s   | Public Network interface bytes/s sent                |
     *
     * Note that the CPU value is not normalized to a fixed 0–100% scale. It is calculated per vCPU:
     * a value of 100 represents full utilization on a 1-vCPU server, and 25% utilization on a
     * 4-vCPU server. To calculate the overall CPU usage, divide the metric value by the number of
     * vCPUs.
     *
     * Metrics are available for the last 30 days only.
     *
     * If you do not provide the step argument we will automatically adjust it so that a maximum of
     * 200 samples are returned.
     *
     * We limit the number of samples returned to a maximum of 500 and will adjust the step
     * parameter accordingly.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new GetServerMetricsQueryParameters($type, $start, $end);
     *   GetServerMetricsExample::getServerMetrics($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetServerMetricsClientErrorException
     * @throws GetServerMetricsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getServerMetrics(
        Client $client,
        int $id,
        GetServerMetricsQueryParameters $queryParameters,
    ): MetricsResponse {
        return $client->servers()->getServerMetrics(
            $id,
            $queryParameters,
        );
    }
}
