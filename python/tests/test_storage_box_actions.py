"""Generated tests for ``storage_box_actions``."""

import asyncio

import pytest

from hetzner_api.models import ActionListResponseWithMeta, ActionResponse
from tests.payloads import ACTION_LIST_RESPONSE_WITH_META, ACTION_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_storage_box_actions_list_storage_boxes_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.storage_box_actions.list_storage_boxes_actions()
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/actions"


def test_async_storage_box_actions_list_storage_boxes_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_actions.list_storage_boxes_actions()
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/actions"


def test_storage_box_actions_get_storage_boxes_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_actions.get_storage_boxes_action(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/actions/42"


def test_async_storage_box_actions_get_storage_boxes_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_actions.get_storage_boxes_action(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/actions/42"


def test_storage_box_actions_list_storage_box_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.storage_box_actions.list_storage_box_actions(42)
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions"


def test_async_storage_box_actions_list_storage_box_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_actions.list_storage_box_actions(42)
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions"


def test_storage_box_actions_get_storage_box_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        deprecated_method = client.storage_box_actions.get_storage_box_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
        with pytest.deprecated_call():
            result = deprecated_method(42, 42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/42"


def test_async_storage_box_actions_get_storage_box_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            deprecated_method = client.storage_box_actions.get_storage_box_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
            with pytest.deprecated_call():
                result = await deprecated_method(42, 42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/42"


def test_storage_box_actions_change_storage_box_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_actions.change_storage_box_protection(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/change_protection"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_storage_box_actions_change_storage_box_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_actions.change_storage_box_protection(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/change_protection"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_storage_box_actions_change_storage_box_type() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_actions.change_storage_box_type(42, storage_box_type="bx20")
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/change_type"
    assert json_of(request) == to_jsonable({"storage_box_type": "bx20"})


def test_async_storage_box_actions_change_storage_box_type() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_actions.change_storage_box_type(
                42, storage_box_type="bx20"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/change_type"
    assert json_of(request) == to_jsonable({"storage_box_type": "bx20"})


def test_storage_box_actions_reset_storage_box_password() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_actions.reset_storage_box_password(42, password="example")
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/reset_password"
    assert json_of(request) == to_jsonable({"password": "example"})


def test_async_storage_box_actions_reset_storage_box_password() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_actions.reset_storage_box_password(
                42, password="example"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/reset_password"
    assert json_of(request) == to_jsonable({"password": "example"})


def test_storage_box_actions_update_storage_box_access_settings() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_actions.update_storage_box_access_settings(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/storage_boxes/42/actions/update_access_settings"
    )
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_storage_box_actions_update_storage_box_access_settings() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_actions.update_storage_box_access_settings(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert (
        request.url.raw_path.split(b"?")[0]
        == b"/v1/storage_boxes/42/actions/update_access_settings"
    )
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_storage_box_actions_rollback_storage_box_snapshot() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_actions.rollback_storage_box_snapshot(
            42, snapshot="my-snapshot"
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/rollback_snapshot"
    assert json_of(request) == to_jsonable({"snapshot": "my-snapshot"})


def test_async_storage_box_actions_rollback_storage_box_snapshot() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_actions.rollback_storage_box_snapshot(
                42, snapshot="my-snapshot"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/rollback_snapshot"
    assert json_of(request) == to_jsonable({"snapshot": "my-snapshot"})


def test_storage_box_actions_disable_storage_box_snapshot_plan() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_actions.disable_storage_box_snapshot_plan(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/disable_snapshot_plan"
    )


def test_async_storage_box_actions_disable_storage_box_snapshot_plan() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_actions.disable_storage_box_snapshot_plan(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/disable_snapshot_plan"
    )


def test_storage_box_actions_enable_storage_box_snapshot_plan() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.storage_box_actions.enable_storage_box_snapshot_plan(
            42, max_snapshots=10, minute=30, hour=3
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/enable_snapshot_plan"
    )
    assert json_of(request) == to_jsonable({"max_snapshots": 10, "minute": 30, "hour": 3})


def test_async_storage_box_actions_enable_storage_box_snapshot_plan() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.storage_box_actions.enable_storage_box_snapshot_plan(
                42, max_snapshots=10, minute=30, hour=3
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.com"
    assert (
        request.url.raw_path.split(b"?")[0] == b"/v1/storage_boxes/42/actions/enable_snapshot_plan"
    )
    assert json_of(request) == to_jsonable({"max_snapshots": 10, "minute": 30, "hour": 3})
