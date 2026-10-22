<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests;

use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Http\ValidationMode;
use Prefabcortex\Hetzner\Parameter\GetActionsQueryParameters;
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\RecordingHttpClient;
use RuntimeException;

use function print_r;
use function sprintf;

/**
 * Each way of building a client, called against an operation that requires exactly the credentials
 * it takes — or, for a scheme the description declares and no operation requires, against the first
 * operation there is: such a client signs every request.
 *
 * The assertions look only at what the credentials put on the wire: a header, a query parameter, an
 * `Authorization` line. Where a requirement names several schemes, all of their marks are checked
 * on the same request — half a signature is no signature.
 *
 * A factory whose credentials no operation in this description requires as they stand has no test
 * here: nothing it signs could be observed.
 */
final class AuthenticationTest extends TestCase
{
    private const string BASE_URL = 'https://auth-test.invalid';

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testWithAPITokenSignsTheRequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::withAPIToken(
                'placeholder-credential',
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            self::assertStringNotContainsString(
                'placeholder-credential',
                print_r($client, true),
                'printing the client shows its credentials',
            );
            $client->actions()->getActionsRaw(new GetActionsQueryParameters([]));
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'withAPIToken', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame(
                'Bearer placeholder-credential',
                $request->getHeaderLine('Authorization'),
                'the request went out without the credentials of the "APIToken" scheme',
            );
        }
    }
}
