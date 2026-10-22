<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Pricing;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\GetPricingClientErrorException;
use Prefabcortex\Hetzner\Exception\GetPricingServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\GetPricingResponse200;

final class GetPricingExample
{
    /**
     * Returns prices for all resources available on the platform. VAT and currency of the Project
     * owner are used for calculations.
     *
     * Both net and gross prices are included in the response.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   GetPricingExample::getPricing($client);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws GetPricingClientErrorException
     * @throws GetPricingServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function getPricing(Client $client): GetPricingResponse200
    {
        return $client->pricing()->getPricing();
    }
}
