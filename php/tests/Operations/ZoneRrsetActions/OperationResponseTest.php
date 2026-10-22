<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Operations\ZoneRrsetActions;

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
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ActionResponseFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\AddZoneRrsetRecordsBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ChangeZoneRrsetTtlBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\RRSetProtectionFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\RRSetRecordsRequestFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\UpdateZoneRrsetRecordsBodyFixture;
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
    public function testZoneRrsetActionsChangeZoneRrsetProtectionReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->zoneRrsetActions()->changeZoneRrsetProtection(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                RRSetProtectionFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'changeZoneRrsetProtection',
                    201,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
        self::assertEquals(ActionResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsChangeZoneRrsetProtectionRejectsAnUndeclaredContentType(): void
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
            $client->zoneRrsetActions()->changeZoneRrsetProtection(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                RRSetProtectionFixture::build(),
            );
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'changeZoneRrsetProtection',
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
                sprintf(
                    '%s answered %d with %s: %s',
                    'changeZoneRrsetProtection',
                    201,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsChangeZoneRrsetTtlReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->zoneRrsetActions()->changeZoneRrsetTtl(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                ChangeZoneRrsetTtlBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'changeZoneRrsetTtl', 201, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(ActionResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsChangeZoneRrsetTtlRejectsAnUndeclaredContentType(): void
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
            $client->zoneRrsetActions()->changeZoneRrsetTtl(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                ChangeZoneRrsetTtlBodyFixture::build(),
            );
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'changeZoneRrsetTtl',
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
                sprintf('%s answered %d with %s: %s', 'changeZoneRrsetTtl', 201, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsSetZoneRrsetRecordsReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->zoneRrsetActions()->setZoneRrsetRecords(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                RRSetRecordsRequestFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'setZoneRrsetRecords', 201, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(ActionResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsSetZoneRrsetRecordsRejectsAnUndeclaredContentType(): void
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
            $client->zoneRrsetActions()->setZoneRrsetRecords(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                RRSetRecordsRequestFixture::build(),
            );
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'setZoneRrsetRecords',
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
                sprintf('%s answered %d with %s: %s', 'setZoneRrsetRecords', 201, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsAddZoneRrsetRecordsReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->zoneRrsetActions()->addZoneRrsetRecords(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                AddZoneRrsetRecordsBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'addZoneRrsetRecords', 201, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(ActionResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsAddZoneRrsetRecordsRejectsAnUndeclaredContentType(): void
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
            $client->zoneRrsetActions()->addZoneRrsetRecords(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                AddZoneRrsetRecordsBodyFixture::build(),
            );
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'addZoneRrsetRecords',
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
                sprintf('%s answered %d with %s: %s', 'addZoneRrsetRecords', 201, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsRemoveZoneRrsetRecordsReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->zoneRrsetActions()->removeZoneRrsetRecords(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                RRSetRecordsRequestFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'removeZoneRrsetRecords',
                    201,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
        self::assertEquals(ActionResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsRemoveZoneRrsetRecordsRejectsAnUndeclaredContentType(): void
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
            $client->zoneRrsetActions()->removeZoneRrsetRecords(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                RRSetRecordsRequestFixture::build(),
            );
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'removeZoneRrsetRecords',
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
                sprintf(
                    '%s answered %d with %s: %s',
                    'removeZoneRrsetRecords',
                    201,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsUpdateZoneRrsetRecordsReads200(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->zoneRrsetActions()->updateZoneRrsetRecords(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                UpdateZoneRrsetRecordsBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'updateZoneRrsetRecords',
                    200,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
        self::assertEquals(ActionResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsUpdateZoneRrsetRecordsRejectsAnUndeclaredContentType(): void
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
            $client->zoneRrsetActions()->updateZoneRrsetRecords(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                UpdateZoneRrsetRecordsBodyFixture::build(),
            );
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'updateZoneRrsetRecords',
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
                sprintf(
                    '%s answered %d with %s: %s',
                    'updateZoneRrsetRecords',
                    200,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
    }
}
