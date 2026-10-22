<?php

declare(strict_types=1);

namespace Prefabcortex\Hetzner\Tests\Fixture\Model;

use DateTime;
use Prefabcortex\Hetzner\Model\Action;
use Prefabcortex\Hetzner\Model\ActionError;
use Prefabcortex\Hetzner\Model\ActionListResponseWithMeta;
use Prefabcortex\Hetzner\Model\ActionResource;
use Prefabcortex\Hetzner\Model\ActionStatus;
use Prefabcortex\Hetzner\Model\ListMeta;
use Prefabcortex\Hetzner\Model\ListMetaPagination;
use Prefabcortex\Hetzner\Validator\ActionListResponseWithMetaConstraint;
use Symfony\Component\Validator\Constraint;

final class ActionListResponseWithMetaFixture
{
    public static function build(): ActionListResponseWithMeta
    {
        $actionResource = ActionResource::builder(
            // id
            42,
            // type
            'server',
        )->build();
        $error = ActionError::builder(
            // code
            'action_failed',
            // message
            'Action failed',
        )->build();
        $action = Action::builder(
            // id
            42,
            // command
            'start_resource',
            // status
            ActionStatus::running,
            // started
            new DateTime('2024-01-01'),
            // finished
            new DateTime('2024-01-01'),
            // progress
            100,
            // resources
            [$actionResource],
            // error
            $error,
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

        return ActionListResponseWithMeta::builder(
            // actions
            [$action],
            // meta
            $meta,
        )->build();
    }

    /** @return callable(array<int|string, mixed>): ActionListResponseWithMeta */
    public static function reader(): callable
    {
        return ActionListResponseWithMeta::fromArray(...);
    }

    /** @return list<Constraint> */
    public static function constraints(): array
    {
        return ActionListResponseWithMetaConstraint::constraints();
    }
}
