<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ErrorResponse;
use Prefabcortex\Hetzner\Model\ErrorResponseError;
use Prefabcortex\Hetzner\Validator\ErrorResponseConstraint;
use Symfony\Component\Validator\Constraint;

final class ErrorResponseFixture
{
    public static function build(): ErrorResponse
    {
        $error = ErrorResponseError::builder(
            // code
            'REPLACE_ME',
            // message
            'REPLACE_ME',
        )->build();

        return ErrorResponse::builder($error)->build();
    }

    /** @return callable(array<int|string, mixed>): ErrorResponse */
    public static function reader(): callable
    {
        return ErrorResponse::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ErrorResponseConstraint::constraints();
    }
}
