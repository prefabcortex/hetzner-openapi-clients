<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Examples\Operations\StorageBoxActions;

use Prefabcortex\Hetzner\Client;
use Prefabcortex\Hetzner\Exception\ApiException;
use Prefabcortex\Hetzner\Exception\EnableStorageBoxSnapshotPlanClientErrorException;
use Prefabcortex\Hetzner\Exception\EnableStorageBoxSnapshotPlanServerErrorException;
use Prefabcortex\Hetzner\Exception\MalformedResponseException;
use Prefabcortex\Hetzner\Exception\ResponseValidationException;
use Prefabcortex\Hetzner\Exception\TransportException;
use Prefabcortex\Hetzner\Exception\UnexpectedContentTypeException;
use Prefabcortex\Hetzner\Exception\UnexpectedStatusCodeException;
use Prefabcortex\Hetzner\Exception\UnsupportedValueException;
use Prefabcortex\Hetzner\Model\ActionResponse;
use Prefabcortex\Hetzner\Model\EnableStorageBoxSnapshotPlanBody;

final class EnableStorageBoxSnapshotPlanExample
{
    /**
     * Enables a Snapshot Plan for a [Storage Box](#tag/storage-boxes).
     *
     * Once enabled, a Snapshot Plan will create Snapshots at predefined intervals. There can only
     * ever be one Snapshot Plan. The existing Snapshot Plan will be deleted before a new one is set
     * up.
     *
     * Automatic Snapshots are retained until explicitly deleted by the user or the maximum snapshot
     * count for the plan ("max_snapshots") is exceeded.
     *
     * You can choose the specific time (UTC timezone), day of the week, and day of the month. The
     * time-related options are cron like. Some typical use cases include:
     *
     * | Interval                                   | Request body                                                  |
     * | ------------------------------------------ | ------------------------------------------------------------- |
     * | Every day at 3 o'clock                     | `{"max_snapshots":10,"minute":0,"hour":3}`                    |
     * | Every Friday at 3 o'clock                  | `{"max_snapshots":10,"minute":0,"hour":3,"day_of_week": 5}`   |
     * | On the first of every month at half past 6 | `{"max_snapshots":10,"minute":30,"hour":6,"day_of_month": 1}` |
     *
     * Usage: pass an already-authenticated Client (see examples/Auth/).
     *
     *   $client = Client::withAPIToken($token, $config); // see examples/Auth/
     *   EnableStorageBoxSnapshotPlanExample::enableStorageBoxSnapshotPlan($client, $id, EnableStorageBoxSnapshotPlanExample::buildExampleRequestBody());
     *
     * @throws ApiException
     * @throws UnsupportedValueException
     * @throws TransportException
     * @throws ResponseValidationException
     * @throws MalformedResponseException
     * @throws EnableStorageBoxSnapshotPlanClientErrorException
     * @throws EnableStorageBoxSnapshotPlanServerErrorException
     * @throws UnexpectedContentTypeException
     * @throws UnexpectedStatusCodeException
     */
    public static function enableStorageBoxSnapshotPlan(
        Client $client,
        int $id,
        EnableStorageBoxSnapshotPlanBody $requestBody,
    ): ActionResponse {
        return $client->storageBoxActions()->enableStorageBoxSnapshotPlan(
            $id,
            $requestBody,
        );
    }

    /**
     * NOTE: This is a structurally valid skeleton generated from the OpenAPI schema (required
     * properties, plus optional properties that carry a spec `example:`). oneOf/anyOf alternatives
     * always pick the first option. It does NOT encode business rules the spec only documents in
     * prose (e.g. "either X or Y must be set"). Review the values and the API documentation before
     * production use.
     */
    public static function buildExampleRequestBody(): EnableStorageBoxSnapshotPlanBody
    {
        return EnableStorageBoxSnapshotPlanBody::builder(
            // maxSnapshots
            10,
            // minute
            30,
            // hour
            3,
        )
            ->setDayOfWeek(7)
            ->build();
    }
}
