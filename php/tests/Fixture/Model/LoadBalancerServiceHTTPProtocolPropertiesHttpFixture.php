<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerServiceHTTPProtocolPropertiesHttp;
use Prefabcortex\Hetzner\Validator\LoadBalancerServiceHTTPProtocolPropertiesHttpConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerServiceHTTPProtocolPropertiesHttpFixture
{
    public static function build(): LoadBalancerServiceHTTPProtocolPropertiesHttp
    {
        return LoadBalancerServiceHTTPProtocolPropertiesHttp::builder(
            // cookieName
            'HCLBSTICKY',
            // cookieLifetime
            300,
            // timeoutIdle
            50,
            // stickySessions
            true,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerServiceHTTPProtocolPropertiesHttp */
    public static function reader(): callable
    {
        return LoadBalancerServiceHTTPProtocolPropertiesHttp::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerServiceHTTPProtocolPropertiesHttpConstraint::constraints();
    }
}
