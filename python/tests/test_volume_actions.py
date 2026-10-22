"""Generated tests for ``volume_actions``."""

import asyncio

import pytest

from hetzner_api.models import ActionListResponseWithMeta, ActionResponse
from tests.payloads import ACTION_LIST_RESPONSE_WITH_META, ACTION_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_volume_actions_list_volumes_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.volume_actions.list_volumes_actions()
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/actions"


def test_async_volume_actions_list_volumes_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.volume_actions.list_volumes_actions()
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/actions"


def test_volume_actions_get_volumes_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.volume_actions.get_volumes_action(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/actions/42"


def test_async_volume_actions_get_volumes_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.volume_actions.get_volumes_action(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/actions/42"


def test_volume_actions_list_volume_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.volume_actions.list_volume_actions(42)
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42/actions"


def test_async_volume_actions_list_volume_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.volume_actions.list_volume_actions(42)
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42/actions"


def test_volume_actions_attach_volume() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.volume_actions.attach_volume(42, server=43)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42/actions/attach"
    assert json_of(request) == to_jsonable({"server": 43})


def test_async_volume_actions_attach_volume() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.volume_actions.attach_volume(42, server=43)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42/actions/attach"
    assert json_of(request) == to_jsonable({"server": 43})


def test_volume_actions_change_volume_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.volume_actions.change_volume_protection(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42/actions/change_protection"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_volume_actions_change_volume_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.volume_actions.change_volume_protection(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42/actions/change_protection"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_volume_actions_detach_volume() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.volume_actions.detach_volume(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42/actions/detach"


def test_async_volume_actions_detach_volume() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.volume_actions.detach_volume(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42/actions/detach"


def test_volume_actions_resize_volume() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.volume_actions.resize_volume(42, size=50)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42/actions/resize"
    assert json_of(request) == to_jsonable({"size": 50})


def test_async_volume_actions_resize_volume() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.volume_actions.resize_volume(42, size=50)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42/actions/resize"
    assert json_of(request) == to_jsonable({"size": 50})


def test_volume_actions_get_volume_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        deprecated_method = client.volume_actions.get_volume_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
        with pytest.deprecated_call():
            result = deprecated_method(42, 42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42/actions/42"


def test_async_volume_actions_get_volume_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            deprecated_method = client.volume_actions.get_volume_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
            with pytest.deprecated_call():
                result = await deprecated_method(42, 42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/volumes/42/actions/42"
