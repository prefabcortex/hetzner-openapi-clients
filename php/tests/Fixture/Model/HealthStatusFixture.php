<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthStatus;
use Prefabcortex\Hetzner\Model\HealthStatusDetail;
use Prefabcortex\Hetzner\Model\HealthStatusStatus;
use Prefabcortex\Hetzner\Validator\HealthStatusConstraint;
use Symfony\Component\Validator\Constraint;

final class HealthStatusFixture
{
    public static function build(): HealthStatus
    {
        return HealthStatus::builder(
            // listenPort
            443,
            // status
            HealthStatusStatus::healthy,
        )
            ->setDetail(HealthStatusDetail::unexpected_http_status)
            ->setHttpStatusCode(503)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): HealthStatus */
    public static function reader(): callable
    {
        return HealthStatus::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return HealthStatusConstraint::constraints();
    }
}
