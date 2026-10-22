"""Generated tests for ``servers``."""

import asyncio

from hetzner_api.models import (
    ActionResponse,
    CreateServerResponse,
    ListServersResponse,
    MetricsResponse,
    ServerResponse,
)
from tests.payloads import (
    ACTION_RESPONSE,
    CREATE_SERVER_RESPONSE,
    LIST_SERVERS_RESPONSE,
    METRICS_RESPONSE,
    SERVER_RESPONSE,
)
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_servers_list_servers() -> None:
    recorder = Recorder(200, LIST_SERVERS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.servers.list_servers()
        assert result == validated(ListServersResponse, LIST_SERVERS_RESPONSE)
        assert hash(result) == hash(validated(ListServersResponse, LIST_SERVERS_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers"


def test_async_servers_list_servers() -> None:
    recorder = Recorder(200, LIST_SERVERS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.servers.list_servers()
            assert result == validated(ListServersResponse, LIST_SERVERS_RESPONSE)
            assert hash(result) == hash(validated(ListServersResponse, LIST_SERVERS_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers"


def test_servers_create_server() -> None:
    recorder = Recorder(200, CREATE_SERVER_RESPONSE)
    with sync_client(recorder) as client:
        result = client.servers.create_server(
            name="my-server", server_type="cpx22", image="ubuntu-24.04"
        )
        assert result == validated(CreateServerResponse, CREATE_SERVER_RESPONSE)
        assert hash(result) == hash(validated(CreateServerResponse, CREATE_SERVER_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers"
    assert json_of(request) == to_jsonable(
        {"name": "my-server", "server_type": "cpx22", "image": "ubuntu-24.04"}
    )


def test_async_servers_create_server() -> None:
    recorder = Recorder(200, CREATE_SERVER_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.servers.create_server(
                name="my-server", server_type="cpx22", image="ubuntu-24.04"
            )
            assert result == validated(CreateServerResponse, CREATE_SERVER_RESPONSE)
            assert hash(result) == hash(validated(CreateServerResponse, CREATE_SERVER_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers"
    assert json_of(request) == to_jsonable(
        {"name": "my-server", "server_type": "cpx22", "image": "ubuntu-24.04"}
    )


def test_servers_get_server() -> None:
    recorder = Recorder(200, SERVER_RESPONSE)
    with sync_client(recorder) as client:
        result = client.servers.get_server(42)
        assert result == validated(ServerResponse, SERVER_RESPONSE)
        assert hash(result) == hash(validated(ServerResponse, SERVER_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42"


def test_async_servers_get_server() -> None:
    recorder = Recorder(200, SERVER_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.servers.get_server(42)
            assert result == validated(ServerResponse, SERVER_RESPONSE)
            assert hash(result) == hash(validated(ServerResponse, SERVER_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42"


def test_servers_update_server() -> None:
    recorder = Recorder(200, SERVER_RESPONSE)
    with sync_client(recorder) as client:
        result = client.servers.update_server(42)
        assert result == validated(ServerResponse, SERVER_RESPONSE)
        assert hash(result) == hash(validated(ServerResponse, SERVER_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_servers_update_server() -> None:
    recorder = Recorder(200, SERVER_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.servers.update_server(42)
            assert result == validated(ServerResponse, SERVER_RESPONSE)
            assert hash(result) == hash(validated(ServerResponse, SERVER_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_servers_delete_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)
    with sync_client(recorder) as client:
        result = client.servers.delete_server(42)
        assert result == validated(ActionResponse, ACTION_RESPONSE)
        assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42"


def test_async_servers_delete_server() -> None:
    recorder = Recorder(200, ACTION_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.servers.delete_server(42)
            assert result == validated(ActionResponse, ACTION_RESPONSE)
            assert hash(result) == hash(validated(ActionResponse, ACTION_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42"


def test_servers_get_server_metrics() -> None:
    recorder = Recorder(200, METRICS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.servers.get_server_metrics(42, type=["cpu"], start="example", end="example")
        assert result == validated(MetricsResponse, METRICS_RESPONSE)
        assert hash(result) == hash(validated(MetricsResponse, METRICS_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/metrics"


def test_async_servers_get_server_metrics() -> None:
    recorder = Recorder(200, METRICS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.servers.get_server_metrics(
                42, type=["cpu"], start="example", end="example"
            )
            assert result == validated(MetricsResponse, METRICS_RESPONSE)
            assert hash(result) == hash(validated(MetricsResponse, METRICS_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/servers/42/metrics"
