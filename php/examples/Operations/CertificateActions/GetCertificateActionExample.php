<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\CertificateActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetCertificateActionClientErrorException;
use Prefabcortex\Hetzner\Exception\GetCertificateActionServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class GetCertificateActionExample
{
    /**
     * Deprecated**: This operation is deprecated, see our
     * [changelog](https://docs.hetzner.cloud/changelog#2026-04-30-deprecate-get-resource-action-endpoints)
     * for more details.
     *
     * Returns a specific Action for a Certificate. Only type `managed` Certificates have Actions.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetCertificateActionExample::getCertificateAction($client, $id, $actionId);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetCertificateActionClientErrorException
     * @throws GetCertificateActionServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getCertificateAction(
        Client $client,
        int $id,
        int $actionId,
    ): ActionResponse {
        return $client->certificateActions()->getCertificateAction(
            $id,
            $actionId,
        );
    }
}
