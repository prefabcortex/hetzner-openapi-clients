<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\AddServerToPlacementGroupClientErrorException;
use Prefabcortex\Hetzner\Exception\AddServerToPlacementGroupServerErrorException;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\AddServerToPlacementGroupBody;

final class AddServerToPlacementGroupExample
{
    /**
     * Adds a Server to a Placement Group.
     *
     * Server must be powered off for this command to succeed.
     *
     * #### Operation specific errors
     *
     * | Status | Code | Description |
     * | --- | --- | --- |
     * | `422` | `server_not_stopped` | The action requires a stopped server |
     * | `422` | `already_in_placement_group` | The server is already part of a placement group |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   AddServerToPlacementGroupExample::addServerToPlacementGroup($client, $id, AddServerToPlacementGroupExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws AddServerToPlacementGroupClientErrorException
     * @throws AddServerToPlacementGroupServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function addServerToPlacementGroup(
        Client $client,
        int $id,
        AddServerToPlacementGroupBody $requestBody,
    ): ActionResponse {
        return $client->serverActions()->addServerToPlacementGroup(
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
    public static function buildExampleRequestBody(): AddServerToPlacementGroupBody
    {
        return AddServerToPlacementGroupBody::builder(1)->build();
    }
}
