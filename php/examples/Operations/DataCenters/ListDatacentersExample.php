<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\DataCenters;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListDatacentersClientErrorException;
use Prefabcortex\Hetzner\Exception\ListDatacentersServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListDatacentersResponse200;
use Prefabcortex\Hetzner\Parameter\ListDatacentersQueryParameters;

final class ListDatacentersExample
{
    /**
     * Deprecated:** This endpoint is deprecated as of 01 June 2026 and will be removed after 01
     * October 2026.
     *
     * Returns all [Data Centers](#tag/data-centers).
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListDatacentersQueryParameters();
     *   ListDatacentersExample::listDatacenters($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListDatacentersClientErrorException
     * @throws ListDatacentersServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listDatacenters(
        Client $client,
        ListDatacentersQueryParameters $queryParameters,
    ): ListDatacentersResponse200 {
        return $client->dataCenters()->listDatacenters($queryParameters);
    }
}
