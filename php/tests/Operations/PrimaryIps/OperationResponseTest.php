<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Operations\PrimaryIps;

use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedDataException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Http\JsonBody;
use Prefabcortex\Hetzner\Http\ValidationMode;
use Prefabcortex\Hetzner\Parameter\ListPrimaryIpsQueryParameters;
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\Model\CreatePrimaryIpBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\CreatePrimaryIpResponse201Fixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ListPrimaryIpsResponse200Fixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\PrimaryIPResponseFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\UpdatePrimaryIpBodyFixture;
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
    public function testPrimaryIpsListPrimaryIpsReads200(): void
    {
        $body = JsonBody::encode(ListPrimaryIpsResponse200Fixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->primaryIps()->listPrimaryIps(new ListPrimaryIpsQueryParameters());
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'listPrimaryIps', 200, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(ListPrimaryIpsResponse200Fixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testPrimaryIpsListPrimaryIpsRejectsAnUndeclaredContentType(): void
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
            $client->primaryIps()->listPrimaryIps(new ListPrimaryIpsQueryParameters());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'listPrimaryIps',
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
                sprintf('%s answered %d with %s: %s', 'listPrimaryIps', 200, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testPrimaryIpsCreatePrimaryIpReads201(): void
    {
        $body = JsonBody::encode(CreatePrimaryIpResponse201Fixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->primaryIps()->createPrimaryIp(CreatePrimaryIpBodyFixture::build());
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'createPrimaryIp', 201, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(CreatePrimaryIpResponse201Fixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testPrimaryIpsCreatePrimaryIpRejectsAnUndeclaredContentType(): void
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
            $client->primaryIps()->createPrimaryIp(CreatePrimaryIpBodyFixture::build());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'createPrimaryIp',
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
                sprintf('%s answered %d with %s: %s', 'createPrimaryIp', 201, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testPrimaryIpsGetPrimaryIpReads200(): void
    {
        $body = JsonBody::encode(PrimaryIPResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->primaryIps()->getPrimaryIp(1);
        } catch (ApiException $error) {
            self::fail(sprintf('%s answered %d with %s: %s', 'getPrimaryIp', 200, $error::class, $error->getMessage()));
        }
        self::assertEquals(PrimaryIPResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testPrimaryIpsGetPrimaryIpRejectsAnUndeclaredContentType(): void
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
            $client->primaryIps()->getPrimaryIp(1);
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'getPrimaryIp',
                    200,
                ),
            );
        } catch (UnexpectedContentTypeException $exception) {
            self::assertSame(
                '<html><body>Served by something in front of the API</body></html>',
                $exception->getResponse()->getBody()->getContents(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s answered %d with %s: %s', 'getPrimaryIp', 200, $error::class, $error->getMessage()));
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testPrimaryIpsUpdatePrimaryIpReads200(): void
    {
        $body = JsonBody::encode(PrimaryIPResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->primaryIps()->updatePrimaryIp(1, UpdatePrimaryIpBodyFixture::build());
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'updatePrimaryIp', 200, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(PrimaryIPResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testPrimaryIpsUpdatePrimaryIpRejectsAnUndeclaredContentType(): void
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
            $client->primaryIps()->updatePrimaryIp(1, UpdatePrimaryIpBodyFixture::build());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'updatePrimaryIp',
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
                sprintf('%s answered %d with %s: %s', 'updatePrimaryIp', 200, $error::class, $error->getMessage()),
            );
        }
    }
}
