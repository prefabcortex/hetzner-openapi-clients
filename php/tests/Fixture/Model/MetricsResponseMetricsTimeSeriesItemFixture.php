<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\MetricsResponseMetricsTimeSeriesItem;

final class MetricsResponseMetricsTimeSeriesItemFixture
{
    public static function build(): MetricsResponseMetricsTimeSeriesItem
    {
        return MetricsResponseMetricsTimeSeriesItem::builder([['REPLACE_ME', 'REPLACE_ME']])->build();
    }

    /** @return callable(array<int|string, mixed>): MetricsResponseMetricsTimeSeriesItem */
    public static function reader(): callable
    {
        return MetricsResponseMetricsTimeSeriesItem::fromArray(...);
    }
}
