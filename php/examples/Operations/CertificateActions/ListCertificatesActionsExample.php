<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\CertificateActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListCertificatesActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListCertificatesActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListCertificatesActionsQueryParameters;

final class ListCertificatesActionsExample
{
    /**
     * Returns all Action objects. You can `sort` the results by using the sort URI parameter, and
     * filter them with the `status` and `id` parameter.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListCertificatesActionsQueryParameters();
     *   ListCertificatesActionsExample::listCertificatesActions($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListCertificatesActionsClientErrorException
     * @throws ListCertificatesActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listCertificatesActions(
        Client $client,
        ListCertificatesActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->certificateActions()->listCertificatesActions($queryParameters);
    }
}
