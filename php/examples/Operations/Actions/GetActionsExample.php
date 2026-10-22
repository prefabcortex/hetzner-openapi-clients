<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Actions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\GetActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponse;
use Prefabcortex\Hetzner\Parameter\GetActionsQueryParameters;

final class GetActionsExample
{
    /**
     * Returns multiple Action objects specified by the `id` parameter.
     *
     * Note**: This endpoint previously allowed listing all actions in the project. This
     * functionality was deprecated in July 2023 and removed on 30 January 2025.
     *
     * - Announcement:
     *   https://docs.hetzner.cloud/changelog#2023-07-20-actions-list-endpoint-is-deprecated
     * - Removal:
     *   https://docs.hetzner.cloud/changelog#2025-01-30-listing-arbitrary-actions-in-the-actions-list-endpoint-is-removed
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new GetActionsQueryParameters($id);
     *   GetActionsExample::getActions($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetActionsClientErrorException
     * @throws GetActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getActions(
        Client $client,
        GetActionsQueryParameters $queryParameters,
    ): ActionListResponse {
        return $client->actions()->getActions($queryParameters);
    }
}
