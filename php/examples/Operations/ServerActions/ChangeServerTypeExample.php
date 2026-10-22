<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ChangeServerTypeClientErrorException;
use Prefabcortex\Hetzner\Exception\ChangeServerTypeServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ChangeServerTypeBody;

final class ChangeServerTypeExample
{
    /**
     * Changes the type (Cores, RAM and disk sizes) of a Server.
     *
     * Server must be powered off for this command to succeed.
     *
     * This copies the content of its disk, and starts it again.
     *
     * You can only migrate to Server types with the same `storage_type` and equal or bigger disks.
     * Shrinking disks is not possible as it might destroy data.
     *
     * If the disk gets upgraded, the Server type can not be downgraded any more. If you plan to
     * downgrade the Server type, set `upgrade_disk` to `false`.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `invalid_server_type` | The server type does not fit for the given server or is deprecated |
     * | `422` | `server_not_stopped` | The action requires a stopped server |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ChangeServerTypeExample::changeServerType($client, $id, ChangeServerTypeExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ChangeServerTypeClientErrorException
     * @throws ChangeServerTypeServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function changeServerType(
        Client $client,
        int $id,
        ChangeServerTypeBody $requestBody,
    ): ActionResponse {
        return $client->serverActions()->changeServerType(
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
    public static function buildExampleRequestBody(): ChangeServerTypeBody
    {
        return ChangeServerTypeBody::builder(
            // upgradeDisk
            true,
            // serverType
            'cpx22',
        )->build();
    }
}
