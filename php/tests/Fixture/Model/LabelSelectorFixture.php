<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\LabelSelector;
use Prefabcortex\Hetzner\Validator\LabelSelectorConstraint;
use Symfony\Component\Validator\Constraint;

final class LabelSelectorFixture
{
    public static function build(): LabelSelector
    {
        return LabelSelector::builder('env=prod')->build();
    }

    /** @return callable(array<int|string, mixed>): LabelSelector */
    public static function reader(): callable
    {
        return LabelSelector::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return LabelSelectorConstraint::constraints();
    }
}
