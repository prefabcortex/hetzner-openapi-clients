<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerServiceBaseHealthCheckHttp;
use Prefabcortex\Hetzner\Validator\LoadBalancerServiceBaseHealthCheckHttpConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerServiceBaseHealthCheckHttpFixture
{
    public static function build(): LoadBalancerServiceBaseHealthCheckHttp
    {
        return LoadBalancerServiceBaseHealthCheckHttp::builder(
            // domain
            'example.com',
            // path
            '/',
        )
            ->setResponse('{"status": "ok"}')
            ->setStatusCodes(['2??', '3??'])
            ->setTls(false)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerServiceBaseHealthCheckHttp */
    public static function reader(): callable
    {
        return LoadBalancerServiceBaseHealthCheckHttp::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerServiceBaseHealthCheckHttpConstraint::constraints();
    }
}
