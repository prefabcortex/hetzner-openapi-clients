<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerTypes;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetServerTypeClientErrorException;
use Prefabcortex\Hetzner\Exception\GetServerTypeServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\GetServerTypeResponse200;

final class GetServerTypeExample
{
    /**
     * Gets a specific Server type object.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetServerTypeExample::getServerType($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetServerTypeClientErrorException
     * @throws GetServerTypeServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getServerType(
        Client $client,
        int $id,
    ): GetServerTypeResponse200 {
        return $client->serverTypes()->getServerType($id);
    }
}
