<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PrimaryIps;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetPrimaryIpClientErrorException;
use Prefabcortex\Hetzner\Exception\GetPrimaryIpServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\PrimaryIPResponse;

final class GetPrimaryIpExample
{
    /**
     * Returns a [Primary IP](#tag/primary-ips).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetPrimaryIpExample::getPrimaryIp($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetPrimaryIpClientErrorException
     * @throws GetPrimaryIpServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getPrimaryIp(
        Client $client,
        int $id,
    ): PrimaryIPResponse {
        return $client->primaryIps()->getPrimaryIp($id);
    }
}
