<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\DataCenters;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetDatacenterClientErrorException;
use Prefabcortex\Hetzner\Exception\GetDatacenterServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\GetDatacenterResponse200;

final class GetDatacenterExample
{
    /**
     * Deprecated:** This endpoint is deprecated as of 01 June 2026 and will be removed after 01
     * October 2026.
     *
     * Returns a single [Data Center](#tag/data-centers).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetDatacenterExample::getDatacenter($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetDatacenterClientErrorException
     * @throws GetDatacenterServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getDatacenter(
        Client $client,
        int $id,
    ): GetDatacenterResponse200 {
        return $client->dataCenters()->getDatacenter($id);
    }
}
