<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Images;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\ListImagesClientErrorException;
use Prefabcortex\Hetzner\Exception\ListImagesServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ListImagesResponse200;
use Prefabcortex\Hetzner\Parameter\ListImagesQueryParameters;

final class ListImagesExample
{
    /**
     * Returns all Image objects. You can select specific Image types only and sort the results by
     * using URI parameters.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   $queryParameters = new ListImagesQueryParameters();
     *   ListImagesExample::listImages($client, $queryParameters);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws ListImagesClientErrorException
     * @throws ListImagesServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function listImages(
        Client $client,
        ListImagesQueryParameters $queryParameters,
    ): ListImagesResponse200 {
        return $client->images()->listImages($queryParameters);
    }
}
