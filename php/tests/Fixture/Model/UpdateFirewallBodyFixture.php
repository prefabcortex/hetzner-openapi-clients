<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\UpdateFirewallBody;
use Prefabcortex\Hetzner\Validator\UpdateFirewallBodyConstraint;
use Symfony\Component\Validator\Constraint;

final class UpdateFirewallBodyFixture
{
    public static function build(): UpdateFirewallBody
    {
        return UpdateFirewallBody::builder()
            ->setName('new-name')
            ->build();
    }

    /** @return callable(array<int|string, mixed>): UpdateFirewallBody */
    public static function reader(): callable
    {
        return UpdateFirewallBody::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return UpdateFirewallBodyConstraint::constraints();
    }
}
