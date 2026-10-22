<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\PlacementGroups;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\CreatePlacementGroupClientErrorException;
use Prefabcortex\Hetzner\Exception\CreatePlacementGroupServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\CreatePlacementGroupBody;
use Prefabcortex\Hetzner\Model\CreatePlacementGroupBodyType;
use Prefabcortex\Hetzner\Model\CreatePlacementGroupResponse201;

final class CreatePlacementGroupExample
{
    /**
     * Creates a new Placement Group.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   CreatePlacementGroupExample::createPlacementGroup($client, CreatePlacementGroupExample::buildDefault());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws CreatePlacementGroupClientErrorException
     * @throws CreatePlacementGroupServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function createPlacementGroup(
        Client $client,
        CreatePlacementGroupBody $requestBody,
    ): CreatePlacementGroupResponse201 {
        return $client->placementGroups()->createPlacementGroup($requestBody);
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildDefault(): CreatePlacementGroupBody
    {
        return CreatePlacementGroupBody::builder(
            // name
            'my Placement Group',
            // type
            CreatePlacementGroupBodyType::spread,
        )->build();
    }
}
