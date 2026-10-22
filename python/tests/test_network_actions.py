"""Generated tests for ``network_actions``."""

import asyncio

import pytest

from hetzner_api.models import ActionListResponseWithMeta, ActionResponse
from tests.payloads import ACTION_LIST_RESPONSE_WITH_META, ACTION_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_network_actions_list_networks_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.network_actions.list_networks_actions()
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/actions"


def test_async_network_actions_list_networks_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.network_actions.list_networks_actions()
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/actions"


def test_network_actions_get_networks_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.network_actions.get_networks_action(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/actions/42"


def test_async_network_actions_get_networks_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.network_actions.get_networks_action(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/actions/42"


def test_network_actions_list_network_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)
    with sync_client(recorder) as client:
        result = client.network_actions.list_network_actions(42)
        assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        assert hash(result) == hash(
            validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions"


def test_async_network_actions_list_network_actions() -> None:
    recorder = Recorder(200, ACTION_LIST_RESPONSE_WITH_META)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.network_actions.list_network_actions(42)
            assert result == validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            assert hash(result) == hash(
                validated(ActionListResponseWithMeta, ACTION_LIST_RESPONSE_WITH_META)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions"


def test_network_actions_add_network_route() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.network_actions.add_network_route(
            42, destination="10.100.1.0/24", gateway="10.0.1.1"
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/add_route"
    assert json_of(request) == to_jsonable({"destination": "10.100.1.0/24", "gateway": "10.0.1.1"})


def test_async_network_actions_add_network_route() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.network_actions.add_network_route(
                42, destination="10.100.1.0/24", gateway="10.0.1.1"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/add_route"
    assert json_of(request) == to_jsonable({"destination": "10.100.1.0/24", "gateway": "10.0.1.1"})


def test_network_actions_add_network_subnet() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.network_actions.add_network_subnet(
            42, type="cloud", network_zone="eu-central"
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/add_subnet"
    assert json_of(request) == to_jsonable({"type": "cloud", "network_zone": "eu-central"})


def test_async_network_actions_add_network_subnet() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.network_actions.add_network_subnet(
                42, type="cloud", network_zone="eu-central"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/add_subnet"
    assert json_of(request) == to_jsonable({"type": "cloud", "network_zone": "eu-central"})


def test_network_actions_change_network_ip_range() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.network_actions.change_network_ip_range(42, ip_range="10.0.0.0/16")
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/change_ip_range"
    assert json_of(request) == to_jsonable({"ip_range": "10.0.0.0/16"})


def test_async_network_actions_change_network_ip_range() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.network_actions.change_network_ip_range(
                42, ip_range="10.0.0.0/16"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/change_ip_range"
    assert json_of(request) == to_jsonable({"ip_range": "10.0.0.0/16"})


def test_network_actions_change_network_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.network_actions.change_network_protection(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/change_protection"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_network_actions_change_network_protection() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.network_actions.change_network_protection(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/change_protection"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_network_actions_delete_network_route() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.network_actions.delete_network_route(
            42, destination="10.100.1.0/24", gateway="10.0.1.1"
        )
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/delete_route"
    assert json_of(request) == to_jsonable({"destination": "10.100.1.0/24", "gateway": "10.0.1.1"})


def test_async_network_actions_delete_network_route() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.network_actions.delete_network_route(
                42, destination="10.100.1.0/24", gateway="10.0.1.1"
            )
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/delete_route"
    assert json_of(request) == to_jsonable({"destination": "10.100.1.0/24", "gateway": "10.0.1.1"})


def test_network_actions_delete_network_subnet() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.network_actions.delete_network_subnet(42, ip_range="10.0.1.0/24")
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/delete_subnet"
    assert json_of(request) == to_jsonable({"ip_range": "10.0.1.0/24"})


def test_async_network_actions_delete_network_subnet() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.network_actions.delete_network_subnet(42, ip_range="10.0.1.0/24")
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/delete_subnet"
    assert json_of(request) == to_jsonable({"ip_range": "10.0.1.0/24"})


def test_network_actions_get_network_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        deprecated_method = client.network_actions.get_network_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
        with pytest.deprecated_call():
            result = deprecated_method(42, 42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/42"


def test_async_network_actions_get_network_action() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            deprecated_method = client.network_actions.get_network_action  # type: ignore[deprecated]  # pyright: ignore[reportDeprecated]
            with pytest.deprecated_call():
                result = await deprecated_method(42, 42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/actions/42"
