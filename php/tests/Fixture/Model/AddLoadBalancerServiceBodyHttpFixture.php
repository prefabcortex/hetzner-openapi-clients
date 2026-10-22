<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\AddLoadBalancerServiceBodyHttp;
use Prefabcortex\Hetzner\Validator\AddLoadBalancerServiceBodyHttpConstraint;
use Symfony\Component\Validator\Constraint;

final class AddLoadBalancerServiceBodyHttpFixture
{
    public static function build(): AddLoadBalancerServiceBodyHttp
    {
        return AddLoadBalancerServiceBodyHttp::builder()
            ->setCookieName('HCLBSTICKY')
            ->setCookieLifetime(300)
            ->setTimeoutIdle(50)
            ->setCertificates([897])
            ->setRedirectHttp(true)
            ->setStickySessions(true)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): AddLoadBalancerServiceBodyHttp */
    public static function reader(): callable
    {
        return AddLoadBalancerServiceBodyHttp::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return AddLoadBalancerServiceBodyHttpConstraint::constraints();
    }
}
