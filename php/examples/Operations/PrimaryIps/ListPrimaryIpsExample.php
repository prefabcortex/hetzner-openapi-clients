<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PrimaryIps;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListPrimaryIpsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListPrimaryIpsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListPrimaryIpsResponse200;
use Prefabcortex\Hetzner\Parameter\ListPrimaryIpsQueryParameters;

final class ListPrimaryIpsExample
{
    /**
     * List multiple [Primary IPs](#tag/primary-ips).
     *
     * Use the provided URI parameters to modify the result.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListPrimaryIpsQueryParameters();
     *   ListPrimaryIpsExample::listPrimaryIps($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListPrimaryIpsClientErrorException
     * @throws ListPrimaryIpsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listPrimaryIps(
        Client $client,
        ListPrimaryIpsQueryParameters $queryParameters,
    ): ListPrimaryIpsResponse200 {
        return $client->primaryIps()->listPrimaryIps($queryParameters);
    }
}
