<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\Route;
use Prefabcortex\Hetzner\Validator\RouteConstraint;
use Symfony\Component\Validator\Constraint;

final class RouteFixture
{
    public static function build(): Route
    {
        return Route::builder(
            // destination
            '10.100.1.0/24',
            // gateway
            '10.0.1.1',
        )->build();
    }

    /** @return callable(array<int|string, mixed>): Route */
    public static function reader(): callable
    {
        return Route::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return RouteConstraint::constraints();
    }
}
