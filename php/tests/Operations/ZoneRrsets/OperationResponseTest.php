<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Operations\ZoneRrsets;

use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedDataException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Http\JsonBody;
use Prefabcortex\Hetzner\Http\ValidationMode;
use Prefabcortex\Hetzner\Model\RRSetType;
use Prefabcortex\Hetzner\Parameter\ListZoneRrsetsQueryParameters;
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ActionResponseFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\CreateZoneRrsetResponse201Fixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ListZoneRrsetsResponse200Fixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\RRSetRequestFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\RrsetResponseFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\UpdateZoneRrsetBodyFixture;
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
    public function testZoneRrsetsListZoneRrsetsReads200(): void
    {
        $body = JsonBody::encode(ListZoneRrsetsResponse200Fixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->zoneRrsets()->listZoneRrsets('smoke-test', new ListZoneRrsetsQueryParameters());
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'listZoneRrsets', 200, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(ListZoneRrsetsResponse200Fixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetsListZoneRrsetsRejectsAnUndeclaredContentType(): void
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
            $client->zoneRrsets()->listZoneRrsets('smoke-test', new ListZoneRrsetsQueryParameters());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'listZoneRrsets',
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
                sprintf('%s answered %d with %s: %s', 'listZoneRrsets', 200, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetsCreateZoneRrsetReads201(): void
    {
        $body = JsonBody::encode(CreateZoneRrsetResponse201Fixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->zoneRrsets()->createZoneRrset('smoke-test', RRSetRequestFixture::build());
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'createZoneRrset', 201, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(CreateZoneRrsetResponse201Fixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetsCreateZoneRrsetRejectsAnUndeclaredContentType(): void
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
            $client->zoneRrsets()->createZoneRrset('smoke-test', RRSetRequestFixture::build());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'createZoneRrset',
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
                sprintf('%s answered %d with %s: %s', 'createZoneRrset', 201, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetsDeleteZoneRrsetReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->zoneRrsets()->deleteZoneRrset('smoke-test', 'smoke-test', RRSetType::A);
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'deleteZoneRrset', 201, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(ActionResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetsDeleteZoneRrsetRejectsAnUndeclaredContentType(): void
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
            $client->zoneRrsets()->deleteZoneRrset('smoke-test', 'smoke-test', RRSetType::A);
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'deleteZoneRrset',
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
                sprintf('%s answered %d with %s: %s', 'deleteZoneRrset', 201, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetsGetZoneRrsetReads200(): void
    {
        $body = JsonBody::encode(RrsetResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->zoneRrsets()->getZoneRrset('smoke-test', 'smoke-test', RRSetType::A);
        } catch (ApiException $error) {
            self::fail(sprintf('%s answered %d with %s: %s', 'getZoneRrset', 200, $error::class, $error->getMessage()));
        }
        self::assertEquals(RrsetResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetsGetZoneRrsetRejectsAnUndeclaredContentType(): void
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
            $client->zoneRrsets()->getZoneRrset('smoke-test', 'smoke-test', RRSetType::A);
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'getZoneRrset',
                    200,
                ),
            );
        } catch (UnexpectedContentTypeException $exception) {
            self::assertSame(
                '<html><body>Served by something in front of the API</body></html>',
                $exception->getResponse()->getBody()->getContents(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s answered %d with %s: %s', 'getZoneRrset', 200, $error::class, $error->getMessage()));
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetsUpdateZoneRrsetReads200(): void
    {
        $body = JsonBody::encode(RrsetResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->zoneRrsets()->updateZoneRrset(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                UpdateZoneRrsetBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'updateZoneRrset', 200, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(RrsetResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetsUpdateZoneRrsetRejectsAnUndeclaredContentType(): void
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
            $client->zoneRrsets()->updateZoneRrset(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                UpdateZoneRrsetBodyFixture::build(),
            );
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'updateZoneRrset',
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
                sprintf('%s answered %d with %s: %s', 'updateZoneRrset', 200, $error::class, $error->getMessage()),
            );
        }
    }
}
