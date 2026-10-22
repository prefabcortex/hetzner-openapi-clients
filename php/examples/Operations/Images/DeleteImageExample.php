<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\Images;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\DeleteImageClientErrorException;
use Prefabcortex\Hetzner\Exception\DeleteImageServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;

final class DeleteImageExample
{
    /**
     * Deletes an Image. Only Images of type `snapshot` and `backup` can be deleted.
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   DeleteImageExample::deleteImage($client, $id);
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws DeleteImageClientErrorException
     * @throws DeleteImageServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function deleteImage(
        Client $client,
        int $id,
    ): null {
        return $client->images()->deleteImage($id);
    }
}
