<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthCheckProtocol;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceBaseHealthCheck;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceHTTPSProtocolPropertiesHttp;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceProtocol;
use Prefabcortex\Hetzner\Model\ServiceHTTPSProtocol;
use Prefabcortex\Hetzner\Validator\ServiceHTTPSProtocolConstraint;
use Symfony\Component\Validator\Constraint;

final class ServiceHTTPSProtocolFixture
{
    public static function build(): ServiceHTTPSProtocol
    {
        $healthCheck = LoadBalancerServiceBaseHealthCheck::builder(
            // protocol
            HealthCheckProtocol::tcp,
            // port
            4711,
            // interval
            15,
            // timeout
            10,
            // retries
            3,
        )->build();
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

        return ServiceHTTPSProtocol::builder(
            // protocol
            LoadBalancerServiceProtocol::https,
            // listenPort
            443,
            // destinationPort
            80,
            // proxyprotocol
            false,
            // healthCheck
            $healthCheck,
            // http
            $http,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ServiceHTTPSProtocol */
    public static function reader(): callable
    {
        return ServiceHTTPSProtocol::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ServiceHTTPSProtocolConstraint::constraints();
    }
}
