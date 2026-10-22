<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreateServerImageClientErrorException;
use Prefabcortex\Hetzner\Exception\CreateServerImageServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreateServerImageBody;
use Prefabcortex\Hetzner\Model\CreateServerImageBodyType;
use Prefabcortex\Hetzner\Model\CreateServerImageResponse201;

final class CreateServerImageExample
{
    /**
     * Creates an Image (snapshot) from a Server by copying the contents of its disks. This creates
     * a snapshot of the current state of the disk and copies it into an Image. If the Server is
     * currently running you must make sure that its disk content is consistent. Otherwise, the
     * created Image may not be readable.
     *
     * To make sure disk content is consistent, we recommend to shut down the Server prior to
     * creating an Image.
     *
     * You can either create a `backup` Image that is bound to the Server and therefore will be
     * deleted when the Server is deleted, or you can create a `snapshot` Image which is completely
     * independent of the Server it was created from and will survive Server deletion. Backup Images
     * are only available when the backup option is enabled for the Server. Snapshot Images are
     * billed on a per GB basis.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreateServerImageExample::createServerImage($client, $id, CreateServerImageExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreateServerImageClientErrorException
     * @throws CreateServerImageServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createServerImage(
        Client $client,
        int $id,
        CreateServerImageBody $requestBody,
    ): CreateServerImageResponse201 {
        return $client->serverActions()->createServerImage(
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
    public static function buildExampleRequestBody(): CreateServerImageBody
    {
        return CreateServerImageBody::builder()
            ->setDescription('my image')
            ->setType(CreateServerImageBodyType::snapshot)
            ->build();
    }
}
