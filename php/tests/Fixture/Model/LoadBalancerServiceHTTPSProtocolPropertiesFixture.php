<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerServiceHTTPSProtocolProperties;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceHTTPSProtocolPropertiesHttp;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceHTTPSProtocolPropertiesProtocol;
use Prefabcortex\Hetzner\Validator\LoadBalancerServiceHTTPSProtocolPropertiesConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerServiceHTTPSProtocolPropertiesFixture
{
    public static function build(): LoadBalancerServiceHTTPSProtocolProperties
    {
        $http = LoadBalancerServiceHTTPSProtocolPropertiesHttp::builder(
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

        return LoadBalancerServiceHTTPSProtocolProperties::builder($http)
            ->setProtocol(LoadBalancerServiceHTTPSProtocolPropertiesProtocol::https)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerServiceHTTPSProtocolProperties */
    public static function reader(): callable
    {
        return LoadBalancerServiceHTTPSProtocolProperties::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerServiceHTTPSProtocolPropertiesConstraint::constraints();
    }
}
