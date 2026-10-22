<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ErrorResponseError;
use Prefabcortex\Hetzner\Validator\ErrorResponseErrorConstraint;
use Symfony\Component\Validator\Constraint;

final class ErrorResponseErrorFixture
{
    public static function build(): ErrorResponseError
    {
        return ErrorResponseError::builder(
            // code
            'REPLACE_ME',
            // message
            'REPLACE_ME',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ErrorResponseError */
    public static function reader(): callable
    {
        return ErrorResponseError::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ErrorResponseErrorConstraint::constraints();
    }
}
