<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerService;
use Prefabcortex\Hetzner\Validator\LoadBalancerServiceConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerServiceFixture
{
    public static function build(): LoadBalancerService
    {
        return LoadBalancerService::builder()
            ->setListenPort(443)
            ->setDestinationPort(80)
            ->setProxyprotocol(false)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerService */
    public static function reader(): callable
    {
        return LoadBalancerService::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerServiceConstraint::constraints();
    }
}
