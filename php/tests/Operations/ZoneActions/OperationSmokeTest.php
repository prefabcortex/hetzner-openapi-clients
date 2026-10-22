<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Operations\ZoneActions;

use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Http\ValidationMode;
use Prefabcortex\Hetzner\Parameter\ListZoneActionsQueryParameters;
use Prefabcortex\Hetzner\Parameter\ListZonesActionsQueryParameters;
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ChangeDeleteProtectionRequestFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ChangeZonePrimaryNameserversBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ChangeZoneTtlBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ZonefileFixture;
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
    public function testZoneActionsListZonesActionsBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneActions()->listZonesActionsRaw(new ListZonesActionsQueryParameters());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'listZonesActions', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('GET', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/zones/actions',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testZoneActionsGetZonesActionBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneActions()->getZonesActionRaw(1);
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'getZonesAction', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('GET', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/zones/actions/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testZoneActionsListZoneActionsBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneActions()->listZoneActionsRaw('smoke-test', new ListZoneActionsQueryParameters());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'listZoneActions', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('GET', $request->getMethod(), 'the request went out with another HTTP method');
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
    public function testZoneActionsGetZoneActionBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneActions()->getZoneActionRaw('smoke-test', 1);
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'getZoneAction', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('GET', $request->getMethod(), 'the request went out with another HTTP method');
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
    public function testZoneActionsChangeZonePrimaryNameserversBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneActions()->changeZonePrimaryNameserversRaw(
                'smoke-test',
                ChangeZonePrimaryNameserversBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'changeZonePrimaryNameservers', $error->getMessage()));
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
    public function testZoneActionsChangeZoneProtectionBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneActions()->changeZoneProtectionRaw(
                'smoke-test',
                ChangeDeleteProtectionRequestFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'changeZoneProtection', $error->getMessage()));
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
    public function testZoneActionsChangeZoneTtlBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneActions()->changeZoneTtlRaw('smoke-test', ChangeZoneTtlBodyFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'changeZoneTtl', $error->getMessage()));
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
    public function testZoneActionsImportZoneZonefileBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneActions()->importZoneZonefileRaw('smoke-test', ZonefileFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'importZoneZonefile', $error->getMessage()));
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
