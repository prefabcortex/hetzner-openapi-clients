<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Volumes;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreateVolumeClientErrorException;
use Prefabcortex\Hetzner\Exception\CreateVolumeServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreateVolumeBody;
use Prefabcortex\Hetzner\Model\CreateVolumeResponse201;

final class CreateVolumeExample
{
    /**
     * Creates a new Volume attached to a Server. If you want to create a Volume that is not
     * attached to a Server, you need to provide the `location` key instead of `server`. This can be
     * either the ID or the name of the Location this Volume will be created in. Note that a Volume
     * can be attached to a Server only in the same Location as the Volume itself.
     *
     * Specifying the Server during Volume creation will automatically attach the Volume to that
     * Server after it has been initialized. In that case, the `next_actions` key in the response is
     * an array which contains a single `attach_volume` action.
     *
     * The minimum Volume size is 10GB and the maximum size is 10TB (10240GB).
     *
     * A volume’s name can consist of alphanumeric characters, dashes, underscores, and dots, but
     * has to start and end with an alphanumeric character. The total length is limited to 64
     * characters. Volume names must be unique per Project.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `no_space_left_in_location` | There is no volume space left in the given location |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreateVolumeExample::createVolume($client, CreateVolumeExample::buildDefault());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreateVolumeClientErrorException
     * @throws CreateVolumeServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createVolume(
        Client $client,
        CreateVolumeBody $requestBody,
    ): CreateVolumeResponse201 {
        return $client->volumes()->createVolume($requestBody);
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildDefault(): CreateVolumeBody
    {
        return CreateVolumeBody::builder(
            // size
            42,
            // name
            'test-database',
        )
            ->setLabels(['key' => 'value'])
            ->setAutomount(false)
            ->setFormat('xfs')
            ->setLocation('nbg1')
            ->build();
    }
}
