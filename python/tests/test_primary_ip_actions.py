"""Generated tests for ``primary_ip_actions``."""

import asyncio

import pytest

from hetzner_api.models import ActionListResponseWithMeta, ActionResponse
from tests.payloads import ACTION_LIST_RESPONSE_WITH_META, ACTION_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_primary_ip_actions_list_primary_ips_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.primary_ip_actions.list_primary_ips_actions()
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/actions"


def test_async_primary_ip_actions_list_primary_ips_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.primary_ip_actions.list_primary_ips_actions()
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/actions"


def test_primary_ip_actions_get_primary_ips_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.primary_ip_actions.get_primary_ips_action(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/actions/42"


def test_async_primary_ip_actions_get_primary_ips_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.primary_ip_actions.get_primary_ips_action(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/actions/42"


def test_primary_ip_actions_list_primary_ip_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.primary_ip_actions.list_primary_ip_actions(42)
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42/actions"


def test_async_primary_ip_actions_list_primary_ip_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.primary_ip_actions.list_primary_ip_actions(42)
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42/actions"


def test_primary_ip_actions_get_primary_ip_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        deprecated_method = client.primary_ip_actions.get_primary_ip_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
        with pytest.deprecated_call():
            result = deprecated_method(42, 42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42/actions/42"


def test_async_primary_ip_actions_get_primary_ip_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            deprecated_method = client.primary_ip_actions.get_primary_ip_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
            with pytest.deprecated_call():
                result = await deprecated_method(42, 42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42/actions/42"


def test_primary_ip_actions_assign_primary_ip() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.primary_ip_actions.assign_primary_ip(
            42, assignee_type="server", assignee_id=4711
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42/actions/assign"
    assert json_of(request) == to_jsonable({"assignee_type": "server", "assignee_id": 4711})


def test_async_primary_ip_actions_assign_primary_ip() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.primary_ip_actions.assign_primary_ip(
                42, assignee_type="server", assignee_id=4711
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42/actions/assign"
    assert json_of(request) == to_jsonable({"assignee_type": "server", "assignee_id": 4711})


def test_primary_ip_actions_change_primary_ip_dns_ptr() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.primary_ip_actions.change_primary_ip_dns_ptr(
            42, ip="2001:db8::1", dns_ptr="server.example.com"
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42/actions/change_dns_ptr"
    assert json_of(request) == to_jsonable({"ip": "2001:db8::1", "dns_ptr": "server.example.com"})


def test_async_primary_ip_actions_change_primary_ip_dns_ptr() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.primary_ip_actions.change_primary_ip_dns_ptr(
                42, ip="2001:db8::1", dns_ptr="server.example.com"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42/actions/change_dns_ptr"
    assert json_of(request) == to_jsonable({"ip": "2001:db8::1", "dns_ptr": "server.example.com"})


def test_primary_ip_actions_change_primary_ip_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.primary_ip_actions.change_primary_ip_protection(42, delete=False)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42/actions/change_protection"
    assert json_of(request) == to_jsonable({"delete": False})


def test_async_primary_ip_actions_change_primary_ip_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.primary_ip_actions.change_primary_ip_protection(42, delete=False)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42/actions/change_protection"
    assert json_of(request) == to_jsonable({"delete": False})


def test_primary_ip_actions_unassign_primary_ip() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.primary_ip_actions.unassign_primary_ip(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42/actions/unassign"


def test_async_primary_ip_actions_unassign_primary_ip() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.primary_ip_actions.unassign_primary_ip(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/primary_ips/42/actions/unassign"
