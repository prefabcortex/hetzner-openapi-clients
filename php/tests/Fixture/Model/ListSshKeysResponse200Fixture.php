<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Model\ListSshKeysResponse200;
use Prefabcortex\Hetzner\Model\SshKey;
use Prefabcortex\Hetzner\Validator\ListSshKeysResponse200Constraint;
use Symfony\Component\Validator\Constraint;

final class ListSshKeysResponse200Fixture
{
    public static function build(): ListSshKeysResponse200
    {
        $sshKey = SshKey::builder(
            // id
            42,
            // name
            'my-resource',
            // fingerprint
            'b7:2f:30:a0:2f:6c:58:6c:21:04:58:61:ba:06:3b:2f',
            // publicKey
            'ssh-rsa AAAjjk76kgf...Xt',
            // labels
            [],
            // created
            new DateTime('2024-01-01'),
        )->build();
        $pagination = ListMetaPagination::builder(
            // page
            3,
            // perPage
            25,
            // previousPage
            2,
            // nextPage
            4,
            // lastPage
            4,
            // totalEntries
            100,
        )->build();
        $meta = ListMeta::builder($pagination)->build();

        return ListSshKeysResponse200::builder(
            // sshKeys
            [$sshKey],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ListSshKeysResponse200 */
    public static function reader(): callable
    {
        return ListSshKeysResponse200::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ListSshKeysResponse200Constraint::constraints();
    }
}
