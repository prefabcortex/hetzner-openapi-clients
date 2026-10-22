<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\HealthCheckProtocol;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceBaseHealthCheck;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceHTTPProtocolPropertiesHttp;
use Prefabcortex\Hetzner\Model\LoadBalancerServiceProtocol;
use Prefabcortex\Hetzner\Model\ServiceHTTPProtocol;
use Prefabcortex\Hetzner\Validator\ServiceHTTPProtocolConstraint;
use Symfony\Component\Validator\Constraint;

final class ServiceHTTPProtocolFixture
{
    public static function build(): ServiceHTTPProtocol
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

        return ServiceHTTPProtocol::builder(
            // protocol
            LoadBalancerServiceProtocol::http,
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

    /** @return callable(array<int|string, mixed>): ServiceHTTPProtocol */
    public static function reader(): callable
    {
        return ServiceHTTPProtocol::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ServiceHTTPProtocolConstraint::constraints();
    }
}
