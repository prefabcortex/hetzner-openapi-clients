<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerTypes;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListServerTypesClientErrorException;
use Prefabcortex\Hetzner\Exception\ListServerTypesServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListServerTypesResponse200;
use Prefabcortex\Hetzner\Parameter\ListServerTypesQueryParameters;

final class ListServerTypesExample
{
    /**
     * Gets all Server type objects.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListServerTypesQueryParameters();
     *   ListServerTypesExample::listServerTypes($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListServerTypesClientErrorException
     * @throws ListServerTypesServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listServerTypes(
        Client $client,
        ListServerTypesQueryParameters $queryParameters,
    ): ListServerTypesResponse200 {
        return $client->serverTypes()->listServerTypes($queryParameters);
    }
}
