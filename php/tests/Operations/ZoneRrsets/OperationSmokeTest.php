<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Operations\ZoneRrsets;

use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Http\ValidationMode;
use Prefabcortex\Hetzner\Model\RRSetType;
use Prefabcortex\Hetzner\Parameter\ListZoneRrsetsQueryParameters;
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\Model\RRSetRequestFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\UpdateZoneRrsetBodyFixture;
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
    public function testZoneRrsetsListZoneRrsetsBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneRrsets()->listZoneRrsetsRaw('smoke-test', new ListZoneRrsetsQueryParameters());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'listZoneRrsets', $error->getMessage()));
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
    public function testZoneRrsetsCreateZoneRrsetBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneRrsets()->createZoneRrsetRaw('smoke-test', RRSetRequestFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'createZoneRrset', $error->getMessage()));
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
    public function testZoneRrsetsDeleteZoneRrsetBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneRrsets()->deleteZoneRrsetRaw('smoke-test', 'smoke-test', RRSetType::A);
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'deleteZoneRrset', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('DELETE', $request->getMethod(), 'the request went out with another HTTP method');
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
    public function testZoneRrsetsGetZoneRrsetBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneRrsets()->getZoneRrsetRaw('smoke-test', 'smoke-test', RRSetType::A);
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'getZoneRrset', $error->getMessage()));
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
    public function testZoneRrsetsUpdateZoneRrsetBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->zoneRrsets()->updateZoneRrsetRaw(
                'smoke-test',
                'smoke-test',
                RRSetType::A,
                UpdateZoneRrsetBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'updateZoneRrset', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('PUT', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/zones/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }
}
