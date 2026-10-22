<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\FloatingIps;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListFloatingIpsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListFloatingIpsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListFloatingIpsResponse200;
use Prefabcortex\Hetzner\Parameter\ListFloatingIpsQueryParameters;

final class ListFloatingIpsExample
{
    /**
     * List multiple [Floating IPs](#tag/floating-ips).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListFloatingIpsQueryParameters();
     *   ListFloatingIpsExample::listFloatingIps($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListFloatingIpsClientErrorException
     * @throws ListFloatingIpsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listFloatingIps(
        Client $client,
        ListFloatingIpsQueryParameters $queryParameters,
    ): ListFloatingIpsResponse200 {
        return $client->floatingIps()->listFloatingIps($queryParameters);
    }
}
