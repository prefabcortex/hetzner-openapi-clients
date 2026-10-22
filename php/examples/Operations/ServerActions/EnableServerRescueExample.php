<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\ServerActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\EnableServerRescueClientErrorException;
use Prefabcortex\Hetzner\Exception\EnableServerRescueServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\EnableServerRescueBody;
use Prefabcortex\Hetzner\Model\EnableServerRescueBodyType;
use Prefabcortex\Hetzner\Model\RootPasswordResponse;

final class EnableServerRescueExample
{
    /**
     * Enable the Hetzner Rescue System for this Server. The next time a Server with enabled rescue
     * mode boots it will start a special minimal Linux distribution designed for repair and
     * reinstall.
     *
     * In case a Server cannot boot on its own you can use this to access a Server’s disks.
     *
     * Rescue Mode is automatically disabled when you first boot into it or if you do not use it for
     * 60 minutes.
     *
     * Enabling rescue mode will not
     * [reboot](https://docs.hetzner.cloud/#server-actions-soft-reboot-a-server) your Server — you
     * will have to do this yourself.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   EnableServerRescueExample::enableServerRescue($client, $id, EnableServerRescueExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws EnableServerRescueClientErrorException
     * @throws EnableServerRescueServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function enableServerRescue(
        Client $client,
        int $id,
        EnableServerRescueBody $requestBody,
    ): RootPasswordResponse {
        return $client->serverActions()->enableServerRescue(
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
    public static function buildExampleRequestBody(): EnableServerRescueBody
    {
        return EnableServerRescueBody::builder()
            ->setType(EnableServerRescueBodyType::linux64)
            ->setSshKeys([2323])
            ->build();
    }
}
