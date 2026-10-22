<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\CertificateActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListCertificateActionsClientErrorException;
use Prefabcortex\Hetzner\Exception\ListCertificateActionsServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Parameter\ListCertificateActionsQueryParameters;

final class ListCertificateActionsExample
{
    /**
     * Returns all Action objects for a Certificate. You can sort the results by using the `sort`
     * URI parameter, and filter them with the `status` parameter.
     *
     * Only type `managed` Certificates can have Actions. For type `uploaded` Certificates the
     * `actions` key will always contain an empty array.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListCertificateActionsQueryParameters();
     *   ListCertificateActionsExample::listCertificateActions($client, $id, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListCertificateActionsClientErrorException
     * @throws ListCertificateActionsServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listCertificateActions(
        Client $client,
        int $id,
        ListCertificateActionsQueryParameters $queryParameters,
    ): ActionListResponseWithMeta {
        return $client->certificateActions()->listCertificateActions(
            $id,
            $queryParameters,
        );
    }
}
