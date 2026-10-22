<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use Prefabcortex\Hetzner\Model\ServerPublicNetIpv4;
use Prefabcortex\Hetzner\Validator\ServerPublicNetIpv4Constraint;
use Symfony\Component\Validator\Constraint;

final class ServerPublicNetIpv4Fixture
{
    public static function build(): ServerPublicNetIpv4
    {
        return ServerPublicNetIpv4::builder(
            // ip
            '1.2.3.4',
            // blocked
            false,
            // dnsPtr
            'server01.example.com',
        )
            ->setId(42)
            ->build();
    }

    /** @return callable(array<int|string, mixed>): ServerPublicNetIpv4 */
    public static function reader(): callable
    {
        return ServerPublicNetIpv4::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ServerPublicNetIpv4Constraint::constraints();
    }
}
