<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Auth;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\NoHttpClientException;
use Prefabcortex\Hetzner\Server;
use InvalidArgumentException;
use RuntimeException;

use function getenv;

/**
 * Example: authenticate against the "APIToken" scheme.
 *
 * This scheme expects a pre-issued bearer token (e.g. a personal access
 * token) — no token exchange is performed here.
 *
 * Usage: set APITOKEN_TOKEN in the environment, then
 *
 *   $client = getAPITokenClient();
 *
 * @throws RuntimeException
 * @throws InvalidArgumentException
 * @throws NoHttpClientException
 */
function getAPITokenClient(): Client
{
    $token = getenv('APITOKEN_TOKEN');

    if (false === $token) {
        throw new RuntimeException('Set APITOKEN_TOKEN before running this example — see the comment above for how to obtain a token.');
    }

    return Client::withAPIToken($token, ClientConfig::forServer(Server::ApiHetznerCloud));
}
