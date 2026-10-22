<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Operations\DataCenters;

use InvalidArgumentException;
use PHPUnit\Framework\TestCase;
use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\ClientConfig;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\MalformedDataException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Http\JsonBody;
use Prefabcortex\Hetzner\Http\ValidationMode;
use Prefabcortex\Hetzner\Parameter\ListDatacentersQueryParameters;
use Prefabcortex\Hetzner\Tests\Fixture\CannedResponse;
use Prefabcortex\Hetzner\Tests\Fixture\Model\GetDatacenterResponse200Fixture;
use Prefabcortex\Hetzner\Tests\Fixture\Model\ListDatacentersResponse200Fixture;
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
    public function testDataCentersListDatacentersReads200(): void
    {
        $body = JsonBody::encode(ListDatacentersResponse200Fixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->dataCenters()->listDatacenters(new ListDatacentersQueryParameters());
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'listDatacenters', 200, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(ListDatacentersResponse200Fixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testDataCentersListDatacentersRejectsAnUndeclaredContentType(): void
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
            $client->dataCenters()->listDatacenters(new ListDatacentersQueryParameters());
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'listDatacenters',
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
                sprintf('%s answered %d with %s: %s', 'listDatacenters', 200, $error::class, $error->getMessage()),
            );
        }
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testDataCentersGetDatacenterReads200(): void
    {
        $body = JsonBody::encode(GetDatacenterResponse200Fixture::build());
        $httpClient = new RecordingHttpClient(CannedResponse::answering(200, 'application/json', $body));
        $client = Client::create(
            ClientConfig::forBaseUrl(self::BASE_URL)->withHttpClient($httpClient)->withValidation(
                ValidationMode::Strict,
            ),
        );
        try {
            $result = $client->dataCenters()->getDatacenter(1);
        } catch (ApiException $error) {
            self::fail(
                sprintf('%s answered %d with %s: %s', 'getDatacenter', 200, $error::class, $error->getMessage()),
            );
        }
        self::assertEquals(GetDatacenterResponse200Fixture::build(), $result);
    }

    /**
     * @throws InvalidArgumentException
     * @throws MalformedDataException
     * @throws RuntimeException
     */
    public function testDataCentersGetDatacenterRejectsAnUndeclaredContentType(): void
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
            $client->dataCenters()->getDatacenter(1);
            self::fail(
                sprintf(
                    '%s did not throw UnexpectedContentTypeException for a %d response it cannot read',
                    'getDatacenter',
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
                sprintf('%s answered %d with %s: %s', 'getDatacenter', 200, $error::class, $error->getMessage()),
            );
        }
    }
}
