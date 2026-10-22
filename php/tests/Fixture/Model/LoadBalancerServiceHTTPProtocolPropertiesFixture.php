<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerServiceHTTPProtocolProperties;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceHTTPProtocolPropertiesHttp;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceHTTPProtocolPropertiesProtocol;
use Prefabcortex\Hetzner\Validator\LoadBalancerServiceHTTPProtocolPropertiesConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerServiceHTTPProtocolPropertiesFixture
{
    public static function build(): LoadBalancerServiceHTTPProtocolProperties
    {
        $http = LoadBalancerServiceHTTPProtocolPropertiesHttp::builder(
            // cookieName
            'HCLBSTICKY',
            // cookieLifetime
            300,
            // timeoutIdle
            50,
            // stickySessions
            true,
        )->build();

        return LoadBalancerServiceHTTPProtocolProperties::builder($http)
            ->setProtocol(LoadBalancerServiceHTTPProtocolPropertiesProtocol::http)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerServiceHTTPProtocolProperties */
    public static function reader(): callable
    {
        return LoadBalancerServiceHTTPProtocolProperties::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerServiceHTTPProtocolPropertiesConstraint::constraints();
    }
}
