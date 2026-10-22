<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ChangeDeleteProtectionRequest;
use Prefabcortex\Hetzner\Validator\ChangeDeleteProtectionRequestConstraint;
use Symfony\Component\Validator\Constraint;

final class ChangeDeleteProtectionRequestFixture
{
    public static function build(): ChangeDeleteProtectionRequest
    {
        return ChangeDeleteProtectionRequest::builder()
            ->setDelete(true)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): ChangeDeleteProtectionRequest */
    public static function reader(): callable
    {
        return ChangeDeleteProtectionRequest::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ChangeDeleteProtectionRequestConstraint::constraints();
    }
}
