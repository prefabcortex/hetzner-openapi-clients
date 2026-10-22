<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Operations\StorageBoxSubaccounts;

use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedDataException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Http\JsonBody;
use Prefabcortex\Hetzner\Http\ValidationMode;
use Prefabcortex\Hetzner\Parameter\ListStorageBoxSubaccountsQueryParameters;
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ActionResponseFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\CreateStorageBoxSubaccountBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\CreateStorageBoxSubaccountResponse201Fixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ListStorageBoxSubaccountsResponse200Fixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\SubaccountResponseFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\UpdateStorageBoxSubaccountBodyFixture;
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
    public function testStorageBoxSubaccountsListStorageBoxSubaccountsReads200(): void
    {
        $body = JsonBody::encode(ListStorageBoxSubaccountsResponse200Fixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxSubaccounts()->listStorageBoxSubaccounts(
                1,
                new ListStorageBoxSubaccountsQueryParameters(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'listStorageBoxSubaccounts',
                    200,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
        self::assertEquals(ListStorageBoxSubaccountsResponse200Fixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testStorageBoxSubaccountsListStorageBoxSubaccountsRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxSubaccounts()->listStorageBoxSubaccounts(
                1,
                new ListStorageBoxSubaccountsQueryParameters(),
            );
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'listStorageBoxSubaccounts',
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
                    'listStorageBoxSubaccounts',
                    200,
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
    public function testStorageBoxSubaccountsCreateStorageBoxSubaccountReads201(): void
    {
        $body = JsonBody::encode(CreateStorageBoxSubaccountResponse201Fixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxSubaccounts()->createStorageBoxSubaccount(
                1,
                CreateStorageBoxSubaccountBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'createStorageBoxSubaccount',
                    201,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
        self::assertEquals(CreateStorageBoxSubaccountResponse201Fixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testStorageBoxSubaccountsCreateStorageBoxSubaccountRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxSubaccounts()->createStorageBoxSubaccount(
                1,
                CreateStorageBoxSubaccountBodyFixture::build(),
            );
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'createStorageBoxSubaccount',
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
                    'createStorageBoxSubaccount',
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
    public function testStorageBoxSubaccountsDeleteStorageBoxSubaccountReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxSubaccounts()->deleteStorageBoxSubaccount(1, 1);
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'deleteStorageBoxSubaccount',
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
    public function testStorageBoxSubaccountsDeleteStorageBoxSubaccountRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxSubaccounts()->deleteStorageBoxSubaccount(1, 1);
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'deleteStorageBoxSubaccount',
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
                    'deleteStorageBoxSubaccount',
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
    public function testStorageBoxSubaccountsGetStorageBoxSubaccountReads200(): void
    {
        $body = JsonBody::encode(SubaccountResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxSubaccounts()->getStorageBoxSubaccount(1, 1);
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'getStorageBoxSubaccount',
                    200,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
        self::assertEquals(SubaccountResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testStorageBoxSubaccountsGetStorageBoxSubaccountRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxSubaccounts()->getStorageBoxSubaccount(1, 1);
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'getStorageBoxSubaccount',
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
                    'getStorageBoxSubaccount',
                    200,
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
    public function testStorageBoxSubaccountsUpdateStorageBoxSubaccountReads200(): void
    {
        $body = JsonBody::encode(SubaccountResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxSubaccounts()->updateStorageBoxSubaccount(
                1,
                1,
                UpdateStorageBoxSubaccountBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'updateStorageBoxSubaccount',
                    200,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
        self::assertEquals(SubaccountResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testStorageBoxSubaccountsUpdateStorageBoxSubaccountRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxSubaccounts()->updateStorageBoxSubaccount(
                1,
                1,
                UpdateStorageBoxSubaccountBodyFixture::build(),
            );
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'updateStorageBoxSubaccount',
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
                    'updateStorageBoxSubaccount',
                    200,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
    }
}
