<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Operations\NetworkActions;

use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Http\ValidationMode;
use Prefabcortex\Hetzner\Parameter\ListNetworkActionsQueryParameters;
use Prefabcortex\Hetzner\Parameter\ListNetworksActionsQueryParameters;
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\Model\AddNetworkSubnetBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ChangeDeleteProtectionRequestFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ChangeNetworkIpRangeBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\DeleteNetworkSubnetBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\RouteFixture;
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
    public function testNetworkActionsListNetworksActionsBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->networkActions()->listNetworksActionsRaw(new ListNetworksActionsQueryParameters());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'listNetworksActions', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('GET', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/networks/actions',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testNetworkActionsGetNetworksActionBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->networkActions()->getNetworksActionRaw(1);
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'getNetworksAction', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('GET', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/networks/actions/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testNetworkActionsListNetworkActionsBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->networkActions()->listNetworkActionsRaw(1, new ListNetworkActionsQueryParameters());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'listNetworkActions', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('GET', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/networks/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testNetworkActionsAddNetworkRouteBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->networkActions()->addNetworkRouteRaw(1, RouteFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'addNetworkRoute', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/networks/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testNetworkActionsAddNetworkSubnetBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->networkActions()->addNetworkSubnetRaw(1, AddNetworkSubnetBodyFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'addNetworkSubnet', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/networks/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testNetworkActionsChangeNetworkIpRangeBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->networkActions()->changeNetworkIpRangeRaw(1, ChangeNetworkIpRangeBodyFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'changeNetworkIpRange', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/networks/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testNetworkActionsChangeNetworkProtectionBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->networkActions()->changeNetworkProtectionRaw(1, ChangeDeleteProtectionRequestFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'changeNetworkProtection', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/networks/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testNetworkActionsDeleteNetworkRouteBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->networkActions()->deleteNetworkRouteRaw(1, RouteFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'deleteNetworkRoute', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/networks/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testNetworkActionsDeleteNetworkSubnetBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->networkActions()->deleteNetworkSubnetRaw(1, DeleteNetworkSubnetBodyFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'deleteNetworkSubnet', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/networks/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testNetworkActionsGetNetworkActionBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->networkActions()->getNetworkActionRaw(1, 1);
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'getNetworkAction', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('GET', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/networks/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }
}
