<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\CertificateActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\RetryCertificateClientErrorException;
use Prefabcortex\Hetzner\Exception\RetryCertificateServerErrorException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;

final class RetryCertificateExample
{
    /**
     * Retry a failed Certificate issuance or renewal.
     *
     * Only applicable if the type of the Certificate is `managed` and the issuance or renewal
     * status is `failed`.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * |  | `caa_record_does_not_allow_ca` | CAA record does not allow certificate authority |
     * |  | `ca_dns_validation_failed` | Certificate Authority: DNS validation failed |
     * |  | `ca_too_many_authorizations_failed_recently` | Certificate Authority: Too many authorizations failed recently |
     * |  | `ca_too_many_certificates_issued_for_registered_domain` | Certificate Authority: Too many certificates issued for registered domain |
     * |  | `ca_too_many_duplicate_certificates` | Certificate Authority: Too many duplicate certificates |
     * |  | `could_not_verify_domain_delegated_to_zone` | Could not verify domain delegated to zone |
     * |  | `dns_zone_not_found` | DNS zone not found |
     * |  | `dns_zone_is_secondary_zone` | DNS zone is a secondary zone |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   RetryCertificateExample::retryCertificate($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws RetryCertificateClientErrorException
     * @throws RetryCertificateServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function retryCertificate(
        Client $client,
        int $id,
    ): ActionResponse {
        return $client->certificateActions()->retryCertificate($id);
    }
}
