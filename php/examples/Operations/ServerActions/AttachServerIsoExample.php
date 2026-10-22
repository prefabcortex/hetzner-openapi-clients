<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\AttachServerIsoClientErrorException;
use Prefabcortex\Hetzner\Exception\AttachServerIsoServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\AttachServerIsoBody;

final class AttachServerIsoExample
{
    /**
     * Attaches an ISO to a Server. The Server will immediately see it as a new disk. An already
     * attached ISO will automatically be detached before the new ISO is attached.
     *
     * Servers with attached ISOs have a modified boot order: They will try to boot from the ISO
     * first before falling back to hard disk.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   AttachServerIsoExample::attachServerIso($client, $id, AttachServerIsoExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws AttachServerIsoClientErrorException
     * @throws AttachServerIsoServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function attachServerIso(
        Client $client,
        int $id,
        AttachServerIsoBody $requestBody,
    ): ActionResponse {
        return $client->serverActions()->attachServerIso(
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
    public static function buildExampleRequestBody(): AttachServerIsoBody
    {
        return AttachServerIsoBody::builder('FreeBSD-11.0-RELEASE-amd64-dvd1')->build();
    }
}
