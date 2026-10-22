<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Operations\LoadBalancerActions;

use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Http\ValidationMode;
use Prefabcortex\Hetzner\Parameter\ListLoadBalancerActionsQueryParameters;
use Prefabcortex\Hetzner\Parameter\ListLoadBalancersActionsQueryParameters;
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\Model\AddLoadBalancerServiceBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\AddLoadBalancerTargetBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\AttachLoadBalancerToNetworkBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ChangeDeleteProtectionRequestFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ChangeLoadBalancerDnsPtrBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ChangeLoadBalancerTypeBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\DeleteLoadBalancerServiceBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\DetachLoadBalancerFromNetworkBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\LoadBalancerAlgorithmFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\LoadBalancerTargetFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\UpdateLoadBalancerServiceBodyFixture;
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
    public function testLoadBalancerActionsListLoadBalancersActionsBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->listLoadBalancersActionsRaw(new ListLoadBalancersActionsQueryParameters());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'listLoadBalancersActions', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('GET', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/actions',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsGetLoadBalancersActionBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->getLoadBalancersActionRaw(1);
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'getLoadBalancersAction', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('GET', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/actions/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsListLoadBalancerActionsBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->listLoadBalancerActionsRaw(1, new ListLoadBalancerActionsQueryParameters());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'listLoadBalancerActions', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('GET', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsAddLoadBalancerServiceBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->addLoadBalancerServiceRaw(1, AddLoadBalancerServiceBodyFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'addLoadBalancerService', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsAddLoadBalancerTargetBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->addLoadBalancerTargetRaw(1, AddLoadBalancerTargetBodyFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'addLoadBalancerTarget', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsAttachLoadBalancerToNetworkBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->attachLoadBalancerToNetworkRaw(
                1,
                AttachLoadBalancerToNetworkBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'attachLoadBalancerToNetwork', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsChangeLoadBalancerAlgorithmBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->changeLoadBalancerAlgorithmRaw(1, LoadBalancerAlgorithmFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'changeLoadBalancerAlgorithm', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsChangeLoadBalancerDnsPtrBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->changeLoadBalancerDnsPtrRaw(
                1,
                ChangeLoadBalancerDnsPtrBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'changeLoadBalancerDnsPtr', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsChangeLoadBalancerProtectionBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->changeLoadBalancerProtectionRaw(
                1,
                ChangeDeleteProtectionRequestFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'changeLoadBalancerProtection', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsChangeLoadBalancerTypeBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->changeLoadBalancerTypeRaw(1, ChangeLoadBalancerTypeBodyFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'changeLoadBalancerType', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsDeleteLoadBalancerServiceBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->deleteLoadBalancerServiceRaw(
                1,
                DeleteLoadBalancerServiceBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'deleteLoadBalancerService', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsDetachLoadBalancerFromNetworkBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->detachLoadBalancerFromNetworkRaw(
                1,
                DetachLoadBalancerFromNetworkBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'detachLoadBalancerFromNetwork', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsDisableLoadBalancerPublicInterfaceBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->disableLoadBalancerPublicInterfaceRaw(1);
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s could not be called: %s', 'disableLoadBalancerPublicInterface', $error->getMessage()),
            );
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsEnableLoadBalancerPublicInterfaceBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->enableLoadBalancerPublicInterfaceRaw(1);
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s could not be called: %s', 'enableLoadBalancerPublicInterface', $error->getMessage()),
            );
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsRemoveLoadBalancerTargetBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->removeLoadBalancerTargetRaw(1, LoadBalancerTargetFixture::build());
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'removeLoadBalancerTarget', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsUpdateLoadBalancerServiceBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->updateLoadBalancerServiceRaw(
                1,
                UpdateLoadBalancerServiceBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'updateLoadBalancerService', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('POST', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws RuntimeException
     */
    public function testLoadBalancerActionsGetLoadBalancerActionBuildsARequest(): void
    {
        $httpClient = new RecordingHttpClient(CannedResponse::empty());
        try {
            $client = Client::create(
                ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                    ValidationMode::Strict,
                ),
            );
            $client->loadBalancerActions()->getLoadBalancerActionRaw(1, 1);
        } catch (ApiException $error) {
            self::fail(sprintf('%s could not be called: %s', 'getLoadBalancerAction', $error->getMessage()));
        }
        $requests = $httpClient->getRequests();
        self::assertCount(1, $requests, 'the operation did not hand exactly one request to the HTTP client');
        foreach ($requests as $request) {
            self::assertSame('GET', $request->getMethod(), 'the request went out with another HTTP method');
            self::assertStringStartsWith(
                self::BASE_URL . '/load_balancers/',
                (string) $request->getUri(),
                "the request did not go to the operation's path below the configured base URL",
            );
        }
    }
}
