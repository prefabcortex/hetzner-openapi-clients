<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Images;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Exception\UpdateImageClientErrorException;
use Prefabcortex\Hetzner\Exception\UpdateImageServerErrorException;
use Prefabcortex\Hetzner\Model\ImageResponse;
use Prefabcortex\Hetzner\Model\UpdateImageBody;

final class UpdateImageExample
{
    /**
     * Updates the Image. You may change the description, convert a Backup Image to a Snapshot Image
     * or change the Image labels. Only Images of type `snapshot` and `backup` can be updated.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   UpdateImageExample::updateImage($client, $id, UpdateImageExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws UpdateImageClientErrorException
     * @throws UpdateImageServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function updateImage(
        Client $client,
        int $id,
        UpdateImageBody $requestBody,
    ): ImageResponse {
        return $client->images()->updateImage(
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
    public static function buildExampleRequestBody(): UpdateImageBody
    {
        return UpdateImageBody::builder()
            ->setDescription('My new Image description')
            ->build();
    }
}
