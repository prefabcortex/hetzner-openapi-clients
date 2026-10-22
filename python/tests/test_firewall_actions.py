"""Generated tests for ``firewall_actions``."""

import asyncio

import pytest

from hetzner_api.models import ActionListResponse, ActionListResponseWithMeta, ActionResponse
from tests.payloads import ACTION_LIST_RESPONSE, ACTION_LIST_RESPONSE_WITH_META, ACTION_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_firewall_actions_list_firewalls_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.firewall_actions.list_firewalls_actions()
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/actions"


def test_async_firewall_actions_list_firewalls_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.firewall_actions.list_firewalls_actions()
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/actions"


def test_firewall_actions_get_firewalls_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.firewall_actions.get_firewalls_action(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/actions/42"


def test_async_firewall_actions_get_firewalls_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.firewall_actions.get_firewalls_action(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/actions/42"


def test_firewall_actions_list_firewall_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.firewall_actions.list_firewall_actions(42)
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42/actions"


def test_async_firewall_actions_list_firewall_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.firewall_actions.list_firewall_actions(42)
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42/actions"


def test_firewall_actions_apply_firewall_to_resources() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE)
    with sync_client(recorder) as client:
        result = client.firewall_actions.apply_firewall_to_resources(
            42, apply_to=[{"type": "server"}]
        )
        assert result == validated(ActionListResponse, ACTION_LIST_RESPONSE)
        assert hash(result) == hash(validated(ActionListResponse, ACTION_LIST_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42/actions/apply_to_resources"
    assert json_of(request) == to_jsonable({"apply_to": [{"type": "server"}]})


def test_async_firewall_actions_apply_firewall_to_resources() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.firewall_actions.apply_firewall_to_resources(
                42, apply_to=[{"type": "server"}]
            )
            assert result == validated(ActionListResponse, ACTION_LIST_RESPONSE)
            assert hash(result) == hash(validated(ActionListResponse, ACTION_LIST_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42/actions/apply_to_resources"
    assert json_of(request) == to_jsonable({"apply_to": [{"type": "server"}]})


def test_firewall_actions_remove_firewall_from_resources() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE)
    with sync_client(recorder) as client:
        result = client.firewall_actions.remove_firewall_from_resources(
            42, remove_from=[{"type": "server"}]
        )
        assert result == validated(ActionListResponse, ACTION_LIST_RESPONSE)
        assert hash(result) == hash(validated(ActionListResponse, ACTION_LIST_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42/actions/remove_from_resources"
    assert json_of(request) == to_jsonable({"remove_from": [{"type": "server"}]})


def test_async_firewall_actions_remove_firewall_from_resources() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.firewall_actions.remove_firewall_from_resources(
                42, remove_from=[{"type": "server"}]
            )
            assert result == validated(ActionListResponse, ACTION_LIST_RESPONSE)
            assert hash(result) == hash(validated(ActionListResponse, ACTION_LIST_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42/actions/remove_from_resources"
    assert json_of(request) == to_jsonable({"remove_from": [{"type": "server"}]})


def test_firewall_actions_set_firewall_rules() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE)
    with sync_client(recorder) as client:
        result = client.firewall_actions.set_firewall_rules(
            42, rules=[{"direction": "in", "protocol": "tcp"}]
        )
        assert result == validated(ActionListResponse, ACTION_LIST_RESPONSE)
        assert hash(result) == hash(validated(ActionListResponse, ACTION_LIST_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42/actions/set_rules"
    assert json_of(request) == to_jsonable({"rules": [{"direction": "in", "protocol": "tcp"}]})


def test_async_firewall_actions_set_firewall_rules() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.firewall_actions.set_firewall_rules(
                42, rules=[{"direction": "in", "protocol": "tcp"}]
            )
            assert result == validated(ActionListResponse, ACTION_LIST_RESPONSE)
            assert hash(result) == hash(validated(ActionListResponse, ACTION_LIST_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42/actions/set_rules"
    assert json_of(request) == to_jsonable({"rules": [{"direction": "in", "protocol": "tcp"}]})


def test_firewall_actions_get_firewall_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        deprecated_method = client.firewall_actions.get_firewall_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
        with pytest.deprecated_call():
            result = deprecated_method(42, 42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42/actions/42"


def test_async_firewall_actions_get_firewall_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            deprecated_method = client.firewall_actions.get_firewall_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
            with pytest.deprecated_call():
                result = await deprecated_method(42, 42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/firewalls/42/actions/42"
