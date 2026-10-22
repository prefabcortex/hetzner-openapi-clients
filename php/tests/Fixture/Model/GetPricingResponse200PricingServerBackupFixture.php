<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\GetPricingResponse200PricingServerBackup;
use Prefabcortex\Hetzner\Validator\GetPricingResponse200PricingServerBackupConstraint;
use Symfony\Component\Validator\Constraint;

final class GetPricingResponse200PricingServerBackupFixture
{
    public static function build(): GetPricingResponse200PricingServerBackup
    {
        return GetPricingResponse200PricingServerBackup::builder('20.00')->build();
    }

    /** @return callable(array<int|string, mixed>): GetPricingResponse200PricingServerBackup */
    public static function reader(): callable
    {
        return GetPricingResponse200PricingServerBackup::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return GetPricingResponse200PricingServerBackupConstraint::constraints();
    }
}
