<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Operations\ZoneRrsetActions;

use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Http\ValidationMode;
use Prefabcortex\Hetzner\Model\RRSetType;
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\Model\AddZoneRrsetRecordsBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ChangeZoneRrsetTtlBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\RRSetProtectionFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\RRSetRecordsRequestFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\UpdateZoneRrsetRecordsBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\RecordingHttpClient;
use RuntimeException;

use function sprintf;

/**
 * Every operation called once, against a client that records the request instead of sending it.
 *
 * Nothing leaves the process and no credentials are needed: PSR-18 is one method, so the client is
 * stood in for. What runs is everything up to the wire — the URI assembled, the query string
 * encoded, the body serialised. The client signs nothing.
 *
 * What is watched is the request: its method, and its path up to the first placeholder. These calls
 * go through the `…Raw()` methods, which hand the response back unparsed, so the canned answer
 * never has to match a status or content type from the description — an answer invented from that
 * document would say nothing about a client built from the same one.
 */
final class OperationSmokeTest extends TestCase
{
    private const string BASE_URL = 'https://smoke-test.invalid';

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsChangeZoneRrsetProtectionBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneRrsetActions()->changeZoneRrsetProtectionRaw(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                RRSetProtectionFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'changeZoneRrsetProtection', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/zones/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsChangeZoneRrsetTtlBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneRrsetActions()->changeZoneRrsetTtlRaw(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                ChangeZoneRrsetTtlBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'changeZoneRrsetTtl', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/zones/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsSetZoneRrsetRecordsBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneRrsetActions()->setZoneRrsetRecordsRaw(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                RRSetRecordsRequestFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'setZoneRrsetRecords', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/zones/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsAddZoneRrsetRecordsBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneRrsetActions()->addZoneRrsetRecordsRaw(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                AddZoneRrsetRecordsBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'addZoneRrsetRecords', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/zones/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsRemoveZoneRrsetRecordsBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneRrsetActions()->removeZoneRrsetRecordsRaw(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                RRSetRecordsRequestFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'removeZoneRrsetRecords', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/zones/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testZoneRrsetActionsUpdateZoneRrsetRecordsBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneRrsetActions()->updateZoneRrsetRecordsRaw(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                UpdateZoneRrsetRecordsBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'updateZoneRrsetRecords', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/zones/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }
}
