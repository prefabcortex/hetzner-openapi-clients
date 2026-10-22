<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Operations\FloatingIps;

use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedDataException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Http\JsonBody;
use Prefabcortex\Hetzner\Http\ValidationMode;
use Prefabcortex\Hetzner\Parameter\ListFloatingIpsQueryParameters;
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\Model\CreateFloatingIpBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\CreateFloatingIpResponse201Fixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\FloatingIpResponseFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ListFloatingIpsResponse200Fixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\UpdateFloatingIpBodyFixture;
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
    public function testFloatingIpsListFloatingIpsReads200(): void
    {
        $body = JsonBody::encode(ListFloatingIpsResponse200Fixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->floatingIps()->listFloatingIps(new ListFloatingIpsQueryParameters());
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'listFloatingIps', 200, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(ListFloatingIpsResponse200Fixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testFloatingIpsListFloatingIpsRejectsAnUndeclaredContentType(): void
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
            $client->floatingIps()->listFloatingIps(new ListFloatingIpsQueryParameters());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'listFloatingIps',
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
                sprintf('%s answered %d with %s: %s', 'listFloatingIps', 200, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testFloatingIpsCreateFloatingIpReads201(): void
    {
        $body = JsonBody::encode(CreateFloatingIpResponse201Fixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->floatingIps()->createFloatingIp(CreateFloatingIpBodyFixture::build());
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'createFloatingIp', 201, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(CreateFloatingIpResponse201Fixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testFloatingIpsCreateFloatingIpRejectsAnUndeclaredContentType(): void
    {
        $httpClient = new RecordingHttpClient(
            CannedResponse::answering(
                201,
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
            $client->floatingIps()->createFloatingIp(CreateFloatingIpBodyFixture::build());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'createFloatingIp',
                    201,
                ),
            );
        } catch (UnexpectedContentTypeException $exception) {
            self::assertSame(
                '<html><body>Served by something in front of the API</body></html>',
                $exception->getResponse()->getBody()->getContents(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'createFloatingIp', 201, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testFloatingIpsGetFloatingIpReads200(): void
    {
        $body = JsonBody::encode(FloatingIpResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->floatingIps()->getFloatingIp(1);
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'getFloatingIp', 200, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(FloatingIpResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testFloatingIpsGetFloatingIpRejectsAnUndeclaredContentType(): void
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
            $client->floatingIps()->getFloatingIp(1);
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'getFloatingIp',
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
                sprintf('%s answered %d with %s: %s', 'getFloatingIp', 200, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testFloatingIpsUpdateFloatingIpReads200(): void
    {
        $body = JsonBody::encode(FloatingIpResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->floatingIps()->updateFloatingIp(1, UpdateFloatingIpBodyFixture::build());
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'updateFloatingIp', 200, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(FloatingIpResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testFloatingIpsUpdateFloatingIpRejectsAnUndeclaredContentType(): void
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
            $client->floatingIps()->updateFloatingIp(1, UpdateFloatingIpBodyFixture::build());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'updateFloatingIp',
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
                sprintf('%s answered %d with %s: %s', 'updateFloatingIp', 200, $error::class, $error->getMessage()),
            );
        }
    }
}
