"""Generated tests for ``actions``."""

import asyncio

from hetzner_api.models import ActionListResponse, ActionResponse
from tests.payloads import ACTION_LIST_RESPONSE, ACTION_RESPONSE
from tests.support import Recorder, async_client, sync_client, validated


def test_actions_get_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE)
    with sync_client(recorder) as client:
        result = client.actions.get_actions(id=[1])
        assert result == validated(ActionListResponse, ACTION_LIST_RESPONSE)
        assert hash(result) == hash(validated(ActionListResponse, ACTION_LIST_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/actions"


def test_async_actions_get_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.actions.get_actions(id=[1])
            assert result == validated(ActionListResponse, ACTION_LIST_RESPONSE)
            assert hash(result) == hash(validated(ActionListResponse, ACTION_LIST_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/actions"


def test_actions_get_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.actions.get_action(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/actions/42"


def test_async_actions_get_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.actions.get_action(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/actions/42"
