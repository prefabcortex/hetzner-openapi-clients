<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ResetPasswordRequest;
use Prefabcortex\Hetzner\Validator\ResetPasswordRequestConstraint;
use Symfony\Component\Validator\Constraint;

final class ResetPasswordRequestFixture
{
    public static function build(): ResetPasswordRequest
    {
        return ResetPasswordRequest::builder('REPLACE_ME')->build();
    }

    /** @return callable(array<int|string, mixed>): ResetPasswordRequest */
    public static function reader(): callable
    {
        return ResetPasswordRequest::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ResetPasswordRequestConstraint::constraints();
    }
}
