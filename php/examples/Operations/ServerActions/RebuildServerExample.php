<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\RebuildServerClientErrorException;
use Prefabcortex\Hetzner\Exception\RebuildServerServerErrorException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\RebuildServerBody;
use Prefabcortex\Hetzner\Model\RebuildServerResponse201;

final class RebuildServerExample
{
    /**
     * Rebuilds a Server overwriting its disk with the content of an Image, thereby **destroying all
     * data** on the target Server.
     *
     * The Image can either be one you have created earlier (`backup` or `snapshot` Image) or it can
     * be a completely fresh `system` Image provided by us. You can get a list of all available
     * Images with `GET /images`.
     *
     * Your Server will automatically be powered off before the rebuild command executes.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   RebuildServerExample::rebuildServer($client, $id, RebuildServerExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws RebuildServerClientErrorException
     * @throws RebuildServerServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function rebuildServer(
        Client $client,
        int $id,
        RebuildServerBody $requestBody,
    ): RebuildServerResponse201 {
        return $client->serverActions()->rebuildServer(
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
    public static function buildExampleRequestBody(): RebuildServerBody
    {
        return RebuildServerBody::builder('ubuntu-24.04')
            ->setUserData('#cloud-config
runcmd:
- [touch, /root/cloud-init-worked]
')
            ->build();
    }
}
