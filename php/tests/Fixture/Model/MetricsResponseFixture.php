<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\MetricsResponse;
use Prefabcortex\Hetzner\Model\MetricsResponseMetrics;
use Prefabcortex\Hetzner\Validator\MetricsResponseConstraint;
use Symfony\Component\Validator\Constraint;

final class MetricsResponseFixture
{
    public static function build(): MetricsResponse
    {
        $metrics = MetricsResponseMetrics::builder(
            // start
            new DateTime('2024-01-01'),
            // end
            new DateTime('2024-01-01'),
            // step
            60.0,
            // timeSeries
            [],
        )->build();

        return MetricsResponse::builder($metrics)->build();
    }

    /** @return callable(array<int|string, mixed>): MetricsResponse */
    public static function reader(): callable
    {
        return MetricsResponse::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return MetricsResponseConstraint::constraints();
    }
}
