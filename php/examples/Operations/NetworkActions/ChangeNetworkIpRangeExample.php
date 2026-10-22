<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\NetworkActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ChangeNetworkIpRangeClientErrorException;
use Prefabcortex\Hetzner\Exception\ChangeNetworkIpRangeServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\ChangeNetworkIpRangeBody;

final class ChangeNetworkIpRangeExample
{
    /**
     * Changes the IP range of a [Network](#tag/networks).
     *
     * The following restrictions apply to changing the IP range:
     * - IP ranges can only be extended and never shrunk.
     * - IPs can only be added to the end of the existing range, therefore only the netmask is
     *   allowed to be changed.
     *
     * To update the routes on the connected [Servers](#tag/servers), they need to be rebooted or
     * the routes to be updated manually.
     *
     * For example if the [Network](#tag/networks) has a range of `10.0.0.0/16` to extend it the new
     * range has to start with the IP `10.0.0.0` as well. The netmask `/16` can be changed to a
     * smaller one then `16` therefore increasing the IP range. A valid entry would be
     * `10.0.0.0/15`, `10.0.0.0/14` or `10.0.0.0/13` and so on.
     *
     * If a change is currently being performed on this [Network](#tag/networks), a error response
     * with code `conflict` will be returned.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   ChangeNetworkIpRangeExample::changeNetworkIpRange($client, $id, ChangeNetworkIpRangeExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ChangeNetworkIpRangeClientErrorException
     * @throws ChangeNetworkIpRangeServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function changeNetworkIpRange(
        Client $client,
        int $id,
        ChangeNetworkIpRangeBody $requestBody,
    ): ActionResponse {
        return $client->networkActions()->changeNetworkIpRange(
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
    public static function buildExampleRequestBody(): ChangeNetworkIpRangeBody
    {
        return ChangeNetworkIpRangeBody::builder('10.0.0.0/16')->build();
    }
}
