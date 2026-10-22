<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Operations\ServerTypes;

use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedDataException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Http\JsonBody;
use Prefabcortex\Hetzner\Http\ValidationMode;
use Prefabcortex\Hetzner\Parameter\ListServerTypesQueryParameters;
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\Model\GetServerTypeResponse200Fixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ListServerTypesResponse200Fixture;
use Prefabcortex\Hetzner\Tests\Fixture\RecordingHttpClient;
use RuntimeException;

use function sprintf;

/**
 * Every response an operation reads, answered once through the method that reads it.
 *
 * A recorded client answers with the status and content type of one branch and a body built from
 * the model fixtures; the test checks that the model comes back, or the declared exception with the
 * response still readable. A status no response declares and a declared status under the wrong
 * content type are answered too.
 *
 * What this cannot show: that the service sends these documents. They come from the same
 * description the client came from, so this proves the package reads what it promises.
 */
final class OperationResponseTest extends TestCase
{
    private const string BASE_URL = 'https://response-test.invalid';

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testServerTypesListServerTypesReads200(): void
    {
        $body = JsonBody::encode(ListServerTypesResponse200Fixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->serverTypes()->listServerTypes(new ListServerTypesQueryParameters());
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'listServerTypes', 200, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(ListServerTypesResponse200Fixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testServerTypesListServerTypesRejectsAnUndeclaredContentType(): void
    {
        $httpClient = new RecordingHttpClient(
            CannedResponse::answering(
                200,
                'text/html',
                '<html><body>Served by something in front of the API</body></html>',
            ),
        );
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $client->serverTypes()->listServerTypes(new ListServerTypesQueryParameters());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'listServerTypes',
                    200,
                ),
            );
        } catch (UnexpectedContentTypeException $exception) {
            self::assertSame(
                '<html><body>Served by something in front of the API</body></html>',
                $exception->getResponse()->getBody()->getContents(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'listServerTypes', 200, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testServerTypesGetServerTypeReads200(): void
    {
        $body = JsonBody::encode(GetServerTypeResponse200Fixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->serverTypes()->getServerType(1);
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'getServerType', 200, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(GetServerTypeResponse200Fixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testServerTypesGetServerTypeRejectsAnUndeclaredContentType(): void
    {
        $httpClient = new RecordingHttpClient(
            CannedResponse::answering(
                200,
                'text/html',
                '<html><body>Served by something in front of the API</body></html>',
            ),
        );
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $client->serverTypes()->getServerType(1);
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'getServerType',
                    200,
                ),
            );
        } catch (UnexpectedContentTypeException $exception) {
            self::assertSame(
                '<html><body>Served by something in front of the API</body></html>',
                $exception->getResponse()->getBody()->getContents(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'getServerType', 200, $error::class, $error->getMessage()),
            );
        }
    }
}
