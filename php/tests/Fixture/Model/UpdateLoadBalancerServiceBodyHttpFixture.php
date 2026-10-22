<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateLoadBalancerServiceBodyHttp;
use Prefabcortex\Hetzner\Validator\UpdateLoadBalancerServiceBodyHttpConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateLoadBalancerServiceBodyHttpFixture
{
    public static function build(): UpdateLoadBalancerServiceBodyHttp
    {
        return UpdateLoadBalancerServiceBodyHttp::builder()
            ->setCookieName('HCLBSTICKY')
            ->setCookieLifetime(300)
            ->setTimeoutIdle(50)
            ->setCertificates([897])
            ->setRedirectHttp(true)
            ->setStickySessions(true)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateLoadBalancerServiceBodyHttp */
    public static function reader(): callable
    {
        return UpdateLoadBalancerServiceBodyHttp::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateLoadBalancerServiceBodyHttpConstraint::constraints();
    }
}
