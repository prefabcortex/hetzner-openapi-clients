<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthCheckHttp;
use Prefabcortex\Hetzner\Validator\HealthCheckHttpConstraint;
use Symfony\Component\Validator\Constraint;

final class HealthCheckHttpFixture
{
    public static function build(): HealthCheckHttp
    {
        return HealthCheckHttp::builder()
            ->setDomain('example.com')
            ->setPath('/')
            ->setResponse('{"status": "ok"}')
            ->setStatusCodes(['2??', '3??'])
            ->setTls(false)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): HealthCheckHttp */
    public static function reader(): callable
    {
        return HealthCheckHttp::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return HealthCheckHttpConstraint::constraints();
    }
}
