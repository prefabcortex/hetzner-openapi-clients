<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Volumes;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListVolumesClientErrorException;
use Prefabcortex\Hetzner\Exception\ListVolumesServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListVolumesResponse200;
use Prefabcortex\Hetzner\Parameter\ListVolumesQueryParameters;

final class ListVolumesExample
{
    /**
     * Gets all existing Volumes that you have available.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListVolumesQueryParameters();
     *   ListVolumesExample::listVolumes($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListVolumesClientErrorException
     * @throws ListVolumesServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listVolumes(
        Client $client,
        ListVolumesQueryParameters $queryParameters,
    ): ListVolumesResponse200 {
        return $client->volumes()->listVolumes($queryParameters);
    }
}
