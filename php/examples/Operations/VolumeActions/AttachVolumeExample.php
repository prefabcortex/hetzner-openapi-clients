<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\VolumeActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\AttachVolumeClientErrorException;
use Prefabcortex\Hetzner\Exception\AttachVolumeServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\AttachVolumeBody;

final class AttachVolumeExample
{
    /**
     * Attaches a Volume to a Server. Works only if the Server is in the same Location as the
     * Volume.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   AttachVolumeExample::attachVolume($client, $id, AttachVolumeExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws AttachVolumeClientErrorException
     * @throws AttachVolumeServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function attachVolume(
        Client $client,
        int $id,
        AttachVolumeBody $requestBody,
    ): ActionResponse {
        return $client->volumeActions()->attachVolume(
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
    public static function buildExampleRequestBody(): AttachVolumeBody
    {
        return AttachVolumeBody::builder(43)
            ->setAutomount(false)
            ->build();
    }
}
