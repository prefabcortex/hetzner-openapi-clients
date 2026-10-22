"""Generated tests for ``networks``."""

import asyncio

from hetzner_api.models import ListNetworkMembersResponse, ListNetworksResponse, NetworkResponse
from tests.payloads import LIST_NETWORK_MEMBERS_RESPONSE, LIST_NETWORKS_RESPONSE, NETWORK_RESPONSE
from tests.support import Recorder, async_client, json_of, sync_client, to_jsonable, validated


def test_networks_list_networks() -> None:
    recorder = Recorder(200, LIST_NETWORKS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.networks.list_networks()
        assert result == validated(ListNetworksResponse, LIST_NETWORKS_RESPONSE)
        assert hash(result) == hash(validated(ListNetworksResponse, LIST_NETWORKS_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks"


def test_async_networks_list_networks() -> None:
    recorder = Recorder(200, LIST_NETWORKS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.networks.list_networks()
            assert result == validated(ListNetworksResponse, LIST_NETWORKS_RESPONSE)
            assert hash(result) == hash(validated(ListNetworksResponse, LIST_NETWORKS_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks"


def test_networks_create_network() -> None:
    recorder = Recorder(200, NETWORK_RESPONSE)
    with sync_client(recorder) as client:
        result = client.networks.create_network(name="mynet", ip_range="10.0.0.0/16")
        assert result == validated(NetworkResponse, NETWORK_RESPONSE)
        assert hash(result) == hash(validated(NetworkResponse, NETWORK_RESPONSE))
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks"
    assert json_of(request) == to_jsonable({"name": "mynet", "ip_range": "10.0.0.0/16"})


def test_async_networks_create_network() -> None:
    recorder = Recorder(200, NETWORK_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.networks.create_network(name="mynet", ip_range="10.0.0.0/16")
            assert result == validated(NetworkResponse, NETWORK_RESPONSE)
            assert hash(result) == hash(validated(NetworkResponse, NETWORK_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "POST"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks"
    assert json_of(request) == to_jsonable({"name": "mynet", "ip_range": "10.0.0.0/16"})


def test_networks_get_network() -> None:
    recorder = Recorder(200, NETWORK_RESPONSE)
    with sync_client(recorder) as client:
        result = client.networks.get_network(42)
        assert result == validated(NetworkResponse, NETWORK_RESPONSE)
        assert hash(result) == hash(validated(NetworkResponse, NETWORK_RESPONSE))
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42"


def test_async_networks_get_network() -> None:
    recorder = Recorder(200, NETWORK_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.networks.get_network(42)
            assert result == validated(NetworkResponse, NETWORK_RESPONSE)
            assert hash(result) == hash(validated(NetworkResponse, NETWORK_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42"


def test_networks_update_network() -> None:
    recorder = Recorder(200, NETWORK_RESPONSE)
    with sync_client(recorder) as client:
        result = client.networks.update_network(42)
        assert result == validated(NetworkResponse, NETWORK_RESPONSE)
        assert hash(result) == hash(validated(NetworkResponse, NETWORK_RESPONSE))
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_async_networks_update_network() -> None:
    recorder = Recorder(200, NETWORK_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.networks.update_network(42)
            assert result == validated(NetworkResponse, NETWORK_RESPONSE)
            assert hash(result) == hash(validated(NetworkResponse, NETWORK_RESPONSE))

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "PUT"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42"
    assert json_of(request) == to_jsonable(dict[str, object]())


def test_networks_delete_network() -> None:
    recorder = Recorder(204, None)
    with sync_client(recorder) as client:
        client.networks.delete_network(42)
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42"


def test_async_networks_delete_network() -> None:
    recorder = Recorder(204, None)

    async def run() -> None:
        async with async_client(recorder) as client:
            await client.networks.delete_network(42)

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "DELETE"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42"


def test_networks_list_network_members() -> None:
    recorder = Recorder(200, LIST_NETWORK_MEMBERS_RESPONSE)
    with sync_client(recorder) as client:
        result = client.networks.list_network_members(42)
        assert result == validated(ListNetworkMembersResponse, LIST_NETWORK_MEMBERS_RESPONSE)
        assert hash(result) == hash(
            validated(ListNetworkMembersResponse, LIST_NETWORK_MEMBERS_RESPONSE)
        )
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/members"


def test_async_networks_list_network_members() -> None:
    recorder = Recorder(200, LIST_NETWORK_MEMBERS_RESPONSE)

    async def run() -> None:
        async with async_client(recorder) as client:
            result = await client.networks.list_network_members(42)
            assert result == validated(ListNetworkMembersResponse, LIST_NETWORK_MEMBERS_RESPONSE)
            assert hash(result) == hash(
                validated(ListNetworkMembersResponse, LIST_NETWORK_MEMBERS_RESPONSE)
            )

    asyncio.run(run())
    request = recorder.only()
    assert request.method == "GET"
    assert request.url.host == "api.hetzner.cloud"
    assert request.url.raw_path.split(b"?")[0] == b"/v1/networks/42/members"
