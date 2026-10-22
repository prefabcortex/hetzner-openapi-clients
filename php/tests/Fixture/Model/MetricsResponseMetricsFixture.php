<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\MetricsResponseMetrics;
use Prefabcortex\Hetzner\Validator\MetricsResponseMetricsConstraint;
use Symfony\Component\Validator\Constraint;

final class MetricsResponseMetricsFixture
{
    public static function build(): MetricsResponseMetrics
    {
        return MetricsResponseMetrics::builder(
            // start
            new DateTime('2024-01-01'),
            // end
            new DateTime('2024-01-01'),
            // step
            60.0,
            // timeSeries
            [],
        )->build();
    }

    /** @return callable(array<int|string, mixed>): MetricsResponseMetrics */
    public static function reader(): callable
    {
        return MetricsResponseMetrics::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return MetricsResponseMetricsConstraint::constraints();
    }
}
