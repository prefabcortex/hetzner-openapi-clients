<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListStorageBoxActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListStorageBoxActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListStorageBoxActionsQueryParameters;

final class ListStorageBoxActionsExample
{
    /**
     * List all Actions related to a specific Storage Box.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListStorageBoxActionsQueryParameters();
     *   ListStorageBoxActionsExample::listStorageBoxActions($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListStorageBoxActionsClientErrorException
     * @throws ListStorageBoxActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listStorageBoxActions(
        Client $client,
        int $id,
        ListStorageBoxActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->storageBoxActions()->listStorageBoxActions(
            $id,
            $queryParameters,
        );
    }
}
