<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LoadBalancerTargetLabelSelector;
use Prefabcortex\Hetzner\Validator\LoadBalancerTargetLabelSelectorConstraint;
use Symfony\Component\Validator\Constraint;

final class LoadBalancerTargetLabelSelectorFixture
{
    public static function build(): LoadBalancerTargetLabelSelector
    {
        return LoadBalancerTargetLabelSelector::builder('env=prod')->build();
    }

    /** @return callable(array<int|string, mixed>): LoadBalancerTargetLabelSelector */
    public static function reader(): callable
    {
        return LoadBalancerTargetLabelSelector::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LoadBalancerTargetLabelSelectorConstraint::constraints();
    }
}
