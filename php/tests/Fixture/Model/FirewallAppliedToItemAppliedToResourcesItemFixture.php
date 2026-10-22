<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\FirewallAppliedToItemAppliedToResourcesItem;
use Prefabcortex\Hetzner\Model\FirewallAppliedToItemAppliedToResourcesItemType;
use Prefabcortex\Hetzner\Validator\FirewallAppliedToItemAppliedToResourcesItemConstraint;
use Symfony\Component\Validator\Constraint;

final class FirewallAppliedToItemAppliedToResourcesItemFixture
{
    public static function build(): FirewallAppliedToItemAppliedToResourcesItem
    {
        return FirewallAppliedToItemAppliedToResourcesItem::builder()
            ->setType(FirewallAppliedToItemAppliedToResourcesItemType::server)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): FirewallAppliedToItemAppliedToResourcesItem */
    public static function reader(): callable
    {
        return FirewallAppliedToItemAppliedToResourcesItem::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return FirewallAppliedToItemAppliedToResourcesItemConstraint::constraints();
    }
}
