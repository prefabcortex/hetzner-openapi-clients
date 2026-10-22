<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Volumes;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateVolumeClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateVolumeServerErrorException;
use Prefabcortex\Hetzner\Model\UpdateVolumeBody;
use Prefabcortex\Hetzner\Model\VolumeResponse;

final class UpdateVolumeExample
{
    /**
     * Updates the Volume properties.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateVolumeExample::updateVolume($client, $id, UpdateVolumeExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateVolumeClientErrorException
     * @throws UpdateVolumeServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateVolume(
        Client $client,
        int $id,
        UpdateVolumeBody $requestBody,
    ): VolumeResponse {
        return $client->volumes()->updateVolume(
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
    public static function buildExampleRequestBody(): UpdateVolumeBody
    {
        return UpdateVolumeBody::builder()
            ->setName('database-storage')
            ->build();
    }
}
