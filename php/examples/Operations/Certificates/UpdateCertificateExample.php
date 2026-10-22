<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Certificates;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateCertificateClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateCertificateServerErrorException;
use Prefabcortex\Hetzner\Model\CertificateResponse;
use Prefabcortex\Hetzner\Model\UpdateCertificateBody;

final class UpdateCertificateExample
{
    /**
     * Updates the Certificate properties.
     *
     * Note: if the Certificate object changes during the request, the response will be a “conflict”
     * error.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateCertificateExample::updateCertificate($client, $id, UpdateCertificateExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateCertificateClientErrorException
     * @throws UpdateCertificateServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateCertificate(
        Client $client,
        int $id,
        UpdateCertificateBody $requestBody,
    ): CertificateResponse {
        return $client->certificates()->updateCertificate(
            $id,
            $requestBody,
        );
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildExampleRequestBody(): UpdateCertificateBody
    {
        return UpdateCertificateBody::builder()
            ->setName('my website cert')
            ->build();
    }
}
