<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Operations\StorageBoxActions;

use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedDataException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Http\JsonBody;
use Prefabcortex\Hetzner\Http\ValidationMode;
use Prefabcortex\Hetzner\Parameter\ListStorageBoxActionsQueryParameters;
use Prefabcortex\Hetzner\Parameter\ListStorageBoxesActionsQueryParameters;
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ActionListResponseWithMetaFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ActionResponseFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ChangeDeleteProtectionRequestFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ChangeStorageBoxTypeBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\EnableStorageBoxSnapshotPlanBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ResetPasswordRequestFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\RollbackStorageBoxSnapshotBodyFixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\UpdateStorageBoxAccessSettingsBodyFixture;
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
    public function testStorageBoxActionsListStorageBoxesActionsReads200(): void
    {
        $body = JsonBody::encode(ActionListResponseWithMetaFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxActions()->listStorageBoxesActions(
                new ListStorageBoxesActionsQueryParameters(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'listStorageBoxesActions',
                    200,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
        self::assertEquals(ActionListResponseWithMetaFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testStorageBoxActionsListStorageBoxesActionsRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxActions()->listStorageBoxesActions(new ListStorageBoxesActionsQueryParameters());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'listStorageBoxesActions',
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
                    'listStorageBoxesActions',
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
    public function testStorageBoxActionsGetStorageBoxesActionReads200(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxActions()->getStorageBoxesAction(1);
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'getStorageBoxesAction',
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
    public function testStorageBoxActionsGetStorageBoxesActionRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxActions()->getStorageBoxesAction(1);
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'getStorageBoxesAction',
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
                    'getStorageBoxesAction',
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
    public function testStorageBoxActionsListStorageBoxActionsReads200(): void
    {
        $body = JsonBody::encode(ActionListResponseWithMetaFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxActions()->listStorageBoxActions(
                1,
                new ListStorageBoxActionsQueryParameters(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'listStorageBoxActions',
                    200,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
        self::assertEquals(ActionListResponseWithMetaFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testStorageBoxActionsListStorageBoxActionsRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxActions()->listStorageBoxActions(1, new ListStorageBoxActionsQueryParameters());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'listStorageBoxActions',
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
                    'listStorageBoxActions',
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
    public function testStorageBoxActionsGetStorageBoxActionReads200(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxActions()->getStorageBoxAction(1, 1);
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'getStorageBoxAction', 200, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(ActionResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testStorageBoxActionsGetStorageBoxActionRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxActions()->getStorageBoxAction(1, 1);
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'getStorageBoxAction',
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
                sprintf('%s answered %d with %s: %s', 'getStorageBoxAction', 200, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testStorageBoxActionsChangeStorageBoxProtectionReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxActions()->changeStorageBoxProtection(
                1,
                ChangeDeleteProtectionRequestFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'changeStorageBoxProtection',
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
    public function testStorageBoxActionsChangeStorageBoxProtectionRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxActions()->changeStorageBoxProtection(1, ChangeDeleteProtectionRequestFixture::build());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'changeStorageBoxProtection',
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
                    'changeStorageBoxProtection',
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
    public function testStorageBoxActionsChangeStorageBoxTypeReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxActions()->changeStorageBoxType(1, ChangeStorageBoxTypeBodyFixture::build());
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'changeStorageBoxType', 201, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(ActionResponseFixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testStorageBoxActionsChangeStorageBoxTypeRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxActions()->changeStorageBoxType(1, ChangeStorageBoxTypeBodyFixture::build());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'changeStorageBoxType',
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
                sprintf('%s answered %d with %s: %s', 'changeStorageBoxType', 201, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testStorageBoxActionsResetStorageBoxPasswordReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxActions()->resetStorageBoxPassword(1, ResetPasswordRequestFixture::build());
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'resetStorageBoxPassword',
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
    public function testStorageBoxActionsResetStorageBoxPasswordRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxActions()->resetStorageBoxPassword(1, ResetPasswordRequestFixture::build());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'resetStorageBoxPassword',
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
                    'resetStorageBoxPassword',
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
    public function testStorageBoxActionsUpdateStorageBoxAccessSettingsReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxActions()->updateStorageBoxAccessSettings(
                1,
                UpdateStorageBoxAccessSettingsBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'updateStorageBoxAccessSettings',
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
    public function testStorageBoxActionsUpdateStorageBoxAccessSettingsRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxActions()->updateStorageBoxAccessSettings(
                1,
                UpdateStorageBoxAccessSettingsBodyFixture::build(),
            );
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'updateStorageBoxAccessSettings',
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
                    'updateStorageBoxAccessSettings',
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
    public function testStorageBoxActionsRollbackStorageBoxSnapshotReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxActions()->rollbackStorageBoxSnapshot(
                1,
                RollbackStorageBoxSnapshotBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'rollbackStorageBoxSnapshot',
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
    public function testStorageBoxActionsRollbackStorageBoxSnapshotRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxActions()->rollbackStorageBoxSnapshot(1, RollbackStorageBoxSnapshotBodyFixture::build());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'rollbackStorageBoxSnapshot',
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
                    'rollbackStorageBoxSnapshot',
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
    public function testStorageBoxActionsDisableStorageBoxSnapshotPlanReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxActions()->disableStorageBoxSnapshotPlan(1);
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'disableStorageBoxSnapshotPlan',
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
    public function testStorageBoxActionsDisableStorageBoxSnapshotPlanRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxActions()->disableStorageBoxSnapshotPlan(1);
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'disableStorageBoxSnapshotPlan',
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
                    'disableStorageBoxSnapshotPlan',
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
    public function testStorageBoxActionsEnableStorageBoxSnapshotPlanReads201(): void
    {
        $body = JsonBody::encode(ActionResponseFixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(201, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->storageBoxActions()->enableStorageBoxSnapshotPlan(
                1,
                EnableStorageBoxSnapshotPlanBodyFixture::build(),
            );
        } catch (ApiException $error) {
            self::fail(
                sprintf(
                    '%s answered %d with %s: %s',
                    'enableStorageBoxSnapshotPlan',
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
    public function testStorageBoxActionsEnableStorageBoxSnapshotPlanRejectsAnUndeclaredContentType(): void
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
            $client->storageBoxActions()->enableStorageBoxSnapshotPlan(
                1,
                EnableStorageBoxSnapshotPlanBodyFixture::build(),
            );
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'enableStorageBoxSnapshotPlan',
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
                    'enableStorageBoxSnapshotPlan',
                    201,
                    $error::class,
                    $error->getMessage(),
                ),
            );
        }
    }
}
