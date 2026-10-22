<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerServiceHTTPSProtocolPropertiesHttp;
use Prefabcortex\Hetzner\Validator\LoadBalancerServiceHTTPSProtocolPropertiesHttpConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerServiceHTTPSProtocolPropertiesHttpFixture
{
    public static function build(): LoadBalancerServiceHTTPSProtocolPropertiesHttp
    {
        return LoadBalancerServiceHTTPSProtocolPropertiesHttp::builder(
            // cookieName
            'HCLBSTICKY',
            // cookieLifetime
            300,
            // timeoutIdle
            50,
            // certificates
            [897],
            // redirectHttp
            true,
            // stickySessions
            true,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerServiceHTTPSProtocolPropertiesHttp */
    public static function reader(): callable
    {
        return LoadBalancerServiceHTTPSProtocolPropertiesHttp::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerServiceHTTPSProtocolPropertiesHttpConstraint::constraints();
    }
}
